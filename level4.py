import math
import re

def verify2(passport):
    if int(passport['byr']) > 2002 or int(passport['byr']) < 1920 :
        return False
    if int(passport['iyr']) > 2020 or int(passport['iyr']) < 2010 :
        return False
    if int(passport['eyr']) > 2030 or int(passport['eyr']) < 2020 :
        return False
    if 'in' in passport['hgt']:
        if int(passport['hgt'].replace('in','')) <59 or int(passport['hgt'].replace('in','')) > 76:
            return False
    elif 'cm' in passport['hgt']:
        if int(passport['hgt'].replace('cm','')) <150 or int(passport['hgt'].replace('cm','')) > 193:
            return False
    else:
        return False

    if not re.match('#[0-9a-f]{6}$',passport['hcl']):
        return False
    if passport['ecl'] not in [ 'amb' ,'blu' ,'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not re.match('\d{9}$',passport['pid']):
        return False
    return True

def verify1(passportstring):
    passport = {}
    fields = re.split('\s',passportstring.strip())
    for field in fields:
        (key,value) = field.split(':')
        passport[key] = value

    for key in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
        if key not in passport.keys():
            return False
    valid2 = verify2(passport)
    print(passport,valid2)
    return valid2
    
passportcount = 0
valid = 0

with open('inputlevel4.txt','r') as inputfile:
    passportstring = ""
    for line in inputfile.readlines():
        if re.match('^$',str(line)):
            passportcount+=1
            validpassport = verify1(passportstring)
            passportstring=""
            if validpassport:
                valid +=1
        else:
            passportstring += line
passportcount+=1
validpassport = verify1(passportstring)
passportstring=""
if validpassport:
    valid +=1
print(passportcount) 
print(valid)

