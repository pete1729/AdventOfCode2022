import numpy as np

with open('/home/peter/Code/AdventOfCode2022/Day10/input', 'r') as reader:
    lines = reader.readlines()

    X_register = np.zeros(100000, dtype=int)
    print(len(X_register))
    print(lines[0])

    cycle = 1
    X_register[cycle-1] = 1
    position_in_cycle = 0 # 0 - start, 1 - middle, 2 - end

    for line in lines:
        if line[0:4] == "noop":
            #print("noop!")
            X_register[cycle] = X_register[cycle-1]
            cycle += 1

        elif line[0:4] == "addx":
            #print("addx!")
            increment = int(line[5:])
            #print(increment)
            X_register[cycle] = X_register[cycle-1]
            cycle += 1
            X_register[cycle] = X_register[cycle-1] + increment
            cycle += 1


signal_strength_sum = 0
for i in range(19,220,40):
    print(X_register[i])
    signal_strength_sum += X_register[i]*(i+1)
print("Sum of signal strengths:", signal_strength_sum)