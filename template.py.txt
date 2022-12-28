#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Day 1, 2022
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from time_it import time_it # pylint: disable=wrong-import-position

@time_it
def problem_1() -> None:
    """Solution to Problem 1"""

    print("Solution 1")

@time_it
def problem_2() -> None:
    """Solution to Problem 2"""

    print("Solution 2")


def main() -> None:
    """Print solutions"""
    problem_1()
    problem_2()

if __name__ == '__main__':
    main()
