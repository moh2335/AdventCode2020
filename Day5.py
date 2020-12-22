import numpy as np

def data():
    data = []
    with open('advent5.txt') as f:
        for line in f:
            contents = line.split()
            data.append(contents)
    return data

def rowcalc(passInfo, rows):
    i = 0
    while i != 7:
        if passInfo[i] == 'F':
            split = np.split(rows, 2)
            rows = split[0]
            i += 1
        elif passInfo[i] == 'B':
            split = np.split(rows, 2)
            rows = split[1]
            i += 1
    return rows

def colcalc(colInfo, col):
    i = 0
    while i != 3:
        if colInfo[i] == 'L':
            split = np.split(col, 2)
            col = split[0]
            i += 1
        elif colInfo[i] == 'R':
            split = np.split(col, 2)
            col = split[1]
            i += 1
    return col

def boardingPass(data):
    n = len(data)
    rows = np.arange(0,128)
    col = np.arange(0,8)
    highID = 0
    all_ID = []
    for i in range(0, n):
        passInfo = data[i][0]
        colInfo = passInfo[7:]
        rowNumber = rowcalc(passInfo, rows)
        colNumber = colcalc(colInfo, col)
        ID = rowNumber[0]*8 + colNumber[0]
        all_ID.append(ID)
        if ID > highID:
            highID = ID
    return highID, all_ID

answer = boardingPass(data())
print(answer[0])

""" PART 2 """
def yourID(IDs):
    IDs = np.sort(IDs)
    n = len(IDs)
    seatID = 0
    for i in range(0, n-1):
        if IDs[i]+1 != IDs[i+1]:
            seatID = IDs[i]+1
    return seatID

answer2 = yourID(answer[1])
print(answer2)