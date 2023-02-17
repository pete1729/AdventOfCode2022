import numpy as np

#with open('/home/peter/Code/AdventOfCode2022/Day8/small_input', 'r') as reader:
with open('/home/peter/Code/AdventOfCode2022/Day8/input', 'r') as reader:
    lines = reader.readlines()
    print(lines[0][:-1])

    print(len(lines[0][:-1]))
    print(len(lines))

    tree_array = np.zeros([len(lines[0][:-1]), len(lines)])

    for i in range(len(lines)):
        for j in range(len(lines[i][:-1])):
            tree_array[i,j] = lines[i][j]

print(tree_array)

max_scenic_score = 0
max_scenic_location = [0,0]

print(tree_array.shape)
for i in range(1,tree_array.shape[0]-1):
    for j in range(1,tree_array.shape[1]-1):
        left_distance = 1
        right_distance = 1
        up_distance = 1
        down_distance = 1

        left_finished = 0
        for k in range(j-1,0,-1):
            if tree_array[i,k] < tree_array[i,j] and left_finished == 0:
                left_distance += 1
            else:
                left_finished = 1

        right_finished = 0
        for k in range(j+1,tree_array.shape[1]-1):
            if tree_array[i,k] < tree_array[i,j] and right_finished == 0:
                right_distance += 1
            else:
                right_finished = 1

        up_finished = 0
        for k in range(i-1,0,-1):
            if tree_array[k,j] < tree_array[i,j] and up_finished == 0:
                up_distance += 1
            else:
                up_finished = 1

        down_finished = 0
        for k in range(i+1,tree_array.shape[1]-1):
            if tree_array[k,j] < tree_array[i,j] and down_finished == 0:
                down_distance += 1
            else:
                down_finished = 1

        print("Location:", i, j)
        scenic_score = left_distance*right_distance*up_distance*down_distance
        print("Scenice score:", scenic_score)

        if scenic_score > max_scenic_score:
            max_scenic_score = scenic_score
            max_scenic_location = [i,j]

print("Max scenic location:", max_scenic_location)
print("Max scenic score:", max_scenic_score)