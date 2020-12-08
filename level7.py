import re
from collections import Counter

def openinput(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parsefile(f):
    return f.readlines()

def main():
    # inputfile = 'demoinput.txt'
    inputfile = 'inputlevel6'
    input = openinput(inputfile,parsefile)

if __name__ == "__main__":
    main()