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

def checktype():
    for i in files:
        if i[0] == ".":
            files.remove(i)

#function that shows the instructions when the user presses "tree --help" in the command line
def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional, use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nOptions:\n  -a  for showing all the files in the directory\n  -f  followed by the name of a file or directory you want to find\n")

#function that shows the branches for the directiories
def tree1(filename):
    num = 0
    color = ""
    sortedlist = sorted(files)
    filescount = len(files)
    cwd = os.getcwd().split("/")
    print(f"\033[1;34m {cwd[-1]}")
    for i in sortedlist:
        num += 1
        if path.isdir(i) == True:
           color = "\033[1;34m"
        elif path.isdir(i) == False:
            color = "\033[0;37m"

        if filename != "/":
            if filename == i:
                color = "\033[1;31m"

        if num < filescount:
            print(f"  {white}{branch}{dash}{color}{i}{white}")
        elif num == filescount:
            print(f"  {white}{end}{dash}{color}{i}{white}")
        else:
            break
    if filename not in sortedlist and filename != "/":
        print(f"\n\033[1;32m[{filename}]{white} does not exist\n")

def tree2():
    pass

#function that combines all the previous functions in order for the program to run
def main():
    if len(sys.argv) == 1:
        checktype()
        tree1("/")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            instructions()
        elif sys.argv[1] == "-a":
            tree1("/")
        else:
            print("\033[1;31m!!Error!!\033[0;37m")
    elif len(sys.argv) >= 2:
        if sys.argv[1] == "-f":
            tree1(sys.argv[2])

#starts the main function
if __name__ == "__main__":
    main()
