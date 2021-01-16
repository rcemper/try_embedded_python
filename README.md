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

3. Run the IRIS container with this project:

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
## Hint  
Directory __.stream/__ contains all my input files and some public test data.  
If you want to use your personal input you should replace them as 1 file by day.  
e.g. input01.txt, input02.txt,........ ,input25.txt exactly as downloaded from AOC2020.  

__%SYS.Python.html__ is a preliminary class docu to see available functions

__iris.key__ is a temporary preview key available from [WRC Distribution](https://wrc.intersystems.com/wrc/coDistPreview.csp)  
It requires your personal update as it might be expired.  
It is not required to run the demo, but access to code might be limited.     

__docker image__:  if you don't have the required image already you need to downlad it from  containers.intersystems.com 
~~~
docker login -u="<username>" -p="<passwd>" containers.intersystems.com
docker pull containers.intersystems.com/intersystems/iris-ml:2020.3.0.304.0
~~~
