import re
import copy
acc = 0

def read_input(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parse_input(inputfileobj):
    arr = []
    for line in inputfileobj.readlines():
        arr.append(list(line.strip()))
    return arr

def get_sqaure(arr,row,col):
    around = []
    # print(row,col)
    for i in range(-1,2):
        for j in range(-1,2):
            crow = row + i
            ccol = col + j
            if i == 0 and j == 0:
                continue
            if crow < 0 or crow > len(arr)-1:
                continue
            if ccol < 0 or ccol > len(arr[row])-1:
                continue
            # print('-',crow,ccol)
            around.append(arr[crow][ccol])
    return around

def get_viewed_seats_status(arr,origx,origy,xstep,ystep):
    x = origx+xstep
    y = origy+ystep
    xlen = len(arr)
    ylen = len(arr[origx])
    while x >= 0 and y >=0 and x < xlen and y < ylen:
        if arr[x][y] != '.':
            return arr[x][y]
        x+= xstep
        y+= ystep

    return None

def get_sqaure2(arr,row,col):
    around = []
    around.append(get_viewed_seats_status(arr,row,col, -1, -1))
    around.append(get_viewed_seats_status(arr,row,col, -1, 0))
    around.append(get_viewed_seats_status(arr,row,col, -1, 1))
    around.append(get_viewed_seats_status(arr,row,col, 0, 1))
    around.append(get_viewed_seats_status(arr,row,col, 1, 1))
    around.append(get_viewed_seats_status(arr,row,col, 1, 0))
    around.append(get_viewed_seats_status(arr,row,col, 1, -1))
    around.append(get_viewed_seats_status(arr,row,col, 0, -1))
    return around

def turn(arr):
    nextphase = []
    changes = 0
    for row in range(len(arr)):
        nextphase.append([None] * len(arr[row]))
        for col in range(len(arr[row])):
            if arr[row][col] == '.':
                nextphase[row][col] = '.'
                continue
            around = get_sqaure(arr,row,col)
            if arr[row][col] == '#':
                if around.count('#') >= 4:
                    nextphase[row][col] = 'L'
                else:
                    nextphase[row][col] = '#'
            if arr[row][col] == 'L':
                if around.count('#') == 0:
                    nextphase[row][col] = '#'
                else:
                    nextphase[row][col] = 'L'
            if arr[row][col] != nextphase[row][col]:
                # print(arr[row][col],nextphase[row][col])
                changes +=1
    return nextphase,changes

def turn2(arr):
    nextphase = []
    changes = 0
    for row in range(len(arr)):
        nextphase.append([None] * len(arr[row]))
        for col in range(len(arr[row])):
            if arr[row][col] == '.':
                nextphase[row][col] = '.'
                continue
            around = get_sqaure2(arr,row,col)
            if arr[row][col] == '#':
                if around.count('#') >= 5:
                    nextphase[row][col] = 'L'
                else:
                    nextphase[row][col] = '#'
            if arr[row][col] == 'L':
                if around.count('#') == 0:
                    nextphase[row][col] = '#'
                else:
                    nextphase[row][col] = 'L'
            if arr[row][col] != nextphase[row][col]:
                # print(arr[row][col],nextphase[row][col])
                changes +=1
    return nextphase,changes

def main():
    inputpath = 'input/inputlevel11'
    # inputpath = 'input/demoinput'
    inputarray = read_input(inputpath,parse_input)
    # print(inputarray)
    arr,changes = turn2(inputarray)
    count = 0
    while changes != 0:
        count +=1
        arr,changes = turn2(arr)
    print(count)
    occupied = 0
    for i in arr:
        occupied += i.count('#')
    print(occupied)

if __name__ == '__main__':
    main()
