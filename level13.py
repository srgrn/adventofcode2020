import re
import copy
acc = 0

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
    timestamp = int(inputfileobj.readline().strip())
    bus_schedule = inputfileobj.readline().strip().split(',')
    return timestamp,bus_schedule

def main():
    # inputpath = 'input/inputlevel9'
    inputpath = 'input/demoinput'
    (timestamp,bus_schedule) = read_input(inputpath,parse_input)
    print(timestamp,bus_schedule)

if __name__ == '__main__':
    main()
