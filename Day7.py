# Used as help: https://github.com/ArcaneIRE/AdventOfCode2020/tree/master/day7

def data():
    with open('advent7.txt', 'r') as rules:
        rules = rules.read().split('.\n')
    return rules 

def analyzer(child):
    for parent in bagsdict:
        contents = bagsdict[parent]
        if child in contents:
            analyzer(parent)
            confirmed_bags.add(parent) 
    return

def find_parents(child_bag):
    for parent in bagsdict:
        contents = bagsdict[parent]
        if child_bag in contents:
            find_parents(parent)
            confirmed_bags.add(parent)
    return

def bags(bags):
    bags_dict = {}
    for bag in bags:
        bag = bag.replace(' bags', '').replace(' bag', '')
        bag = bag.split('contain ')
        bags_dict[bag[0].strip()] = bag[1]
    return bags_dict

bagsdict = bags(data())
confirmed_bags = set()
find_parents('shiny gold')
print(len(confirmed_bags))

""" PART 2 """
def part2(parent_bag):
    content = bagsdict[parent_bag]
    if content  == 'no other' or content == 'no other.':
        return
    else:    
        inner_bags = content.split(', ')
        for bags in inner_bags:
            amount = int(bags[:2])
            bag_name = bags[2:]
            if bag_name in bag_count:
                bag_count[bag_name] += amount
            else:
                bag_count[bag_name] = amount
            for i in range(amount):
                part2(bag_name)
        return  
    
bag_count = {}
part2('shiny gold')
answer2 = sum(bag_count.values())
print(answer2)