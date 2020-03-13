#libary for system directories
import os
#library that takes arguments by the system's command line
import sys 

#function that shows the instructions when the user presses "tree --help" in the command line
def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional.Use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nOptions:\n  -a  for showing all the files in the directory\n --help  for showing instructions\n")

#function that shows the branches for the directiories
def tree1(typef):
    num = 0
    branch = '├'
    end = '└'
    dash = '─'

    alls = os.listdir()
    files = []
    for i in alls:
        if i[0] != ".":
            files.append(i)

    show = len(files)
    hid = len(alls)
    cwd = os.getcwd().split("/")
    print(cwd[-1])
    if typef == "show":
        for i in files:
            num += 1
            if num < show:
                print(f"  {branch}{dash}{i}")
            elif num == show:
                print(f"  {end}{dash}{i}")
            else:
                break
    if typef == "hidden":
        for i in alls:
            num += 1
            if num < hid:
                print(f"  {branch}{dash}{i}")
            elif num == hid:
                print(f"  {end}{dash}{i}")

#function that combines all the previous functions in order for the program to run
def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            instructions()
        elif sys.argv[1] == "-a":
            tree1("hidden")
        else:
            print("ERROR")
    elif len(sys.argv) == 1:
        tree1("show")

#starts the main function
if __name__ == "__main__":
    main()

