This is a first attempt to use Embedded Python in IRIS
The Python code is andapted from solutions for [Advent of Code 2020](https://adventofcode.com/) contest.
Test data are all input to personal challenge.

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
```
## Hint
Directory __.stream/__ contains all my input files and some public test data.  
If you want to use your personal input you should replace them as 1 file by day.  
e.g. input01.txt, input02.txt,........ ,input25.txt exactly as downloaded from AOC2020.
