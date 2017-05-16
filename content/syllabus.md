---
title: "Syllabus"
date: "2017-05-05"
---


## Instructors: 

David LeBauer, Carl R Woese Institute for Genomic Biology

Neal Davis, Deparatment of Computer Science, University of Illinois

Stefan Klajbor (TA), Department of Mathematics, University of Illinois

## Course Objectives

A two week course designed to introduce Math graduate students with little or no programming experience to methods in data analysis and computation. The goal is to prepare students to apply their understanding of math to solve problems in industry.

## Pre-requisites

### Accounts

Each student should have an account on GitHub.com and terraref.ndslabs.org. 

### Familarity with basic syntax and operations in R and Python

Although the course is aimed at students with limited experience using software, you are expected to complete two introductory courses in order to become familiar with the basic syntax and operations in R and Python. Two free courses from DataCamp are **Required***; completion certificates must be mailed to the instructors by midnight May 25. Each of these courses should take a few hours to complete: 
* [Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r) 
* [Introduction to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science).

*Students who have significant experience with R and / or Python may elect to substitute a more advanced course.

### Computers and Software 

The only software requirement is a modern web browser.

The classroom is equiped with desktop computers, though students are encouraged to bring laptops. Much of the instruction and collaborative work will be done using the NDS Labs Workbench. The NDS labs workbench provides Shell, R, and Python editors as well as access to large datasets within a web browser. Please sign up for an account here:  at [terraref.ndslabs.org](https://terraref.ndslabs.org).

Students are welcome and encouraged to run the software on their own computers, however some of the software is challenging to install and will be limited time for instructors to assist with installation and configuration.

## Agenda

### Dates: May 26 -- June 9, 2017

* May 26: Computing Basics
* May 30-June 2: Data and Statistics in R
* June 5-June 8: Data and Machine Learning with Python
* June 9: Conclusion and Project Presentations

### Daily Schedule:

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

### Day 1: Computing Fundamentals

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
   * Collaboration using Agile / Scrum iterative methodology
   * Guest lecture 'from the trenches?'
5. Group Projects: Setup
   * Overview of available data
   * Overview of scientific questions 
   * Divide into Teams
   * Setup GitHub repository
   * Formulate questions and hypotheses

### Day 2: Getting started with R

1. [Getting Started with R and Rstudio (SWC 1-3)](http://swcarpentry.github.io/r-novice-gapminder/01-rstudio-intro/)
2. Loading and Evaluating Data
   * data types
   * [vectorization](http://swcarpentry.github.io/r-novice-gapminder/09-vectorization/)
3. Control Flow (if, else, for) [SWC 7](http://swcarpentry.github.io/r-novice-gapminder/07-control-flow/)
4. Visualization [SWC 8](http://swcarpentry.github.io/r-novice-gapminder/08-plot-ggplot2/)
5. Data Manipulation
   * [filtering, subsetting, summarizing, new variables with dplyr](http://swcarpentry.github.io/r-novice-gapminder/13-dplyr/)
   * [Converting data from wide to long with tidyr](http://swcarpentry.github.io/r-novice-gapminder/14-tidyr/)
6. Project 
   * curate data 
   * design data management plan
   * identify data that is needed / open questions


The first half of the day will follow the R Novice Gapminder lesson http://swcarpentry.github.io/r-novice-gapminder/

### Day 3: Databases and Visualization

1. Data structures
   * Spreadsheets [DC lesson](http://www.datacarpentry.org/spreadsheet-ecology-lesson/)
   * Relational Databases
   * non-relational databases
   * Raster data and databases
2. Querying databases
   * SQL
   * Connecting from R using the dplyr package
5. Data Curation
   * Metadata and Vocabularies
   * Publishing Data, Archives and Repositories
4. exploratory Data Analysis
   * Data Cleaning with Open Refine [DC lesson 1-4](http://www.datacarpentry.org/OpenRefine-ecology-lesson/)
   * Data Cleaning in R
   * Scatter Plots
3. Visualization
   * bestiary of plots, which plots for which data
   * Turning tables into graphs [Gelman et al 2002](http://www.tandfonline.com/doi/abs/10.1198/000313002317572790)
   * Beyond Bar and line graphs [Weissgerber et al 2015](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1002128)
   * Tufte, sparklines 
4. Project: Find data, clean, evaluate, and summarize, publish to GitHub

### Day 4: Probability and Statistics

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

- Presumptive background:  [Intro to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science) (covers through NumPy)

1. Pandas and MatPlotLib
2. Data cleaning
3. Principal Component Analysis

### Day 7

1. $k$-nearest-neighbor
2. $k$-d tree
3. Support Vector Machines

### Day 8

1. $k$-means clustering
2. Hierarchical clustering
3. Hidden Markov models
4. Amazon Web Services

### Day 9

1. Hadoop and MapReduce
2. The Hadoop zoo

### Day 10 Project Wrapup and Presentations

* Morning: Group project completion and write-up.
* Afternoon: Group Presentations (15 min each, open to public).
