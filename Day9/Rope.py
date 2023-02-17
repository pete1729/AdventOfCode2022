import numpy as np
array_size = 10000
offset = 5000

with open('/home/peter/Code/AdventOfCode2022/Day9/input', 'r') as reader:
#with open('/home/peter/Code/AdventOfCode2022/Day9/SmallInput', 'r') as reader:
    lines = reader.readlines()



grid = np.zeros([array_size, array_size], dtype=np.int8)
grid[offset,offset] = 1

H_pos = np.array([0,0], dtype=np.int8)
T_pos = np.array([0,0], dtype=np.int8)

for line in lines:
    direction = line[0]
    distance = int(line[2])
    
    for i in range(distance):
        if direction == "L":
            H_pos = H_pos + np.array([-1,0])
        if direction == "R":
            H_pos = H_pos + np.array([1,0])
        if direction == "U":
            H_pos = H_pos + np.array([0,1])
        if direction == "D":
            H_pos = H_pos + np.array([0,-1])

        if np.linalg.norm(H_pos - T_pos) > 1.5:
            movement_vector = H_pos - T_pos
            if movement_vector[0] > 1:
                movement_vector[0] = 1
            if movement_vector[0] < -1:
                movement_vector[0] = -1
            if movement_vector[1] > 1:
                movement_vector[1] = 1
            if movement_vector[1] < -1:
                movement_vector[1] = -1
            print("H pos", H_pos)
            print("T pos", T_pos)
            print("Movement vector", movement_vector)
            T_pos = T_pos + movement_vector
            grid[T_pos[0] + offset, T_pos[1] + offset] = 1

print(H_pos)
print(T_pos)

print("Number of positions visited:", np.sum(grid))


#2587 too low