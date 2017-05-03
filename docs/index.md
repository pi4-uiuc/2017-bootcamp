# Computational Bootcamp 2017

Computational Bootcamp for the PI4 program, Department of Mathematics,  University of Illinois at Urbana-Champaign

## Instructors: 

David LeBauer, Carl R Woese Institute for Genomic Biology, University of Illinois

Neal Davis, Deparatment of Comptuer Science, University of Illinois

Teaching Assistant: Stefan Klajbor, Deparatment of Comptuer Science, University of Illinois

## Objectives

A two week course designed to introduce Math graduate students with little or no programming experience to methods in data analysis and computation. The goal is to prepare students to apply their understanding of math to solve problems in industry.

This is the material from a 2 week Computational Bootcamp for PI4 students prior to beginning summer internships as part of the NSF funded [PI4 Program for Interdisciplinary and Industrial Internships at Illinois](https://pi4.math.illinois.edu/). 

Previous years: [2016](http://www.math.uiuc.edu/~hirani/cbmg/index.html), [2015](http://math.illinois.edu/~shahkar2/cbmg/), [2014](http://www.math.uiuc.edu/~hirani/teaching/cbmgsu14) courses focused more on numerical analysis. This year the focus is shifting to the use and analysis of large and complex data.

## Pre-requisites

Although the course is aimed at students with limited experience using software, you are expected to complete two introductory courses in order to become familiar with the basic syntax and operations in R and Python. Two free courses from DataCamp are **Required***; completion certificates must be mailed to the instructors by midnight June 25. Each of these courses should take a few hours to complete: 
* [Introduction to R](https://www.datacamp.com/courses/free-introduction-to-r) 
* [Introduction to Python for Data Science](https://www.datacamp.com/courses/intro-to-python-for-data-science).

*Students who have significant experience with R and / or Python may elect to substitute a more advanced course.

## Agenda

### Dates: May 26 -- June 9, 2017

* May 26: Computing Basics
* May 30-June 2: Data and Statistics in R
* June 5-June 8: Data and Machine Learning with Python
* June 9: Conclusion and Project Presentations

### Daily Schedule:

| Time | Activity |
|---|---|
| 9:00 -- 9:30 | Review of questions related to material covered on previous days |
| 9:30 -- 10:30 | Topic 1 | 
| 10:30 -- 10:45 | Break | 
| 10:45 -- 12:00 | Topic 2 |
| 12:00 -- 1:00 | Lunch, ocassionally with guest lecture |
| 1:00 -- 2:00 | Topic 3 | 
| 2:00 -- 3:00 | Topic 4 |
| 3:00 -- 3:15 | Break | 
| 3:15 -- 5:00 | Group Projects | 

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
   * Data Cleaning with Open Refine (DC lesson 1-4)[http://www.datacarpentry.org/OpenRefine-ecology-lesson/]
     * or, port to R
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
   * ANOVA
   * GLM
   * HB
  
## Days 6-9 (Neal Davis)

- Data mining (from MATLAB tutorials)
- Hadoop and MapReduce algorithm
- Basic ML (from MATLAB tutorials)

Data mining topics:
- Data cleaning
- Principal component analysis
- k-Nearest Neighbor clustering
- k-D tree
- Support Vector Machine
- Monte Carlo simulation
- k-Means clustering
- Hierarchical clustering
- Hidden Markov model

Hadoop lesson:
- MapReduce algorithm
- What are Hadoop and friends?
- Hadoop interface
- Basic examples (word count, etc.)
- PMU example

### Day 10 Project Wrapup and Presentations

* Morning: Group project completion and write-up.
* Afternoon: Group Presentations (15 min each, open to public).

## Projects


<!-- adding Draft watermark http://stackoverflow.com/a/2486786/199217 -->
<style type="text/css">
#watermark {
  color: #F5F5F5;
  font-size: 200pt;
  -webkit-transform: rotate(-45deg);
  -moz-transform: rotate(-45deg);
  position: absolute;
  width: 100%;
  height: 100%;
  margin: -5;
  z-index: -1;
  left:-100px;
  top:-200px;
}
</style>

<div id="watermark">
<p>DRAFT. DRAFT. DRAFT</p>
</div>
