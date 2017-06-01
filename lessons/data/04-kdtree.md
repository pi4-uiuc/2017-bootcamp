#   Lesson 4:  $k$-d tree for classification and regression


---

### Contents

-   [Introduction](#1)
-   [Example:  Online news data](#2)
-   [Fitting a classification tree from an original data set](#3)
-   [Fitting a classification tree from PCA](#4)
-   [References](#5)
-   [Contributors](#6)


---

As usual, a standard header to load necessary libraries:

    import pandas as pd
    import numpy as np
    from scipy import spatial
    import matplotlib.pyplot as plt
    %matplotlib inline

##  [Introduction](#1)

[$k$-d trees](https://infogalactic.com/info/K-d_tree) partition $k$-dimensional space in order to organize points and data access.  They are particularly apt for multidimensional key searches.  Today we will use a $k$-d tree for identifying similarity of values based on their parameterized description.


---

##  [Example:  Online news data](#2)

The University of California—Irvine provides [a collection of standard data sets](http://archive.ics.uci.edu/ml/datasets/Online+News+Popularity) suitable for machine learning and data mining applications.  We will use a data set containing a summary of articles published by [Mashable](https://mashable.com/).  The data file contains 39,644 rows and 61 columns (corresponding to 58 predictive attributes, 2 non-predictive attributes and 1 numerical label about article popularity).  The source website contains more information (about dates, content, etc.).

We will use Pandas to represent the data, and SciPy to provide the $k$-d tree data structure and processing.

    data = pd.read_csv( './data_OnlineNewsPopularity.csv' )

-   How can you check what the column headers are labeled as?  What about the basic range and order-of-magnitude of the entries?

We will transform the original (numerical) labels to binary labels. Each article will be designated as either popular (label is more than median value, indicated by `True`), or not popular (label is less than median value, indicated by `False`).

    values = data.median()
    # What is the data type of `values`?

    pop = data.copy()
    for label in values.keys():
        pop[ label ] = data[ label ] > values[ label ]


---

##  [Fitting a classification tree from an original data set](#3)

To construct a $k$-d tree using SciPy:

    tree = spatial.KDTree( pop.loc[ :,' timedelta':' shares' ] )

There's not a really great tool in Python for visualizing this tree (although generally one can use `pygraphviz`), but in MATLAB it looks something like this:

Although Python makes visualization of the tree challenging in this case, here is what the equivalent structure looks like in MATLAB:

![](Demo4_ML_Tree_02.png)

You can tune the number of leaves from each node using a second parameter in `spatial.KDTree`, although quantifying the relative efficiency is a drawn-out process.  From the [SciPy documentation](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.KDTree.html):

> High-dimensional nearest-neighbor queries are a substantial open problem in computer science.

We can construct an array of trees and compare their relative performance for lookups.  First, we will sample a subset of the overall data set for efficiency in timing (since this can be a time-intensive process).

    n = 1000
    pop_sample = pop.sample( n=n )

    leaves = [ 1,2,4,10,20,50,100 ]
    trees = []
    for leaf in leaves:
        itree = spatial.KDTree( pop_sample.loc[ :,' timedelta':' shares' ],leafsize=leaf )
        trees.append( itree )

    for i,tree in enumerate( trees ):
        %timeit tree.query_pairs( 2.0 )

This will take quite a while (several minutes on my machine).

    1 loop, best of 3: 52.2 s per loop
    1 loop, best of 3: 31.2 s per loop
    1 loop, best of 3: 16.3 s per loop
    1 loop, best of 3: 5.49 s per loop
    1 loop, best of 3: 2.21 s per loop
    1 loop, best of 3: 1.13 s per loop
    1 loop, best of 3: 601 ms per loop

-   Do other operations show a similar or opposite trend?

$k$-d trees can become unbalanced.  They tend to be more effective tools when you don't know the underlying data distribution.


---

##  [Fitting a classification tree from PCA](#4)

Right now the dataset has 53 dimensions.  With PCA, we can reduce this to 27 while maintaining 80% of our accuracy:

    covMatrix = pop.loc[ :,' timedelta':' shares' ].cov()

    from numpy.linalg import eig
    eigV = eig( covMatrix )
    eigVal = eigV[ 0 ]
    eigVec = eigV[ 1 ]

    info = 0.80
    sortedValue = sorted( eigVal,reverse=True )
    sortedIndex = sorted( range( len( eigVal ) ), key=lambda k:eigVal[ k ],reverse=True)

    fig,ax = plt.subplots()
    ax.plot( range( 1,len( sortedValue )+1 ),np.cumsum( sortedValue ) / np.sum( sortedValue ),'mo--',linewidth=2 )
    ax.plot( range( 1,len( sortedValue )+1),np.ones( len( sortedValue ) )*info,'b-' )
    plt.xlabel('Number of principal components')
    plt.ylabel('Percentage of information (%)')
    plt.show()

Filter out the indices corresponding to the eigenvalues required to hit this information carrying capacity:

    eigIDs = []
    for i in range( 0,len( sortedValue ) ):
        if sum( sortedValue[ 0:i+1 ] ) / sum( sortedValue ) > info:
            eigIDs = sortedIndex[ 0:i+1 ]
            break

    eigVal_pca = eigVal[ eigIDs ]
    eigVec_pca = eigVec[ :,eigIDs ]

Use the PCA eigenvectors to produce the reduced-dimensional data set:

    data_array = pop.loc[ :,' timedelta':' shares' ].as_matrix()
    data_pca = data_array.dot( eigVec_pca )
    plt.plot( data_pca[ :,0 ],data_pca[ :,1 ],'bo' )
    plt.show()

Finally, construct the $k$-d tree from the PCA data:

    pca_tree = spatial.KDTree( data_pca )

To quantify how much "better" this tree is, we can carry out time trials:

    %timeit pca_tree.query_ball_point( np.ones((1,27))*True,5 )
    %timeit tree.query_ball_point( np.ones((1,27))*True,5 )

or figure out the relative error rate.

-   How could we measure the error rate?


##  [References](#5)

-   K. Fernandes, P. Vinagre and P. Cortez.  (2015)  A Proactive Intelligent Decision Support System for Predicting the Popularity of Online News. *Proceedings of the 17th EPIA 2015 (Portuguese Conference on Artificial
Intelligence)*.  Coimbra, Portugal.


---

##  [Contributors](#6)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
