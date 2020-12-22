import re
from collections import Counter

def data():    
    with open("advent6.txt") as f:
        lines = f.read()
    questions = lines.split('\n\n')
    return questions

def part1(data):
    n = len(data)
    count = []
    for i in range(0, n):
        repeats = data[i]
        non_repeats = "".join(set(repeats))
        non_repeats_clean = non_repeats.replace('\n', '')
        n_answers = len(non_repeats_clean)
        count.append(n_answers)
    Total = sum(count)
    return Total

answer1 = part1(data())
print(answer1)

""" PART 2 """

def part2(data):
    n = len(data)
    count = []
    for i in range(0, n):
        string = re.split('\n', data[i])
        maxRange = len(string)
        if maxRange == 1:
            n_answers = len(string[0])
            count.append(n_answers)
        else:
            smallest_string = min(string, key=len)
            min_length = len(smallest_string)
            miniCount = 0
            char_list = []
            for i in range(0, maxRange):
                char = re.findall('[a-z]', string[i])
                char_list.extend(char)
            c = Counter(char_list)
            c = list((dict(c)).items())
            for i in range(0, len(c)):
                if c[i][1] == maxRange:
                    miniCount += 1
            count.append(miniCount)
    return sum(count)

answer2 = part2(data())
print(answer2)