import numpy as np
grid = []

alphabet = "abcdefghijklmnopqrstuvwxyz"

with open('/home/peter/Code/AdventOfCode2022/Day12/input', 'r') as reader:
    lines = reader.readlines()
    for pos,line in enumerate(lines):
        grid.append([])
        for letter in line:
            if letter != "\n":
                grid[pos].append(letter)

start_x = 0
start_y = 0

finish_x = 0
finish_y = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start_x = i
            start_y = j
        if grid[i][j] == "E":
            finish_x = i
            finish_y = j

print("Start Coordinates:", start_x, start_y)
print("Finish Coordinates:", finish_x, finish_y)

to_finish = np.zeros((len(grid), len(grid[0])), dtype=int)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        to_finish[i][j] = 10000
to_finish[finish_x][finish_y] = 0
print(to_finish)

finished = 0

current_x = finish_x
current_y = finish_y
grid[finish_x][finish_y] = "z"
grid[start_x][start_y] = "a"

#while finished == 0:
for k in range(1000):
    print("Round", k)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if to_finish[i][j] < 10000:
                current_x = i
                current_y = j
                #print("Steps to finish", to_finish[i,j])

                #print("Current x:", current_x)
                #print("Current y:", current_y)
                #print()

                if current_y > 0:
                    left_x = current_x
                    left_y = current_y - 1
                    if ord(grid[current_x][current_y]) - ord(grid[left_x][left_y]) <= 1:
                        to_finish[left_x][left_y] = min(to_finish[left_x][left_y], to_finish[current_x][current_y] +1)

                if current_y < len(grid[0]) - 1:
                    right_x = current_x
                    right_y = current_y + 1
                    if  ord(grid[current_x][current_y]) - ord(grid[right_x][right_y])<= 1:
                        to_finish[right_x][right_y] = min(to_finish[right_x][right_y], to_finish[current_x][current_y] +1)

                if current_x > 0:
                    up_x = current_x - 1
                    up_y = current_y
                    if ord(grid[current_x][current_y]) - ord(grid[up_x][up_y])  <= 1:
                        to_finish[up_x][up_y] = min(to_finish[up_x][up_y], to_finish[current_x][current_y] +1)

                if current_x < len(grid) - 1:
                    down_x = current_x + 1
                    down_y = current_y
                    if  ord(grid[current_x][current_y]) - ord(grid[down_x][down_y]) <= 1:
                        to_finish[down_x][down_y] = min(to_finish[down_x][down_y], to_finish[current_x][current_y] +1)


print("Number of steps required:", to_finish[start_x][start_y])

fewest_steps_from_a = 1000

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "a":
            if to_finish[i][j] < fewest_steps_from_a:
                fewest_steps_from_a = to_finish[i][j]

print("Fewest steps from a:", fewest_steps_from_a)