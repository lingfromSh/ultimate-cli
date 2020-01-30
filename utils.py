'''
Filename: /home/ling/文档/ultimate-cli/utils.py
Path: /home/ling/文档/ultimate-cli
Created Date: Wednesday, January 29th 2020, 5:28:57 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''


import typing as ty
import secrets
from Components import (
    TextComponent,
    OptionComponent,
    ChoiceComponent,
    CheckBoxComponent,
    RangeComponent,
    valid_type as VALID_TYPE,
)

"""Convert python type into cli component."""


def std_log(content):
    print(f"********\n{content}\n********")


def parse(menu: ty.List, father: object=None) -> ty.List:
    """Convert each element in the menu into cli components."""
    # a new menu consists of cli components
    render_menu = []
    row = 0
    col = 0
    # ensure menu is a list.if not, stop render.
    if not isinstance(menu, list):
        return render_menu
    # convert element in the list into a correct cli component
    for idx, elem in enumerate(menu):
        # ensure elem has key <type>.if not,stop render it.
        if not elem.get("type", False):
            continue
        # ensure elem's type is valid.if not,stop render it.
        if elem.get("type") not in VALID_TYPE:
            continue 
        _type = elem.get("type")
        if _type == "text":
            """make a text component."""
            _name = f"text__component__{secrets.token_hex(8)}"
            params = {
                "name": _name,
                "text": elem.get("text", ""),
                "handler": elem.get("handler", None),
                "start_row": row,
                "start_col": col,
                "father": father,
                "children": []
            }
            row += 1    # row + 1
            e = TextComponent(**params)
            render_menu.append(e)
        elif _type == "checkbox":
            """make a checkbox component."""
            _name = f"checkbox__component__{secrets.token_hex(8)}"
            params = {
                "name": _name,
                "handler": elem.get("handler", None),
                "start_row": row,
                "start_col": col,
                "father": father,
                "children": parse(elem.get("children",[]), _name),
            }
            row += 1    # row + 1
            e = CheckBoxComponent(**params)
            render_menu.append(e)
        elif _type == "choice":
            """make a choice component."""
            _name = f"choice__component__{secrets.token_hex(8)}"
            params = {
                "name": _name,
                "handler": elem.get("handler", None),
                "start_row": row,
                "start_col": col,
                "father": father,
                "children": parse(elem.get("children", []), _name),
            }
            row += 1    # row + 1
            e = ChoiceComponent(**params)
            render_menu.append(e)
        elif _type == "option":
            """make an option component."""
            _name = f"option__component__{secrets.token_hex(8)}"
            params = {
                "name": _name,
                "handler": elem.get("handler", None),
                "start_row": row,
                "start_col": col,
                "father": father,
                "children": parse(elem.get("children", []), _name),
            }
            row += 1    # row + 1
            e = OptionComponent(**params)
            render_menu.append(e)
        elif _type == "range":
            """make a range component."""
            _name = f"range__component__{secrets.token_hex(8)}"
            params = {
                "name": _name,
                "handler": father,
                "start_row": row,
                "start_col": col,
                "father": father,
                "children": parse(elem.get("children", []), _name)
            }
            row += 1    # row + 1
            e = RangeComponent(**params)
            render_menu.append(e)
    return render_menu


if __name__ == "__main__":
    header = {
        "type": "text",
        "text": "Hello,World! This is a header.",
        "handler": None,
    }
    subject = {
        "type": "text",
        "text": "I am the author: Stephen Ling. Thanks for using my ultimate-cli and this is a subject.",
        "handler": None,
    }
    option = {
        "type": "option",
        "children":[
            {
                "type": "text",
                "text": "1.Option1",
                "handler": None,
            },
            {
                "type": "text",
                "text": "2.Option2",
                "handler": None,
            }
        ]
    }

    # create a menu
    menu = [
        header,
        subject,
        option,
    ]   # ultimate-cli will render the menu in order.
    root = None
    render_menu = parse(menu, root)
    print(render_menu)
    for i in render_menu:
        print(i)
