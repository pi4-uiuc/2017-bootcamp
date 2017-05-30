---
title: "Syllabus"
date: "2017-05-05"
output:
  blogdown::html_page:
    toc: "true"
---


## Instructors: 

David LeBauer

* Carl R Woese Institute for Genomic Biology and National Center for Supercomputing Applications, University of Illinois
* email:dlebauer@illinois.edu 

Neal Davis

* Deparatment of Computer Science, University of Illinois
* email:davis68@illinois.edu

Stefan Klajbor (TA) 

* Department of Mathematics, University of Illinois
* email:klajbor2@illinois.edu

## Course Objectives

A two week course designed to introduce Math graduate students with little or no programming experience to methods in data analysis and computation. The goal is to prepare students to apply their understanding of math to solve problems in industry.

## Pre-requisites

### Accounts

Each student should register for the following accounts: 

* github.com
* TERRA REF Alpha User program https://goo.gl/forms/M0ZEMi3PSLENhspl2

And will receive email notifications that they are signed up for the following:

* National Data Service workbench http://www.pi4.ndslabs.org
* Slack (an invitation will be sent to you via email)

### Familarity with basic syntax and operations in R and Python

Although the course is aimed at students with limited experience using software, you are expected to complete two introductory courses in order to become familiar with the basic syntax and operations in R and Python. Two free courses from DataCamp are **Required***; completion certificates must be mailed to the instructors by the start of the first day of class (Friday May 25). These courses should take a few hours to complete: 
* [Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r) 
* [Introduction to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science).

*Students who have significant experience with R and / or Python may elect to substitute a more advanced course.

### Computers and Software 

The only software requirement is a modern web browser.

The classroom is equiped with desktop computers, though students are encouraged to bring laptops. Much of the instruction and collaborative work will be done using the NDS Labs Workbench. The NDS labs workbench provides Shell, R, and Python editors as well as access to large datasets within a web browser.

Students are welcome and encouraged to run the software on their own computers, however some of the software is challenging to install and there will be limited time for instructors to assist with installation and configuration.

### Code of Conduct

