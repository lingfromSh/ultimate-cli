'''
Filename: /home/ling/文档/ultimate-cli/cli.py
Path: /home/ling/文档/ultimate-cli
Created Date: Friday, January 31st 2020, 10:54:21 am
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import collections
import curses
import traceback
import typing
from copy import deepcopy

from components import TextComponent

# color-constant
COLOR_TRANSPARENT = -1
COLOR_BLACK = 0
COLOR_RED = 1
COLOR_GREEN = 2
COLOR_YELLOW = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7
# text style-constant
TEXT_NORMAL = curses.A_NORMAL
TEXT_BOLD = curses.A_BOLD
TEXT_BLINK = curses.A_BLINK
TEXT_UNDERLINE = curses.A_UNDERLINE


def catch_exception(func):
    """Ensure Got Correct Format Traceback."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            curses.endwin()
            print(traceback.format_exc())
    return inner


class CLI:
    # info
    _name = "ultimate-cli"
    _version = "0.1"
    # common
    _VALID_COMPONENT_TYPE = {
        "text": TextComponent,
        # "choice": ChoiceComponent,
        # "checkbox": CheckBoxComponent,
        # "range": RangeComponent
    }

    @catch_exception
    def __init__(self, color_setting: typing.Dict = {}, auto_clear: bool = False):
        """Init cli."""
        # init screen
        self.screen = curses.initscr()
        self.cursor_y, self.cursor_x = self.screen.getyx()
        # init screen color, color pair
        self.__colors = []
        self.__color_count = 0
        self.__color_pairs = []
        curses.start_color()
        curses.use_default_colors()
        self._init_colors()
        self.set_color(color_setting)
        # init screen elements
        self.__elements = {}
        # auto clear when exit
        self.auto_clear = auto_clear

    def __str__(self) -> typing.AnyStr:
        """Return Introduction"""
        return """
        === === === === === === === === === === === ===
        ===               Ultimate CLI              ===
        ===               Version: 0.1              ===
        === === === === === === === === === === === ===
        """

    def __del__(self) -> None:
        """Clear the screen."""
        if self.auto_clear:
            self.screen.clear()
            curses.endwin()

    def _init_colors(self):
        """Init colors"""
        # default colors only will be generated after screen has been inited.
        _DEFAULT_COLORS = (
            ("black", curses.color_content(curses.COLOR_BLACK)),        # 0
            ("red", curses.color_content(curses.COLOR_RED)),            # 1
            ("green", curses.color_content(curses.COLOR_GREEN)),        # 2
            ("yellow", curses.color_content(curses.COLOR_YELLOW)),      # 3
            ("blue", curses.color_content(curses.COLOR_BLUE)),          # 4
            ("magenta", curses.color_content(curses.COLOR_MAGENTA)),    # 5
            ("cyan", curses.color_content(curses.COLOR_CYAN)),          # 6
            ("white", curses.color_content(curses.COLOR_WHITE)),        # 7
        )
        self.__colors = list(_DEFAULT_COLORS)
        self.__color_count = 8
        # term max number of supported defined colors.
        self.__max_color_number = 255

    @catch_exception
    def add_color(self,
                  name: typing.AnyStr,
                  r: typing.SupportsInt,
                  g: typing.SupportsInt,
                  b: typing.SupportsInt) -> int:
        """Add a custom color and return color's number(positive). 
           Return -1 when the current term doesn't support color."""
        # Ensure current terminal has colors.
        if not (curses.has_colors or curses.can_change_color()):
            return -1
        curses.init_color(self.__color_count - 1, r, g, b)
        self.__color_count += 1     # color + 1
        # insert a lowered color name with its rgb
        self.__colors.append((name.lower(), (r, g, b)))
        return self.__color_count - 1

    @catch_exception
    def reset_color(self) -> bool:
        """Remove all custom colors."""
        self.__colors = []
        self.__color_count = 8
        return True

    @catch_exception
    def set_color(self, color_setting: typing.Dict) -> typing.Tuple:
        """Set custom color at one time."""
        # Ensure color_setting is a dict
        if not isinstance(color_setting, dict):
            raise TypeError("color_setting must be a dict.")

        if color_setting:
            _color_setting = collections.OrderedDict(color_setting)
            for color_name, rgb in _color_setting.items():
                self.add_color(color_name, rgb[0], rgb[1], rgb[2])

    def get_colors(self) -> typing.List:
        """Return color list."""
        return self.__colors

    def get_colors_count(self) -> typing.SupportsInt:
        """Return color's amount."""
        return self.__color_count

    @staticmethod
    def get_color_rgb(color_number: typing.SupportsInt) -> typing.Tuple:
        """Return self's color RGB tuple."""
        return curses.color_content(color_number)

    def __set_color_pair(self, color: typing.SupportsInt, background: typing.SupportsInt) -> typing.SupportsInt:
        """Set a new color pair."""
        if not (-1 <= color < self.__color_count) and not (-1 <= background < self.__color_count):
            raise ValueError("Invalid Color Number.")
        curses.init_pair(self.__color_count, color, background)
        self.__color_count += 1      # color + 1
        self.__color_pairs.append((color, background))
        return self.__color_count - 1

    @catch_exception
    def add(self, element: typing.Dict) -> None:
        """Add new element into cli."""
        # Ensure element is a dict.
        if not isinstance(element, dict):
            # Not valid type
            raise TypeError("element must be a dict.")
        # Create a proper component according to the element's KEY:'type'.
        _element = deepcopy(element)
        _type = _element.pop("type", None)
        # default: transparent
        _color = _element.pop("color", COLOR_TRANSPARENT)
        _background = _element.pop(
            "background", COLOR_TRANSPARENT)    # default: transparent
        _component_proto = CLI._VALID_COMPONENT_TYPE[_type]
        # Get current cursor y,x
        self.cursor_y, self.cursor_x = self.screen.getyx()
        _element.update({
            "screen": self.screen,
            "start_row": self.cursor_y,
            "start_col": 0,
            "color_pair": self.__set_color_pair(_color, _background)
        })
        component = _component_proto(**_element)
        # Add component into cli's element tree.
        self.__elements.update({f"{component.name}": component})
        self.run()

    def clear(self) -> None:
        """Clear the screen & remove all elements."""
        # Init screen & clear the screen.
        curses.endwin()
        self.screen = curses.initscr()
        self.screen.clear()
        self.screen.refresh()
        # Remove all elements.
        self.__elements = {}

    @catch_exception
    def run(self):
        """Run the cli."""
        self._render()

    def get_elements(self) -> typing.Dict:
        """Return elements"""
        return self.__elements

    def _render(self):
        """Use run instead of using _render directly"""
        for elem in self.__elements.values():
            elem.render()
        self.screen.refresh()

    def get_handler(self):
        """Return the handler for user input"""
        ...


if __name__ == "__main__":
    """Unit Test For CLI."""
    color_setting = {
        "LightPink": (255, 182, 193),
        "Crimson": (220, 20, 60)
    }
    cli = CLI(color_setting, False)
    slateblue = {
        "name": "SlateBlue",
        "r": 106,
        "g": 90,
        "b": 205,
    }
    slateblue = cli.add_color(**slateblue)
    text1 = {
        "type": "text",
        "text": "Hello,World!",
        "color": COLOR_MAGENTA,
        "background": COLOR_TRANSPARENT
    }
    text2 = {
        "type": "text",
        "text": "Hello,World!",
        "color": slateblue,
        "background": COLOR_TRANSPARENT
    }
    text3 = {
        "type": "text",
        "text": "Hello,World!",
        "color": COLOR_BLUE,
        "background": slateblue,
    }
    cli.add(text1)
    cli.add(text2)
    cli.add(text3)
    cli.run()
