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
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional.Use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nOptions:\n  -a  for showing all the files in the directory\n --help  for showing instructions")

def main():
    checktype()
    if sys.argv[1] == "--help":
        instructions()
    elif len(sys.argv) == 3:
        
    elif sys.argv[1] == "-a":
        print()
    

if __name__ == "__main__":
    main()
branch = '├'
pipe = '|'
end = '└'
dash = '─'