All participants must read and abide by our [Code of Conduct](https://github.com/pi4-uiuc/2017-bootcamp/blob/master/CODE_OF_CONDUCT.md). 

## Logistics


#### Location: 239 [Altgeld Hall](https://en.wikipedia.org/wiki/Altgeld_Hall), 

University of Illinois Department of Mathematics
1409 West Green Street
Urbana, Il

#### Time: 9AM - 5PM

We will have a one hour break each day for lunch. On days with a guest lecture, we will break from 11:30 12:00 so that students have time to purchase a lunch and bring it back to the classroom in time for the talk.

#### Dates: May 26 -- June 9, 2017

* May 26: Computing Basics
* May 30-June 2: Data and Statistics in R
* June 5-June 8: Data and Machine Learning with Python
* June 9: Conclusion and Project Presentations

#### Daily Schedule:

| Time | Activity |
|:---|:---|
| 9:00--9:30 | Review, questions, overview |
| 9:30--10:30 | Topic 1 | 
| 10:30--10:45 | Break | 
| 10:45--12:00 | Topic 2 |
| 12:00--1:00 | Lunch, ocassionally with guest lecture |
| 1:00--2:00 | Topic 3 | 
| 2:00--3:00 | Topic 4 |
| 3:00--3:15 | Break | 
| 3:15--5:00 | Group Projects | 

#### Guest Presentations

All lectures will be from 12:00 to 1:00 unless otherwise noted.

* Tuesday, May 30: "TBD" Aaron Saxton, PhD. Senior Data Scientist, Agrible Inc.
* Wednesday May 31: "Data in Nuclear Engineering" Katy Huff, PhD, Department of Nuclear, Plasma, and Radiological Engineering, UIUC
* Friday, June 2: "TBD" Rob Kooper, Senior Research Programmer, National Center for Supercomputing Applications


## Course Schedule

### Day 1: Computing Fundamentals

Friday May 26

1. The Terminal [SWC The Unix Shell](http://swcarpentry.github.io/shell-novice/))
   * file system navigation
   * scripting
   * control flow
2. Version Control [SWC Git Novice 1-6](http://swcarpentry.github.io/git-novice/)
   * commiting changes
   * branching
   * merging
4.  Collaborative Coding [SWC Git Novice 7-14](http://swcarpentry.github.io/git-novice/)
    * GitHub
    * Code Reviews
3. Software Development
   * Reproducible Research
   * Agile / Scrum
5. Group Projects: Setup
   * Overview of available data
   * Overview of scientific questions 
   * Divide into Teams
   * Setup GitHub repository
   * Formulate questions and hypotheses

### Day 2: Getting started with R

Tuesday May 30

1. Best Practices in Scientific Computing
1. [Getting Started with R and Rstudio (SWC 1-3)](http://swcarpentry.github.io/r-novice-gapminder/01-rstudio-intro/)
   * Importing data
   * [vectorization](http://swcarpentry.github.io/r-novice-gapminder/09-vectorization/)
   * Control Flow (if, else, for) [SWC 7](http://swcarpentry.github.io/r-novice-gapminder/07-control-flow/)
   * Writing Reports with Rmarkdown
1. Data structures
   * Spreadsheets [DC lesson](http://www.datacarpentry.org/spreadsheet-ecology-lesson/)
   * Relational Databases
   * non-relational databases
   * Raster data and databases
2. Querying databases
   * SQL
   * Connecting from R using the dplyr package
   * Connecting to BETYdb using the traits package
6. Project 
   * curate data 
   * design data management plan
   * identify data that is needed / open questions

The first half of the day will follow the R Novice Gapminder lesson http://swcarpentry.github.io/r-novice-gapminder/

### Day 3: Databases and Visualization

Wednesday May 31 

2. Intro to Agile Development (lecture)
4. Data Cleaning 
   * Data Cleaning with Open Refine [DC lesson 1-4](http://www.datacarpentry.org/OpenRefine-ecology-lesson/)
   * Data Cleaning in R
5. Exploratory Analysis
   * Summary Statistics
   * Scatter Plots
5. Data Curation
   * Metadata and Vocabularies
   * Publishing Data, Archives and Repositories
5. Data Manipulation
   * [filtering, subsetting, summarizing, new variables with dplyr](http://swcarpentry.github.io/r-novice-gapminder/13-dplyr/)
   * [Converting data from wide to long with tidyr](http://swcarpentry.github.io/r-novice-gapminder/14-tidyr/)
3. Visualization
   * bestiary of plots, which plots for which data
   * Turning tables into graphs [Gelman et al 2002](http://www.tandfonline.com/doi/abs/10.1198/000313002317572790)
   * Beyond Bar and line graphs [Weissgerber et al 2015](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)
   * Tufte, sparklines
   * ggplot starting with [SWC 8](http://swcarpentry.github.io/r-novice-gapminder/08-plot-ggplot2/)
4. Project: Find data, clean, evaluate, and summarize, publish to GitHub

### Day 4: Probability and Statistics

Thursday June 1

1. Probability Distributions
   * Bestiary, meaning, PDFs (Bolker Ch4, [Dietze EE509](https://github.com/mdietze/EE509/blob/master/Exercise_02_Distributions.Rmd))
   * Stochastic Simulation (Bolker Ch5)
2. Summary statistics
   * Estimates of central tendency, variance, shape
   * Fitting PDFs - 
      * parameter estimation 
      * goodness of fit (_L_, [A,B,D,]IC)
3. Statistical Modeling
   * Regression
   * Functions
   * Dynamic Models

### Day 5

Friday June 2

1. Model Building
   * Descriptive Analysis
   * Hypothesis Driven Analysis
4. Model Fitting 
   * Frequentist, Bayesian
   * Inference and Prediction
6. Multilevel modeling
   * ANOVA ([Gelman et al 2005](https://projecteuclid.org/download/pdfview_1/euclid.aos/1112967698))
   * GLM
   * HB
  
### Day 6

Monday June 5

- Presumptive background:  [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science) (covers through NumPy)

1. Pandas
2. MatPlotLib etc
2. Data cleaning
3. Principal Component Analysis

### Day 7

Tuesday June 6

1. $k$-nearest-neighbor
2. $k$-d tree
3. Support Vector Machines
4. Monte Carlo sampling

### Day 8

Wednesday June 7


1. $k$-means clustering
2. Hierarchical clustering
3. Hidden Markov models
4. Data Mining Project

### Day 9

Thursday June 8

1. Amazon Web Services (Cloud computing)
1. Hadoop MapReduce
2. Hadoop Pig

### Day 10 Project Wrapup and Presentations

Friday June 9

* Morning: Group project completion and write-up.
* Afternoon: Group Presentations (15 min each, open to public).
