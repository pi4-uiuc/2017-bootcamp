#   Lesson 7:  $k$-Means Clustering


---

### Contents

-   [Introduction](#1)
-   [$k$-means clustering method](#2)
-   [Evaluation:  silhouette method](#3)
-   [Evaluation:  gap statistics method](#4)
-   [Conclusion](#5)
-   [Contributors](#6)


---

First, a standard header to load necessary libraries:

    import numpy as np
    from numpy import random as npr
    import matplotlib.pyplot as plt
    import matplotlib.cm as cm
    %matplotlib inline

##  [Introduction](#1)

Clustering analysis is a type of unsupervised learning.  Two common methods will be examined:  $k$-means and hierarchical clustering.  In this section, we will be introducing the $k$-means method as well as criteria to evaluate the performance of clustering.

We will generate a clean random data set to demonstrate the technique initially.

    k = 3       # number of clusters
    n = 50      # number of points per cluster

    sigma = 0.4 # stdev of cluster
    centers = [ ( 0,1 ),( 1,0 ),( -0.5,-0.5 ) ]

    samples = np.zeros( ( k*n,2 ) )
    for index,center in enumerate( centers ):
        samples[ index*n:( index+1 )*n,: ] = npr.randn( n,2 ) * sigma + center

    fig,ax = plt.subplots()
    for index,mrkr in enumerate( [ 'bo','ro','go' ] ):
        data = samples[ index*n:( index+1 )*n,: ]
        ax.plot( data[ :,0 ],data[ :,1 ],mrkr )
    plt.title( 'Original Data' )
    plt.show()

    fig,ax = plt.subplots()
    plt.plot( samples[ :,0 ],samples[ :,1 ],'ko' )
    plt.title( 'Original Data' )
    plt.show()


---

##  [$k$-means clustering method](#2)

[$k$-means clustering](https://infogalactic.com/info/K-means_clustering) takes a set of observations or samples and attempts to partition them into $k$ groups or clusters.  Obviously different values of $k$ will yield different clusters.

$k$ centroids are randomly chosen in the domain*.  Clusters are created by associating every observation with the nearest centroid.  The new centroid of this updated cluster is then used, and the process proceeds iteratively to convergence.  Conveniently, cluster centroids can be suggested as well to "seed" the algorithm with suggestions from a human observer.

*:  Specifically, the algorithm is reinitialized several times with random centroids and the best fit of several is returned.

**$k$ = 2**:

    from sklearn.cluster import KMeans

    k = 2
    est = KMeans( n_clusters=k )
    est.fit( samples )
    labels = est.labels_

    fig,ax = plt.subplots()
    data0 = samples[ labels == 0 ]
    ax.plot( data0[ :,0 ],data0[ :,1 ],'bo' )
    data1 = samples[ labels == 1 ]
    ax.plot( data1[ :,0 ],data1[ :,1 ],'ro' )
    plt.title( 'Clustered data, k = %i'%k )
    plt.show()

    fig,ax = plt.subplots()
    ax.plot( data0[ :,0 ],data0[ :,1 ],'bo' )
    ax.plot( data1[ :,0 ],data1[ :,1 ],'ro' )
    for index,mrkr in enumerate( [ 'bx','rx','gx' ] ):
        data = samples[ index*n:( index+1 )*n,: ]
        ax.plot( data[ :,0 ],data[ :,1 ],mrkr )
    plt.title( 'Clustered data, k = %i'%k )
    plt.show()


**$k$ = 3**:

    k = 3
    est = KMeans( n_clusters=k )
    est.fit( samples )
    labels = est.labels_

    fig,ax = plt.subplots()
    colors = [ 'bo','ro','go','mo','yo','co','ko' ]
    for i in range( k ):
        data = samples[ labels == i ]
        ax.plot( data[ :,0 ],data[ :,1 ],colors[ i ] )
    plt.title( 'Clustered data, k = %i'%k )
    plt.show()

    fig,ax = plt.subplots()
    for i in range( k ):
        data = samples[ labels == i ]
        ax.plot( data[ :,0 ],data[ :,1 ],colors[ i ] )
    for index,mrkr in enumerate( [ 'bx','rx','gx' ] ):
        data = samples[ index*n:( index+1 )*n,: ]
        ax.plot( data[ :,0 ],data[ :,1 ],mrkr )
    plt.title( 'Clustered data, k = %i'%k )
    plt.show()

Try $k \in \{ 4..7 \}$ to explore how the model responds.  (The colour vector doesn't contain more entries than seven however.)

To get the cluster centroids, use `est.cluster_centers_`.

To specify the number of cluster centers, use `est = KMeans( n_cluster=k,)`

To predict the association of new values, use `est.predict()`:

    X,Y = np.meshgrid( np.linspace( samples[ :,0 ].min(),samples[ :,0 ].max() ),np.linspace( samples[ :,1 ].min(),samples[ :,1 ].max() ) )
    X = X.ravel()
    X.shape = len( X ),1
    Y = Y.ravel()
    Y.shape = len( Y ),1
    C = est.predict( np.concatenate( ( X,Y ),axis=1 ) )

    fig,ax = plt.subplots()
    colors = [ 'bo','ro','go','mo','yo','co','ko' ]
    for i in range( k ):
        data = samples[ labels == i ]
        ax.plot( data[ :,0 ],data[ :,1 ],colors[ i ] )
    colors = [ 'b+','r+','g+','m+','y+','c+','k+' ]
    for i in range( len( C ) ):
        ax.plot( X[ i ],Y[ i ],colors[ C[ i ] ] )
    plt.title( 'Clustered data, k = %i'%k )
    plt.show()

-   Compare the relative speed of $k$-means clustering prediction to SVM prediction.


---

##  [Evaluation:  silhouette method](#3)

Since any $k$ yields results, we need a way to determine which set of clusters is the "best", by whatever metric.  For instance, if outside criteria dictate some number of categories, then $k$ is fixed by the external factors.  But if we are mining data abstractly, how do we distinguish the goodness of fit for several $k$s?

The silhouette method assigns a figure of merit for the separation distance between clusters.  Silhouette coefficients are in the range $[ -1,+1 ]$; positive values indicate samples are far from cluster boundaries, values near zero indicate samples are near or on boundaries, and negative values indicate that the samples may have been assigned to the wrong cluster.  (In other words, a value closer to +1 is indicative of a better fit for the particular value of $k$.)  (Note that most of the following block is plotting code.)

    from sklearn.metrics import silhouette_samples, silhouette_score

    k_candidates = list( range( 2,8 ) )

    s_values = np.zeros( ( len( k_candidates ),1 ) )

    for k in k_candidates:
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # silhouette plot
        ax1.set_xlim( [ -1,1 ] )
        ax1.set_ylim( [ 0,len( samples )+( k+1 )*10 ] )

        est = KMeans( n_clusters=k )
        C_labels = est.fit_predict( samples )

        # average silhouette score per k
        silhouette_avg = silhouette_score( samples,C_labels )
        print( "k = %d yields average silhouette_score = %f."%( k,silhouette_avg ) )

        # silhouette scores for each sample
        sample_silhouette_values = silhouette_samples( samples,C_labels )

        ## plot of silhouette scores
        y_lower = 10
        for i in range( k ):
            # aggregate silhouette scores for samples in cluster i
            ith_cluster_silhouette_values = sample_silhouette_values[ C_labels == i ]
            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[ 0 ]
            y_upper = y_lower + size_cluster_i

            color = cm.spectral( float( i ) / k )
            ax1.fill_betweenx( np.arange( y_lower,y_upper ),0,ith_cluster_silhouette_values,facecolor=color,edgecolor=color,alpha=0.7 )

            # label by cluster number
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # compute y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title( "The silhouette plot for the various clusters." )
        ax1.set_xlabel( "The silhouette coefficient values" )
        ax1.set_ylabel( "Cluster label" )

        # average silhouette score as vertical line
        ax1.axvline( x=silhouette_avg,color='red',linestyle='--' )

        ax1.set_yticks( [] )    # clear y-axis labels/ticks
        ax1.set_xticks( np.linspace( -1,1,11 ) )

        ## plot of clusters
        colors = cm.spectral( C_labels.astype( float ) / k )
        ax2.scatter( samples[ :,0 ],samples[ :,1 ],marker='.',s=30,lw=0,alpha=0.7,c=colors )

        # label clusters with white circles and numbers
        centers = est.cluster_centers_
        ax2.scatter( centers[ :,0 ],centers[ :,1 ],marker='o',c="white",alpha=1,s=200 )
        for i,c in enumerate( centers ):
            ax2.scatter( c[ 0 ],c[ 1 ],marker='$%d$'%i,alpha=1,s=50 )

        ax2.set_title( "The visualization of the clustered data." )
        ax2.set_xlabel( "Feature space for the 1st feature" )
        ax2.set_ylabel( "Feature space for the 2nd feature" )

        plt.suptitle( ( "Silhouette analysis for KMeans clustering on sample data with n_clusters = %d"%k ),fontsize=14,fontweight='bold' )
        plt.show()


---

##  [Evaluation:  gap statistics method](#4)

The gap statistics method similarly assigns a figure of merit for the separation distance between clusters.  The gap statistic method seeks to maximize the gap statistic, or the spacing (gap) between clusters.  Since a `scikit-learn`-native gap statistic method has not been implemented, we will use [Miles Granger's implementation](https://github.com/milesgranger/gap_statistic).  At a new instance of the command line, enter

    pip install git+git://github.com/milesgranger/gap_statistic.git

Once that package has been installed, return to the Python instance you were using previously.

    from gap_statistic import optimalK

    k_candidates = list( range( 2,8 ) )

    n,gapdf = optimalK( samples,nrefs=3,maxClusters=k_candidates[ -1 ] )

    plt.plot( gapdf.clusterCount,gapdf.gap,linewidth=3 )
    plt.scatter( gapdf[ gapdf.clusterCount == n ].clusterCount,gapdf[ gapdf.clusterCount == n ].gap,s=250,c='r' )
    plt.xlabel('Cluster Count')
    plt.ylabel('Gap Value')
    plt.title('Gap Values by Cluster Count')
    plt.show()

In this case, the two methods are in agreement that three clusters best describe the underlying data set.


---

##  [Conclusion](#5)

$k$-means clustering is a crude but easily implemented heuristic, and sometimes does surprisingly well.  A brief analysis of its practical limits is available with [the `scikit-learn` documentation](http://scikit-learn.org/stable/auto_examples/cluster/plot_kmeans_assumptions.html#sphx-glr-auto-examples-cluster-plot-kmeans-assumptions-py).

-   Examine the satellite data $k$-means clustering example in `satellite.ipynb`.  Once a suitable $k$ has been identified for detecting, say, snow cover or cloud cover, how transferable is that $k$ between images?  Does seeding the algorithm with certain colours help even when new colours (such as water) are present?

-   Explore the [clustering gallery](http://scikit-learn.org/stable/auto_examples/index.html#cluster-examples) for `scikit-learn`.


---

##  [Contributors](#6)

These lessons were developed by Erhu Du, Jane Lee, and Neal Davis for Computational Science and Engineering at the University of Illinois.  Development was supported by a grant from MathWorks, Inc.
