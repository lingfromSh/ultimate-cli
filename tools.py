# TOOLS.py
#   by Stephen Ling
#
# Created:
#   2020/1/24 下午9:31:48
# Last edited:
#   2020/1/24 下午9:49:57
# Auto updated?
#   Yes
#
# Description:
#   <Todo>
#

import decorators


class Cli:
    @decorators.only_supported_elements(params=('mode',),
                                        supported=('list', 'checkbox', 'choice'))
    @decorators.need_type(params=('mode', 'header', 'subject'), t=str)
    @decorators.need_type(params=('menu',), t=list)
    def __init__(self, mode: str = "list", header: str = "Hello, World!",
                 subject: str = "I am Stephen Ling", menu: list = []) -> None:
        self.mode = mode
        self.header = header
        self.subject = subject
        self.menu = menu

    @decorators.only_supported_elements(params=('mode',),
                                        supported=('list', 'checkbox', 'choice'))
    @decorators.need_type(params=('mode',), t=str)
    def set_mode(self, mode: str = "list") -> None:
        self.mode = mode

    @decorators.need_type(params=('header',), t=str)
    def set_header(self, header: str = "Hello,World!") -> None:
        self.header = header

    @decorators.need_type(params=('subject',), t=str)
    def set_subject(self, subject: str = "I am Stephen Ling") -> None:
        self.subject = subject

    @decorators.need_type(params=('menu',), t=list)
    def set_menu(self, menu: list = []) -> None:
        self.menu = menu

    @decorators.need_type(params=('menu',), t=list)
    def add_menu(self, elements: list = []) -> None:
        self.menu.extend(elements)

    def render(self):
        return
