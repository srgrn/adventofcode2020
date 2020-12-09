import re
import copy
acc = 0

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_commands(inputfileobj):
    commands = []
    for line in inputfileobj.readlines():
        c = {}
        (c['instruction'],c['arg']) = line.strip().split(' ')
        c['visited'] = 0
        commands.append(c)
    return commands

def execute(command,i,changed):
    global acc
    command['acc'] = acc
    command['visited'] += 1
    if command['visited'] > 1:
        raise ValueError
    if command['instruction'] == 'nop':
        return command,i+1
    elif command['instruction'] == 'acc':
        acc += int(command['arg'])
        return command,i+1
    elif command['instruction'] == 'jmp':
        return command,i+int(command['arg'])

def find_loop(commands):
    i = 0
    changed = None
    while i < len(commands):
        curr = commands[i]
        print(curr)
        try:
            (commands[i],i) = execute(curr,i,changed)
        except ValueError:
            print(curr,"was visited already at",i)
            return i
    print('Done acc is ',acc)
    return i

            

def main():
    # inputpath = 'input/inputlevel8'
    inputpath = 'input/demoinput'
    commands = read_input(inputpath,parse_commands)
    commands2 = copy.deepcopy(commands)
    find_loop(commands)
    
            

if __name__ == '__main__':
    main()
