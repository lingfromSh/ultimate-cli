'''
Filename: /home/ling/文档/ultimate-cli/Components/option.py
Path: /home/ling/文档/ultimate-cli/Components
Created Date: Wednesday, January 29th 2020, 2:49:05 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import typing as ty

from .base import ComponentBase
from .common import KEY_DOWN, KEY_ENTER, KEY_UP
from .text import TextComponent


class OptionComponent(ComponentBase):
    _name = "option__component"
    _choosen_prefix = ">"
    _normal_prefix = "\u2002"

    def __init__(self, 
                 name: ty.AnyStr, 
                 handler: ty.Callable, 
                 start_row: ty.SupportsInt, 
                 start_col: ty.SupportsInt, 
                 father: ty.Union[None, ComponentBase],
                 children: ty.Union[ty.List, ComponentBase],
                 choosen_prefix: str=">"):
        self._current_choosen = 0  # current choosen element
        self.choosen_prefix = choosen_prefix if choosen_prefix else OptionComponent._choosen_prefix
        self.normal_prefix = OptionComponent._normal_prefix * \
            len(self.choosen_prefix)
        super().__init__(name, handler, start_row, start_col, father, children)

    def render(self, screen):
        # render
        self._render_childern(screen)
        # wait user input
        while True:
            user_input = self._get_response(screen)
            screen.addstr(8, 0, "                  ")
            screen.addstr(8, 0, str(user_input))
            if user_input == KEY_UP:
                # move cursor to previous one
                current_choosen = self._current_choosen - 1
                self._set_current_choosen(current_choosen)

            elif user_input == KEY_DOWN:
                # move cursor to next one
                current_choosen = self._current_choosen + 1
                self._set_current_choosen(current_choosen)

            elif user_input == KEY_ENTER:
                # get chosen element
                return self._get_current_element()

            else:
                # do nothing
                ...

    def _render_childern(self, screen):
        # render children elements
        elements = self.children
        for idx, elem in enumerate(elements):
            elem.render(screen)

    def _get_current_element(self):
        return self.children[self._current_choosen]

    def _set_current_choosen(self, index: ty.SupportsInt) -> bool:
        """set the current choosen element."""
        self.current_choosen = index


if __name__ == "__main__":
    pass
