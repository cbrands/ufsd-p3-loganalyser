# ufsd-p3-loganalyser
## Introduction
This project is my implementation of the log\_analysis project. This is the third project of the Udacity Full stack developer nanodegree program.


## What you get.
* README.md (this file)
* internal\_reporting\_tool.py -- Contains the program
* .gitignore -- A file to make sure that git does not add the whole virtual machine to the repository. You can ignore this file

## How to start.
### Preparing the environment
* [Download the virtual machine](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)
* unzip this file in a directory of your choice. This directory I will call $BASEDIR. Please replace $BASEDIR with your directory in the rest of these instructions.
* [Download the data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
* Unzipping this file give you a file newsdata.sql.
* copy this file to $BASEDIR/vagrant
* Open your terminal and type
```
cd $BASEDIR/vagrant
```

### Starting the application
```
vagrant up
vagrant ssh
psql -d news -f newsdata.sql
```

## Result
TODO

## Stopping
To logout and stop the virtual machine type
```
exit
vagrant halt
```

