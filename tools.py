"""
Filename: /home/ling/文档/ultimate-cli/tools.py
Path: /home/ling/文档/ultimate-cli
Created Date: Sunday, January 26th 2020, 2:24:40 pm
Author: ling

Copyright (c) 2020 Your Company
"""

import curses  # 界面绘图,键盘响应
import decorators   # 参数检查

__all__ = ["get_handler"]


class RenderObj:
    def __init__(self, menu):
        # init screen for render
        self.scr = curses.initscr()
        self.scr.clear()
        self.length = 0  # str length 文字所占行
        self.crow = 0  # current cursor row  光标所在行
        self.ccol = 0  # current cursor column   光标所在列

    def render(self):
        ...

    def __del__(self):
        self.scr.clear()
        curses.endwin()


class Choice(RenderObj):
    def __init__(self, menu):
        super().__init__(menu)
        curses.noecho()     # 不允许显示输入
        self.scr.keypad(True)    # 接受特殊键盘
        curses.cbreak()       # 直接响应
        # set header
        self.header = menu.get("header", "")
        # set choices
        self.choices = menu.get("choices", [])
        self.choices_length = len(self.choices)
        self.choices_start_row = 1 if self.header else 0
        # set cursor
        self.cursor = menu.get("cursor", ">")
        if len(self.cursor) != 1 or not isinstance(self.cursor, str):
            self.cursor = ">"

    def render(self):
        """Choice"""
        # render header
        if self.header:
            self.scr.addstr(self.crow, self.ccol, self.header)
            self.crow += 1      # line + 1
            self.length += 1    # length + 1
        # render choices
        for idx, choice in enumerate(self.choices):
            self.scr.addstr(self.crow, self.ccol, f"\u2002{choice}")
            if idx == 0:
                self.scr.addstr(self.crow, self.ccol, self.cursor)
            self.crow += 1      # line + 1
            self.length += 1    # length + 1
        # set cursor to the first choice
        self.crow = self.choices_start_row
        self.scr.move(self.crow, self.ccol)
        self.scr.refresh()
        while True:
            key = self.scr.getch()
            if key == curses.KEY_UP:
                # remove last choice selected flag
                self.scr.addstr(self.crow, self.ccol,
                                f" {self.choices[self.crow-1]}")
                # set flag to the new selected
                self.crow = self.crow - 1 if self.crow > self.choices_start_row else self.length - 1
                self.scr.addstr(self.crow, self.ccol, self.cursor)
                self.scr.move(self.crow, self.ccol)
            elif key == curses.KEY_DOWN:
                # remove last choice selected flag
                self.scr.addstr(self.crow, self.ccol,
                                f" {self.choices[self.crow-1]}")
                # set flag to the new selected
                self.crow = self.crow + 1 if self.crow < self.length - 1 else self.choices_start_row
                self.scr.addstr(self.crow, self.ccol, self.cursor)
                self.scr.move(self.crow, self.ccol)
            elif key == curses.KEY_LEFT or key == curses.KEY_RIGHT:
                # do nothing
                self.scr.move(self.crow, self.ccol)
            elif key == 10 or key == curses.KEY_ENTER:
                return self.choices[self.crow-self.choices_start_row]
            self.scr.refresh()


