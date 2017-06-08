#   Lesson 10:  Amazon Web Services


---

### Contents

-   [Cloud computing](#1)
-   [Amazon Web Services](#2)
-   [Elastic Compute Cloud](#3)
-   [Simple Storage Service](#5)
-   [Lambda](#6)
-   [Elastic MapReduce](#4)
-   [Contributors](#7)


---

##  [Cloud computing](#1)

Cloud computing marks the rise of computing as a utility, a resource that can be metered and accessed essentially anywhere.  Although the lines can be blurry, cloud computing services are typically bundled into four categories:

-   **cloud storage**

    Dropbox and Box provide storage services, but naturally for enterprise customers there are many more competitors.  Backup services are typically cloud storage.

-   **software as a service (SaaS)**

    With SaaS, you log in via a web browser and manipulate data as if they were local to you---although they reside on a remote machine.

    You are familiar with SaaS, whether you've known it by this name or not.  This describes applications delivered via the cloud, from Google Docs to Office 365 to Slack.

-   **platform as a service (PaaS)**

    PaaS focuses on offering a software stack ready to go, with a focus on applications like database services, web serving, and developer tools.

-   **infrastructure as a service (IaaS)**

    Machines (servers or mainframes) are available as physical or virtual machines.  Typically this is buried down the stack from the end user since the platform needs to be built on top of it to be useful for many applications.

One of the interesting corollaries of cloud computing as a utility is that within a decade, say, all you will need locally is a portal; all end-user computing will be tablet computing.


---

##  [Amazon Web Services](#2)

AWS, like other cloud service providers (Azure, Google), is really a collection of marginally-related services and tools which allow you to provision a fairly capable online service of your own; sort of an online data center without the upkeep, which is their value proposition.

-   Sign up for a free tier account, if necessary using a fresh email address.


---

##  [Elastic Compute Cloud (EC2) [IaaS]](#3)

EC2 provides a scalable army of virtual machines (VMs).  A VM is a nominal "machine" in that you can log into it remotely and then treat it as you would any other computer.  Indeed, a virtual machine on your desktop is quite similar in concept and execution.  The difference is that in cloud computing the underlying hardware is completely abstracted away, leaving the user with a
EC2 is "elastic" because any number of identical machine instances can be provisioned on demand.

### Provisioning and Using a Machine

Amazon designates *machine instances* (AMIs) as a match of hardware and a software stack which is then instantiated (think a Docker container).

You can use either command-line tools (like `ssh`) to access AMIs remotely, or you can use a console.  AWS is designed as an API, which makes many tasks awkward to carry out manually but relatively easy to set up programmatically.

Most machine instances only exist for the lifetime of their task.  For EC2, this could be a long-lived server; for EMR, this could be only a few minutes as a task completes.

Our major exercise today will be to provision and access a simple server setup with a basic web page.  This exercise is based on an [AWS tutorial](https://aws.illinois.edu/EC2%20Linux%20HOL.pdf).

-   Create a basic EC2 server.

-   Connect to the server instance using `ssh`.  Modify as necessary this statement (the `pem` file and the URL):

        $ export EC2_CERT=tmp/math-su17.pem
        $ export REMOTE=ec2-13-58-137-31.us-east-2.compute.amazonaws.com
        $ ssh -i $EC2_CERT -v -l ec2-user $REMOTE


---

## [Simple Storage Service (S3) [storage]](#5)

S3 organizes files into "buckets" (which are like folders).  Although you can manipulate files using a web interface, it was really intended as a programmatic API and is a bit cumbersome to use.

-   S3 can be used with other AWS components like Route 53 to host websites as well.


---

## [Lambda](#6)

Lambda offers an event-driven task execution service, good for tracking things like ad clicks or file uploads.  There isn't an underlying machine you can access in this case---you just set the triggers and the functions to be called as a result.  Any language is supported via call-outs, although Node.js, Python, and Java are the major supported languages.

Triggers can come from mobile apps, HTTP endpoints, or AWS services, and then you pay only for the actual compute time used in 100 ms intervals.

![](./img/Lambda_FileProcessing.png)

![](./img/Lambda_WebApplications.png)


---

##  [Elastic MapReduce (EMR) [PaaS]](#4)

EMR is an implementation of Apache Hadoop to responsively process certain categories of data.  We will use it to build a couple of different applications in the next lesson.


---

##  [Contributors](#7)

This lesson was developed by Neal Davis for Computer Science at the University of Illinois for the class CS 491TC.  The web server example is based on an [AWS Immersion Day tutorial](https://aws.illinois.edu/EC2%20Linux%20HOL.pdf).
