# https://adventofcode.com/2021/day/1

from typing import List # Tuple
# import pandas as pd
import re
inputFile = 'input/day01_part1_input' # dummy_input'


# def compare(depth_value: List[int], previous_depth_value: int = None) -> Tuple[str, int]:
#     '''Compare function for comparing each input depth value with the previous value
#     Parameters:
#     depth_value (int): the input
#     previous_depth_value (int): the input
#     Returns:
#     (change_value, acc_increase): Tuple[int, str]: A tuple of the depth and the increase or decrease of the depth input value compared to the previous value
#     '''
#
#     inc = 0
#     dec = 0
#     equal = 0
#     diff_value = (depth_value - previous_depth_value)
#     if diff_value > 0:
#         change_value = '(increased)'
#         inc += 1
#     elif diff_value < 0:
#         change_value = '(decreased)'
#         dec += 1
#     elif diff_value == 0:
#         change_value = '(N/A - no previous measurement)'
#         equal += 1
#     return change_value

def diff_depth(depth_values: List[int]) -> List[int]:
    """

    """
    depth = file2intList(depth_values)
    print(f"depth : {depth}")
    changed_values = [depth[line] - depth[line - 1] for line in depth if line >= 1]
    return changed_values

def summy(lst):
    '''Returns the sum of all int in a list
    Parameters:
    l [int]: the input list
    Returns:
    int: sum of all inputs
    '''
    return sum(lst)


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
        # acc_increase = [list[line], list[line] - [line - 1] for line, item in line.strip().split(' ')]
        inc_count = 0
        dec_count = 0
        eq_count = 0
        for idx, line in enumerate(input_file):
            for item in line.strip().split(' '):
                print(f"item: {item}")
                if idx == 0:
                    inc_dec = '(N/A - no prevoius meassurement)'
                    print(f"idx0: {idx}")
                    # list_depth.append(int(item))
                    list_w_depth_change.append(str(item) + ' ' + str(inc_dec))
                    previous_item = item
                    print(f"list0: {list_depth}")
                    print(f"list_w_depth_change: {list_w_depth_change}")
                elif idx > 0:
                    print(f"idx1: {idx}")
                    print(f"item: {item}, previousitem: {previous_item}")
                    change_value = int(item) - int(previous_item)
                    print(f"change_value: {change_value}")
                    print(f"item1: {item}, idx: {idx}, previous_item: {previous_item}")
                    print(f"list_w_depth_change>0: {list_depth}")
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

# def sonar_sweep(depth_value: List[int], change: str) -> List[Tuple[int, str]]:
#     # acc_increase = file2intList(inputFile)
#     pass

def day01PartOne():
    input_data = inputFile
    list1, inc_count = file2intList(input_data)
    print(f"list1: {list1}")

    output = inc_count

    print(
        f'Solution Day 01, Part one:\nAnswer: {output} \n\n')


def day01PartTwo():
    input_data = file2intList(inputFile)
    output = summy(input)

    print(
        f'Solution Day 01, Part two:\nAnswer: {output} \n\n')


if __name__ == "__main__":
    day01PartOne()
    # day01PartTwo()

# Run from terminal:
# $ python day_01.py