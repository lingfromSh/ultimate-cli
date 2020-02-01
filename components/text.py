'''
Filename: /home/ling/文档/ultimate-cli/components/text.py
Path: /home/ling/文档/ultimate-cli/components
Created Date: Friday, January 31st 2020, 10:54:31 am
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import curses
import typing
from .base import ComponentBase


class TextComponent(ComponentBase):
    _type = "text"

    def __init__(self,
                 screen: object,
                 start_row: typing.SupportsInt,
                 start_col: typing.SupportsInt,
                 text: typing.AnyStr,
                 color_pair: typing.SupportsInt,
                 #  style: typing.SupportsInt = curses.A_NORMAL
                 ):
        # get text style
        # self.__style = style
        # get a color pair
        self.__color_pair = color_pair
        # if you want to get text, use get_text instead.
        self.__text = text
        super().__init__(screen=screen, start_row=start_row, start_col=start_col)

    @staticmethod
    def get_type() -> typing.AnyStr:
        """Return self's type."""
        return TextComponent._type

    @staticmethod
    def is_type(_type: typing.AnyStr) -> bool:
        """Return type==self's type."""
        return _type == ComponentBase.get_type()

    def get_color_number(self) -> typing.SupportsInt:
        """Return self's color number."""
        return self.__color

    def set_color(self, color: typing.SupportsInt) -> bool:
        """Set color for text."""
        if not isinstance(color, int) or color <= -1:
            return False
        self.__color = color
        return True

    def get_background(self) -> typing.SupportsInt:
        """Return self's background number."""
        return self.__background

    def set_background(self, background: typing.SupportsInt) -> bool:
        """Set background for text."""
        if not isinstance(background, int) or background <= -1:
            return False
        self.__background = background
        return True

    def get_text(self) -> typing.AnyStr:
        """Return self's text."""
        return self.__text

    def set_text(self, text: typing.AnyStr) -> bool:
        """Set the text for render."""
        if not isinstance(text, str):
            return False
        self.__text = text
        return True

    def render(self) -> bool:
        """Render a text."""
        if not self._active:
            # Don't render self when _active is False
            return False
        _row = self._start_row
        for t in self.__text.split("\n"):
            # render text in a row
            self._screen.addstr(
                _row, self._start_col, t, curses.color_pair(self.__color_pair))
            # move cursor to the next row
            _row += 1
            self._screen.move(_row, self._start_col)
        return True
