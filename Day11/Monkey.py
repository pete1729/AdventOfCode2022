with open('/home/peter/Code/AdventOfCode2022/Day11/input', 'r') as reader:
    lines = reader.readlines()

items = []
for line_num, line in enumerate(lines):
    if line[0:6] == "Monkey":
        next_items = lines[line_num+1][18:]
        next_item_list = next_items.split(",")
        for pos, item in enumerate(next_item_list):
            next_item_list[pos] = int(item.strip())
        print(next_item_list)