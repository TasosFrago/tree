import os
import sys

alls = os.listdir()

def checktype():
    hidden = []
    files = []
    for i in alls:
        if i[0] == ".":
            hidden.append(i)
        else:
            files.append(i)

def instructions():
    print(f"Usage: {sys.argv[0]} [OPTION]... [PATH]\nPATH is optional.Use it if you want the tree of a specific folder.\nBy default it will use the current path you are in.\n\nq")

def main():
    instructions()
    print(sys.argv[1])
    if sys.argv[1] == "--help":
        instructions()

if __name__ == "__main__":
    main()
