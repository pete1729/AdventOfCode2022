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

trees_visible = 2*tree_array.shape[0]+2*tree_array.shape[1]-4
print(tree_array.shape)
for i in range(1,tree_array.shape[0]-1):
    for j in range(1,tree_array.shape[1]-1):
        tree_height = tree_array[i,j]
        left_visible = True
        right_visible = True
        top_visible = True
        bottom_visible = True
        
        for k in range(0,j):
            if tree_array[i,k] >= tree_array[i,j]:
                left_visible = False
        for k in range(j+1,tree_array.shape[1]):
            if tree_array[i,k] >= tree_array[i,j]:
                right_visible = False
        for k in range(0,i):
            if tree_array[k,j] >= tree_array[i,j]:
                top_visible = False        
        for k in range(i+1,tree_array.shape[0]):
            if tree_array[k,j] >= tree_array[i,j]:
                bottom_visible = False

        print("Position", i,j)
        print(tree_height)
        print(left_visible)
        print(right_visible)
        print(top_visible)
        print(bottom_visible)

        overall_visibility = left_visible or right_visible or top_visible or bottom_visible
        print("Visible:", overall_visibility)
        if overall_visibility == True:
            trees_visible += 1
        print()

print("Trees visible:", trees_visible)