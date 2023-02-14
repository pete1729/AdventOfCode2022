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

    start_line = base_line_num -1
    print("Start line:", start_line)
    print(lines[start_line])

    for current_line in range(start_line,-1,-1):
        for i in range(len(stack_contents)):
            next_crate = lines[current_line][4*i+1]
            if next_crate != " ":
                stack_contents[i].append(next_crate)
    
    print("Stack contents", stack_contents)

    for line_num in range(base_line_num+2,len(lines)):
        print(lines[line_num])
        if lines[line_num][6] == "":
            num_to_move = int(lines[line_num][5])
        else:
            num_to_move = int(lines[line_num][5:7])
        source_stack = int(lines[line_num][-7])
        dest_stack = int(lines[line_num][-2])
        print("Num to move:", num_to_move)
        print("Source stack:", source_stack)
        print("Destination stack:", dest_stack)

        removed_contents = []
        for i in range(num_to_move):
            removed_contents.append(stack_contents[source_stack-1].pop())
        print("Removed contents:", removed_contents)

        for i in range(num_to_move):
            stack_contents[dest_stack-1].append(removed_contents[num_to_move-1-i])
        print(stack_contents)
        print()

    out_message = ""
    for i in range(len(stack_contents)):
        out_message = out_message + stack_contents[i][-1]
    print(out_message)