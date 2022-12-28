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

    score = 0

    with open('./solutions/2022/data/day_02.data', encoding="utf-8") as file:
        for line in file:
            moves = line.rstrip().split(' ')
            player_move = moves[1]

            match player_move:
                case 'X':
                    score += 1
                case 'Y':
                    score += 2
                case 'Z':
                    score += 3

            match moves:
                case ['A', 'Z'] | ['B', 'A'] | ['C', 'B']:
                    score += 0
                case ['A', 'X'] | ['B', 'Y'] | ['C', 'Z']:
                    score += 3
                case ['A', 'Y'] | ['B', 'Z'] | ['C', 'X']:
                    score += 6

    print(score)


@time_it
def problem_2() -> None:
    """Solution to Problem 2"""

    with open('./solutions/2022/data/day_02.data', encoding="utf-8") as file:
        for line in file:
            print(line)


def main() -> None:
    """Print solutions"""

    problem_1()
    # problem_2()

if __name__ == '__main__':
    main()
