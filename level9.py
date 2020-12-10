import re
import copy
preamble_length = 25

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
    arr = []
    for line in inputfileobj.readlines():
        arr.append(int(line.strip()))
    return arr

def validate(preamble, element):
    # print(element,preamble)
    for number in preamble:
        complacent = element - number
        if complacent == number:
            continue
        if complacent in preamble:
            return True
    return False

def find_sum(inputarr, total):
    start = 0
    end = 1
    sumarr = 0
    while end < len(inputarr):
        sumarr = sum(inputarr[start:end]) 
        if sumarr > total: 
            start +=1
        elif sumarr < total:
            end+=1
        else: 
            return inputarr[start:end]
    raise ValueError

def main():
    inputpath = 'input/inputlevel9'
    # inputpath = 'input/demoinput'
    inputarray = read_input(inputpath,parse_input)
    preamble = inputarray[:preamble_length]
    invalid = 0
    for element in inputarray[preamble_length:]:
        valid = validate(preamble,element)
        if not valid:
            invalid = element
            break
        preamble.pop(0)
        preamble.append(element)
    invalid_index = inputarray.index(invalid)
    print('invalid number',invalid, 'index:',invalid_index)
    invalid_sum_parts = find_sum(inputarray[:invalid_index],invalid)
    minelem = min(invalid_sum_parts)
    maxelem = max(invalid_sum_parts)
    print(invalid_sum_parts,minelem,maxelem)
    print(minelem+maxelem)
    print('done')

if __name__ == '__main__':
    main()
