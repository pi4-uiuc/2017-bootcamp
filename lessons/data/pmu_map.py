#!/usr/bin/env python2
import pandas as pd
from numpy import nan, isnan

# Column headers are in the format _NAME[-PMUID]:[VENDOR-]TYPE[_Quality].  This means that
# we need to account (and parse) for the fields NAME (string), PMUDID (string),
# VENDOR (string), TYPE (string), and QUALITY (bool).  We'll use a dictionary to do this.
# TYPE:
#   F   frequency           ~60 Hz
#   DF  dF/dt               ~0 Hz/s
#   V   voltage             ~120 V
#   VH  voltage phase angle -180--180 deg
#   I   current             ~20 A
#   IH  current phase angle -180--180 deg
#   S   status flag         text
def parse_header_line(header_titles):
    fields = {}
    vendor_acronyms = ('ABB', 'ARB', 'ATK', 'BPA', 'GE', 'HWY', 'MAC', 'MTA', \
                       'NPT', 'OTR', 'SEL', 'GPA', 'UTK', 'SIE', 'EPG')
    # GE doesn't occur in these data (by grep), so we're okay assuming three letters each.
    
    # Parse into data fields according to '_NAME[-PMUID]:[VENDOR]TYPE[_Quality]'.
    for title in header_titles:
        if title == 'Timestamp':
            field = {'name': title, 'id': None, 'vendor': None, 'type': 'T', 'quality': None}
            fields[title] = field
            continue
        name_id_vendor_type_qual = title.split(':')
        name_id = name_id_vendor_type_qual[0].split('-')
        (name, id) = (name_id[0][1:], name_id[1]) if len(name_id) > 1 else (name_id[0][1:], None)
        # Vendor and type are a little tricky to tease out since they aren't delimited,
        # but we know from inspection that only UTK is expected.
        vendor_type = name_id_vendor_type_qual[1].split('_')[0]
        (vendor, type) = (vendor_type[0:3], vendor_type[3:]) if (vendor_type[0:3] in vendor_acronyms) else (None, vendor_type)
        quality = True if len(name_id_vendor_type_qual[1].split('_')) > 1 else False
        
        field = {'name': name, 'id': id, 'vendor': vendor, 'type': type, 'quality': quality}
        fields[title] = field
    return fields

# Return the acceptable limits on physical values from the PMU (in SI units).
# 20% seems to be about right to keep 60 Hz from overlapping with 120 V.
def get_limits(field):
    if   field == 'F':
        return (0.8*60, 1.2*60)
    elif field == 'DF':
        return (0, 0)
    elif field == 'V':
        return (0.8*120, 1.2*120)
    elif field == 'VH':
        return (-180, 180)
    elif field == 'I':
        return (0.8*20, 1.2*20)
    elif field == 'VH':
        return (-180, 180)
    elif field == 'S':
        return (0, 0)
    else:
        return (0, 0)

from sys import stdin
def parse_pmu_stdin():
    fields  = []
    headers = []
    data = []
    
    for line in stdin:
        # Tokenize and count columns.
        entries = line.split(',')
        # Although a little byzantine, read the first line since we need the index of
        # the headers as well as their decomposition from the parse_csv_header above.
        # By byzantine, I mean that now you end up writing something like
        #    fields[headers[i]]['type']
        # to get the type corresponding to the i-th header.  You can think of this as
        #    fields(headers[i]).type
        # if that makes you feel better (this latter of course doesn't work).
        if entries[0] == 'Timestamp':
            fields  = parse_header_line(entries)
            headers = entries
            continue
        cols = len(fields)
        
        # Filter each value by the expected physical limits.
        row_dict = {}
        for (i, entry) in enumerate(entries):
            if i == 0: # first column is the time stamp in format 'DD-MMM-YYYY HH:MM:SS.mmm'
                row_dict[headers[0]] = entry
                continue
            else:
                if i >= cols: continue      # data without a header are invalid
                # Convert entry value to float if possible.
                try:
                    entry = float(entry)
                except ValueError:
                    continue # ignore status flags for now
                # Align by the header, which shouldn't be any problem but just to be safe...
                try:
                    x = headers[i]
                except IndexError:
                    print(cols, '\n', headers, i, len(headers), '\n', entries, len(entries))
                (llim, ulim) = get_limits(fields[headers[i]]['type'])
                if (llim == ulim == 0 or    # no pertinent physical limit exists
                    entry < ulim and        # value lies below upper physical limit
                    entry > llim):          # value lies above lower physical limit
                    # This is a valid entry, so log it.
                    row_dict[headers[i]] = entry
                else:
                    # This entry is beyond acceptable limits.
                    row_dict[headers[i]] = nan
        data.append(row_dict)
        row_dict = {}
    # Convert timestamp to indexable list.
    time_index = []
    for i in data:
        time_index.append(i['Timestamp'])
    #return (pd.DataFrame(data, index=time_index), fields)
    return (pd.DataFrame(data), fields)

# Filter the data according to a low-order median filter.  This is more robust against
# noise than a mean filter, but not as good as an optimal FFT/deconvolution approach.
# Inputs:
#   data  pandas dataframe of data in csv file
#   twom  2M, M points to sample each side for median
# Rules:
#   1.  Don't smooth earlier than the first M data points.
#   2.  Ignore NaNs.
#   3.  
from math import ceil
from pandas import rolling_median
from numpy import abs
def filter_data(data, fields, m=10):
    # Now we need to calculate the median and to do this in a vectorized (rather than an
    # iterative) manner if possible.
    filtered = pd.DataFrame(data['Timestamp'])
    stdevs   = pd.DataFrame(data['Timestamp'])
    for (col, srs) in data.iteritems():
        if col == 'Timestamp': continue
        flds = fields[col]
        if flds['type'] == 'S':     continue    # this is often 0
        if flds['type'] == 'DF':    continue    # this can be queried or calculated if needed
        if flds['type'] == 'VH':    continue    # phase angles are generally not very noisy
        if flds['type'] == 'IH':    continue    # ditto
        if flds['quality']:         continue
        
        # Calculate the median for a sliding window of 2M+1 values.
        srs = abs(srs)
        newsrs  = rolling_median(srs, window=10, min_periods=int(ceil(0.9*10)))
        newstdev= rolling_std(   srs, window=m,  min_periods=int(ceil(0.9*m)))
        filtered[col] = newsrs.copy(deep=True)
        stdevs[col]   = newstdev.copy(deep=True)
    return (filtered, stdevs)

