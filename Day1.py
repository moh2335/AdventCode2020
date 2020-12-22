def data():
    data = []
    with open('advent1.txt') as f:
        for line in f:
            contents = line.split()
            data.append(int(contents[0]))
    return data

def current_year(data):
    sum = 0
    i = 0
    j = 0
    count = len(data)
    for i in range(0,count):
        for j in range(0,count):
            for k in range(0,count):
                sum = data[i] + data[j] + data[k]
                if sum==2020:
                    mult = data[i]*data[j]*data[k]
                    return mult
                else:
                    k += 1
            j += 1
        i += 1

answer = current_year(data()) 
print(answer)
