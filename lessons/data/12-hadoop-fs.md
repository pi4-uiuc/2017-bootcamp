#   Lesson 12:  Apache Hadoop Architecture


---

### Contents

-   [Apache Hadoop components](#1)
-   [Hadoop Distributed File System](#2)
-   [Hadoop Zoo](#3)
-   [Contributors](#6)


---

##  [Apache Hadoop components](#1)

Apache Hadoop is composed of a collection of tools and services, and embedded in a wider environment as well (the Hadoop Zoo).  Hadoop itself consists of:

-   the MapReduce component, including the Mapper, Reducer, JobTracker, TaskTrackers, shufflers, sorters, etc.
-   the Hadoop Distributed File System
-   interfaces like Hadoop Streaming and Pig, etc.


---

##  [Hadoop Distributed File System](#2)

-   What is a file system?  It is an abstraction which allows you to map collections of bytes to files, and then to access them efficiently.

HDFS is a file system designed particularly for distributed systems.  It will feel quite different from a regular file system in Linux or Windows.

-   Notably, it is *write-once, read-many*:  when you create a file, you cannot modify it online.
-   HDFS also prioritizes data access (since data sets tend to be enormous).  This means two things:  first, program logic is logically located adjacent to the data because the data size is much larger than the application.  (Contrast this with typical applications like Microsoft Office.)  Secondly, large files are "chunked" into 100-MB file sizes which allow them to be processed in parallel quickly.
-   Redudancy and duplication are key.  The system has to be robust against failures, so by default three replicas of each file chunk are maintained.

HDFS logically distinguishes accessing "nodes".  The `NameNode` is a process/software instance which contains the metadata for all files, and acts like a transit terminal telling accessing processes which `DataNode`s contain the information they need.  Files are stored in blocks on `DataNode`s, in triplicate, as mentioned.

Files are stored in blocks, which may be physically distributed across many machines.


---

##  [Hadoop Zoo](#3)

The basic components of Hadoop are listed above, but there are a lot of ancillary tools of varying scope which support Hadoop applications.  Prominent among these are:

-   **Pig**.  Originally billed as just a SQL-like interface, Pig has evolved into a MapReduce programming environment.  We will explore Pig in a later exercise.

-   **Hadoop Streaming**.  You've seen this already, but it enables you to compatibly operate Hadoop MapReduce with effectively any language.

-   **Hive**.  This provides a data warehouse, or a SQL-like interface for querying databases and file systems which integrate with Hadoop.

-   **Mahout**.  This is a machine learning tool for Hadoop MapReduce, with a focus on predictive analytics.

-   **Fuse**.  Makes HDFS pretend to be a regular file system.

-   **Spark**.  Provides an API for *resilient distributed dataset* (RDD) computing.  Explicitly designed to transcend the limitations of a linear MapReduce-based workflows.


---

##  [References](#5)

-   [Hadoop Big Data Example (from IBM)](https://www.ibm.com/developerworks/data/library/techarticle/dm-1209hadoopbigdata/)
-   [HDFS Architecture guide](https://hadoop.apache.org/docs/r1.2.1/hdfs_design.html)
-   [HDFS tutorial and overview](http://www.nmaptutorial.com/hdfs/)

---

##  [Contributors](#6)

This lesson was developed by Neal Davis for Computer Science at the University of Illinois for the class CS 491TC.
