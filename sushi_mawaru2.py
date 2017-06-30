#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function

import curses
import random
import time
import sys

SUSHI_COUNT = 50
SUSHI_ONLY = True
MAX_WIDTH = 40
MAX_HEIGHT = 12

class Obj(object):
    if SUSHI_ONLY:
        neta = ['\U0001F363'] # sushi
    else:
        neta = ['\U0001F354',
                '\U0001F355',
                '\U0001F356',
                '\U0001F357',
                '\U0001F358',
                '\U0001F359',
                '\U0001F35A',
                '\U0001F35B',
                '\U0001F35C',
                '\U0001F35D',
                '\U0001F35E',
                '\U0001F35F',
                '\U0001F360',
                '\U0001F361',
                '\U0001F362',
                '\U0001F363',
                '\U0001F364',
                '\U0001F365',
                '\U0001F366',
                '\U0001F367',
                '\U0001F368',
                '\U0001F369',
                '\U0001F36A',
                '\U0001F36B',
                '\U0001F36C',
                '\U0001F36D',
                '\U0001F36E',
                '\U0001F36F',]
    pos = [(x, y) for x in range(0, MAX_WIDTH + 1, 2)
                  for y in range(0, MAX_HEIGHT + 1, 2)
                  if x in [0, MAX_WIDTH] or y in [0, MAX_HEIGHT]]

    select_pos = []

    @classmethod
    def get_pos(cls):
        plist = list(set(cls.pos) - set(cls.select_pos))
        p = random.choice(plist)
        cls.select_pos.append(p)
        return p

    @classmethod
    def delete_pos(cls, p):
        idx = cls.select_pos.find(p)
        if idx != -1:
            del cls.select_pos[idx]

    def __init__(self, term_area):
        self.term_area = term_area
        self.x, self.y = Obj.get_pos()
        self.text = random.choice(Obj.neta)
        self.vx = random.randint(1, 5)
        self.vy = random.randint(1, 5)
        self.check_point()

    def check_point(self):
        if self.y == 0 and self.x != MAX_WIDTH:
            self.vx, self.vy = (1, 0)
        elif self.x == MAX_WIDTH and self.y != MAX_HEIGHT:
            self.vx, self.vy = (0, 1)
        elif self.y == MAX_HEIGHT and self.x != 0:
            self.vx, self.vy = (-1, 0)
        elif self.x == 0 and self.y != 0:
            self.vx, self.vy = (0, -1)


    def get_addstr_args(self):
        return (self.y, self.x, self.text.encode('utf-8'))


    def move(self):
        self.x += self.vx
        self.y += self.vy
        self.check_point()


    def __repr__(self):
        return 'Obj[area={},x={},y={},vx={},vy={},text={}]'.format(
                self.term_area,
                self.x,
                self.y,
                self.vx,
                self.vy,
                self.text.encode('utf-8'))


if __name__ == '__main__':
    term = curses.initscr()

    # 入力エコーバックをオフ
    curses.noecho()
    # カーソル削除
    curses.curs_set(False)

    # term.getch()のメソッドを非ブロックで動作
    term.nodelay(1)

    # 起動時のterminalの大きさ取得
    term_h, term_w = term.getmaxyx()
    term_area = (term_w, term_h)

    sushis = [Obj(term_area) for _ in range(SUSHI_COUNT)]

    q = -1
    while q != ord('q'):
        term.clear()

        # draw
        for sushi in sushis:
            term.addstr(*sushi.get_addstr_args())


        q = term.getch()
        time.sleep(0.1)

        # move
        for sushi in sushis:
            sushi.move()

    curses.endwin()

