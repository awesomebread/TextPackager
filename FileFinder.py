import os

def findFile(filename):
    for i in os.listdir():
        if os.path.isfile(i) and i.startswith(filename):
            return i
    raise Exception("Document '" + filename + "' was listed, but no file of that name could be found")