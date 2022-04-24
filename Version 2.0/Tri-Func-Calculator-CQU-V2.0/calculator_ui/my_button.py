##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 该文件包括按钮类，每个按钮都继承自MyButton。
##########

from abc import ABC
import tkinter as tk
from tkinter import font as font
from calculator_ui.constants import *


class MyButton(ABC):
    """这是一个抽象类，代表一个按钮。"""

    def __init__(self, key, loc, func):
        """
        按钮对象的构造函数。 按钮具有颜色、大小（高度、宽度）、
        字体大小和颜色、按钮（键）上的文本、按钮和屏幕上的位置 (x,y)。
        """
        self.color = None
        self.height = None
        self.width = None
        self.f_size = None
        self.font_color = B_FG
        self.key = key
        self.func = func
        self.x = loc[0]
        self.y = loc[1]

    def create(self, screen):
        """
        该方法获取一个屏幕，并根据按钮的属性，
        把它放在给定的屏幕上。
        """
        button_font = font.Font(family=FONT, size=self.f_size, weight=font.BOLD)
        button = tk.Button(screen, text=self.key, command=self.func, bg=self.color,
                           fg=self.font_color, font=button_font)
        button.pack()
        button.place(height=self.height, width=self.width, x=self.x, y=self.y)


class StandardButton(MyButton):
    """B1型按钮。该类表示计算器底部的一些常规按钮。"""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.f_size = B1_SIZE
        self.color = B1_COLOR
        self.height = B1_HEIGHT
        self.width = B1_WIDTH


class EqualsButton(StandardButton):
    """B3 型按钮。 此类表示“=”按钮。 它比标准按钮宽。"""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.width = B3_WIDTH


class ResetButtons(StandardButton):
    """B4 型按钮。此类表示“AC”和“DEL”按钮。"""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.color = B4_COLOR
        self.font_color = B4_FG


class ExtraButton(MyButton):
    """B2 型按钮。此类代表了上半部分的计算器按钮"""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.f_size = B2_SIZE
        self.color = B2_COLOR
        self.height = B2_HEIGHT
        self.width = B2_WIDTH


class ArrowButton(ExtraButton):
    def __init__(self, key, loc, func):
        """B5 型按钮。此类表示箭头键。"""
        super().__init__(key, loc, func)
        self.color = B5_COLOR
