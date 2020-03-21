#!/usr/bin/env python3
#libary for system directories
import os
#library that takes arguments by the system's command line
import sys 
from os import path 

files = os.listdir()
branch = '├'
end = '└'
dash = '─'
white = "\033[0;37m"

def treegraph(i, color, num):
    filescount = len(files)
    if num < filescount:
        print(f"  {white}{branch}{dash}{color}{i}{white}")
    elif num == filescount:
        print(f"  {white}{end}{dash}{color}{i}{white}")
    

def checktype():
    for i in files:
        if i[0] == ".":
            files.remove(i)

#function that shows the instructions when the user presses "tree --help" in the command line
def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... \nThe default path is the current path you are in.\n\nOptions:\n  -a  for showing all the files in the directory\n  -f  followed by the name of a file or directory you want to find\n  --help  for displaing instructions")

#function that shows the branches for the directiories
def tree(filename):
    num = 0
    color = ""
    sortedlist = sorted(files)
    cwd = os.getcwd().split("/")
    print(f"\033[1;34m {cwd[-1]}")
    for i in sortedlist:
        num += 1
        if path.isdir(i) == True:
           color = "\033[1;34m"
           treegraph(i, color, num)
        elif path.isdir(i) == False:
            color = "\033[0;37m"
            treegraph(i, color, num)
        if filename != "/":
            if filename == i:
                color = "\033[1;31m"
                treegraph(i, color, num)    
    if filename not in sortedlist and filename != "/":
        print(f"\n\033[1;32m[{filename}]{white} does not exist\n")

#function that combines all the previous functions in order for the program to run
def main():
    if len(sys.argv) == 1:
        checktype()
        tree("/")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            instructions()
        elif sys.argv[1] == "-a":
            tree("/")
        else:
            print("\033[1;31m!!Error!!\033[0;37m")
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "-f":
            tree(sys.argv[2])

#starts the main function
if __name__ == "__main__":
    main()
