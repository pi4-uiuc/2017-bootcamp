#   Lesson 5:  Support vector machines


---

### Contents

-   [Introduction](#1)
-   [SVM for binary-class classification](#2)
-   [The kernel function](#3)
-   [SVM for three-class classification](#4)
-   [Exercise](#5)
-   [References](#6)
-   [Contributors](#7)


---

As usual, a standard header to load necessary libraries:

    import pandas as pd
    import numpy as np
    from sklearn import svm
    import matplotlib.pyplot as plt
    %matplotlib inline

##  [Introduction](#1)

"[Support vector machines](https://infogalactic.com/info/Support_vector_machines) are a set of supervised learning methods used for classification, regressions, and outliers detection."  ([`scikit-learn` documentation](http://scikit-learn.org/stable/modules/svm.html))

SVM approaches are good for high-dimensional spaces, even when there are more features than samples.

First we will load the data (using Pandas) and select the salient features we would like to base our assessment on.  We will use the wine data set you have encountered previously.

    data = pd.read_csv( './data_wine_complete.csv' )
    plt.plot( data[ 'Alcohol' ],data[ 'Flavanoids' ],'bo' )
    plt.xlabel( 'Alcohol level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'Scatter Diagram of Wine Data' )
    plt.show()


---

##  [SVM for binary-class classification](#2)

In order to prepare the data, we need to select out a subset of data; in this case, the first two wines.  We need to build a boolean mask in order to pick out these values:

    mask = ( data[ 'Y' ] == 1 ) | ( data[ 'Y' ] == 2 )
    traindata = data[ mask ][ data.columns[ [ 1,7 ] ] ]  # why nested brackets?
    plt.plot( traindata[ 'Alcohol' ],traindata[ 'Flavanoids' ],'ro' )
    plt.xlabel( 'Alcohol level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'Scatter Diagram of Wine Data' )
    plt.show()

Fit the SVM for classification:

    clf = svm.SVC( kernel='linear' )
    clf.fit( traindata,data[ mask ][ 'Y' ] )

Plot points along with a grid illustrating the regions identified by the SVM for each classification:

    X,Y = np.meshgrid( np.linspace( traindata[ 'Alcohol' ].min(),traindata[ 'Alcohol' ].max() ),np.linspace( traindata[ 'Flavanoids' ].min(),traindata[ 'Flavanoids' ].max() ) )
    X = X.ravel()
    X.shape = 2500,1
    Y = Y.ravel()
    Y.shape = 2500,1
    C = clf.predict( np.concatenate( ( X,Y ),axis=1 ) )

    fig,ax = plt.subplots()
    wine1data = traindata[ data[ 'Y' ] == 1 ]
    ax.plot( wine1data[ 'Alcohol' ],wine1data[ 'Flavanoids' ],'bo',label='Wine 1' )
    wine2data = traindata[ data[ 'Y' ] == 2 ]
    ax.plot( wine2data[ 'Alcohol' ],wine2data[ 'Flavanoids' ],'ro',label='Wine 2' )
    for i in range( len( C ) ):
        if C[ i ] == 1:
            ax.plot( X[ i ],Y[ i ],'b+' )
        else:
            ax.plot( X[ i ],Y[ i ],'r+' )
    plt.xlabel( 'Alcohol Level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'SVM Classification (Linear Kernel)' )
    plt.legend()
    plt.show()

Save the image so we can compare outcomes later.


---

##  [The kernel function](#3)

Sometimes the data cannot be seperated by linear functions. We can use kernel functions instead.  Here we demonstrate two additional types of kernel functions:  polynomial and gaussian.

###### Polynomial kernel function

Fit the SVM for classification:

    clf = svm.SVC( kernel='poly',degree=3 )
    clf.fit( traindata,data[ mask ][ 'Y' ] )

Plot points along with a grid illustrating the regions identified by the SVM for each classification:

    X,Y = np.meshgrid( np.linspace( traindata[ 'Alcohol' ].min(),traindata[ 'Alcohol' ].max() ),np.linspace( traindata[ 'Flavanoids' ].min(),traindata[ 'Flavanoids' ].max() ) )
    X = X.ravel()
    X.shape = 2500,1
    Y = Y.ravel()
    Y.shape = 2500,1
    C = clf.predict( np.concatenate( ( X,Y ),axis=1 ) )

    fig,ax = plt.subplots()
    wine1data = traindata[ data[ 'Y' ] == 1 ]
    ax.plot( wine1data[ 'Alcohol' ],wine1data[ 'Flavanoids' ],'bo',label='Wine 1' )
    wine2data = traindata[ data[ 'Y' ] == 2 ]
    ax.plot( wine2data[ 'Alcohol' ],wine2data[ 'Flavanoids' ],'ro',label='Wine 2' )
    for i in range( len( C ) ):
        if C[ i ] == 1:
            ax.plot( X[ i ],Y[ i ],'b+' )
        else:
            ax.plot( X[ i ],Y[ i ],'r+' )
    plt.xlabel( 'Alcohol Level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'SVM Classification (Polynomial Kernel)' )
    plt.legend()
    plt.show()

Again, save the image so we can compare outcomes later.

###### RBF kernel function

The [radial basis function (RBF) method](https://infogalactic.com/info/Radial_basis_function_kernel) provides an exponential basis for representing the classification.

Fit the SVM for classification:

    clf = svm.SVC( kernel='rbf' )
    clf.fit( traindata,data[ mask ][ 'Y' ] )

Plot points along with a grid illustrating the regions identified by the SVM for each classification:

    X,Y = np.meshgrid( np.linspace( traindata[ 'Alcohol' ].min(),traindata[ 'Alcohol' ].max() ),np.linspace( traindata[ 'Flavanoids' ].min(),traindata[ 'Flavanoids' ].max() ) )
    X = X.ravel()
    X.shape = 2500,1
    Y = Y.ravel()
    Y.shape = 2500,1
    C = clf.predict( np.concatenate( ( X,Y ),axis=1 ) )

    fig,ax = plt.subplots()
    wine1data = traindata[ data[ 'Y' ] == 1 ]
    ax.plot( wine1data[ 'Alcohol' ],wine1data[ 'Flavanoids' ],'bo',label='Wine 1' )
    wine2data = traindata[ data[ 'Y' ] == 2 ]
    ax.plot( wine2data[ 'Alcohol' ],wine2data[ 'Flavanoids' ],'ro',label='Wine 2' )
    for i in range( len( C ) ):
        if C[ i ] == 1:
            ax.plot( X[ i ],Y[ i ],'b+' )
        else:
            ax.plot( X[ i ],Y[ i ],'r+' )
    plt.xlabel( 'Alcohol Level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'SVM Classification (Gaussian Kernel)' )
    plt.legend()
    plt.show()

Finally, compare the three images to each other.


---

##  [SVM for three-class classification](#4)

How about classifying data points into three categories, or three-class classification?  Let's explore using different kernels for this case as well.

Set up the expanded data set:

    traindata = data[ data.columns[ [ 1,7 ] ] ]
    plt.plot( traindata[ 'Alcohol' ],traindata[ 'Flavanoids' ],'ro' )
    plt.xlabel( 'Alcohol level' )
    plt.ylabel( 'Flavanoids' )
    plt.title( 'Scatter Diagram of Wine Data' )
    plt.show()

Fit the SVMs for classification:

    clf_lin = svm.SVC( kernel='linear' )
    clf_lin.fit( traindata,data[ 'Y' ] )
    clf_pol = svm.SVC( kernel='poly',degree=3 )
    clf_pol.fit( traindata,data[ 'Y' ] )
    clf_rbf = svm.SVC( kernel='rbf' )
    clf_rbf.fit( traindata,data[ 'Y' ] )

Plot points along with a grid illustrating the regions identified by the SVM for each classification:

    X,Y = np.meshgrid( np.linspace( traindata[ 'Alcohol' ].min(),traindata[ 'Alcohol' ].max() ),np.linspace( traindata[ 'Flavanoids' ].min(),traindata[ 'Flavanoids' ].max() ) )
    X = X.ravel()
    X.shape = 2500,1
    Y = Y.ravel()
    Y.shape = 2500,1
    C_lin = clf_lin.predict( np.concatenate( ( X,Y ),axis=1 ) )
    C_pol = clf_pol.predict( np.concatenate( ( X,Y ),axis=1 ) )
    C_rbf = clf_rbf.predict( np.concatenate( ( X,Y ),axis=1 ) )

    fig,axes = plt.subplots( 1,3 )
    for ax,C in zip( axes,[ C_lin,C_pol,C_rbf ] ):
        wine1data = traindata[ data[ 'Y' ] == 1 ]
        ax.plot( wine1data[ 'Alcohol' ],wine1data[ 'Flavanoids' ],'bo',label='Wine 1' )
        wine2data = traindata[ data[ 'Y' ] == 2 ]
        ax.plot( wine2data[ 'Alcohol' ],wine2data[ 'Flavanoids' ],'go',label='Wine 2' )
        wine3data = traindata[ data[ 'Y' ] == 3 ]
        ax.plot( wine3data[ 'Alcohol' ],wine3data[ 'Flavanoids' ],'ro',label='Wine 3' )
        for i in range( len( C ) ):
            if C[ i ] == 1:
                ax.plot( X[ i ],Y[ i ],'b+' )
            elif C[ i ] == 2:
                ax.plot( X[ i ],Y[ i ],'g+' )
            else:
                ax.plot( X[ i ],Y[ i ],'r+' )
        plt.xlabel( 'Alcohol Level' )
        plt.ylabel( 'Flavanoids' )
    plt.legend()
    plt.show()


---

##  [Exercise](#5)

**Exercise**:  Use the `sklearn` built-in dataset representing hand-written digits to build a predictive SVM.  Use the first 90% of the database to train the SVM and the last 10% to test it.  Try various kernels to see which one yields the best performance.

    from sklearn import datasets
    datasets.load_digits()
    digits = datasets.load_digits()
    plt.imshow( digits.images[ 5 ],cmap=plt.cm.gray_r )
    plt.show()

(`digits.target` contains the labels.)


---

##  [References](#6)

-   [`scikit-learn` Lectures Notes on SVMs for Classification](http://www.scipy-lectures.org/advanced/scikit-learn/#support-vector-machines-svms-for-classification)
-   [Support Vector Machines in MATLAB](http://www.mathworks.com/help/stats/support-vector-machines-svm.html)
-   [Support Vector Machines in Python with `scikit-learn`](http://scikit-learn.org/stable/modules/svm.html)


---

##  [Contributors](#7)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
