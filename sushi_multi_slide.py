#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function


import os
import sys
import time
import random

sushi_str = '\U0001F363'
crown_str = '\U0001F451'

def main():
    sushi_count = 10
    line_length = 50
    line_numbers = [0] * sushi_count
    goal_list = []
    while True:
        os.system('clear')
        for i in range(sushi_count):
            line_numbers[i] += random.randint(0, 3)
            if line_numbers[i] > line_length:
                line_numbers[i] = line_length
                if not i in goal_list:
                    goal_list.append(i)
            print('{}{}'
                    .format(' ' * line_numbers[i], sushi_str),
                    end = '')
            if len(goal_list) > 0 and goal_list[0] == i:
                print(' {}'.format(crown_str))
            else:
                print()
        time.sleep(0.2)
        if len(goal_list) == sushi_count:
            break
    print(goal_list[:3])

if __name__ == '__main__':
    main()
