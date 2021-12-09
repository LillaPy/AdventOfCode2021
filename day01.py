# https://adventofcode.com/2021/day/1

from typing import List # Tuple
# import pandas as pd
import re
inputFile = 'input/day01_part1_input' # dummy_input'

def file2intList(file):
    '''Reads file return list with the items in file as int
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list_depth = []
    list_w_depth_change = list_depth
    with open(file) as input_file:
        inc_count = 0
        dec_count = 0
        eq_count = 0
        for idx, line in enumerate(input_file):
            for item in line.strip().split(' '):
                if idx == 0:
                    inc_dec = '(N/A - no prevoius meassurement)'
                    list_w_depth_change.append(str(item) + ' ' + str(inc_dec))
                    previous_item = item
#                    print(f"list0: {list_depth}")
#                    print(f"list_w_depth_change: {list_w_depth_change}")
                elif idx > 0:
                    change_value = int(item) - int(previous_item)
#                    print(f"change_value: {change_value}")
#                    print(f"item1: {item}, idx: {idx}, previous_item: {previous_item}")
                    if change_value > 0:
                        inc_dec = '(increased)'
                        inc_count += 1
                    elif change_value < 0:
                        inc_dec = '(decreased)'
                        dec_count += 1
                    elif change_value == 0:
                        inc_dec = '(no change)'
                        eq_count += 1
                    else:
                        inc_dec = '(N/A - no prevoius meassurement)'
                    list_w_depth_change.append(str(item) + ' ' + str(inc_dec))
                    previous_item = item
                else:
                    print(f"Unexpected result!")

    return list_w_depth_change, inc_count


def day01PartOne():
    input_data = inputFile
    list1, inc_count = file2intList(input_data)
#    print(f"list1: {list1}")

    output = inc_count

    print(
        f'Solution Day 01, Part one:\nAnswer: {output} \n\n')


def day01PartTwo():
    input_data = file2intList(inputFile)
    output = sum(input)

    print(
        f'Solution Day 01, Part two:\nAnswer: {output} \n\n')


if __name__ == "__main__":
    day01PartOne()
    # day01PartTwo()

# Run from terminal:
# $ python day_01.py