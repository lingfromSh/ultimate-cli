'''
Filename: /home/ling/文档/ultimate-cli/Components/base.py
Path: /home/ling/文档/ultimate-cli/Components
Created Date: Wednesday, January 29th 2020, 2:25:41 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

"""
# Common Option List
e.g-1:
    My_CLI = [
        header,         # HeaderComponent
        subject,        # SubjectComponent
        {
            option1:[
                _text1,         # TextComponent
                _option1,       # OptionComponent
                _option2,       # OptionComponent
                _choice1,       # ChoiceComponent
                _checkbox1,     # CheckboxComponent
                _range1,        # RangeComponent
            ]    # OptionComponent
        },  # only accpet one pair of key:value
    ]

# Multiple Range List
e.g-2:
    My_CLI = [
        header,         # HeaderComponent
        subject,        # SubjectComponent
        range1,         # RangeComponent
        range2,         # RangeComponent
        range3,         # RangeComponent
        range4,         # RangeComponent
        submit,         # ButtonComponent
    ]

"""




import curses
import secrets
import typing as ty

from .common import KEY_ENTER, KEY_SPACE, KEY_UP, KEY_DOWN, KEY_LEFT, KEY_RIGHT


class ComponentBase:
    _name = "base__component"

    def __init__(self,
                 name: ty.AnyStr, 
                 handler: ty.Callable, 
                 start_row: ty.SupportsInt, 
                 start_col: ty.SupportsInt, 
                 father: ty.Union[object, None],
                 children: ty.Union[object, ty.List]):
        self.name = name if name else f"{ComponentBase._name}__{sercrets.token_hex(8)}"
        self.handler = handler
        self.start_row = start_row
        self.start_col = start_col
        self.father = father
        self.children = children

    def __str__(self):
        return self.name

    def _get_response(self, screen) -> ty.SupportsInt:
        # only accept left,right,up,down,enter,space actions
        k = screen.getch()  # get an int
        if k == curses.KEY_LEFT:
            return KEY_LEFT
        elif k == curses.KEY_RIGHT:
            return KEY_RIGHT
        elif k == curses.KEY_UP:
            return KEY_UP
        elif k == curses.KEY_DOWN:
            return KEY_DOWN
        elif k == curses.KEY_ENTER or k == 13 or k == 10:
            return KEY_ENTER
        elif k == 32:
            return KEY_SPACE
        else:
            return -65536
