import os

alls = os.listdir()

def checktype():
    hidden = []
    files = []
    for i in alls:
        if i[0] == ".":
            hidden.append(i)
        else:
            files.append(i)


