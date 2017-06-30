#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from PIL import Image
from PIL import ImageOps
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

import time

import curses

char_map = ' ' * 70 + ''.join([c * 20 for c in '._:|+*#&$@'])

def pixels2ascii(pmatrix, sx, sy):
    return [''.join([char_map[pmatrix.getpixel((x, y))]
            for x in range(sx * 2)])
            for y in range(sy)]

def edit_iamge(image_handle, term_area):
    term_w, term_h = term_area

    # 長さの短い方
    image_size = min((term_w-1) / 2, term_h)

    # 画像resize
    image = image_handle.resize((image_size * 2, image_size),
                                Image.ANTIALIAS)

    # グレースケール化
    gray = ImageOps.grayscale(image)

    return pixels2ascii(gray, image_size, image_size)

if __name__ == '__main__':
    term = curses.initscr()

    # 入力エコーバックをオフ
    curses.noecho()
    # カーソル削除
    curses.curs_set(False)

    # 起動時のterminalの大きさ取得
    term_h, term_w = term.getmaxyx()
    term_area = (term_w, term_h)

    image = edit_iamge(Image.open('./img/mesoko_01.png'), term_area)

    term.clear()
    for y, line in enumerate(image):
        term.addstr(y, 0, line.encode('utf-8'))
    term.refresh()
    q = term.getch()

    curses.endwin()
