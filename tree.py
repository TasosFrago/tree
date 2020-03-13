import os
import sys 

def checktype():
    alls = os.listdir()
    hidden = []
    files = []
    for i in alls:
        if i[0] == ".":
            hidden.append(i)
        else:
            files.append(i)

def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional.Use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nOptions:\n  -a  for showing all the files in the directory\n --help  for showing instructions\n")

def tree(typef):
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

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == "--help":
            instructions()
        elif sys.argv[1] == "-a":
            tree("hidden")
        else:
            print("ERROR")
    elif len(sys.argv) == 1:
        tree("show")

if __name__ == "__main__":
    main()

