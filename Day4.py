import re

def data():    
    with open("advent4.txt") as f:
        lines = f.read()
    passports = lines.split('\n\n')
    return passports

def passport_check(data):
    validPassports = []
    count = 0
    checks = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    total = len(data)
    for i in range(0, total):
        if all(x in data[i] for x in checks):
            count += 1
            validPassports.append(data[i])
    return validPassports, count

passports,answer1 = passport_check(data())
print(answer1)

""" PART 2 """

def passport_check2(passports):
    d = {}
    count = 0
    eclCheck = ['amb', 'blu', 'brn', 'grn', 'hzl', 'oth', 'gry']
    total = len(passports)
    for i in range(0, total):
        idInfo = re.split(' |\n',passports[i])
        for n in range(0, len(idInfo)):
            keyval = re.split(':',idInfo[n])
            key = keyval[0]
            val = keyval[1]
            if key == 'byr' or key == 'iyr' or key == 'eyr':
                d[key] = int(val)
            else:
                d[key] = val        
        if (len(d['pid']) == 9) and (d['pid'].isnumeric() == True):             # Check pid
            if any(x in d['ecl'] for x in eclCheck):                            # Check eyecolour
                hcl = d['hcl']
                hcl = hcl[1:]
                if len(hcl) == 6 and (re.search('[a-f]+',hcl) or (hcl.isnumeric() == True)):        # Check haircolour
                    if (1920 <= d['byr'] <= 2002) and (2010 <= d['iyr'] <= 2020) and (2020 <= d['eyr'] <= 2030):    # Check all dates
                        if re.search('cm', d['hgt']) and len(d['hgt']) == 5:                        # Check heights
                             height = d['hgt']
                             heightInt = int(height[0:3])
                             if 150 <= heightInt <= 193:
                                 count += 1
                        elif re.search('in', d['hgt']) and len(d['hgt']) == 4:
                            height = d['hgt']
                            heightInt = int(height[0:2])
                            if 59 <= heightInt <= 76:
                                count += 1
    return count

answer2 = passport_check2(passports)
print(answer2)