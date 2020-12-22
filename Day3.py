def data():
    data = []
    with open('advent3.txt') as f:
        for line in f:
            contents = line.split()
            data.append(contents)
    return data

def nav(data):
    treeCount = 0
    rows = len(data)
    columns = len(data[0][0])
    j = 0
    i = 0
    while True:
        i += 1
        j += 3
        if i >= rows:
            break
        else:
            string = data[i][0] 
            if j >= columns:
                j = j - columns
                if string[j] == '#':
                    treeCount += 1    
            else: 
                if string[j] == '#':
                    treeCount += 1
    return treeCount

info = nav(data())
print(info)


""" PART 2 """

def nav2(data):
    allCount = []
    result = 1
    slope_i = [1,1,1,1,2]
    slope_j = [1,3,5,7,1]
    for n in range(0, len(slope_i)):
        treeCount = 0
        rows = len(data)
        columns = len(data[0][0])
        j = 0
        i = 0
        while True:
            i += slope_i[n]
            j += slope_j[n]
            if i >= rows:
                break
            else:
                string = data[i][0] 
                if j >= columns:
                    j = j - columns
                    if string[j] == '#':
                        treeCount += 1    
                else: 
                    if string[j] == '#':
                        treeCount += 1
        allCount.append(treeCount)
    for trees in allCount:
        result = result * trees
    return result

info2 = nav2(data())
print(info2)