class Checkbox(RenderObj):
    def __init__(self, menu):
        super().__init__(menu)
        curses.noecho()     # 不允许显示输入
        self.scr.keypad(True)    # 接受特殊键盘
        curses.cbreak()       # 直接响应
        # set header
        self.header = menu.get("header", "")
        # set choices
        self.choices = menu.get("choices", [])
        self.choices_length = len(self.choices)
        self.choices_start_row = 1 if self.header else 0
        # set selected
        self.selected = []
        # set cursor
        self.cursor = menu.get("cursor", ">")
        if len(self.cursor) != 1 or not isinstance(self.cursor, str):
            self.cursor = ">"
        # set checkbox icon
        self.unchecked_icon = menu.get("unchecked", "\u2610")
        self.checked_icon = menu.get("checked", "\u2611")
        if len(self.unchecked_icon) != 1 or not isinstance(self.unchecked_icon, str):
            self.unchecked_icon = "\u2610"
        if len(self.checked_icon) != 1 or not isinstance(self.checked_icon, str):
            self.checked_icon = "\u2611"

    def render(self):
        """Checkbox"""
        # render header
        if self.header:
            self.scr.addstr(self.crow, self.ccol, self.header)
            self.crow += 1
            self.length += 1
        # render choices
        for idx, choice in enumerate(self.choices):
            if idx == 0:
                self.scr.addstr(self.crow, self.ccol,
                                f"{self.cursor}{self.unchecked_icon} {choice}")
            else:
                self.scr.addstr(self.crow, self.ccol,
                                f" {self.unchecked_icon} {choice}")
            self.crow += 1
            self.length += 1
        # set cursor to the first choice
        self.crow = self.choices_start_row
        self.scr.move(self.crow, self.ccol)
        self.scr.refresh()
        while True:
            key = self.scr.getch()
            if key == curses.KEY_UP:
                # remove last choice selected flag
                self.scr.addstr(self.crow, self.ccol,
                                f" ")
                # set flag to the new selected
                self.crow = self.crow - 1 if self.crow > self.choices_start_row else self.length - 1
                self.scr.addstr(self.crow, self.ccol, self.cursor)
                self.scr.move(self.crow, self.ccol)
            elif key == curses.KEY_DOWN:
                # remove last choice selected flag
                self.scr.addstr(self.crow, self.ccol,
                                f" ")
                # set flag to the new selected
                self.crow = self.crow + 1 if self.crow < self.length - 1 else self.choices_start_row
                self.scr.addstr(self.crow, self.ccol, self.cursor)
                self.scr.move(self.crow, self.ccol)
            elif key == curses.KEY_LEFT or key == curses.KEY_RIGHT:
                # do nothing
                self.scr.move(self.crow, self.ccol)
            elif key == 32:
                tmp = self.choices[self.crow-self.choices_start_row]
                if tmp in self.selected:
                    self.scr.addstr(self.crow, self.ccol+1, self.unchecked_icon)
                    self.selected.remove(tmp)
                else:
                    self.scr.addstr(self.crow, self.ccol+1, self.checked_icon)
                    self.selected.append(tmp)
                self.scr.move(self.crow, self.ccol)
            elif key == 10 or key == curses.KEY_ENTER:
                return self.selected
            self.scr.refresh()


@decorators.need_keys(param="menu", keys={"type"})
@decorators.need_type(params=("menu",), t=dict)
def get_handler(menu: dict) -> RenderObj:
    if menu["type"] == "choice":
        return Choice(menu).render()
    elif menu["type"] == "checkbox":
        return Checkbox(menu).render()


if __name__ == "__main__":
    menu1 = {
        "type": "choice",
        "header": "Ultimate CLi 用于打造终端交互的cli.",
        "choices": [
                "1. 配置简单",
                "2. 效果丰富",
                "3. 高可用",
                "4. 高复用",
                "5. 退出"
        ],
        "cursor": ">",        # utf8 符号 TODO:显示有错
    }
    handler = get_handler(menu=menu1)
    with open("log.log", "w+") as f:
        f.writelines([handler, "\n"])
    menu2 = {
        "type": "checkbox",
        "header": "Ultimate CLi 用于打造终端交互的cli.",
        "choices": [
            "1. 配置简单",
            "2. 效果丰富",
            "3. 高可用",
            "4. 高复用",
            "5. 返回"
            "6. 退出"
        ],
        "cursor": ">",        # utf8 符号 TODO:显示有错
        "checked": "\u2611",
        "unchecked": "\u2610",
    }
    handler = get_handler(menu=menu2)
    with open("log.log", "a+") as f:
        f.write("\n".join(handler))
    if "6. 退出" in handler:
        exit()
