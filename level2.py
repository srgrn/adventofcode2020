import sys
valid = 0

def validate_part1(policy, password):
    (policynum,policychar) = policy.split(' ')
    pmin,pmax = policynum.split('-')
    if  int(pmin) <= password.count(policychar) <= int(pmax):
        return True
    return False
    
def validate_part2(policy, password):
    (policynum,policychar) = policy.split(' ')
    first,second = policynum.split('-')
    charfirst = password[int(first)-1]
    charsecond = password[int(second)-1]
    if charfirst == charsecond:
        return False
    if charfirst != charsecond:
        if charfirst == policychar:
            return True
        elif charsecond == policychar:
            return True
        return False


with open('inputlevel2.txt','r') as inputfile:
    for line in inputfile.readlines():
        (policy,password) = line.split(': ')
        if validate_part2(policy, password):
            print("true for",line)
            valid+=1

print(valid)