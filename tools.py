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
        self.length = 0  # str length 文字所占行
        self.crow = 0  # current cursor row  光标所在行
        self.ccol = 0  # current cursor column   光标所在列
        self.menu = menu

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
        # set exit
        self.exit = menu.get("exit")

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

    def render(self):
        """Checkbox"""
        print("checkbox")


@decorators.need_keys(param="menu", keys={"type"})
@decorators.need_type(params=("menu",), t=dict)
def get_handler(menu: dict) -> RenderObj:
    if menu["type"] == "choice":
        return Choice(menu).render()
    elif menu["type"] == "checkbox":
        return Checkbox(menu).render()


if __name__ == "__main__":
    menu = {
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
    handler = get_handler(menu=menu)
    with open("log.log", "w+") as f:
        f.writelines([handler, "\n"])
