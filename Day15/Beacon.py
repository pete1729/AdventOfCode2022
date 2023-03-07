import re
import numpy as np

grid_universe = np.zeros([100,100])
num_locations = 0

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

    sensor_locations[i][0] = coordinates[0]
    sensor_locations[i][1] = coordinates[1]
    beacon_locations[i][0] = coordinates[2]
    beacon_locations[i][1] = coordinates[3]

print(sensor_locations)
print(beacon_locations)
print(beacon_locations[0]-sensor_locations[0])
print(np.sum(np.abs(beacon_locations[0]-sensor_locations[0])))
distances = [0]*num_locations

for i in range(num_locations):
    distances[i] = np.sum(np.abs(sensor_locations[i]-beacon_locations[i]))

    for x in range(sensor_locations[i][0]-distances[i], sensor_locations[i][0]+distances[i]):
        for y in range(sensor_locations[i][1]-distances[i], sensor_locations[i][1]+distances[i]):
            pass

print(distances)