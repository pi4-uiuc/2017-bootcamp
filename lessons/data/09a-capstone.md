#   Lesson 09a:  Data Mining Capstone


---

### Contents

-   [The data set](#1)
-   [The challenge](#2)
-   [Contributors](#6)


---

##  [The data set](#1)

The [MovieLens database](https://grouplens.org/datasets/movielens/) represents an extraction from IMDB of movies, tag data, and ratings data.  For a capstone exercise, use the data mining techniques we have covered to analyze the tagging/metadata and the ratings data in order to make predictions about movie and tag popularity.

Two data sets are available:

-   [`ml-latest-small`](http://files.grouplens.org/datasets/movielens/ml-latest-small.zip)
-   [`ml-latest`](http://files.grouplens.org/datasets/movielens/ml-latest.zip)

Start with the smaller data set (100,000 entries) to set up your approach.  You can then try to repeat the process with the larger data set (20,000,000+ entries).

Because the full data set is fairly large, it may be more effective to work on a local machine rather than remotely, if you have the software.

Data sets like this allow you to analyze the structure of online communities and to generate recommender systems.


---

##  [The challenge](#2)

-   Load the data sets in `movies.csv` and `ratings.csv`.  How can you connect information from one to the other?  One idea is to have a data frame mapping ratings to movies, another mapping movies to titles (or perhaps a `dict`), and a third mapping movies to tags.  The average rating could then be used to predict popularity, as with the $k$-d tree example, for instance.

-   Verify that the data set is clean, or, if it needs cleaning, do so.

-   Analyze the data set.  Select a possible goal from the following list.  If you complete one, go ahead and tackle another.

    1.  Given someone's movie preference, recommend a similar movie with a high rating they will also likely enjoy.
    2.  Calculate correlations between tags and movie popularity (rating).
    3.  Identify major clusters of tags (i.e., tags that tend to co-occur).

    Techniques like MC sampling and particularly clustering are likely to be useful.

    You may find PCA, SVM, and $k$-d trees to be useful.  ($k$-d trees will be particularly useful for goal #1.)

    We are not working with time series data, so HMM is not likely to be useful.

-   Which factors are most predictive?  (Note that this is not PCA, since we are not diagonalizing the data set first.  Simply apply a reasonable threshold for significance.)

-   Which movies are the most predictive (i.e., have the most near neighbors)?  Which are the least?


---

##  [Contributors](#6)

This lesson was developed by Neal Davis for the PI4 Mathematics boot camp at the University of Illinois.
