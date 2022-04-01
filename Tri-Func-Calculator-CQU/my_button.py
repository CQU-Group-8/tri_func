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
from constants import *


class MyButton(ABC):
    """This is an abstract class, which representing a button. """

    def __init__(self, key, loc, func):
        """The constructor of button object. A button has color, size (height,width),
        font size and color, the text on the button (key), the functionality of the
        button and location on the screen (x,y)."""
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
        """This method gets a screen, and according to the attributes of the button,
        placed it on the given screen."""
        button_font = font.Font(family=FONT, size=self.f_size, weight=font.BOLD)
        button = tk.Button(screen, text=self.key, command=self.func, bg=self.color,
                           fg=self.font_color, font=button_font)
        button.pack()
        button.place(height=self.height, width=self.width, x=self.x, y=self.y)


class StandardButton(MyButton):
    """B1 type buttons. This class represents the buttons at the lower part of the
    calculator."""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.f_size = B1_SIZE
        self.color = B1_COLOR
        self.height = B1_HEIGHT
        self.width = B1_WIDTH


class EqualsButton(StandardButton):
    """B3 type buttons. This class represents the '=' button. It is wider than the
    standard buttons."""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.width = B3_WIDTH


class ResetButtons(StandardButton):
    """B4 type buttons. This class represents 'AC' and 'DEL' buttons."""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.color = B4_COLOR
        self.font_color = B4_FG


class ExtraButton(MyButton):
    """B2 type buttons. This class represents the buttons at the upper part of the
    calculator."""
    def __init__(self, key, loc, func):
        super().__init__(key, loc, func)
        self.f_size = B2_SIZE
        self.color = B2_COLOR
        self.height = B2_HEIGHT
        self.width = B2_WIDTH


class ArrowButton(ExtraButton):
    def __init__(self, key, loc, func):
        """B5 type buttons. This class represents the arrows keys."""
        super().__init__(key, loc, func)
        self.color = B5_COLOR
