This is a first attempt to use Embedded Python in IRIS  
The Python code is adapted from solutions for [Advent of Code 2020](https://adventofcode.com/) contest.  
Test data are all input to my personal challenge.

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

## Installation 

Clone/git pull this repo into any local directory
```
$ git clone https://github.com/rcemper/try_embedded_python  
```

Open the terminal in this directory and run:
```
$ docker-compose build
```
this may take some time to complete

Run the IRIS container with this project:
```
$ docker-compose up -d
```

## How to Test it

Using IRIS terminal:
```
$ docker-compose exec iris iris session iris "##class(rccpy.AoC20).Run()"

Welcome to embedded Python Demo
select day as described on https://adventofcode.com/
day 0 to exit
     day (1..25) [1]:
+++++ starting : day1 +++++++++
     select part (1,2,*=all,0=skip) [*] :1
     part 1: 181044
     select part (1,2,*=all,0=skip) [*] :2
     part 2: 82660352
     select part (1,2,*=all,0=skip) [*] :0
+++++++++ done : day1 +++++++++
     day (1..25) [2]:
+++++ starting : day2 +++++++++
     select part (1,2,*=all,0=skip) [*] :*
     part 1: 456
     part 2: 308
+++++++++ done : day2 +++++++++
     day (1..25) [3]:
```
## Hints  
Directory __.stream/__ contains all my input files and some public test data.  
If you want to use your personal input you should replace them as 1 file by day.  
e.g. input01.txt, input02.txt,........ ,input25.txt exactly as downloaded from AOC2020.  

__%SYS.Python.html__ is a preliminary class docu to see available functions

__run time__: for most tests replies are pretty immediate.  
But a few tests take quite long time for calculations before showing a reaction.   
Don't get nervous for day 11, 15!!, 17, 19, 22, 23. 

[Article in DC](https://community.intersystems.com/post/trying-embedded-python)

[Demo Server SMP](https://try-embedded-python.demo.community.intersystems.com/csp/sys/UtilHome.csp)   
[Demo Server WebTerminal](https://try-embedded-python.demo.community.intersystems.com/terminal/)    
        
**Code Quality**   
<img width="85%" src="https://openexchange.intersystems.com/mp/img/packages/1152/screenshots/y6ta2wht7mzwvvefxl1aug8j8l4.jpg">
