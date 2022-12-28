#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
time_it has a decorator to help annotate functions and get their execution time
"""

import time

def time_it(func):
    """time_it has a decorator to help annotate functions and get their execution time"""
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        total_time = end_time - start_time
        print(f'Execution Time => {func.__name__} : {total_time}')
    return wrapper
