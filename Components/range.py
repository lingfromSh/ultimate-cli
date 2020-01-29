'''
Filename: /home/ling/文档/ultimate-cli/Components/range.py
Path: /home/ling/文档/ultimate-cli/Components
Created Date: Wednesday, January 29th 2020, 3:06:41 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''
import typing as ty
from base import ComponentBase


class OptionComponent(ComponentBase):
    _name = "option__component"

    def __init__(self, name: ty.AnyStr, content: ty.List, handler: ty.Callable):
        self.content = content
        super().__init__(name, handler)

    def __str__(self):
        return self.name


if __name__ == "__main__":
    option = OptionComponent(name="Top Level Option", content=[
                             "a", "b", "c"], handler=lambda value: value % 2)
    print(option)
    print(type(option))
