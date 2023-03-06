import numpy as np

with open('/home/peter/Code/AdventOfCode2022/Day14/smallinput', 'r') as reader:
    lines = reader.readlines()

slice = np.zeros((1000,1000), dtype=int)

def process_input(lines):
    for line in lines:
        points_with_whitespace = line.split(" -> ")
        endpoints = [point_with_whitespace.strip() for point_with_whitespace in points_with_whitespace]
        print(line.strip())
        #print(endpoints)
        #print()

        for i in range(len(endpoints)-1):
            start_point_str = endpoints[i].split(",")
            end_point_str = endpoints[i+1].split(",")
            start_point = np.array([int(start_point_str[0]),int(start_point_str[1])])
            end_point = np.array([int(end_point_str[0]),int(end_point_str[1])])
            #print("Start point:", start_point)
            #print("End point:", end_point)

            #traverse = end_point - start_point
            #step = traverse / (abs(traverse[0]) + abs(traverse[1]))

            num_steps = int(np.linalg.norm(end_point-start_point)+0.1)
            step = (end_point - start_point) / num_steps
            step = np.array([int(step[0]), int(step[1])])
            #print("Step:", step)
            #print(start_point + step)

            for j in range(num_steps + 1):
                next_step = start_point + j*step
                print(next_step)


def process_sand_movement():
    pass

process_input(lines)