import numpy as np
array_size = 100000

#with open('/home/peter/Code/AdventOfCode2022/Day9/input', 'r') as reader:
with open('/home/peter/Code/AdventOfCode2022/Day9/SmallInput', 'r') as reader:
    lines = reader.readlines()

grid = np.zeros([array_size, array_size], dtype=np.int8)

H_pos = np.array([0,0], dtype=np.int8)
T_pos = np.array([0,0], dtype=np.int8)

for line in lines:
    direction = line[0]
    distance = int(line[2])
    
    if direction == "L":
        for i in range(distance):
            H_pos = H_pos + np.array([0,-1])
    if direction == "R":
        for i in range(distance):
            H_pos = H_pos + np.array([0,1])
    if direction == "U":
        for i in range(distance):
            H_pos = H_pos + np.array([1,0])
    if direction == "D":
        for i in range(distance):
            H_pos = H_pos + np.array([-1,0])

print(H_pos)