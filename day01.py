# https://adventofcode.com/2021/day/1

from typing import List # Tuple
import pandas as pd
import re
import numpy as np
inputFile = 'input/day01_part1_input' # dummy_input'

# def compare_depth(List: list_w_depth_change):
#     """Compare depth
#     Parameters:
#         list_w_depth_change
#     Returns:
#         No. of inreased depth
#     """
#     inc_count = 0
#     dec_count = 0
#     eq_count = 0
#     for idx in enumerate(list_w_depth_change):
#         if idx == 0:
#             inc_dec = '(N/A - no prevoius meassurement)'
#             change_value = list_w_depth_change[idx + 1]
#         #                    print(f"list_w_depth_change: {list_w_depth_change}")
#         elif idx > 0:
#             change_value = list_w_depth_change[idx + 1] - list_w_depth_change[idx]
#             if change_value > 0:
#                 inc_dec = '(increased)'
#                 inc_count += 1
#             elif change_value < 0:
#                 inc_dec = '(decreased)'
#                 dec_count += 1
#             elif change_value == 0:
#                 inc_dec = '(no change)'
#                 eq_count += 1
#             else:
#                 inc_dec = '(N/A - no prevoius meassurement)'
#             list_w_depth_change[idx + 1] - list_w_depth_change[idx]
#             # previous_item = item
#         else:
#             print(f"Unexpected result!")
#
#
#     return list_w_depth_change, inc_count

def file2intList_day_one_part_one(file):
    '''Reads file return list with the items in file as int
    Parameters:
    file: the input file
    Returns:
    list: output as list
    '''
    list_w_depth_change = []
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

def sliding_window_comparison(depth):
    """Compares a sliding window of three depth measurement with the next three depth measurements.
    Parameter:
    depth

    """
    depth_window = [sum(depth[n + 1:n + 4]) > sum(depth[n:n + 3]) for n, dp in enumerate(depth)]
    return sum(depth_window)

def file2intList(file):
    """Reads file return list with the items in file as int
    Parameters:
    file: the input file
    Returns:
    list: output as list
    """
    list_w_depth_change = []
    with open(file) as input_file:
        for idx, line in enumerate(input_file):
            for item in line.strip().split(' '):
                list_w_depth_change.append(int(item))

    return list_w_depth_change


def day01PartOne():
    input_data = inputFile
    # list1 = file2intList(input_data)
    _, inc_count = file2intList_day_one_part_one(input_data)
    output = inc_count

    print(f'Solution Day 01, Part one:\nAnswer: {output} \n\n')


def day01PartTwo():
    input_data = file2intList(inputFile)
    window_inc_count = sliding_window_comparison(input_data)
    # print(f"{type(sum(int(input_data[0 + 2]), int(input_data[0 + 1]), int(input_data[0])))}")
    # print(f"zip(input[])")
    output = window_inc_count # [sum(sum(int(input_data[idx + 2]), int(input_data[idx + 1]), int(input_data[idx])) > sum(int(input_data[idx + 3]), int(input_data[idx + 2]), int(input_data[idx + 1]) for idx in enumerate(input_data))]

    print(f'Solution Day 01, Part two:\nAnswer: {output} \n\n')


if __name__ == "__main__":
    # day01PartOne()
    day01PartTwo()

# Run from terminal:
# $ python day_01.py