import numpy as np

class Monkey:
    def __init__(self, item_list, a_in, b_in, c_in, d_in, t_in, f_in):
        self.items = item_list
        self.a = a_in
        self.b = b_in
        self.c = c_in
        self.d = d_in
        self.t_monk = t_in
        self.f_monk = f_in
    
    # new = a*old*old + b*old + c
    a = 0
    b = 0
    c = 0

    # divisibility test
    d = 1

    # true monkey
    t_monk = 1

    #false monkey
    f_monk = 1

    number_of_inspections = 0

    items = []

    def receive_item(self, item):
        self.items.append(item)
        self.items.sort()

    def process_items(self):
        while(len(self.items) > 0):
            next_item = self.items.pop(0)
            next_item = self.a*next_item*next_item + self.b*next_item + self.c
            print(next_item)
            next_item = int(np.floor(next_item/3))
            print(next_item)
            if next_item % self.d == 0:
                monkeys[self.t_monk].receive_item(next_item)
                print("Throwing to", self.t_monk)
            else:
                monkeys[self.f_monk].receive_item(next_item)
                print("Throwing to", self.f_monk)
            print()
            self.number_of_inspections += 1


with open('/home/peter/Code/AdventOfCode2022/Day11/input', 'r') as reader:
    lines = reader.readlines()

monkeys = []

# set up initial array of items
#items = []
for line_num, line in enumerate(lines):
    if line[0:6] == "Monkey":
        aa = 0
        bb = 0
        cc = 0
        dd = 0
        true_monk = 0
        false_monk = 0
        next_items = lines[line_num+1][18:]
        next_item_list = next_items.split(",")
        for pos, item in enumerate(next_item_list):
            next_item_list[pos] = int(item.strip())
        next_operation = lines[line_num+2][23:]
        if next_operation[0:5] == "* old":
            aa = 1
        elif next_operation[0] == "*":
            bb = int(next_operation[2:])
        elif next_operation[0] == "+":
            bb = 1
            cc = int(next_operation[2:])
        dd = int(lines[line_num+3][21:])
        true_monk = int(lines[line_num+4][29:])
        false_monk = int(lines[line_num+5][29:])

        
        #items.append(next_item_list)
        monkeys.append(Monkey(next_item_list, aa, bb, cc, dd, true_monk, false_monk))

#print("Initial item list:", items)

num_rounds = 20

top_num_inspect = 0
second_num_inspect = 0

for round in range(num_rounds):
    for next_monkey in monkeys:
        next_monkey.process_items()

    for next_monkey in monkeys:
        print(next_monkey.items)
        print("Number of inspections:", next_monkey.number_of_inspections)
        if next_monkey.number_of_inspections > top_num_inspect:
            second_num_inspect = top_num_inspect
            top_num_inspect = next_monkey.number_of_inspections
        elif next_monkey.number_of_inspections > second_num_inspect:
            second_num_inspect = next_monkey.number_of_inspections
#    print(next_monkey.a)
#    print(next_monkey.b)
#    print(next_monkey.c)
#    print(next_monkey.d)
#    print(next_monkey.t_monk)
#    print(next_monkey.f_monk)
#    print()

print("Monkey business:", top_num_inspect*second_num_inspect)