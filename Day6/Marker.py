with open('/home/peter/Code/AdventOfCode2022/Day6/input', 'r') as reader:
    lines = reader.readlines()
    text_input = lines[0]
    print(len(text_input))

    target_index = 0
    for i in range(len(text_input)-4):
        next_four = text_input[i:i+4]
        print(next_four)
        if next_four[0] != next_four[1]:
            if next_four[0] != next_four[2]:
                if next_four[0] != next_four[3]:
                    if next_four[1] != next_four[2]:
                        if next_four[1] != next_four[3]:
                            if next_four[2] != next_four[3]:
                                target_index = i
                                break
    print(target_index)
    print("Position of four unique chars:", target_index+4)