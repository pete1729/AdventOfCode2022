
with open('/home/peter/Code/AdventOfCode2022/Day1/input', 'r') as reader:
# Read & print the first 5 characters of the line 5 times
    lines = reader.readlines()
    print("Number of lines:", len(lines))
    num_elves = 1
    for i in range(len(lines)):
        if lines[i] == '\n':
            num_elves += 1
        #if isinstance(lines[i].strip(), int):
        #    num_elves += 1
    print("Number of elves:", num_elves)

    max_carry = 0
    next_carry = 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            next_carry += int(lines[i])
        else:
            if next_carry > max_carry:
                max_carry = next_carry
            next_carry = 0
    print("Maximum load:", max_carry)

    top_three = [0,0,0]
    next_carry = 0
    for i in range(len(lines)):
        if lines[i] != "\n":
            next_carry += int(lines[i])
        else:
            if next_carry > top_three[0]:
                if next_carry > top_three[2]:
                    top_three[0] = top_three[1]
                    top_three[1] = top_three[2]
                    top_three[2] = next_carry
                elif next_carry > top_three[1]:
                    top_three[0] = top_three[1]
                    top_three[1] = next_carry
                else:
                    top_three[0] = next_carry
            next_carry = 0
    print("Top three:", top_three[0], top_three[1], top_three[2])
    print("Sum of top three:", sum(top_three))