#   Lesson 1:  Data access and data cleaning


---

### Contents

-   [Data description and data access](#1)
-   [Data cleaning](#2)
-   [Basic statistical analysis](#3)
-   [Data smoothing](#4)
-   [Correlation between different variables](#5)
-   [Contributors](#6)


---

First, a standard header to load necessary libraries:

    import pandas as pd
    import matplotlib.pyplot as plt
    %matplotlib inline

##  [Data description and data access](#1)

We will utilize weather data for the Coleto Creek Reservoir from 2003–14, provided by the [National Oceanic and Atmospheric Administration (NOAA)](https://www.noaa.gov/).  The data set contains 4,197 daily weather observations of evaporation–transpiration, precipitation, and temperature extremes.

![](http://water.weather.gov/ahps2/images/hydrograph_photos/ckdt2/dsc00171.jpg)

The data set is organized as a comma-separated value (CSV) file with the fields `LATITUDE`, `LONGITUDE`, `DATE`, `ET`, `PRCP`, `TMAX`, `TMIN`.  Pandas provides a spreadsheet-like or database-like window on the data structure.  We will load the data with the Pandas function `read_csv`:

    data = pd.read_csv( './data_ColetoCreek.csv' )

The data structure itself is what Pandas calls a `DataFrame`.  Again, think of a spreadsheet containing columns of data.  These columns are Pandas `Series` and can be accessed by their column header:

    type( data )
    type( data[ 'TMAX' ] )


---

##  [Data cleaning](#2)

Many of the observations included in this data set as raw data are incomplete—in other words, the raw data contain missing values and outliers.  These can be troublesome since the format of missing data can vary widely—for instance, `0`, `NaN`, `""`, `NULL`, and `-9999` all occur in practice—and so we commonly need to clean data by either removing entries, standardizing missing values to a useful default, or interpolating values (only if necessary and done carefully!).

In this tutorial, we will focus on `TMAX` and `TMIN` data to demonstrate how to clean data of missing values and outliers.  First, let's examine the distribution of `TMAX` values.

    plt.figure()
    data[ "TMAX" ].plot.hist()
    plt.xlabel( 'Temperature' )
    plt.ylabel( 'n' )
    plt.show()

    data[ "TMIN" ].plot.hist()
    plt.show()

For this particular data set, missing values are represented by `-9999`.  We need to filter out these rows and handle the values in a more transparent way.  We could either replace the values with non-calculating values (like `NaN`), or remove the lines directly.  In this case, we will remove the lines directly, but I'll show you as well how the first approach works.

    data[ "TMAX" ].plot.hist()
    plt.show()

    data[ "TMAX" ] = data[ "TMAX" ].dropna()  # this doesn't work; why?
    data[ "TMAX" ] = data[ "TMAX" ].drop( data[ "TMAX" ].index[ data.TMAX == -9999 ] )
    data[ "TMIN" ] = data[ "TMIN" ].drop( data[ "TMIN" ].index[ data.TMIN == -9999 ] )

    data = data.dropna( subset=[ 'TMAX','TMIN' ] )

What else could need checking in this database for $T_\textrm{min}$ and $T_\textrm{max}$?  Let's make sure they are ordered properly.  (Note that we can access a column then a row, or a row then a column.)  Simply find and swap any cases where this occurs:

    for i in data[ data[ "TMAX" ] < data[ "TMIN" ] ].index:
        data.loc[ i,[ "TMAX","TMIN" ] ] = data.loc[ i,[ "TMIN","TMAX" ] ].values  # first w/o .values

Oops, that gives us the persistent problem that DataFrames don't like to change their values.  Explicitly, if you mutate data, Pandas generates a copy.  Thus the `values` method at the end there.

Now plot the histogram of temperature data again:

    plt.figure()
    data[ "TMAX" ].plot.hist( bins=50 )
    data[ "TMIN" ].plot.hist( bins=50 )
    plt.xlabel( 'Temperature' )
    plt.ylabel( 'n' )
    plt.legend()
    plt.show()

Next, what's going on with the scale?  Well, it turns out that the values are stored in tenths of a degree centigrade, which allows them to be stored without a decimal point.  Let's fix that as well:

    data[ "TMAX" ] /= 10
    data[ "TMIN" ] /= 10

Given the correct range and cleaned data values, now examine the time series form:

    plt.figure()
    data.plot( data[ "DATE" ],data[ "TMAX" ],'b.' )  # try this first
    data.plot( "DATE","TMIN",color='orange',marker='.',linestyle='' )
    plt.xlabel( 'Time series' )
    plt.ylabel( 'Temperature' )
    plt.legend()
    plt.show()

-   Why are the values clustered apart from each other?  We'll need to convert that column (`DATE`) to a Python `datetime` representation:

        data[ "DATE" ] = pd.to_datetime( data["DATE"],format="%Y%m%d" )

    Try again:

        fig,ax = plt.subplots()
        for series in zip( [ "TMAX","TMIN" ],[ "blue","orange" ] ):
            ax.plot( data[ "DATE" ],data[ series[ 0 ] ],color=series[ 1 ],marker='.',linestyle='' )
        plt.legend()
        plt.xlabel( 'Time series in year 2008 / day' )
        plt.ylabel( 'Temperature / C' )
        plt.show()

Also check the box plot distribution form:

    plt.figure()
    data.boxplot( column=[ "TMAX","TMIN" ] )
    plt.ylabel( 'Temperature' )
    plt.legend()
    plt.show()


---

##  [Basic statistical analysis](#3)


In this section, we will show you how to perform some basic statistical
analysis of the dataset.  This will help us diagnose any additional basic features.  As an example, select year 2008.

    import datetime
    year = 2008
    data_year = data[ data[ "DATE" ] < datetime.datetime( year+1,1,1 ) ][ data[ "DATE" ] >= datetime.datetime( year,1,1 ) ]

    fig,ax = plt.subplots()
    for series in zip( [ "TMAX","TMIN" ],[ "blue","orange" ] ):
        ax.plot( data_year[ "DATE" ],data_year[ series[ 0 ] ],color=series[ 1 ],marker='.',linestyle='' )
    plt.legend()
    plt.xlabel( 'Time series in year 2008 / day' )
    plt.ylabel( 'Temperature / C' )
    plt.show()

Locate the extremes---the hottest and the coldest day in the year.

    data_year[ "TMAX" ].max()
    data_year[ "TMAX" ].idxmax()
    data_year.loc[ data_year[ "TMAX" ].idxmax() ][ "DATE" ]

    data_year[ "TMIN" ].min()
    data_year[ "TMIN" ].idxmin()
    data_year.loc[ data_year[ "TMIN" ].idxmin() ][ "DATE" ]

We can also find the days in which the maximum temperature exceeds 35 °C.

    hot = data_year[ data_year[ "TMAX" ] > 35 ]
    hot.plot.bar( "DATE","TMAX" )
    plt.legend()
    plt.xlabel( 'day' )
    plt.ylabel( 'Temperature / C' )
    plt.title( 'Max T exceeds 35 °C' )
    plt.show()


---

##  [Data smoothing](#4)

Data smoothing is an important way to see general patterns
associated with a dataset.  Noisy data tend to obscure the visibility of trends.  In this section, we will introduce several data smoothing functions available in Pandas.

Some of these rely on the concept of a _rolling window_, in which a sample of several neighboring values is used to determine the behavior at a given point in time.  Others are sampling filters used in signal processing applications.

First, let's examine the _rolling mean_ and _rolling standard deviation_.  These are built into Pandas.

    n = 11
    data_year[ "TMAXR" ] = pd.rolling_mean( data_year[ "TMAX" ],n )
    std = pd.rolling_std( data_year[ "TMAX" ],n )
    fig,ax = plt.subplots()
    ax.plot( data_year[ "DATE" ],data_year[ "TMAX" ],color="blue",marker='.',linestyle='' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXR" ],color="darkblue",marker='',linestyle='-' )
    ax.plot( data_year[ "DATE" ],std,color="darkblue",marker='',linestyle='--' )
    plt.show()

-   Why are there gaps in the rolling mean?

-   How sensitive is the system to the value of `n`?

We can use these together to build a very nice profile plot:

    n = 11
    data_year[ "TMAXR" ] = pd.rolling_mean( data_year[ "TMAX" ],n )
    std = pd.rolling_std( data_year[ "TMAX" ],n )
    data_year[ "TMAXRP" ] = data_year[ "TMAXR" ] + std
    data_year[ "TMAXRM" ] = data_year[ "TMAXR" ] - std
    fig,ax = plt.subplots()
    ax.plot( data_year[ "DATE" ],data_year[ "TMAX" ],color="blue",marker='.',linestyle='' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXR" ],color="darkblue",marker='',linestyle='-' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXRP" ],color="darkblue",marker='',linestyle='--' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXRM" ],color="darkblue",marker='',linestyle='--' )
    plt.legend()
    plt.xlabel( 'Time series / day' )
    plt.ylabel( 'Temperature / C' )
    plt.show()

Next, let's use some low-pass filtering to smooth the data.  (Low-pass filters only pass signal components that are below a threshold frequency.  This helps because noise tends to look like high-frequency variability.)  The Savitsky–Golay filter is well known:

    import scipy.signal as sps
    n = 5  # 17, etc.
    data_year[ "TMAXG" ] = sps.savgol_filter( [ data_year[ "TMAX" ] ],n,3 )[ 0 ]
    fig,ax = plt.subplots()
    ax.plot( data_year[ "DATE" ],data_year[ "TMAX" ],color="blue",marker='.',linestyle='' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXG" ],color="cornflowerblue",marker='',linestyle='-' )
    plt.show()


Thirdly, we use a [forward–backward filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.filtfilt.html) to smooth the data.  (This technique applies a linear filter once forward and once backward to remove offset.  Note that the rolling mean, for instance, tends to lag the signal in time series.)  Since we need to use a filtering algorithm with this, we'll introduce the [Butterworth](https://infogalatic.com/info/Butterworth_filter) [filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html#scipy.signal.butter), which is designed to be as "flat" as possible.

    import scipy.signal as sps
    n = 5  # 17, etc.
    b,a = sps.butter( n,0.125 )
    data_year[ "TMAXF" ] = sps.filtfilt( b,a,data_year[ "TMAX" ],padlen=150 )
    fig,ax = plt.subplots()
    ax.plot( data_year[ "DATE" ],data_year[ "TMAX" ],color="blue",marker='.',linestyle='' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXF" ],color="seagreen",marker='',linestyle='-' )
    plt.show()


Finally, we can compare the original data with each of the smoothed data methods:

    fig,ax = plt.subplots()

    ax.plot( data_year[ "DATE" ],data_year[ "TMAX" ],color="blue",marker='.',linestyle='' )

    ax.plot( data_year[ "DATE" ],data_year[ "TMAXR" ],color="darkblue",marker='',linestyle='-' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXRP" ],color="darkblue",marker='',linestyle='--' )
    ax.plot( data_year[ "DATE" ],data_year[ "TMAXRM" ],color="darkblue",marker='',linestyle='--' )

    ax.plot( data_year[ "DATE" ],data_year[ "TMAXG" ],color="cornflowerblue",marker='',linestyle='-' )

    ax.plot( data_year[ "DATE" ],data_year[ "TMAXF" ],color="seagreen",marker='',linestyle='-' )

    plt.legend()
    plt.xlabel( 'Time series / day' )
    plt.ylabel( 'Temperature / C' )
    plt.title( 'data_year Smoothing Comparison' )
    plt.show()

-   How can we quantify the "goodness" of these smooth sets?  [differentiability,residuals]


---

## [Correlation between different variables](#5)

Correlation can help us understand the relationship between different
variables.  For variables $x$ and $y$, correlation $\rho$ can be computered
as:

$$
\rho_{x,y}
=
\frac{E[x-\mu_x][y-\mu_y]}{\sigma_{x}\sigma_{y}}
$$

Let's see the correlation of maximum temperature, minimum temperature and E–T:

    data_restrict = data.loc[ :,"DATE":"TMIN"]
    data_restrict.corr()
    plt.imshow( data_restrict.corr() )
    plt.show()

If you are willing to install some other packages, there are some nice visualizations available:

    from biokit.viz import corrplot
    ax = corrplot.Corrplot( data_restrict.corr() )
    ax.plot()
    plt.show()

`TMAX` and `TMIN` are clearly correlated with each other, while they are not
correlated with `EVAP`.

Now we want to see if the `TMAX` of one day is correlated with the `TMAX` of other days.

    data_tmax = data.loc[ :,[ "TMAX" ] ]
    for i in range( 1,5 ):
        data_tmax[ "TMAX%s"%i ] = data_tmax[ "TMAX" ].shift( -i )
    data_tmax = data_tmax[ :-4 ]
    data_tmax.corr()

    ax = corrplot.Corrplot( data_tmax.corr() )
    ax.plot()
    plt.show()

Clearly `TMAX` values become less correlated as time lag increases.

    data_tmax = data.loc[ :,[ "TMAX" ] ]
    n = 30
    for i in range( 1,n ):
        data_tmax[ "TMAX%i"%i ] = data_tmax[ "TMAX" ].shift( -i )
    data_tmax = data_tmax[ :-(n-1) ]

    data_tmax.corr().plot(marker='+',linestyle='')
    plt.xlabel('Time lag (day)')
    plt.ylabel('Correlation')
    plt.show()


---

##  [Contributors](#6)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
