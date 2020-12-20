from os import wait
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

def get_minimal_wait_time(timestamp,bus_schedule):
    best_wait_time = None
    selected_bus = None
    for b in bus_schedule:
        if b != 'x':
            busid = int(b)
            next_arriaval = (timestamp//busid +1) * busid
            wait_time = next_arriaval - timestamp
            if best_wait_time is None or best_wait_time > wait_time:
                best_wait_time = wait_time
                selected_bus = busid
    return best_wait_time,selected_bus

def main():
    inputpath = 'input/inputlevel13'
    # inputpath = 'input/demoinput'
    (timestamp,bus_schedule) = read_input(inputpath,parse_input)
    print(timestamp,bus_schedule)
    (minimal_wait_time,bus) = get_minimal_wait_time(timestamp,bus_schedule)
    print(minimal_wait_time,bus,minimal_wait_time*bus)
if __name__ == '__main__':
    main()
