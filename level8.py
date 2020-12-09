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

def execute(command,i):
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

def execute2(command,i,changed):
    global acc
    changeid = i
    command['acc'] = acc
    command['visited'] += 1
    print(command,i,changed)
    if command['visited'] > 1:
        raise ValueError
    if command['instruction'] == 'nop':
        if 'skip' not in command:
            if changed == False:
                print('changing nop to jmp',changeid,command)
                return command,i+int(command['arg']),changeid
        return command,i+1,None
    elif command['instruction'] == 'acc':
        acc += int(command['arg'])
        return command,i+1,None
    elif command['instruction'] == 'jmp':
        if 'skip' not in command:
            if changed == False:
                print('changing jmp to nop',changeid,command)
                return command,i+1,changeid
        return command,i+int(command['arg']),None


def find_loop(commands):
    i = 0
    while i < len(commands):
        curr = commands[i]
        # print(curr)
        try:
            (commands[i],i) = execute(curr,i)
        except ValueError:
            # print(curr,"was visited already at",i)
            return i
    print('Done acc is ',acc)
    return -1
    
def find_loop2(commands,startat):
    global acc
    changed = False
    changeid = None
    i = startat
    while i < len(commands):
        curr = commands[i]
        # print(curr)
        try:
            prei = copy.deepcopy(i)
            # print(changeid)
            (commands[i],i,temp) = execute2(curr,i,changed)
            commands[i]['prev'] = prei
            if changeid is None:
                changeid = temp
            if not changed:
                changed = changeid is not None
        except ValueError:
            print(curr,"was visited already at",i)
            if changeid is None:
                changeid = startat
            return changeid,i
        except IndexError:
            return -1,-1
    
def reset_commands(commands,id):
    global acc
    acc = 0
    commands[id]['skip'] = True
    for c in commands:
        c['visited'] = 0
        c['acc'] = 0
    # print(commands[stopid],commands[id])



def main():
    inputpath = 'input/inputlevel8'
    # inputpath = 'input/demoinput'
    commands = read_input(inputpath,parse_commands)
    reset = 0
    while reset != -1:
        (reset,stopid) =find_loop2(commands,0) 
        if reset != -1:
            print("resetting",reset,stopid,commands)
            reset_commands(commands,reset)
            reset = commands[reset]['prev']
        # print(commands)
    print(acc)
        # reset = -1
            

if __name__ == '__main__':
    main()
