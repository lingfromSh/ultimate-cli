'''
Filename: /home/ling/文档/ultimate-cli/Components/text.py
Path: /home/ling/文档/ultimate-cli/Components
Created Date: Wednesday, January 29th 2020, 4:11:10 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

import typing as ty
from .base import ComponentBase


class TextComponent(ComponentBase):
    _name = "text__component"

    def __init__(self, name: ty.AnyStr, handler: ty.Callable, start_row: ty.SupportsInt, start_col: ty.SupportsInt, father: ty.Union[ComponentBase, None], children: ty.Union[ComponentBase, None], text: ty.AnyStr):
        self.text = text
        super().__init__(name, handler, start_row, start_col, father, None)

    def get_render_obj(self):
        return self

    def render(self, screen):
        screen.addstr(self.start_row, self.start_col, self.text)
