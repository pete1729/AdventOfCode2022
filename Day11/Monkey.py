
class Monkey:
    def __init__(self, item_list):
        self.items = item_list
        print("Item list:", item_list)
    
    # new = a*old*old + b*old
    a = 0
    b = 0

    # divisibility test
    c = 1

    # true monkey
    t_monk = 1

    #false monkey
    f_monk = 1

    items = []

    #monkey number
    monkey_num = 0


with open('/home/peter/Code/AdventOfCode2022/Day11/smallinput', 'r') as reader:
    lines = reader.readlines()

monkeys = []

# set up initial array of items
items = []
for line_num, line in enumerate(lines):
    if line[0:6] == "Monkey":
        next_items = lines[line_num+1][18:]
        next_item_list = next_items.split(",")
        for pos, item in enumerate(next_item_list):
            next_item_list[pos] = int(item.strip())
        items.append(next_item_list)
        monkeys.append(Monkey(next_item_list))

print("Initial item list:", items)

round = 1

for next_monkey in monkeys:
    print(next_monkey.items)
