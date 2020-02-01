'''
Filename: /home/ling/文档/ultimate-cli/components/choice.py
Path: /home/ling/文档/ultimate-cli/components
Created Date: Friday, January 31st 2020, 10:54:35 am
Author: Stephen Ling

Copyright (c) 2020 Stephen Ling
'''


import curses
import typing

from .base import ComponentBase
from .text import TextComponent


class ChoiceComponent(ComponentBase):
    _type = "chocie"
    _prefix = ">"
    _space = " "

    def __init__(self,
                 screen: object,
                 start_row: typing.SupportsInt,
                 start_col: typing.SupportsInt,
                 choices: typing.List,
                 color_pair: typing.SupportsInt,
                 prefix: typing.AnyStr = None,
                 ):
        super().__init__(screen=screen, start_row=start_row, start_col=start_col)
        # set prefix
        self.__prefix = prefix if prefix else ChoiceComponent._prefix
        self.__spaces = len(self.__prefix) * ChoiceComponent._space
        # get a color pair
        self.__color_pair = color_pair
        # if you want to get choices, use get_text instead.
        if not isinstance(choices, list):
            raise TypeError("choices must be a list.")
        self.__choices = choices
        self.__choices_components = self.parse_choices()

    def get_choices(self) -> typing.List:
        """Return self's choices."""
        return self.__choices

    def set_choices(self, choices: typing.List) -> bool:
        """Set choices."""
        if not isinstance(choices, list):
            return False
        self.__choices = choices
        return True

    def parse_choices(self) -> typing.List:
        """Convert choice in choices to TextComponent."""
        params = {
            "screen": self._screen,
            "color_pair": self.__color_pair,
        }
        _components = []
        _row = self._start_row
        _col = self._start_col
        for idx, choice in enumerate(self.__choices):
            params.update({"text": f"{self.__spaces}{choice}",
                           "start_row": _row,
                           "start_col": _col})
            if idx == 0:
                params.update({"text": f"{self.__prefix}{choice}"})
            text = TextComponent(**params)
            _components.append(text)
            _row += 1
        return _components

    def render(self) -> bool:
        """Render Choice."""
        # Ensure being active.
        if not self.is_active:
            return False
        for choice in self.__choices_components:
            choice.render()
        self._screen.move(self._start_row, self._start_col)

    def get_handler(self):
        """Make proper response after user input."""
        while True:
            key = self._screen.getch()
            if key == 10 or key == 13:   # enter
                self.deactivate()
                return self.__choices[self._screen.getyx()[0] - self._start_row]
            elif key == curses.KEY_DOWN:    # down
                _row, _col = self._screen.getyx()
                self._screen.addstr(_row, _col, self.__spaces)
                _row = (_row - self._start_row + 1) % len(self.__choices) + \
                    self._start_row
                self._screen.addstr(_row, _col, self.__prefix)
                self._screen.move(_row, _col)
            elif key == curses.KEY_UP:  # up
                _row, _col = self._screen.getyx()
                self._screen.addstr(_row, _col, self.__spaces)
                _row = (_row - self._start_row - 1) % len(self.__choices) + \
                    self._start_row
                self._screen.addstr(_row, _col, self.__prefix)
                self._screen.move(_row, _col)
            else:
                # do nothing
                ...
            self._screen.refresh()
