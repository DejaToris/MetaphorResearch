# MetaphorResearch
This repository contains various tools and utilities which aid in linguistic research.

## Copyright and license
Read the LICENSE.txt file. Project developed by Olga Beskrovniy.

## Tools
### User tools
#### Word-Object Prototypicality Matcher
Gets as input a verb (in future, will support other parts of speech), and returns a list of that verb's prototypical objects.

## Installation guide
The code is built for Python 2.7.
In order to run all the tools, the following packages are required:
### nltk
See information about [installing NLTK here](http://www.nltk.org/install.html) and about [adding data to NLTK here](http://www.nltk.org/data.html). 
### pymssql
In order to install _pymssql_ correctly, one must choose the correct .whl file based on the environment. For more information see [this article on MSDN](https://msdn.microsoft.com/en-us/library/mt694094%28v=sql.1%29.aspx?f=255&MSPPError=-2147217396)

## User's guide
All tools should be executed from the command line. All tools may be executed with the `-h` or `--help` flag to see what arguments need to be passed to the script. For example:
~~~~
$ python matcher.py -h
usage: matcher.py [-h] [-n NUMBER_OF_OBJECTS_TO_RETURN] verb

positional arguments:
  verb                  The target verb.

optional arguments:
  -h, --help            show this help message and exit
  -n NUMBER_OF_OBJECTS_TO_RETURN, --number_of_objects_to_return NUMBER_OF_OBJECTS_TO_RETURN
                        Number of prototypical objects to match to the verb
                        and return in the final list. Defaults to 10.

~~~~

## Contact Info
For bugs, features, etc., oggiebesk@gmail.com.

