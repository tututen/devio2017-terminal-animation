#/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function

import time
import sys


def main():
    size = 30
    str_format = "[{{:{size}}}] {{:>6.2f}}%".format(size=size)
    for i in range(1, size + 1):
        print(str_format
                .format("#" * i, i * 100.0 / size) + '\r', end='')
        sys.stdout.flush()
        time.sleep(0.25)
    print()

if __name__ == '__main__':
    main()


