# ufsd-p3-loganalyser
## Introduction
This project is my implementation of the log\_analysis project. This is the third project of the Udacity Full stack developer nanodegree program.


## What you get.
* README.md (this file)
* internal\_reporting\_tool.py -- Contains the program
* db\_manager.py -- A class used by internal\_reporting\_tool.py
* create\_views.sql -- This sql file creates the views
* .gitignore -- A file to make sure that git does not add the whole virtual machine to the repository. You can ignore this file

## How to start.
### Prerequisites
* [Virtualbox](https://www.virtualbox.org/)
* [Vagrant](https://www.vagrantup.com/)
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
To start the virtual machine and login type the following commands
```
vagrant up
vagrant ssh
```
Go to the /vagrant directory and load the data.
```
cd /vagrant
psql -d news -f newsdata.sql
```
To load the views type
```
psql -d news -f create_views.sql
```
To start the application type 
```
./internal_reporting_tool.py
```
## Result
The resilts look like this
```
vagrant@vagrant:/vagrant$ ./internal_reporting_tool.py 
Executing queries, please be patient
 
1. What are the most popular three articles of all time?
	Candidate is jerk, alleges rival - 338647 views
	Bears love berries, alleges bear - 253801 views
	Bad things gone, say good people - 170098 views
 
2. Who are the most popular article authors of all time?
	Ursula La Multa - 507594 views
	Rudolf von Treppenwitz - 423457 views
	Anonymous Contributor - 170098 views
	Markoff Chaney - 84557 views
 
3. On which days did more than 1% of requests lead to errors?
	17 July 2016 - 2.26 %
 
```

## Stopping
To logout and stop the virtual machine type
```
exit
vagrant halt
```

