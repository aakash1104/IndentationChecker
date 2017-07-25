#!/bin/bash
if [[ $# -ne 2 ]]; then
  echo "Usage: checkIndentation.sh <Name_of_File_To_Test> <TAB_WIDTH>"
  exit
fi

python3 checker.py $1 $2
 
