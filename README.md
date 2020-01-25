# Ultimate CLI version: 0.1 
> **超级CLI 为Python提供一个快速，方便，高可用的开发终端交互的工具包.**

## 环境
Python3.8

## 第三方包
1. curses

## 模块
| Name  | Description           |  Finished  | 
| ----  | --------------------- | ---------  |
| tools | 包含各种常用的cli类型工具 | in process |
| decorators|用于检查传值等等| finished|

## 模块设计
### 1. tools
使用传入字典来表示要渲染的类型和内容，渲染后当得到用户输入后返回相应的对象
```python
# e.g
# 需要用dict来控制渲染类型和渲染内容
menu = {
    'type': 'checkbox', # checkbox复选, choice单选, 不可为空
    'render': ['1. checkbox', '2. choice'],
    'handler': lambda val : val # 支持匿名函数，或者函数
}
```
1. choice 单选


2. checkbox 复选