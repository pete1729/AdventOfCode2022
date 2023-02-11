with open('/home/peter/Code/AdventOfCode2022/Day3/input', 'r') as reader:
    lines = reader.readlines()

    total_priority = 0

    for line in lines:
        print(line.strip())
        print(len(line))
        length_half = int((len(line)-1)/2)
        first_half = line[0:length_half]
        second_half = line[length_half:]
        print(first_half.strip())
        print(second_half.strip())
        priority = 0

        for letter in first_half:
            if letter in second_half:
                print(letter)
                

                unicodePos = ord(letter)
                if unicodePos > 96:
                    priority = unicodePos - 96
                else:
                    priority = unicodePos - 38
                print("Priority:", priority)
            
        total_priority += priority
        print()
    print("Total Priority:", total_priority)