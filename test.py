'''
Filename: /home/ling/文档/ultimate-cli/test.py
Path: /home/ling/文档/ultimate-cli
Created Date: Friday, January 31st 2020, 1:44:05 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import curses
from components.base import ComponentBase
from components.text import TextComponent


if __name__ == "__main__":
    # Create screen ===>
    scr = curses.initscr()
    # Create Base Component ===>
    base = ComponentBase(scr)
    # Create Text Component ===>
    text = TextComponent(scr)
    # curses end ===>
    curses.endwin()
    print("### Base Component ###")
    print(base)
    print("### Text Component ###")
    print(f"TextComponent().is_type('text'): {TextComponent.is_type('text')}")
    print(f"name: {text}")
    print(f"type: {text.get_type()}")
