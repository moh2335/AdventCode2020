import re
# 1-2 x: xpxc
def data():
    data = []
    with open('advent2.txt') as f:
        for line in f:
            contents = line.split()
            data.append(contents)
    return data

def pass_check(data):
    n = 0
    j = 0
    for i in range(0, len(data)):
        rule_count = re.split("-", data[i][0])
        rule_letter = re.split(":", data[i][1])
        letter = rule_letter[0]
        password_rule = re.split("^(.+)", data[i][2])
        password = password_rule[1]
        min_count = int(rule_count[0])
        max_count = int(rule_count[1])
        count = password.count(letter)
        if min_count <= count <= max_count:
            n += 1
        else:
            j += 1
    return n,j



answer = pass_check(data())
print(answer)


""" PART 2  """

def pass_check_toboggan(data):
    n = 0
    j = 0
    for i in range(0, len(data)):
        rule_count = re.split("-", data[i][0])
        rule_letter = re.split(":", data[i][1])
        letter = rule_letter[0]
        password_rule = re.split("^(.+)", data[i][2])
        password = password_rule[1]
        first_location = int(rule_count[0]) - 1
        second_location = int(rule_count[1]) - 1
        if password[first_location] == letter or password[second_location] == letter:
            if password[first_location] == letter and password[second_location] == letter:
                j += 1
            else:
                n += 1
    return n,j

answer2 = pass_check_toboggan(data())
print(answer2)