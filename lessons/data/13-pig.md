#   Lesson 13:  Apache Pig


---

### Contents

-   [Apache Pig rationale](#1)
-   [Pig Latin](#2)
-   [Exercise](#3)
-   [Contributors](#6)


---

##  [Apache Pig rationale](#1)

Apache Pig is a procedural SQL-ish language which lets Hadoop users work with the distributed data sets of HDFS.

Everything in Pig is a tuple (or a variation on a tuple, like a bag or an atom).


---

##  [Pig Latin](#2)

The best way to get a feel for Pig is to just run an example.  Our word count application from before could be implemented in Pig Latin without much trouble.

(If you are on your own machine you may need the following:)
    $ export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
    $ export HADOOP_HOME=/home/davis68/Code/hadoop-2.8.0/

We will work on a machine which provides HDFS and Pig.

-   Launch an EMR cluster [per these instructions](https://aws.illinois.edu/01-LaunchingEMRInteractively.pdf).

-   Add an inbound SSH rule to `ElasticMapReduce-master` so that you can access the cluster remotely.

We will also need [a sample file](https://s3.us-east-2.amazonaws.com/math-su17/input/Defoe_RobinsonCrusoe.txt) to count words.  Download this sample file using `wget` and copy it to the HDFS.

    $ wget https://s3.us-east-2.amazonaws.com/math-su17/input/Defoe_RobinsonCrusoe.txt
    $ hdfs dfs -mkdir /home
    $ hdfs dfs -mkdir /home/davis68
    $ hdfs dfs -put Defoe_RobinsonCrusoe.txt  /home/username/

To run Pig locally (instead of in MapReduce mode), type:

    $ pig -x local

(Subsequent commands are executed at the Pig prompt.)

    input_lines = LOAD 'hdfs://localhost:22/home/username/Defoe_RobinsonCrusoe.txt' AS (line:chararray);
    input_lines = LOAD 's3://math-su17/input/Defoe_RobinsonCrusoe.txt' AS (line:chararray);

    -- Use `dump a` to show a variable, and `display a` to show its schema.

    -- Extract words from each line and put them into a pig bag
    -- datatype, then flatten the bag to get one word on each row
    words = FOREACH input_lines GENERATE FLATTEN(TOKENIZE(line)) AS word;

    -- filter out any words that are just white spaces
    filtered_words = FILTER words BY word MATCHES '\\w+';

    -- create a group for each word
    word_groups = GROUP filtered_words BY word;

    -- count the entries in each group
    word_count = FOREACH word_groups GENERATE COUNT(filtered_words) AS count, group AS word;

    -- order the records by count
    ordered_word_count = ORDER word_count BY count DESC;
    STORE ordered_word_count INTO 's3://math-su17/output/number-of-words-in-defoe';


---

##  [Exercise](#3)

-   Carry out the [Pig example](https://aws.illinois.edu/01-LaunchingEMRInteractively.pdf).

This exercise is based on an [AWS tutorial](https://aws.illinois.edu/labs) provided for UIUC's Research IT.


---

##  [References](#5)

-   [BMC Guide to Apache Pig](http://www.bmc.com/guides/hadoop-apache-pig.html)


---

##  [Contributors](#6)

This lessons was developed by Neal Davis for Computer Science at the University of Illinois for the class CS 491TC.
