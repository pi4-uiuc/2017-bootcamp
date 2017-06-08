#   Lesson 11:  Apache Hadoop MapReduce


---

### Contents

-   [MapReduce algorithm](#1)
-   [Elastic MapReduce](#2)
-   [Hadoop Streaming example:  Word count](#3)
-   [Contributors](#6)


---

##  [MapReduce algorithm](#1)

The MapReduce algorithm is a specific low-communication parallel programming technique.  It's suitable for certain types of problems with iterated one-time local computational steps followed by a data trading step.  Essentially, a Map step filters or sorts data, then a Reduce operation carries out a summarization procedure.  Key to this is to stop thinking of *machines* carrying out *tasks* and instead just think in terms of *functions*.

> MapReduce programs are not guaranteed to be fast. The main benefit of this programming model is to exploit the optimized shuffle operation of the platform, and only having to write the Map and Reduce parts of the program.  (Wikipedia)

1.  An **Input reader** chunks data into standard sizes, assigning one to each Map function (think of a thread or a process, although it can be a single machine).

    For a word count, one or many text files are read and converted into lines (records).

2.  The **Map function** accepts the data structured as key/value pairs, analyzes each one, and yields key/value pairs as output.

    For a word count, each line would be broken into words and a key/value pair for each word would be generated:  `clutter`→`1`.

3.  A **Partition function** and a **Comparison function** are used to transfer data sensibly between the Map function and the Reduce function.  These steps are typically automatic.

4.  The **Reduce function** accepts the aggregated output from the Map stage and reprocesses it into a summarized report.  Reduce() is called once for each key/value pair from Map().

    For a word count, each key/value pair `clutter`→`1` is summed, yielding, for example, `clutter`→`24` for the entire problem.

It's worth reiterating that MR isn't the most *efficient* algorithm by a long shot, but it is well-adapted to the redundancy, communications, and scalability demands which cloud computing applications typically make.

Apache Hadoop MapReduce has become *the* canonical implementation of the algorithm, and it is rarely implemented on any other platform.


---

##  [Elastic MapReduce (EMR) [PaaS]](#2)

One of the early prominent services which EC2 undergirds is EMR, an implementation of the MapReduce algorithm as a software service.  Apache Hadoop is the most popular implementation.

EMR applications can be scaled (again, the "elastic" part) based on load size.  The best way to learn EMR, however, is to just dive in.

<div class="alert alert-info">
If you would like to use Hadoop on a local machine rather than remotely, please follow <a href="https://hadoop.apache.org/docs/r2.7.2/hadoop-project-dist/hadoop-common/SingleCluster.html">the relevant instructions</a> on setting up a local node.  (Download a version in the 2.x line.)
</div>


---

##  [Hadoop Streaming example:  Word count](#3)

For our first EMR exercise, we will use the [Hadoop Streaming interface](https://hadoop.apache.org/docs/r1.2.1/streaming.html).  This allows you to run any scripting language with Hadoop using `stdin`/`stdout`.  The glue from Map() to Reduce() is handled automatically.  Although you will implement this through the AWS Console, the equivalent command-line tool you could use is:

    elastic-mapreduce --create --stream \
        --mapper  s3://elasticmapreduce/samples/wordcount/wordSplitter.py \
        --input   s3://math-su17/input/Defoe_RobinsonCrusoe.txt \
        --output  s3://math-su17/output \
        --reducer aggregate

You can view the exact command line construction after you create the job steps and before you submit them to run.

You will use the Amazon Web Services Elastic MapReduce platform to count the number of words in a large file.

1.  Log in to AWS and open the [Elastic MapReduce (EMR) console](https://us-east-2.console.aws.amazon.com/elasticmapreduce/home?region=us-east-2#).  Switch your region to Ohio (in the upper right-hand corner).

2.  Click `Create cluster`.

    1.  **General Configuration**  Name it as you like, and leave the logging on with the default location.

        Launch as a `Step execution`.  Select `Streaming program` and then `Configure`.

    2.  **Mapper**  The `Map()` function uses a Python script to count words (counting `1` for each word):

            #!/usr/bin/python
            import sys
            import re

            def main(argv):
                line = sys.stdin.readline()
                pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
                try:
                    while line:
                        for word in  pattern.findall(line):
                            print  "LongValueSum:" + word.lower() + "\t" + "1"
                    line =  sys.stdin.readline()
                except "end of file":
                    return None

            if __name__ == "__main__":
                main(sys.argv)

        This script is located on AWS at `s3://elasticmapreduce/samples/wordcount/wordSplitter.py`.

    3.  **Reducer**  The `Reduce()` function will use a standard built-in process, `aggregate`, which sums values from matching keys.

    4.  **Input**  I have posted several texts from Project Gutenberg in an S3 bucket at `s3://math-su17/input/`.  Select one (or more) of these as your input:

        -   [`Cao_DreamOfTheRedChamber.txt`](./Cao_DreamOfTheRedChamber.txt)
        -   [`Cervantes_DonQuixote.txt`](./Cervantes_DonQuixote.txt)
        -   [`Defoe_RobinsonCrusoe.txt`](./Defoe_RobinsonCrusoe.txt)

    5.  **Output**  Direct the output to a folder `s3://math-su17/output/{your_netid}`; this folder _must not exist_ yet—delete it if necessary.  (I am experimenting with the permissions policy as well; if there's a problem let me know.  Don't assume that you're necessarily doing something wrong, I may need to add permissions for S3 to the student policy.)  Alternatively, you may redirect output to a bucket you control (the bucket must exist already though!).

    6.  **Software and Hardware**  Leave the software stack as-is.

        Create an `*.large` instance with 3 instances.  (You can select memory-optimized, compute-optimized, etc.)

    You will need to create a secure key pair.  Click `Create an Amazon EC2 Key Pair and PEM File` and follow the instructions to do so.  This allows you to access the materials.


3.  Run (and monitor) the job.  Explore the various fields, especially *Steps* and *Events*.

    If the job fails, you can `Clone` it and modify any steps you think may be at fault.

4.  When you are done, make sure that you shut down any instances you started if they don't terminate automatically.  I will clear AMIs after the course ends, so don't worry about deleting them from storage.

    I will retrieve your submission directly from the S3 bucket.  You can check that as well to see what the output looks like.  You should see files like `_SUCCESS` and `part-00000` which contain the output from the streaming script.

<div class="alert alert-info">
In principle, you can run this locally if you want to set up a Hadoop instance on your own machine.  That requires a Hadoop file system, which is kind of like a Docker for your file system, and it gets weird fast.
</div>

This assignment is based on an AWS Hadoop Streaming [tutorial](https://aws.amazon.com/code/Elastic-MapReduce/2273).  You may also find the [Tech Services AWS Labs](https://aws.illinois.edu/labs/) to be useful.

-   What other sorts of problems can you think of that MapReduce would work well for?  _classification problems, network problems ([some ideas](https://stackoverflow.com/questions/12375761/good-mapreduce-examples#12375878))_

-   This exercise will focus on using MapReduce to sift electrical grid data for threshold-level power excursions.  The base data set contains *phasor measurement unit* (PMU) data.  It is fairly dirty and may require cleaning (or the algorithm may be robust against dirty data).
    -   Examine [`pmu_map.py`](	https://s3.us-east-2.amazonaws.com/math-su17/scripts/pmu_map.py).  What does this program do, in an MR sense?
    -   Implement a Hadoop Streaming realization of this code from start to finish, as above.
    -   How could these data, once identified, be useful?  (correlate with weather, solar magnetic activity, other nonlocal grid events)


---

##  [Contributors](#6)

This lesson was developed by Neal Davis for Computer Science at the University of Illinois for the class CS 491TC.
