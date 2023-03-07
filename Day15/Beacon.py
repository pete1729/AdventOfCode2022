import re
import numpy as np

sensor_locations = []
beacon_locations = []

grid_universe = np.zeros([100,100])

with open('/home/peter/Code/AdventOfCode2022/Day15/smallinput', 'r') as reader:
    lines = reader.readlines()

    for line in lines:
        if line:
            split_line = line.split("=")
            split_line = split_line[1:]
            coordinates = [int(re.sub("[^0-9-]", "", token)) for token in split_line]

            sensor_locations.append([coordinates[0], coordinates[1]])
            beacon_locations.append([coordinates[2], coordinates[3]])
        

print(sensor_locations)
print(beacon_locations)
distances = [0]*len(sensor_locations)
np_sens_loc = np.zeros((len(sensor_locations),2), dtype=int)
np_beac_loc = np.zeros((len(sensor_locations),2), dtype=int)

for i in range(len(sensor_locations)):
    np_sens_loc[i][0] = sensor_locations[i][0]
    np_sens_loc[i][1] = sensor_locations[i][1]
    np_beac_loc[i][0] = beacon_locations[i][0]
    np_beac_loc[i][1] = beacon_locations[i][1]

    #distances[i] = np.sum(np.abs([sensor_locations[i][0] - beacon_locations[i][0], sensor_locations[i][1] - beacon_locations[i][1]]))
    distances[i] = np.sum(np.abs([sensor_locations[i][0] - beacon_locations[i][0], sensor_locations[i][1] - beacon_locations[i][1]]))

    for x in range(sensor_locations[i][0]-distances[i], sensor_locations[i][0]+distances[i]):
        for y in range(sensor_locations[i][1]-distances[i], sensor_locations[i][1]+distances[i]):
            pass

print(distances)