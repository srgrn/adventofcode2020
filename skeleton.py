import re
import copy
acc = 0

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
    return []

def main():
    # inputpath = 'input/inputlevel9'
    inputpath = 'input/demoinput'
    inputarray = read_input(inputpath,parse_input)

if __name__ == '__main__':
    main()
