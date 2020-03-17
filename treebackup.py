#libary for system directories
import os
#library that takes arguments by the system's command line
import sys 

files = os.listdir()
num = 0
branch = '├'
end = '└'
dash = '─'

def checktype():
    for i in files:
        if i[0] != ".":
            files.append(i)


#function that shows the instructions when the user presses "tree --help" in the command line
def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional, use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nOptions:\n  -a  for showing the visible and the hidden files in the directory\n")

#function that shows the branches for the directiories
def tree1():
    filescount = len(files)
    cwd = os.getcwd().split("/")
    print(f"\033[1;34m {cwd[-1]}")
    for i in files:
        num += 1
        if num < filescount:
            print(f"  {branch}{dash}{i}")
        elif num == filescount:
            print(f"  {end}{dash}{i}")
        else:
            break

#function that combines all the previous functions in order for the program to run
def main():

    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            instructions()
        elif sys.argv[1] == "-a":
            tree1()
        else:
            print("ERROR")
    elif len(sys.argv) == 1:
        checktype()
        tree1()

#starts the main function
if __name__ == "__main__":
    main()
    print("\nfor instructions,press --help")
