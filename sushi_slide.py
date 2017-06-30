#!/usr/bin/env python
from __future__ import unicode_literals
from __future__ import print_function


import sys
import time

sushi_str = '\U0001F363'

def main():
    size = 30
    for i in range(0, size):
        print('\r{}{}'.format(' ' * i, sushi_str), end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print()


if __name__ == '__main__':
    main()
