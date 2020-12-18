import re
import copy
acc = 0

EAST = (1,0)
WEST = (-1,0)
NORTH = (0,1)
SOUTH = (0,-1)
ORDER= [NORTH, EAST, SOUTH, WEST]

def get_direction(s):
    if s == 'E':
        return EAST
    if s == 'N':
        return NORTH
    if s == 'W':
        return WEST
    if s == 'S':
        return SOUTH
        

class ship(object):
    """
    defines a ship
    """
    def __init__(self) -> None:
        super().__init__()
        self.direction = 1
        self.currenteast = 0
        self.currentsouth = 0
        self.waypoint = [10,1]
    
    def manhattenDistance(self):
        d = abs(self.currenteast) + abs(self.currentsouth)
        print(d)

    def parse_command(self,command):
        cmd = command[0]
        arg = int(command[1:])
        print(cmd,arg)
        if cmd in 'RL':
           self.turn(cmd,arg)
        if cmd == 'F':
            self.foreward(arg)
        if cmd in 'NESW':
            direction = get_direction(cmd)
            self.move(direction,arg) 

    def parse_command2(self,command):
        cmd = command[0]
        arg = int(command[1:])
        print(cmd,arg,self.currenteast,self.currentsouth,self.waypoint)
        if cmd in 'RL':
           self.turn_waypoint(cmd,arg)
        if cmd == 'F':
            self.toward(arg)
        if cmd in 'NESW':
            direction = get_direction(cmd)
            self.move_waypoint(direction,arg) 

    def move_waypoint(self, direction,number):
        """
        docstring
        """
        self.waypoint[0] = self.waypoint[0] + direction[0]*number
        self.waypoint[1] = self.waypoint[1] + direction[1]*number

    def move(self, direction,number):
        """
        docstring
        """
        self.currenteast = self.currenteast + direction[0]*number
        self.currentsouth = self.currentsouth + direction[1]*number

    def toward(self,number):
        self.currenteast += self.waypoint[0]*number
        self.currentsouth += self.waypoint[1]*number


    def foreward(self, number):
        """
        docstring
        """
        print(number,self.direction)
        self.currenteast = self.currenteast + ORDER[self.direction][0]*number
        self.currentsouth = self.currentsouth + ORDER[self.direction][1]*number

    def turn_waypoint(self, direction,degrees):
        turns = int(degrees/90 % 4)
        temp = self.waypoint
        if turns == 2:
            self.waypoint[0],self.waypoint[1] = self.waypoint[0]*-1,self.waypoint[1]*-1
            return
        if turns == 1:
            if direction == 'L':
                self.waypoint[0],self.waypoint[1] = self.waypoint[1]*-1, self.waypoint[0]
            if direction == 'R':
                self.waypoint[0],self.waypoint[1] = self.waypoint[1], self.waypoint[0]*-1
        if turns == 3:
            if direction == 'L':
                self.waypoint[0],self.waypoint[1] = self.waypoint[1], self.waypoint[0]*-1
            if direction == 'R':
                self.waypoint[0],self.waypoint[1] = self.waypoint[1]*-1, self.waypoint[0]
        if turns == 4 or turns == 0:
            return


    def turn(self,direction,degrees):
        turns = degrees/90 % 4
        if direction == 'L':
            self.direction = int(self.direction - turns) % 4
        if direction == 'R':
            self.direction = int(self.direction + turns) % 4


def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
        return [x.strip() for x in inputfileobj.readlines()]

def main():
    inputpath = 'input/inputlevel12'
    # inputpath = 'input/demoinput'
    inputarray = read_input(inputpath,parse_input)
    print(inputarray)
    ferry = ship()
    for command in inputarray:
        ferry.parse_command2(command)
    
    ferry.manhattenDistance()

if __name__ == '__main__':
    main()
