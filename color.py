# ==========================
#        color,py
#      version: 0.1
#    created:2020.1.24
# ==========================
import typing as ty
import decorators

# HEX Color

_COLOR_BLACK = "#000000"
_COLOR_WHITE = "#ffffff"
_COLOR_RED = "#ff0000"
_COLOR_GREEN = "#00ff00"
_COLOR_BLUE = "#0000ff"


@decorators.need_type(params=('r', 'g', 'b'), t=int)
def rgb_to_hex(r: int, g: int, b: int) -> str:
    """rgb color to hex."""
    hex_str = ""  # hex color
    for num in (r, g, b):
        hex_str += str(hex(num))[-2:].replace('x', '0').lower()
    else:
        return f"#{(hex_str)}"


@decorators.need_type(params=('h',), t=str)
def hex_to_rgb(h: str) -> tuple:
    """hex color to rgb"""
    hexcolor = h.strip("#")
    r = eval(f"0x{hexcolor[:2]}")
    g = eval(f"0x{hexcolor[2:4]}")
    b = eval(f"0x{hexcolor[4:]}")
    return r, g, b


if __name__ == "__main__":
    # test
    print(rgb_to_hex(r=255, g=0, b=0))
    print(hex_to_rgb(h='#ff0000'))
