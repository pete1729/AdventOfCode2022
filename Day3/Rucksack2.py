
def get_priority(letter):
    unicodePos = ord(letter)
    if unicodePos > 96:
        priority = unicodePos - 96
    else:
        priority = unicodePos - 38
    return priority


sum_priorities = 0

with open('/home/peter/Code/AdventOfCode2022/Day3/input', 'r') as reader:
    lines = reader.readlines()

    a_sack = ""
    b_sack = ""
    c_sack = ""

    for i in range(int(len(lines)/3)):
        a_sack = lines[3*i].strip()
        b_sack = lines[3*i+1].strip()
        c_sack = lines[3*i+2].strip()

        next_priority = 0

        for letter in a_sack:
            if letter in b_sack:
                if letter in c_sack:
                    next_priority = get_priority(letter)
        sum_priorities += next_priority
    #for line in lines:
    #    for letter in line:
    #        if 

print("Sum of priorities:", sum_priorities)