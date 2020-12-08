import math

trees = 0
map = []

with open('inputlevel3.txt','r') as inputfile:
    # going to cheat a little
    map = [x.strip() for x in inputfile.readlines()]

def slope(right,down):
    x=0
    y=0
    map2 = []
    while len(map2) <len(map)-1:
        # print('before',x,y,map[x][y])
        x+=down
        y+=right
        if y>=len(map[0]):
            y-=len(map[0])
        # print('after',x,y,map[x][y])
        if x > len(map):
            break    
        map2.append(map[x][y])
    return map2.count('#')

slopes = []
slopes.append(slope(1,1))
slopes.append(slope(3,1))
slopes.append(slope(5,1))
slopes.append(slope(7,1))
slopes.append(slope(1,2))



print(slopes,math.prod(slopes))