from io import StringIO
import sys
import traceback

def get_item(input):
    pass

# left_input and right_input both arrays
def compare_input(left_input, right_input, correct_order):
    print("Left input:", left_input)
    print("Right input:", right_input)

    for j in range(len(left_input)):
        try:
            left_array = 0
            right_array = 0
            # testing whether left expression is array
            a = left_input[j] + 1
        except TypeError as e:
            left_array = 1
            print("Left input position", j, "is array")
        try:
            # testing whether left expression is array
            b = right_input[j] + 1
        except TypeError as e:
            right_array = 1
            print("Right input position", j, "is array")
        except IndexError as e:
            correct_order = 0
            return correct_order

        if left_array == 0 and right_array == 0:
            if left_input[j] > right_input[j]:
                correct_order = 0
                return correct_order
            elif left_input[j] < right_input[j]:
                correct_order = 1
                return correct_order

        if left_array == 0 and right_array == 1:
            correct_order = compare_input([left_input[j]], right_input[j], correct_order)
            if correct_order == 0:
                return correct_order
        
        if left_array == 1 and right_array == 0:
            correct_order = compare_input(left_input[j], [right_input[j]], correct_order)
            if correct_order == 0:
                return correct_order

        if left_array == 1 and right_array == 1:
            correct_order = compare_input(left_input[j], right_input[j], correct_order)
            if correct_order == 0:
                return correct_order

    return correct_order


with open('/home/peter/Code/AdventOfCode2022/Day13/input', 'r') as reader:
    lines = reader.readlines()

sum_pairs_correct_order = 0

for i in range(int(len(lines)/3)+1):
#for i in range(1):
    left_exp = eval(lines[3*i])
    right_exp = eval(lines[3*i+1])

    print(left_exp)
    print(right_exp)

    correct_order = 1
    correct_order = compare_input(left_exp, right_exp, correct_order)
    if correct_order == 1:
        sum_pairs_correct_order += (i+1)
    print("Test ", i+1, "- Correct order:", correct_order)
    print()

print("Sum of positions of pairs in correct order:", sum_pairs_correct_order)

# 594 too low