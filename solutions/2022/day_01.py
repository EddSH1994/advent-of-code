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
    highest_elf_calories = 0
    with open("./solutions/2022/data/day_01.data", encoding="utf-8") as file:
        elfs_calories = 0

        for line in file:
            if line.strip():
                elfs_calories += int(line)
            else:
                if elfs_calories > highest_elf_calories:
                    highest_elf_calories = elfs_calories
                elfs_calories = 0

        print(highest_elf_calories)

@time_it
def problem_2() -> None:
    """Solution to Problem 2"""
    three_highest_elfs_calories = [0, 0, 0]

    with open("./solutions/2022/data/day_01.data", encoding="utf-8") as file:
        elfs_calories = 0

        for line in file:
            if line.strip():
                elfs_calories += int(line)
            else:
                if elfs_calories > three_highest_elfs_calories[0]:
                    three_highest_elfs_calories[2] = three_highest_elfs_calories[1]
                    three_highest_elfs_calories[1] = three_highest_elfs_calories[0]
                    three_highest_elfs_calories[0] = elfs_calories
                elif elfs_calories > three_highest_elfs_calories[1]:
                    three_highest_elfs_calories[2] = three_highest_elfs_calories[1]
                    three_highest_elfs_calories[1] = elfs_calories
                elif elfs_calories > three_highest_elfs_calories[2]:
                    three_highest_elfs_calories[2] = elfs_calories

                elfs_calories = 0

    print(sum(three_highest_elfs_calories))


def main() -> None:
    """Print solutions"""

    problem_1()
    problem_2()

if __name__ == '__main__':
    main()
