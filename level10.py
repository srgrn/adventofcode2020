import re
import copy
from collections import Counter
acc = 0

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
    arr = []
    for line in inputfileobj.readlines():
        arr.append(int(line.strip()))
    return arr

def find_differences(arr):
    prev = 0
    counter = []
    arr = sorted(arr)
    for elem in arr:
        counter.append(elem-prev)
        prev = elem
        
    counter.append(3)
    return Counter(counter)
    
def find_possible_strings(arr):
    arr = sorted(arr)
    # arr.append(arr[-1] + 3)
    # arr.insert(0,0)
    valid = lambda x: arr[x]+3 <= arr[x+1]
    return 0

def main():
    inputpath = 'input/inputlevel10'
    # inputpath = 'input/demoinput'
    inputarray = read_input(inputpath,parse_input)
    diffcount = find_differences(inputarray)
    print(diffcount)
    print(diffcount[1] * diffcount[3])

if __name__ == '__main__':
    main()
