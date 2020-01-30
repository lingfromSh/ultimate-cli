#!/usr/bin/env python
# coding=utf-8

import curses
import secrets
from Components import (
    TextComponent,
)

def test_text_component():
    scr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    text = {
        "name": f"text__component__{secrets.token_hex(8)}",
        "text": "hello,<world>!",
        "start_row": 0,
        "start_col": 0,
        "father": None,
        "children": [],
        "handler": None,
    }
    t = TextComponent(**text)
    t.render(scr)

if __name__ == "__main__":
    test_text_component()
