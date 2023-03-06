import numpy as np

with open('/home/peter/Code/AdventOfCode2022/Day14/input', 'r') as reader:
    lines = reader.readlines()

slice = np.zeros((1000,1000), dtype=int)

def process_input(lines):
    highest_y_coord = 0
    for line in lines:
        points_with_whitespace = line.split(" -> ")
        endpoints = [point_with_whitespace.strip() for point_with_whitespace in points_with_whitespace]
        print(line.strip())

        for i in range(len(endpoints)-1):
            start_point_str = endpoints[i].split(",")
            end_point_str = endpoints[i+1].split(",")
            start_point = np.array([int(start_point_str[0]),int(start_point_str[1])])
            if start_point[1] > highest_y_coord:
                highest_y_coord = start_point[1]
            end_point = np.array([int(end_point_str[0]),int(end_point_str[1])])
            if end_point[1] > highest_y_coord:
                highest_y_coord = end_point[1]

            num_steps = int(np.linalg.norm(end_point-start_point)+0.1)
            step = (end_point - start_point) / num_steps
            step = np.array([int(step[0]), int(step[1])])

            for j in range(num_steps + 1):
                next_step = start_point + j*step
                slice[next_step[0]][next_step[1]] = 1

    start_point = np.array([0,highest_y_coord+2])
    end_point = np.array([999, highest_y_coord+2])

    num_steps = int(np.linalg.norm(end_point-start_point)+0.1)
    step = (end_point - start_point) / num_steps
    step = np.array([int(step[0]), int(step[1])])

    for j in range(num_steps + 1):
        next_step = start_point + j*step
        slice[next_step[0]][next_step[1]] = 1

    print("Highest y coordinate", highest_y_coord)
    


def process_sand_movement():
    finished = 0
    start_point = np.array([500,0])
    sand_at_rest = 0
    print("Start Point:", start_point)
    while(finished == 0):
        current_sand_point = start_point
        sand_still_moving = 1
        while(sand_still_moving == 1):
            if slice[current_sand_point[0], current_sand_point[1]+1] == 0:
                current_sand_point = np.array([current_sand_point[0], current_sand_point[1]+1])
            elif slice[current_sand_point[0]-1, current_sand_point[1]+1] == 0:
                current_sand_point = np.array([current_sand_point[0]-1, current_sand_point[1]+1])
            elif slice[current_sand_point[0]+1, current_sand_point[1]+1] == 0:
                current_sand_point = np.array([current_sand_point[0]+1, current_sand_point[1]+1])
            else:
                sand_still_moving = 0
                sand_at_rest += 1
                slice[current_sand_point[0], current_sand_point[1]] = 1
                if current_sand_point[0] == 500 and current_sand_point[1] == 0:
                    finished = 1
                #print("New filled in spot:", current_sand_point[0], current_sand_point[1])
    print("Number of sand particles at rest:", sand_at_rest)


process_input(lines)
process_sand_movement()