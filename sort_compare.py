#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This is Kerry Rainford's Week 4 Assignment, Part 2

import time
import random

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
           a_list[position] = a_list[position - 1]
           position = position - 1
        a_list[position] = current_value

    end = time.time()
    return end-start

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)



def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2

    end = time.time()
    return end-start

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


# a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# shell_sort(a_list)
# print(a_list)

def python_sort(a_list):
    start = time.time()
    a_list.sort()
    end = time.time()
    return end-start

def main():
    for k in [500, 1000, 10000]:
        print('For List Sizes: %d' %k)
        Kerry_Insertion_Sort = 0
        Kerry_Shell_Sort = 0
        Kerry_Python_Sort = 0

        for x in range(0,100):
            kerrys_random_list = random.sample(range(1, 100000), k)
            temptime = insertion_sort(kerrys_random_list)
            Kerry_Insertion_Sort += temptime

            kerrys_random_list = random.sample(range(1, 100000), k)
            temptime = shell_sort(kerrys_random_list)
            Kerry_Shell_Sort += temptime

            kerrys_random_list = random.sample(range(1, 100000), k)
            temptime = python_sort(kerrys_random_list)
            Kerry_Python_Sort += temptime

        print("Insertion Sort took %10.7f seconds to run, on average" %(Kerry_Insertion_Sort/100))
        print("Shell Sort took %10.7f seconds to run, on average" %(Kerry_Shell_Sort/100))
        print("Python Sort took %10.7f seconds to run, on average" %(Kerry_Python_Sort/100))

if __name__ == "__main__":
    main()
