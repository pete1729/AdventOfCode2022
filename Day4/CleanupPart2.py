import re

overlap_count = 0

with open('/home/peter/Code/AdventOfCode2022/Day4/input', 'r') as reader:
    lines = reader.readlines()
    for line in lines:
        line = line[0:-1]
        end_points = re.split(r',|-', line)
        for i in range(4):
            end_points[i] = int(end_points[i])
        print(end_points)
        if (end_points[2] <= end_points [1]) and (end_points[3] >= end_points[0]):
            overlap_count += 1
            print("a")
        elif (end_points[0] <= end_points [3]) and (end_points[1] >= end_points[2]):
            overlap_count += 1
            print("a")

print("Overlap count:", overlap_count)