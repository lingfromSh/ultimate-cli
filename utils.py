'''
Filename: /home/ling/文档/ultimate-cli/utils.py
Path: /home/ling/文档/ultimate-cli
Created Date: Wednesday, January 29th 2020, 5:28:57 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''


def parse(menu: list):
    if not isinstance(menu, list):
        raise TypeError("Wrong Type.")
    for i, m in enumerate(menu):
        if isinstance(m, dict):
            