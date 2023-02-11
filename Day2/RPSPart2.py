with open('/home/peter/Code/AdventOfCode2022/Day2/input', 'r') as reader:
# Read & print the first 5 characters of the line 5 times
    lines = reader.readlines()
    print(len(lines))
    total_score = 0

    for line in lines:
        if line[0] == "A" and line[2] == "X":
            total_score += 3
        elif  line[0] == "A" and line[2] == "Y":
            total_score += 4
        elif  line[0] == "A" and line[2] == "Z":
            total_score += 8
        elif  line[0] == "B" and line[2] == "X":
            total_score += 1
        elif  line[0] == "B" and line[2] == "Y":
            total_score += 5
        elif  line[0] == "B" and line[2] == "Z":
            total_score += 9
        elif  line[0] == "C" and line[2] == "X":
            total_score += 2
        elif  line[0] == "C" and line[2] == "Y":
            total_score += 6
        elif  line[0] == "C" and line[2] == "Z":
            total_score += 7
    print(total_score)