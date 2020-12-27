""" PART 2  """

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
def nop(value,i):
    i += 1
    return i

def main(instruct):
    n = len(instruct)
    count = [0]*n
    i = 0
    while True:    
        if i == n:
            return False
        elif (count[i] == 1):
            global acc_count
            acc_count = 0
            break
        else:
            instruction = instruct[i]
            command = instruction[:3]
            value = int(instruction[4:])
            if command == 'nop':
                count[i] += 1
                i = nop(value,i)
            elif command == 'acc':
                count[i] += 1
                i = acc(value,i)
            elif command == 'jmp':
                count[i] += 1
                i= jmp(value,i)

def alter(instruct):
    jmp_index = []
    nop_index = []
    for i in range(0, len(instruct)):
        instruction = instruct[i]
        command = instruction[:3]
        value = int(instruction[4:])
        if command == 'jmp':
            jmp_index.append(i)
        elif command == 'nop':
            nop_index.append(i)
    for index in jmp_index:
        instruct_alt = instruct.copy()
        old_instruct = instruct_alt[index]
        new_instruct = old_instruct.replace('jmp', 'nop')
        instruct_alt[index] = new_instruct
        test = main(instruct_alt)
        if test  == False:
            return "The boot_loop is solved, with acc:"
    for index in nop_index:
        instruct_alt = instruct.copy()
        old_instruct = instruct_alt[index]
        new_instruct = old_instruct.replace('nop', 'jmp')
        instruct_alt[index] = new_instruct
        test = main(instruct_alt)
        if test == False:
            return "The boot_loop is solved, with acc:"
            
acc_count = 0
test = alter(data())
print(test, acc_count)

