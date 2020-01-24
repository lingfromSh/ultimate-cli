# STDOUT.py
#   by Stephen Ling
#
# Created:
#   2020/1/24 下午8:39:02
# Last edited:
#   2020/1/24 下午8:56:47
# Auto updated?
#   Yes
#
# Description:
#   <Todo>
#


import decorators


@decorators.need_type(params=('text', 'display_mode', 'fg_color', 'bg_color'), t=str)
def cprint(text: str = None, display_mode: str = "normal", fg_color: str = None, bg_color: str = None):
    """
        \033[ 颜色开头
        显示方式:
            - 0 默认
            - 1 高亮+粗体
            - 2 淡色
            - 3 斜体
            - 4 下划线
            - 5 闪烁
            - 6 闪烁
            - 7 反色
        字体颜色:
            - 30 黑色   black
            - 31 红色   red
            - 32 绿色   green
            - 33 黄色   yellow
            - 34 蓝色   blue
            - 35 紫色   purple
            - 36 青色   cyan
            - 37 灰色   grey
        背景颜色:
            - 40 黑色   black
            - 41 红色   red
            - 42 绿色   green    
            - 43 黄色   yellow
            - 44 蓝色   blue
            - 45 紫色   purple 
            - 46 青色   cyan
            - 47 灰色   grey 
    """
    # display mode
    _format_prefix = "\033["
    if display_mode == "normal":
        _format_prefix += "1;"
    elif display_mode == "bold":
        _format_prefix += "2;"
    elif display_mode == "italic":
        _format_prefix += "3;"
    elif display_mode == "underline":
        _format_prefix += "4;"
    elif display_mode == "flash":
        _format_prefix += "5;"
    elif display_mode == "invert":
        _format_prefix += "7;"
    else:
        _format_prefix += "1;"
    # text color
    if fg_color == "black":
        _format_prefix += "30;"
    elif fg_color == "red":
        _format_prefix += "31;"
    elif fg_color == "green":
        _format_prefix += "32;"
    elif fg_color == "yellow":
        _format_prefix += '33;'
    elif fg_color == "blue":
        _format_prefix += "34;"
    elif fg_color == "purple":
        _format_prefix += "35;"
    elif fg_color == "cyan":
        _format_prefix += "36;"
    elif fg_color == "grey":
        _format_prefix += "37;"
    else:
        _format_prefix += "37;"
    # background color
    if bg_color == "black":
        _format_prefix += "40m"
    elif bg_color == "red":
        _format_prefix += "41m"
    elif bg_color == "green":
        _format_prefix += "42m"
    elif bg_color == "yellow":
        _format_prefix += "43m"
    elif bg_color == "blue":
        _format_prefix += "44m"
    elif bg_color == "purple":
        _format_prefix += "45m"
    elif bg_color == "cyan":
        _format_prefix += "46m"
    elif bg_color == "grey":
        _format_prefix += "47m"

    print(f"{_format_prefix}{text}\033[0m")


@decorators.need_type(params=('text', 'display_mode', 'fg_color', 'bg_color'), t=str)
def ctext(text: str = None, display_mode: str = "normal", fg_color: str = None, bg_color: str = None):
    """
        \033[ 颜色开头
        显示方式:
            - 0 默认
            - 1 高亮+粗体
            - 2 淡色
            - 3 斜体
            - 4 下划线
            - 5 闪烁
            - 6 闪烁
            - 7 反色
        字体颜色:
            - 30 黑色   black
            - 31 红色   red
            - 32 绿色   green
            - 33 黄色   yellow
            - 34 蓝色   blue
            - 35 紫色   purple
            - 36 青色   cyan
            - 37 灰色   grey
        背景颜色:
            - 40 黑色   black
            - 41 红色   red
            - 42 绿色   green    
            - 43 黄色   yellow
            - 44 蓝色   blue
            - 45 紫色   purple 
            - 46 青色   cyan
            - 47 灰色   grey 
    """
    # display mode
    _format_prefix = "\033["
    if display_mode == "normal":
        _format_prefix += "1;"
    elif display_mode == "bold":
        _format_prefix += "2;"
    elif display_mode == "italic":
        _format_prefix += "3;"
    elif display_mode == "underline":
        _format_prefix += "4;"
    elif display_mode == "flash":
        _format_prefix += "5;"
    elif display_mode == "invert":
        _format_prefix += "7;"
    else:
        _format_prefix += "1;"
    # text color
    if fg_color == "black":
        _format_prefix += "30;"
    elif fg_color == "red":
        _format_prefix += "31;"
    elif fg_color == "green":
        _format_prefix += "32;"
    elif fg_color == "yellow":
        _format_prefix += '33;'
    elif fg_color == "blue":
        _format_prefix += "34;"
    elif fg_color == "purple":
        _format_prefix += "35;"
    elif fg_color == "cyan":
        _format_prefix += "36;"
    elif fg_color == "grey":
        _format_prefix += "37;"
    else:
        _format_prefix += "37;"
    # background color
    if bg_color == "black":
        _format_prefix += "40m"
    elif bg_color == "red":
        _format_prefix += "41m"
    elif bg_color == "green":
        _format_prefix += "42m"
    elif bg_color == "yellow":
        _format_prefix += "43m"
    elif bg_color == "blue":
        _format_prefix += "44m"
    elif bg_color == "purple":
        _format_prefix += "45m"
    elif bg_color == "cyan":
        _format_prefix += "46m"
    elif bg_color == "grey":
        _format_prefix += "47m"

    return f"{_format_prefix}{text}\033[0m"


if __name__ == "__main__":
    # test
    cprint(text="Hello", display_mode="flash",
           fg_color="white", bg_color="cyan")

    t1 = ctext(text="Hello", display_mode="flash",
               fg_color="white", bg_color="blue")
    t2 = ctext(text="World,", display_mode="normal",
               fg_color="black", bg_color="green")
    t3 = ctext(text="I am", display_mode="underline",
               fg_color="green", bg_color="purple")
    t4 = ctext(text="Ling", display_mode="bold",
               fg_color="red", bg_color="yellow")
    print(f"{t1}{t2}{t3}{t4}")
