import re
import numpy as np

grid = np.zeros([200,200])
num_locations = 0
offset = 100

with open('/home/peter/Code/AdventOfCode2022/Day15/smallinput', 'r') as reader:
    lines = reader.readlines()

    for line in lines:
        if line:
            num_locations += 1

sensor_locations = np.zeros((num_locations,2), dtype=int)
beacon_locations = np.zeros((num_locations,2), dtype=int)

for i,line in enumerate(lines):
    split_line = line.split("=")
    split_line = split_line[1:]
    coordinates = [int(re.sub("[^0-9-]", "", token)) for token in split_line]

    sensor_locations[i][0] = coordinates[0] + offset
    sensor_locations[i][1] = coordinates[1] + offset
    beacon_locations[i][0] = coordinates[2] + offset
    beacon_locations[i][1] = coordinates[3] + offset

print(sensor_locations)
print(beacon_locations)
print(beacon_locations[0]-sensor_locations[0])
print(np.sum(np.abs(beacon_locations[0]-sensor_locations[0])))
distances = [0]*num_locations

for i in range(num_locations):
    distances[i] = np.sum(np.abs(sensor_locations[i]-beacon_locations[i]))

    for x in range(max(sensor_locations[i][0]-distances[i],0), sensor_locations[i][0]+distances[i]):
        for y in range(max(sensor_locations[i][1]-distances[i],0), sensor_locations[i][1]+distances[i]):
            if np.sum(np.abs(sensor_locations[i]-np.array([x,y]))) <= distances[i]:
                #print("X", x)
                #print("Y", y)
                #print(distances[i])
                #print(sensor_locations[i])
                #if np.array([x,y]) not in beacon_locations and np.array([x,y]) not in sensor_locations:
                grid[x,y] = 1

for i in range(num_locations):
    grid[sensor_locations[i][0], sensor_locations[i][1]] = 0
    grid[beacon_locations[i][0], beacon_locations[i][1]] = 0

print(grid)
print("Total number of impossible beacon locations:", sum(sum(grid)))
print(sum(grid[110]))
for i in range(100,120):
    print(grid[i][100:120])
print(grid[108,110])
print()
for i in range(109,112):
    print(grid[i][96:127])

print(distances)
a = np.array([102,118])
b = np.array([40,80])
print(a not in sensor_locations)
print(b not in sensor_locations)