from pandas import rolling_std
from numpy import abs
def get_data_stdev(data, fields, m=100):
    # Get m-element standard deviation rolling windows.
    filtered = pd.DataFrame(data['Timestamp'])
    for (col, srs) in data.iteritems():
        if col == 'Timestamp': continue
        flds = fields[col]
        if flds['type'] != 'V': continue
        if flds['quality']:     continue
        srs = abs(srs)
        newsrs = rolling_std(srs, window=m, min_periods=int(ceil(0.9*m)))
        filtered[col] = newsrs.copy(deep=True)
    return filtered

# Convert a string to a time object.
from datetime import datetime
def str_to_time(string):
    day = int(string[0:2])
    mo  = datetime.strptime(string[3:6], '%b').month
    yr  = int(string[7:11])
    hr  = int(string[12:14])
    mn  = int(string[15:17])
    sec = int(string[18:20])
    usec= int(string[21:24])*1000
    return datetime(yr, mo, day, hr, mn, sec, usec)

# When you perform a logical test on a DataFrame object, it returns a DataFrame of all of
# the satisfying values.  However, we also need this information by contiguity so that we
# can calculate the maximum of each excursion event.  Thus we need this function to break each
# contiguous sector out as its own list of indices.  Then it is trivial to get the maximum
# and extract a range for the excursion event.
#
# Thus find_threshold_ranges returns a dictionary with keys as column titles and values as
# lists of tuple pairs of starting and ending indices of contiguous above-threshold values.
def find_threshold_ranges(data_stdev, fields, threshold=0.12):
    grps = {} # list of Series
    for (col, srs) in data_stdev.iteritems():
        flds = fields[col]
        if flds['name'] == 'Timestamp': continue
        if flds['type'] == 'S':     continue    # this is often 0
        if flds['type'] == 'DF':    continue    # this can be queried or calculated if needed
        if flds['type'] == 'VH':    continue    # phase angles are generally not very noisy
        if flds['type'] == 'IH':    continue    # ditto
        if flds['quality']:         continue
        
        # For each voltage column, find the index of the group of each above-threshold
        # standard deviation index---that is, one group is False, one is True.
        stdev_above_threshold = (srs.groupby(srs > threshold).cumcount())
        
        # Now find the start and end of contiguous groups.
        grp = []
        pair_start = nan
        for (i, j) in enumerate(stdev_above_threshold):
            # i are indices of above_threshold
            # j are indices of srs (stored in stdev_above_threshold)---that is,
            #   stdev_above_threshold[i] is j
            #print i, j
            if i == 0: continue                                   # if there is no prior index
            if abs(stdev_above_threshold[i-1] - j) <= 1: continue # if indices are contiguous
            # We've now eliminated all but crossing indices---indices which indicate if
            # we've just crossed the threshold in value.
            if srs[i] > threshold: # start of contiguous above-threshold values
                pair_start = i
            elif srs[i] < threshold and not isnan(pair_start) and i > 0:
                # end the contiguity and write the pairs to the list
                grp.append((pair_start, i))
                pair_start = nan
            else:
                # the contiguity wasn't started properly---this should never happen
                pair_start = nan
        grps[col] = grp
        #srs[srs.groupby(srs>threshold).cumcount()==0] #first indices of False and True
    return grps

# Find the local maximum within a group as well as its index; return both in dicts of lists.
def find_local_maxima(data_stdev, fields, index_pairs):
    maxima_all  = {}
    indices_all = {}
    for (col, srs) in data_stdev.iteritems():
        flds = fields[col]
        if flds['name'] == 'Timestamp': continue
        if flds['type'] == 'S':     continue    # this is often 0
        if flds['type'] == 'DF':    continue    # this can be queried or calculated if needed
        if flds['type'] == 'VH':    continue    # phase angles are generally not very noisy
        if flds['type'] == 'IH':    continue    # ditto
        if flds['quality']:         continue
        
        # Get maximum and its index in each range.
        maxima  = []
        indices = []
        for pair in index_pairs[col]:
            i_max = srs[pair[0]:pair[1]].argmax()
            indices.append(i_max)
            maxima.append(srs[i_max])
        maxima_all[col]  = maxima
        indices_all[col] = indices
    return (maxima_all, indices_all)

def main():
    thresh = 0.20
    (data, fields) = parse_pmu_stdin()
    data_median = filter_data(   data, fields)
    data_stdev  = get_data_stdev(data, fields)
    
    groups = find_threshold_ranges(data_stdev, fields, threshold=thresh)
    (maxima, indices) = find_local_maxima(data_stdev, fields, groups)
    
    # Output key--value pairs:  (timestamp),(field header) \t (index of stdev peak),(stdev peak)
    for c in fields:
        if c not in indices: continue
        for idx in indices[c]:
            print(repr(data['Timestamp'][idx]) + ',' + repr(c) + '\t' + \
                  repr(idx) + ',' + repr(data_stdev[c][idx]))
    
if __name__ == "__main__":
    main()
