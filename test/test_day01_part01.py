#!/usr/bin/env python3

import pytest

import day01
import template_day

@pytest.mark.parametrize("test_input, expected_result",
                          [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)])
def test_file2intList(test_input, expected_result):
    assert day01.file2intList(test_input) == expected_result

@pytest.mark.parametrize("test_input, expected_result",
                          [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)])
def test_file2intList_day_one_part_one(test_input, expected_result):
    assert day01.file2intList(test_input) == expected_result


def test_dummy_02():
    assert template_day.summy([1, 2, 3]) == 6


# @pytest.mark.parametrize("test_input, expected_result",
#                          [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 7)])

@pytest.mark.parametrize("test_input, expected_result",
                         [([199, 200, 208, 210, 200, 207, 240, 269, 260, 263], 5)]) # [607, 618, 618, 617, 647, 716, 769, 792], 5)])
def test_sliding_window_comparison(test_input, expected_result):
    assert day01.sliding_window_comparison(test_input) == expected_result

# Run tests from terminal:
# $ pytest test/test_day01_part01.py

