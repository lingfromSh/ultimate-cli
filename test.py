'''
Filename: /home/ling/文档/ultimate-cli/test.py
Path: /home/ling/文档/ultimate-cli
Created Date: Friday, January 31st 2020, 1:44:05 pm
Author: Stephen Ling

Copyright (c) 2020 Your Company
'''

from components.base import ComponentBase
from components.text import TextComponent


if __name__ == "__main__":
    # Test Base Component
    base = ComponentBase()
    print(base)
    # Test Text Component
    text = TextComponent()
    print(text)