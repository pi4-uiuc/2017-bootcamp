#   Lesson 2:  Principal component analysis


---

### Contents

-   [Introduction](#1)
-   [Data access and data description](#2)
-   [PCA Implementation](#3)
-   [Example:  Iris data](#4)
-   [References](#5)
-   [Contributors](#6)


---

As usual, a standard header to load necessary libraries:

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    %matplotlib inline

##  [Introduction](#1)

Principle component analysis (PCA) is a well-known technique for reducing the number of dimensions in a data set.  PCA takes a linear transformation of features of the original dataset to reduce dimensionality.

The steps associated with PCA are:

1.  feature scaling

2.  get covariance matrix of the scaled features

3.  calculate eigenvalues and eigenvectors of covariance matrix

4.  choose eigenvalues and eigenvectors

5.  compute dimension-reduced data

You can think of this as an orthogonalization followed by a culling of low-weight values.  (*Compressed sensing* is related, but is predicated on reconstructing a randomly sampled signal.)

We will utilize a well-known standard data set describing chemical tests on wine.  The data set contains 130 measurements of wine organized as a comma-separated value (CSV) file with the fields `Alcohol`, `MalicAcid`, `Ash`, etc.  Load the data with the Pandas function `read_csv`:

    data = pd.read_csv( './data_wine.csv' )


---

##  [Data access and data description](#2)

Let's pull some features of the data set out for separate analysis:

    labels = list( data.columns )

    # a little bit of cleaning is necessary
    for column in data.columns:
        data = data.rename( columns={ column:column.strip() } )

Observe the first six rows to get a cursory notion of the values and ranges of the measurements.

    data.loc[ :6,: ]


---

##  [PCA implementation](#3)


### 1.  Feature scaling

We use the *standardization method*, in which we rescale quantities to be of the same relative order of magnitude.  This reduces the likelihood that important quantities of a small range and order of magnitude will be masked by relatively less important larger values.

Consider, for instance, how the coefficients of a polynomial must become vastly smaller to produce commensurate effects for values much distant from $10^0$.  This can make it difficult to judge if a term is significant or not.

The [$z$-score](https://infogalactic.com/info/Standard_score) normalizes the data against a mean of zero and a standard deviation of one.

$$
x'_i
=
\frac{x_i-\bar{x}}{\sigma_x}
$$

We shouldn't rescale values that aren't numerically commensurable, such as labels or text; in this case, the field `Category`.

    def zscore( value ):
        result = ( value - value.mean() ) / value.std()
        return result

    data_scaled = zscore( data.loc[ :,'Alcohol':'Proline' ] )
    data_scaled.insert( 0,'Category',data[ 'Category' ] )

Compare the data before and after:

    data.plot()
    plt.show()

    data_scaled.plot()
    plt.show()


### 2.  Obtain covariance matrix

The [covariance matrix](https://infogalactic.com/info/Covariance_matrix) is trivial to obtain:

    covMatrix = data_scaled.loc[ :,'Alcohol':'Proline' ].cov()

(This is related to the correlation coefficient matrix obtained in `lesson01`.)

    plt.imshow( data_scaled.cov() )
    plt.show()

    from biokit.viz import corrplot
    ax = corrplot.Corrplot( data_scaled.cov().loc[ :,'Alcohol':'Proline' ] )
    ax.plot()
    plt.show()


### 3.  Obtain eigenvalues and eigenvectors of covariance matrix

Again, this step is trivial in modern systems:

    from numpy.linalg import eig
    eigV = eig( covMatrix )
    eigVal = eigV[ 0 ]
    eigVec = eigV[ 1 ]

-   What are the return values of `eig`?  How do you access each piece?
-   Are the eigenvalues already sorted?


### 4.  Select eigenvalues and eigenvectors

Some eigenvectors carry a significant amount of information about this system; others almost none.  In order to reduce our dimensionality to something more manageable, we need to select a threshold either by number of vectors we can use or by the lowest acceptable eigenvalue.

In this case, let's keep 80% of our information.  This looks like:

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

### 5.  Compute dimension-reduced data

Finally, use the PCA eigenvectors to produce the reduced-dimensional data set:

    data_array = data_scaled.loc[ :,'Alcohol':'Proline' ].as_matrix()
    data_pca = data_array.dot( eigVec_pca )
    plt.plot( data_pca[ :,0 ],data_pca[ :,1 ],'bo' )
    plt.show()


---

##  [Example:  Iris data](#4)

Now you have an opportunity to perform PCA on a fresh data set.

    iris = pd.read_csv( './data_iris.csv' )

Examine the data set:

    from mpl_toolkits.mplot3d import Axes3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter( xs,ys,zs,'ro' )
    ax.set_xlabel( 'sepal length' )
    ax.set_ylabel( 'sepal width' )
    ax.set_zlabel( 'petal length' )
    plt.title( 'Iris Features' )
    plt.show()

Proceed to reduce the data set from 3D to 2D, then plot again:

    fig,ax = plt.subplots()
    data_pca.plot()
    ax.set_xlabel( 'PCA1' )
    ax.set_ylabel( 'PCA1' )
    plt.title( 'Iris Features' )
    plt.show()


---

##  [References](#5)

-   [Principal component analysis](https://infogalactic.com/info/Principal_component_analysis)


---

##  [Contributors](#6)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
