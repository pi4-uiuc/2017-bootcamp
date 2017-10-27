
# 2017 PI4 Computational Bootcamp

This repository includes material for the 2017 PI4 Computational Bootcamp taught to students in the Department of Mathematics, University of Illinois at Urbana-Champaign May 26 - June 9, 2017 in 239 Altgeld Hall.

See the website pi4-uiuc.github.io/2017-bootcamp for more information about the course

## License and Reuse 

Computational Bootcamp materials are available for reuse by others. We ask that when materials are re-used, the following statement be included:

> These materials were created by David LeBauer and Neal Davis at the University of Illinois, with support from National Science Foundation grant DMS 1345032 “MCTP: PI4: Program for Interdisciplinary and Industrial Internships at Illinois.”

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This <span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" rel="dct:type">work</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

A great way to reuse and improve this material is to fork this repository - in this way you will have the option of 'pushing' any improvements back.

<iframe src="https://ghbtns.com/github-btn.html?user=pi4-uiuc&repo=2017-bootcamp&type=fork&count=true&size=large" frameborder="0" scrolling="0" width="158px" height="30px"></iframe>

## Dependencies

Because the dependencies are complex, most of the tutorials are written in environments hosted at terraref.ndslabs.org. There, students are able to launch web-based programming environments with all of the dependencies already available. [This article](http://www.nationaldataservice.org/news/170329_workbench.html) describes this tool, which is really amazing as it is incredibly difficult to setup identical environments for students. With many connections to remote computers this becomes even more challenging. And previously, there was no way to provide students with easy access to a very large filesystem and a friendly programming environment.

The computing environments are provided as Docker images defined in the [terraref/toolserver-dockerfiles](https://github.com/terraref/toolserver-dockerfiles) GitHub repository and hosted on Dockerhub in the terraref organization, hub.docker.com/terraref.

### Data

* Many online databases (especially betydb.org and terraref.ncsa.illinois.edu/bety) will be used via both the web front end and through connections to the Postgresql database.
* Data on the ROGER supercomputer is mounted to the terraref.ndslabs.org workbench in the `/data` directory. This is not publicly avaialable but see terraref.org/data for instructions on how to access the workbench.

### R Lessons

Use the build and launch the terraref Rstudio server:

```sh
docker run -d -p 8787:8787 terraref/rstudio-terraref
```

### SQL and R Lessons

SQL Lessons 
This will setup a local instance of the terraref trait database. https://hub.docker.com/r/terraref/bety-postgis/

```sh
docker run --name betydb -p 5432:5432 terraref/betydb-postgis
```


Then navigate to https://localhost:8787

## How to modify and rebuild the website

This website is built with the R blogdown package. The following provides a quick overview of how to add lessons and build the site, but see the ([blogdown documentation](https://bookdown.org/yihui/blogdown/)) for complete instructions.

### EZ post a new lesson

* find a file in `lessons/post` and update the filename header, and content.
* update syllabus in `content/syllabus.md`

### Advanced 

#### Install blogdown package

* open R studio
* install `blogdown` package

```r
# works with R <= 3.3
install.packages('blogdown') 

# if using R 3.4
install.packages('devtools')
devtools::install_github("rstudio/blogdown")
```

#### Update information

* homepage in `content/_index.md`
* syllabus in `content/syllabus.md`.

#### Post a new lesson

```r
blogdown::new_post()
```


#### build site

```r
blogdown::build_site()
```

### Commit and push 

Check in all .md, .Rmd, and .html files.
