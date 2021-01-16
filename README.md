This is a practical example how __CPIPE__ can be used to communicate with modules written in a different  
programming language as a somewhat realistic case based on [Advent of Code](https://adventofcode.com/) contest.

## Prerequisites
Make sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and [Docker desktop](https://www.docker.com/products/docker-desktop) installed.

## Installation 

Clone/git pull the repo into any local directory

```
$ git clone https://github.com/intersystems-community/objectscript-docker-template.git
```

Open the terminal in this directory and run:

```
$ docker-compose build
```

3. Run the IRIS container with your project:

```
$ docker-compose up -d
```

## How to Test it

Using IRIS terminal:

```
$ docker-compose exec iris iris session iris "##class(rcc.AoC20).Run()"
```
## Hint
Directory __.in/__ contains all my input files and some public test data.  
If you want to use your personal input you should replace them as 1 file by day.  
e.g. input01.txt, input02.txt,........ ,input25.txt exactly as downloaded from AOC2020.
