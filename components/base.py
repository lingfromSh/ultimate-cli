'''
Filename: /home/ling/文档/ultimate-cli/components/base.py
Path: /home/ling/文档/ultimate-cli/components
Created Date: Friday, January 31st 2020, 10:54:26 am
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import curses
import secrets
import typing
from abc import abstractmethod, abstractstaticmethod


class ComponentBase:
    _type = "base"

    def __init__(self,
                 screen: object,
                 start_row: typing.SupportsInt,
                 start_col: typing.SupportsInt):
        self.__token = self.token()
        # Ensure screen is a curses._CursesWindow
        # But i can't import _CursesWindow directly
        # So i use checking its attributes instead.
        # if you want to get __screen, use get_screen instead.
        if not hasattr(screen, "addstr"):
            raise TypeError("Invalid Screen.")
        self._screen = screen
        self._start_row = start_row
        self._start_col = start_col
        # is active
        self._active = True

    def __str__(self):
        return self.name

    def __del__(self):
        # Do nothing.
        ...

    @classmethod
    def token(cls: object) -> typing.AnyStr:
        """Return a unique token."""
        return f"{cls.__name__}__{secrets.token_hex(8)}"

    @property
    def name(self) -> typing.AnyStr:
        """Return self's token as a unique name."""
        return self.__token

    @abstractstaticmethod
    def get_type() -> typing.AnyStr:
        """Return self's type."""
        ...

    @abstractstaticmethod
    def is_type(_type: typing.AnyStr) -> bool:
        """Return type==self's type."""
        ...

    @abstractmethod
    def render(self):
        """Render self to the screen."""
        ...

    def set_screen(self, screen: object) -> bool:
        # Ensure screen is a curses._CursesWindow
        # But i can't import _CursesWindow directly
        # So i use checking its attributes instead.
        if not hasattr(screen, "addstr"):
            return False
        self._screen = screen
        return True

    def get_screen(self) -> object:
        """Return self's __screen."""
        return self.__screen

    @property
    def is_active(self) -> bool:
        return self._active

    def deactivate(self):
        """Set self inactive."""
        self._active = False

    def activate(self):
        """Set self active."""
        self._active = True

    def get_start_row(self) -> typing.SupportsInt:
        """Return self's _start_row."""
        return self._start_row

    def set_start_row(self, start_row: typing.SupportsInt):
        """Set self _start_row."""
        self._start_row = start_row

    def get_start_col(self) -> typing.SupportsInt:
        """Return self's _start_col."""
        return self._start_col

    def set_start_col(self, start_col: typing.SupportsInt):
        """Set self _start_col."""
        self._start_col = start_col

    def get_handler(self):
        """Make proper response after user input."""
        ...