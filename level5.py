
def openinput(path,callback):
    with open(path,'r') as inputfile:
        return callback(inputfile)

def parsefile(f):
    return f.readlines()

def main():
    # inputfile = 'demoinput.txt'
    inputfile = 'inputlevel5.txt'
    maxseat = 0
    seats = []
    for line in openinput(inputfile,parsefile):
        row = line[:7]
        col = line[7:]
        colnum = 0
        row = row.replace('F','0').replace('B','1')
        rownum = int(row,2)
        col = col.replace('L','0').replace('R','1')
        colnum = int(col,2)

        seatid = rownum*8 + colnum
        seats.append(seatid)
        print(rownum, colnum, seatid)
        if seatid > maxseat: 
            maxseat = seatid
    seats = sorted(seats)
    for i in range(seats[0],seats[-1]):
        if i not in seats:
            print('missing',i)
    print(maxseat,seats)

if __name__ == "__main__":
    main()