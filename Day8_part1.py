""" PART 1  """

def data():
    instruction_set = []
    with open('advent8.txt', 'r') as instruct:
        instruct = instruct.read().split('\n')
        for instruction in instruct:
            instruction = instruction.strip()
            instruction_set.append(instruction)
    return instruction_set

def acc(value,i):
    global acc_count
    acc_count += value
    i += 1
    return i
def jmp(value,i):
    i = value + i
    return i
def nop(value, i):
    if value == 0:
        i += 1
        return i
    else:
        i += value
        return i

def main(instruct):
    n = len(instruct)
    count = [0]*n
    i = 0
    while True:
        instruction = instruct[i]
        command = instruction[:3]
        value = int(instruction[4:])
        if (count[i] == 1) or (i > len(instruction)):
            break
        elif command == 'nop':
            count[i] += 1
            i = nop(value,i)
        elif command == 'acc':
            count[i] += 1
            i = acc(value,i)
        elif command == 'jmp':
            count[i] += 1
            i= jmp(value,i)
    return "Loop finished, the value of acc is: "

acc_count = 0
test = main(data())
print(test, acc_count)



