# Ultimate CLI version: 0.1 
> **超级CLI 为Python提供一个快速，方便，高可用的开发终端交互的工具包.**

## 环境
Python3.6+

## 第三方包
1. curses

## 快速上手
1. JSON
```python
header = {
    "type": "header",
    "text": "Hello,World!"
}
cli = Ulitimate_CLI(header)
cli.render()
```


## 模块
|Name|Description|
|:- |:- |
|Components| components |


## 模块进度
1. Components
    - [  ] base
    - [  ] checkbox
    - [  ] choice
    - [  ] option
    - [  ] range
    - [  ] text
    
## 模块设计
1. base - ComponentBase
> 这是一个基本类,描述所有组件的基本操作，基本属性。

    1. name      用于子组件查找父组件,命名规范为 {组件名}__component__{16位16进制token}
    2. start_row 开始渲染的行
    3. start_col 开始渲染的列
    4. father    父组件,可以用于返回
    5. children  子组件,接受用户操作直接渲染无需用户编程决定
    6. handler   返回用户输入的结果,支持函数

2. text - TextComponent
> 这是一个文字类,单行文字用于说明.

    1. text 需要渲染的文字

