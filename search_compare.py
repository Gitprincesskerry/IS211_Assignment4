#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 4 Assignment, Part 1

import time
import random

def sequential_search(a_list, item):
    start = time.time()

    pos = 0
    found = False
    while pos < len(a_list) and not found:
        if a_list[pos] == item:
            found = True
        else:
            pos = pos+1
    end = time.time()
    return found, end-start

# test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# print(sequential_search(test_list, 3))
# print(sequential_search(test_list, 13))


def ordered_sequential_search(a_list, item):
    start1 = time.time()

    pos = 0
    found = False
    stop = False
    while pos < len(a_list) and not found and not stop:
        if a_list[pos] == item:
            found = True
        else:
            if a_list[pos] > item:
                stop = True
            else:
                pos = pos+1
    end1 = time.time()
    return found, end1-start1

# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(ordered_sequential_search(test_list, 3))
# print(ordered_sequential_search(test_list, 13))


def binary_search_iterative(a_list, item):
    start2 = time.time()

    first = 0
    last = len(a_list) - 1
    found = False
    while first <= last and not found:
       midpoint = (first + last) // 2
       if a_list[midpoint] == item:
         found = True
       else:
           if item < a_list[midpoint]:
               last = midpoint - 1
           else:
               first = midpoint + 1
    end2 = time.time()
    return found, end2-start2

# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binary_search_iterative(test_list, 3))
# print(binary_search_iterative(test_list, 13))

def binary_search_recursive(a_list, item):
    
    if len(a_list) == 0:
        return False
    else:
        midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
        return True
    else:
        if item < a_list[midpoint]:
            return binary_search_recursive(a_list[:midpoint], item)
        else:
            return binary_search_recursive(a_list[midpoint + 1:], item)

def test_wrapper(a_list, item):
    """Calls the function binary_search_recursive and computes the time of the aforemetioned function."""
    start3 = time.time()
    result = binary_search_recursive(a_list, item)
    end3 = time.time()
    return result, end3-start3

# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(test_wrapper(test_list, 3))
# print(test_wrapper(test_list, 13))

def main():
    """This function prints how long it takes for the sequential_search,
    ordered_sequential_search, binary_search_iterative,
    and binary_search_recursive functions to run on average"""
    for k in [500, 1000, 10000]:
        print('For List Sizes: %d' %k)
        Kerry_Sequential_Search = 0
        Kerry_Ordered_Sequential_Search = 0
        Kerry_Binary_Search_Iterative = 0
        Kerry_Binary_Search_Recursive = 0

        for x in range(0,100):
            kerrys_random_list = random.sample(range(1, 100000), k)
            tempresult, temptime = sequential_search(kerrys_random_list, -1)
            Kerry_Sequential_Search += temptime

            kerrys_random_list.sort()
            tempresult, temptime = ordered_sequential_search(kerrys_random_list, -1)
            Kerry_Ordered_Sequential_Search += temptime

            tempresult, temptime = binary_search_iterative(kerrys_random_list, -1)
            Kerry_Binary_Search_Iterative += temptime

            tempresult, temptime = test_wrapper(kerrys_random_list, -1)
            Kerry_Binary_Search_Recursive += temptime

        print("Sequential Search took %10.7f seconds to run, on average" %(Kerry_Sequential_Search/100))
        print("Ordered Sequential Search took %10.7f seconds to run, on average" %(Kerry_Ordered_Sequential_Search/100))
        print("Binary Search Iterative took %10.7f seconds to run, on average" %(Kerry_Binary_Search_Iterative/100))
        print("Binary Search Recursive took %10.7f seconds to run, on average" %(Kerry_Binary_Search_Recursive/100))

if __name__ == "__main__":
    main()
