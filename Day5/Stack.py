import re

with open('/home/peter/Code/AdventOfCode2022/Day5/input', 'r') as reader:
    lines = reader.readlines()

    base_line_num = 0
    base_line_found = 0
    line_num = 0
    while base_line_found == 0:
        line_num += 1
        if lines[line_num][1] == "1":
            base_line_found = 1
            base_line_num = line_num
    print("Line of bin numbers:", base_line_num)

    bin_nums = re.split(r'   ', lines[base_line_num])
    for i in range(len(bin_nums)):
        bin_nums[i] = int(bin_nums[i].strip())
    print("Bin numbers:", bin_nums)

    stack_contents = []
    for i in range(len(bin_nums)):
        stack_contents.append([])
    print(stack_contents)

    line_3 = re.split(r'\W+', lines[3])
    line_3.remove('')
    line_3.remove('')
    print(line_3)

    start_line = base_line_num -1
    print("Start line:", start_line)
    print(lines[start_line])


    for current_line in range(start_line,0,-1):
        for i in range(len(stack_contents)):
            next_crate = lines[current_line][4*i+1]
            if next_crate != " ":
                stack_contents[i].append(next_crate)
        print("Stack contents", stack_contents)

my_list = [3,4,5]
my_list.append(6)
print(my_list)
print(my_list.pop())
print(my_list)

list_of_lists = []
list_of_lists.append([])
list_of_lists.append([1,2,3])
list_of_lists.append([4,5,6])
list_of_lists[1].append(7)
print(list_of_lists)
print(list_of_lists[0])
