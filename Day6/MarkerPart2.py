with open('/home/peter/Code/AdventOfCode2022/Day6/input', 'r') as reader:
    lines = reader.readlines()
    text_input = lines[0]
    print(len(text_input))

    target_index = 0
    for i in range(len(text_input)-4):
        next_message = text_input[i:i+14]
        duplicate = False
        for j in range(14):
            for k in range(j+1,14):
                if next_message[j] == next_message[k]:
                    duplicate = True
        if duplicate == False:
            target_index = i+14
            break
    print(target_index)
    print("Position of message:", target_index)