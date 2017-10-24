---
title: "Projects"
date: "2017-06-01"
---


## Final group projects

Each group has a github repository that contains code developed to answer a specific question with data from the TERRA REF project.

Here are the project topics / questions and links to their repositories.

* Can the shortwave infrared solar spectrum be predicted from visible spectra? https://github.com/pi4-uiuc/Team_1
* Can genotype be predicted from leaf traits? https://github.com/pi4-uiuc/TeamTwo
* Comparing growth rates of plants grown indoors versus outdoors https://github.com/pi4-uiuc/IndoorOutdoor
* Can plant growth in greenhouses predict how plants will grow in the field? https://github.com/pi4-uiuc/Group-4
* An exploration of genotype-phenotype correlation in _Sorghum bicolor_ https://github.com/pi4-uiuc/Team5


## Objectives

Students should experience a collaborative development cycle similar to what they might encounter as a research programmer / software engineer / data scientist etc. 

They will have the opportunity to contribute to open source projects (e.g. TERRA REF and PEcAn Projects). Their GitHub repositories, reports, and code will become part of their portfolio. 

Projects will provide the opportunity for students to apply what we have learned in class to new datasets and analyses.

### Project Components

* curate data from > 1 source
* use data from > 1 source in a single analysis
* perform exploratory data analysis: generating tables and graphs
* predictions, hypothesis tests and / or inference
* reproducible report 
* executable / reusable code

### Expectations / Requirements

* work collaboratively, 
   * clear tasks in GitHub - at least one / person in progress
   * clearly defined roles
* Use data from > 1 source
* provide metadata for each dataset
   * raw data 
   * derived data
* Exploratory Data Analysis
   * multiple figures and tables that _illustrate_ data
* At least one script that
   * takes raw data and generates useful output (figures, new derived data sets, results of analyses)
   * runs with sample data in data/ folder
   * can be re-run on new data as it becomes available
   * outputs to results/ folder
   * is stored in src/ folder
* Report with executable code stored in docs/ folder, containing:
   * Background / justification
   * Data description / illustration
   * Approach (Methods)
   * Analysis (results)
      * include demo of self-contained script
   * Discussion 
      * findings
      * next steps


## Introduction to the TERRA REF dataset

* [TERRA REF Documentation](https://terraref.gitbooks.io/terraref-documentation/content/)

<iframe src="https://docs.google.com/presentation/d/1mmBjUGsCGXQbaAIFfQNG3HuDJgm0scY9ltDQMXj_q6k/embed?start=false&loop=false&delayms=3000" frameborder="0" width="480" height="299" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## Daily Tasks

### Day 1

Form a team of 3-4 people
Discuss project ideas

1. create a team github repository and slack channel
2. create a README with:
  * team members
  * ideas that you want to work on
  * what types of data you will need
  * what types of analyses / algorithms you might use
3. Spend the next three days thinking about your project

### Day 2

#### Flush out ideas from Friday (Day 1)

* narrow the scope
* define data sets that are needed
* clarify questions
* write hypotheses / predictions
* draft of methods that you will use to test hypotheses
* what figures and tables will you create?
* divide tasks within the group

#### Set up project

* create project directories following recommendations in ["Good Enough Practices for Scientific Computing"](https://swcarpentry.github.io/good-enough-practices-in-scientific-computing/)
* create an Rmd files for analysis

#### Download data

* Download and subset data that you will use from BETYdb
  * find data that you will need
  * design data management plan
* For data not in BETYdb, write down what you will need. 
  * Tomorrow we will learn to access sensor and meteorological data

### Day 3

* Refine questions / methods
* Create visualizations
* Import met data

### Day 4

### By end of day you should have

* GitHub issues for 
  * any data you need
  * any issues that are blocking your work
* A project document containing
  * steps to access data
  * >= eploratory data analysis figures
     * time series
     * histograms, boxplots
     * faceted & or color by (trait, site, genotype etc)
  * outlines of 
     * background
     * approach
