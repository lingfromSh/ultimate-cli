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
    _DEFAULT_COLORS = (
        curses.COLOR_BLACK,     # 0
        curses.COLOR_RED,       # 1
        curses.COLOR_GREEN,     # 2
        curses.COLOR_YELLOW,    # 3
        curses.COLOR_BLUE,      # 4
        curses.COLOR_MAGENTA,   # 5
        curses.COLOR_CYAN,      # 6
        curses.COLOR_WHITE,     # 7
    )

    @catch_exception
    def __init__(self, color_setting: typing.Dict = {}):
        """Init cli."""
        # init screen
        self.screen = curses.initscr()
        self.cursor_y, self.cursor_x = self.screen.getyx()
        # init screen color
        self.colors = []        # store custom colors
        self.color_idx = 8      # because default color idx is from 0 to 7
        curses.start_color()
        curses.use_default_colors()
        self.set_color(color_setting)
        # init screen elements
        self.__elements = {}

    def __str__(self) -> typing.AnyStr:
        """Return Introduction"""
        return """
        === === === === === === === === === === === ===
        ===               Ultimate CLI              ===
        ===               Version: 0.1              ===
        === === === === === === === === === === === ===
        """

    @catch_exception
    def add_color(self,
                  name: typing.AnyStr,
                  r: typing.SupportsInt,
                  g: typing.SupportsInt,
                  b: typing.SupportsInt) -> int:
        """Add a custom color."""
        curses.init_color(self.color_idx, r, g, b)
        self.color_idx += 1     # color + 1
        # insert a lowered color name with its rgb
        self.colors.append((name.lower(), (r, g, b)))
        return self.color_idx

    @catch_exception
    def reset_color(self) -> bool:
        """Remove all custom colors."""
        self.colors = []
        self.color_idx = 8
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

    @catch_exception
    def add(self, element: typing.Dict) -> None:
        """Add new element into cli."""
        # Ensure element is a dict.
        if not isinstance(element, dict):
            # Not valid type
            raise TypeError("element must be a dict.")
        # Create a proper component according to the element's KEY:'type'.
        _element = deepcopy(element)
        _type = _element.pop("type")
        _component_proto = CLI._VALID_COMPONENT_TYPE[_type]
        # Get current cursor y,x
        self.cursor_y, self.cursor_x = self.screen.getyx()
        _element.update({
            "screen": self.screen,
            "start_row": self.cursor_y,
            "start_col": 0,
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
    cli = CLI(color_setting=color_setting)
    slateblue = {
        "name": "SlateBlue",
        "r": 106,
        "g": 90,
        "b": 205,
    }
    cli.add_color(**slateblue)
    cli.run()
    text1 = {
        "type": "text",
        "text": "Hello,World!",
    }
    cli.add(text1)
    cli.add(text1)
    cli.add(text1)
    cli.add(text1)
    cli.add(text1)
    cli.clear()
