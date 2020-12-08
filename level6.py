import re
from collections import Counter

def openinput(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parsefile(f):
    return f.readlines()

def get_counts(count,num_of_people):
    return list(count.keys())

def get_counts2(count,num_of_people):
    result = []
    for key in count:
        if count[key] == num_of_people:
            result.append(key)
    return result

def main():
    # inputfile = 'demoinput.txt'
    inputfile = 'inputlevel6'
    input = openinput(inputfile,parsefile)
    count = Counter()
    members = 0
    input.append('\n')
    groups = []
    for line in input:
        if re.match('^$',line):
            groups.append(get_counts2(count,members))
            print(count,members,groups[-1])
            count.clear()
            members = 0
            continue
        count.update(line.strip())
        members+=1
    yes = [len(x) for x in groups]
    sum_of_yes = sum(yes)
    print(sum_of_yes)

if __name__ == "__main__":
    main()