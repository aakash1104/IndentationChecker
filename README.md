# Indentation Checker

This is a simple indentation checker that checks your entire C++ code for incorrect indentation based on a specified tab width

## Purpose

Good code should be made readable and self-explanatory to a third party. One of the most important thing to do in order to provide good code to the audience is to write code with proper indentation! Often times in college, freshmen are graded heavily on style (naming conventions, comments, and indentation) when they submit programs. I wrote this script to scan an entire piece of code and point out where and how to correct misplaced indents.

### How to use

Simply download *checkIndentation.sh* and *checker.py*. Make sure you have your C++ file in the same directory as the python and bash scripts. Give executable permissions to *checkIndentation.sh*

```
chmod 700 checkIndentation.sh
```

Run the script

```
./checkIndentation.sh <NAME_OF_C++_FILE> <TAB_WIDTH>
```

## Assumptions

This script assumes that your C++ code compiles. If you have extra curly braces that may cause your program to throw an error, the script will not compute indentation widths correctly!

## Author

Written By: Aakash Prabhu, December 2016 (University of California, Davis)
