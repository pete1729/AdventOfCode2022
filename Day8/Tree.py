import numpy as np

with open('/home/peter/Code/AdventOfCode2022/Day8/small_input', 'r') as reader:
    lines = reader.readlines()
    print(lines[0][:-1])

    print(len(lines[0][:-1]))
    print(len(lines))

    tree_array = np.zeros([len(lines[0][:-1]), len(lines)])

    for i in range(len(lines)):
        for j in range(len(lines[i][:-1])):
            tree_array[i,j] = lines[i][j]

print(tree_array)

