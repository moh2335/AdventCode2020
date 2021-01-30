import numpy as np
import itertools
def data():
    input = []
    with open('advent9.txt', 'r') as lines:
        lines = lines.read().split('\n')
        for line in lines:
            line = int(line)
            input.append(line)
    return input

# Recursive function
def prmble(input):
    start = np.array(input[:25])
    return start

def main(input, start):
    checks = []
    input = np.array(input)
    data = input.copy()
    for digit in input[25:]:
        res = digit - start
        check = np.intersect1d(res, start)
        if check.any() == 0:
            checks.append(digit)
        else:
            data = np.delete(data, 0)
            start = prmble(data)
    return checks[0]

preamble = prmble(data())
N = main(data(), preamble)
print("The number you're looking for is {}.".format(N))

""" PART 2 """

def main2(N, input):
    index  = np.where(input == N)
    data = input[:index[0][0]]
    for i in range(len(data)):
        for j in itertools.combinations(data, i):
            print(j)

test = main2(N, data())

