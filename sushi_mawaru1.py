#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import random
import time
import os

SUSHI_COUNT = 50
SUSHI_ONLY = True
MAX_WIDTH = 40
MAX_HEIGHT = 12

pos = [(x, y) for x in range(0, MAX_WIDTH + 1, 2)
              for y in range(0, MAX_HEIGHT + 1, 2)
              if x in [0, MAX_WIDTH] or y in [0, MAX_HEIGHT]]
select_pos = []

SPACE_VALUE=-1

if SUSHI_ONLY:
    neta = ['\U0001F363'] # sushi
else:
    neta = ['\U0001F354', '\U0001F355', '\U0001F356', '\U0001F357', '\U0001F358', '\U0001F359', '\U0001F35A', '\U0001F35B', '\U0001F35C', '\U0001F35D', '\U0001F35E', '\U0001F35F', '\U0001F360', '\U0001F361', '\U0001F362', '\U0001F363', '\U0001F364', '\U0001F365', '\U0001F366', '\U0001F367', '\U0001F368', '\U0001F369', '\U0001F36A', '\U0001F36B', '\U0001F36C', '\U0001F36D', '\U0001F36E', '\U0001F36F',]

def main():
    f = [[SPACE_VALUE for y in range(MAX_HEIGHT + 1)]
                      for x in range(MAX_WIDTH + 1)]
    back = [[SPACE_VALUE for y in range(MAX_HEIGHT + 1)]
                         for x in range(MAX_WIDTH + 1)]
    for _ in range(SUSHI_COUNT):
        plist = list(set(pos) - set(select_pos))
        x, y = random.choice(plist)
        n = random.choice(neta)
        f[x][y] = neta.index(n)

    while True:
        # draw
        for y in range(MAX_HEIGHT + 1):
            for x in range(MAX_WIDTH + 1):
                c = ' '
                if f[x][y] != SPACE_VALUE:
                    c = neta[f[x][y]]
                print(c, end='')
            print()
        time.sleep(0.1)
        os.system('clear')

        # move
        for y in range(MAX_HEIGHT + 1):
            for x in range(MAX_WIDTH + 1):
                if f[x][y] != SPACE_VALUE:
                    if y == 0 and x != MAX_WIDTH:
                        vx, vy = (1, 0)
                    elif x == MAX_WIDTH and y != MAX_HEIGHT:
                        vx, vy = (0, 1)
                    elif y == MAX_HEIGHT and x != 0:
                        vx, vy = (-1, 0)
                    elif x == 0 and y != 0:
                        vx, vy = (0, -1)
                    mx, my = x + vx, y + vy
                    back[x][y], back[mx][my] = SPACE_VALUE, f[x][y]
        f = back
        back = [[SPACE_VALUE for y in range(MAX_HEIGHT + 1)]
                             for x in range(MAX_WIDTH + 1)]

if __name__ == '__main__':
    main()

