##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 计算器功能和GUI实现。
##########

from tkinter import *
from functools import partial
from calculator_ui.my_button import *
from tri_function.sin import sin
from tri_function.cos import cos
from tri_function.tan import tan
from tri_function.asin import asin
from tri_function.acos import acos
from tri_function.atan import atan
from PyQt5 import QtWidgets

class Calculator:
    """计算器的UI由矩形屏幕、按钮、和一个展示当前表达式的横幅。"""
    arithmetic = {POW: OP_POW, POW_3: OP_POW_3, POW_2: OP_POW_2,
                  DIVIDE: OP_DIVIDE, MUL: OP_MUL, PLUS: PLUS, MINUS: MINUS}
    extra_functions = {SQRT: OP_SQRT, SIN: OP_SIN, COS: OP_COS, TAN: OP_TAN, ASIN: OP_ASIN,
                       ACOS: OP_ACOS, ATAN: OP_ATAN}
    powers = {POW_2: POW_2_DIS, POW_3: POW_3_DIS, POW: POW_DIS}
    rounding = {L_FLOOR: OP_L_FLOOR, R_FLOOR: OP_R_FLOOR, L_CEIL: OP_L_CEIL,
                R_CEIL: OP_R_CEIL}
    # 计算器的按钮。 每个按钮都表示为一个元组，
    # 格式如下：(<display_name>, <button_type>)
    # 按钮类型可以在 constants.py 中找到
    buttons = [[(EQUALS, B3), (EQUALS, B3), (ANS, B1), (DOT, B1), (ZERO, B1)],
               [(MINUS, B1), (PLUS, B1), (THREE, B1), (TWO, B1), (ONE, B1)],
               [(DIVIDE, B1), (MUL, B1), (SIX, B1), (FIVE, B1), (FOUR, B1)],
               [(AC, B4), (DEL, B4), (NINE, B1), (EIGHT, B1), (SEVEN, B1)],
               [(POW, B2), (POW_3, B2), (POW_2, B2), (SQRT, B2), (R_PAR, B2),
                (L_PAR, B2)],
               [(ATAN, B2), (ACOS, B2), (ASIN, B2), (TAN, B2), (COS, B2), (SIN, B2)],
               [(R_FLOOR, B2), (L_FLOOR, B2), (R_ARR, B5), (L_ARR, B5), (R_CEIL, B2),
                (L_CEIL, B2)]]

    def __init__(self):
        """GUI的构造函数。"""
        self.screen = tk.Tk()
        # 表示用户输入的当前表达式的列表。
        # 列表的每个元素都是一个元组，格式为 (<expression>, <display>)：
        # 表达式是python计算出来的实际操作数
        # 和 display 是显示横幅上表达式的表示。
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        self.pre_ans = INIT_ANS
        self.is_error = False
        self.is_answer = False
        self.is_rad = False
        self._cur_idx = 0
        self._display_var = StringVar()
        self._init_screen()
        self.display_box = QtWidgets.QLineEdit

    def str_to_number(self):
        """
        将显示框的文本转为对应的数值，判断字符串是否为空，
        对字符串中是否包含“°”进行判读，并改变self.is_rad状态
        :return: number，字符串对应的值或者None
        """
        number_str = self.display_box.text()
        if len(number_str) < 1:
            self.is_error = True
            return None
        if "°" in number_str:
            self.is_rad = False
            number_str = number_str[:-1]  # 去掉度数单位，截取数字文本 并且转换为弧度
        if self.is_error:
            return None
        return eval(number_str)

    def display_to_box(self, content):
        """
        在显示框上显示内容
        :param content: str，要的显示内容；
        :return: None
        """
        self.display_box.setText(content)

    def compute(self, compute_type):
        """
        根据不同的按钮功能，对用户输入进行计算，将计算结果显示到显示框上；
        :param compute_type: int，计算类型的标识；
        :return: None；
        """

        input_value = self.str_to_number()  # 获取用户输入

        if self.is_error or input_value is None:
            return None
        if compute_type == 0:
            result = sin(input_value, self.is_rad)  # 计算sin
        elif compute_type == 1:
            result = cos(input_value, self.is_rad)  # 计算cos
        elif compute_type == 2 and self.is_rad:
            # 这里使用self.is_rad进行判读，是为了防止输入值是度数
            result = str(atan(input_value)) + "°"  # 计算arctan
        elif compute_type == 3 and self.is_rad:

            result = asin(input_value)  # 计算arcsin
            if isinstance(result, bool):
                # 返回一个bool值说明输入有误，显示提示信息
                result = "无效输入"
                self.is_error = True
            else:
                result = str(result) + "°"
        else:
            result = "无效输入"
            self.is_error = True  # 出错 锁死
        self.display_to_box(str(result))  # 显示结果
        self.is_rad = True
        self.is_compute = True

    def display_number(self, number):
        """
        在显示框上显示按钮对应的值
        :param number: 按钮对应的值
        :return: None
        """
        display_content = self.display_box.text()  # 获取显示框的文本
        if display_content == "0" or self.is_compute:
            display_content = str(number)  # 当前内容为0，直接更新为的按钮数字
        else:
            display_content += str(number)  # 当前内容不为0，追加数字
        self.display_to_box(display_content)  # 回显内容
        self.is_compute = False
        self.is_error = False

    def display_dot(self):
        """
        在显示框上显示一个小数点.
        :return: None
        """
        display_content = self.display_box.text()  # 获取显示框的文本
        if "." in display_content or self.is_compute:
            return
        else:
            display_content += "."  # 追加一个小数点
            self.display_to_box(display_content)  # 回显内容

    def _init_screen(self):
        """设置计算器屏幕。"""
        self._set_background()
        self._set_labels()
        self._set_buttons()
        self._set_display_banner()
        self._display_exp()
        # 开始光标动作
        self.screen.after(CURSOR_BLINK, self._set_cursor)

    def _set_background(self):
        """设置屏幕的背面，它的标题、大小和颜色。"""
        self.screen.title(TITLE)
        self.screen.geometry(SCREEN_SIZE)
        self.screen.resizable(width=False, height=False)
        self.screen.configure(background=S_COLOR)

    def _set_labels(self):
        """在屏幕上设置标签。"""
        self.gen_label(NAME_S, NAME_T, NAME_FG, NAME_SIZE, NAME_LOC)
        self.gen_label(COMP_S, COMP_T, COMP_FG, COMP_SIZE, COMP_LOC)
        self.gen_label(MOD_S, MOD_T, MOD_FG, MOD_SIZE, MOD_LOC)

    def gen_label(self, text_size, text, fg, size, loc):
        """set_labels 的辅助函数，在屏幕上设置给定的标签"""
        label_font = font.Font(family=FONT, size=text_size, weight=font.BOLD)
        label = tk.Label(self.screen, text=text, bg=S_COLOR, font=label_font, fg=fg)
        label.pack()
        label.place(height=size[0], width=size[1], x=loc[0], y=loc[1])

    def _set_display_banner(self):
        """设置显示横幅并将其放置在屏幕上"""
        display_font = font.Font(family=FONT, size=D_F_SIZE)
        display = Entry(self.screen, textvariable=self._display_var, bd=BORDER_SIZE,
                        bg=DISPLAY_BG, font=display_font, fg=DISPLAY_FG)
        display.pack()
        display.place(height=DISPLAY_H, width=DISPLAY_W, x=DISPLAY_X, y=DISPLAY_Y)

    def _set_cursor(self):
        """光标动画。每隔 CURSOR_BLINK 秒将调用此方法并切换当前光标表示（从 '|' 到 ''）"""
        if not self.is_answer and not self.is_error:
            cursor = self.exp_stack[self._cur_idx]
            blink = [DIS_SEP, ""]
            self.exp_stack[self._cur_idx] = (EXP_SEP, blink[1 - blink.index(cursor[1])])
            self._display_exp()
        self.screen.after(CURSOR_BLINK, self._set_cursor)

    def _set_buttons(self):
        """负责在屏幕上放置按钮"""
        x = S_WIDTH - (2 * (WIDTH_GAP + B1_WIDTH))
        y = S_HEIGHT - (HEIGHT_GAP - WIDTH_GAP + B1_HEIGHT)
        i, j = 0, 0
        self.buttons_factory(EQUALS, B3, x, y)
        j = 2
        # create big buttons
        i, j, x, y = self._place_buttons(i, j, x, y, 4, 5, B1_HEIGHT, B1_WIDTH)
        y += HEIGHT_GAP
        # create small buttons
        self._place_buttons(i, j, x, y, 7, 6, B2_HEIGHT, B2_WIDTH)

    def _place_buttons(self, i, j, x, y, rows, cols, height_gap, width_gap):
        """给定网格大小（行、列），此方法将按钮从(i,j)索引处的self.buttons矩阵，位于屏幕上所需的位置根据(x,y)参数。"""
        while i < rows:
            while j < cols:
                x -= (WIDTH_GAP + width_gap)
                key = self.buttons[i][j][0]
                b_type = self.buttons[i][j][1]
                self.buttons_factory(key, b_type, x, y)
                j += 1
            y -= (HEIGHT_GAP + height_gap)
            x = S_WIDTH
            j = 0
            i += 1
        return i, j, x, y

    def get_func(self, key):
        """获取按钮显示名称（键），并返回该按钮应执行的功能。"""
        if key == EQUALS:
            return self._equals_func
        elif key == ANS:
            return self._ans_func
        elif key == DEL:
            return self._del_func
        elif key == AC:
            return self._ac_func
        elif key == L_ARR:
            return partial(self._arrow_func, L)
        elif key == R_ARR:
            return partial(self._arrow_func, R)
        else:
            return partial(self._key_func, key)

    def buttons_factory(self, key, t, x, y):
        """给定按钮的键和类型，工厂创建相关的按钮对象然后使用“创建”可共享方法将其放置在屏幕上。"""
        func = self.get_func(key)
        button = None
        if t == B1:
            button = StandardButton(key, (x, y), func)
        elif t == B2:
            button = ExtraButton(key, (x, y), func)
        elif t == B3:
            button = EqualsButton(key, (x, y), func)
        elif t == B4:
            button = ResetButtons(key, (x, y), func)
        elif t == B5:
            button = ArrowButton(key, (x, y), func)
        button.create(self.screen)

    def _display_exp(self):
        """该方法生成cur_display，它是一个字符串，包含
         显示用户键入的当前表达式的表示。 然后将它放置在显示横幅中。"""
        cur_display = "".join(elem[1] for elem in self.exp_stack)
        self._display_var.set(cur_display)

    def _add_elem(self, exp_elem, dis_elem):
        """
        将新元素添加到当前表达式数组。
        :param exp_elem: python 执行的实际表达式。
        :param dis_elem：显示横幅上的表达式表示。
        """
        self.exp_stack = self.exp_stack[:self._cur_idx] + [(exp_elem, dis_elem)] \
                         + [(EXP_SEP, DIS_SEP)] + self.exp_stack[self._cur_idx + 1:]
        self._cur_idx += 1

    def _remove_elem(self):
        """根据光标位置删除一个元素。光标之前的元素将被删除。"""
        self.exp_stack = self.exp_stack[:self._cur_idx - 1] + self.exp_stack[self._cur_idx:]
        self._cur_idx -= 1


    def get_exp(self, key):
        """获取出现在按钮上的字符串并返回该键表示的表达式。"""
        if key in self.arithmetic:
            return self.arithmetic.get(key)
        elif key in self.extra_functions:
            return self.extra_functions.get(key)
        elif key in self.rounding:
            return self.rounding.get(key)
        return key

    def get_dis(self, key):
        """获取出现在按钮上的字符串并返回此键的显示名称，如显示横幅中所示"""
        if key in self.extra_functions:
            return key + L_PAR
        elif key in self.powers:
            return self.powers.get(key)
        else:
            return key

    def _arrow_func(self, direction):
        """负责箭头键的动作。"""
        if not self.is_error and \
                not ((direction == L and self._cur_idx == 0) or
                     (direction == R and self._cur_idx == len(self.exp_stack) - 1)):
            self.is_answer = False
            self.exp_stack[self._cur_idx] = self.exp_stack[self._cur_idx + direction]
            self.exp_stack[self._cur_idx + direction] = (EXP_SEP, DIS_SEP)
            self._display_exp()
            self._cur_idx += direction

    def _check_power(self):
        """在实际的科学计算器中，一个数字后只能放置一个幂字符。此方法返回True
        以防用户尝试将电源元件按顺序排列。"""
        if self._cur_idx - 1 >= 0 and \
                self.exp_stack[self._cur_idx - 1][1] in self.powers.values():
            # if there is an element left to the cursor and it's a power:
            return True
        elif self._cur_idx + 1 <= len(self.exp_stack) - 1 and \
                self.exp_stack[self._cur_idx + 1][1] in self.powers.values():
            # if there is an element right to the cursor and it's a power:
            return True
        else:
            return False

    def _key_func(self, key):
        """这个方法负责大部分按钮的动作，除了特殊按钮：AC、DEL、Ans、箭头和等号。"""
        if not self.is_error:
            self.is_answer = False
            if len(self.exp_stack) == 1 and self.pre_ans != INIT_ANS \
                    and key in self.arithmetic:
                # to allow concatenation of previous answer with a new arithmetic operand
                self._add_elem(self.pre_ans, ANS)
            if key in self.powers and self._check_power():
                # in case the user tries to do multiple powers, do not allow it
                return
            self._add_elem(self.get_exp(key), self.get_dis(key))
            self._display_exp()

    def _ans_func(self):
        """负责'Ans'按钮的动作"""
        if not self.is_error:
            self.is_answer = False
            if self.pre_ans == INIT_ANS:
                # in case there is no pre answer, and however the user try using it:
                self.pre_ans = "0"
            self._add_elem(self.pre_ans, ANS)
            self._display_exp()

    def _del_func(self):
        """负责'DEL'按钮的动作"""
        if not self.is_error and len(self.exp_stack) != 1:
            self.is_answer = False
            self._remove_elem()
            self._display_exp()

    def _ac_func(self):
        """负责'AC'按钮的动作"""
        if self.is_error:
            # in case an error occurred, only pressing AC button will continue the run
            self.is_error = False
            self.pre_ans = INIT_ANS
        self.is_answer = False
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        self._cur_idx = 0
        self._display_exp()

    def _calc_expression(self):
        """此方法生成表达式，它是一个字符串，包含
         用户输入的当前表达式，计算它的值并返回它。"""
        expression = "".join(elem[0] for elem in self.exp_stack)
        return str(eval(expression))[:MAX_CHARS_NUM]

    def _equals_func(self):
        """负责'='按钮的动作"""
        if not self.is_error:
            try:
                if len(self.exp_stack) != 1:
                    result = self._calc_expression()
                    self._display_var.set(result)
                    self.pre_ans = result
                    self.is_answer = True
            except OverflowError:
                self._display_var.set(STACK_ERROR)
                self.is_error = True
            except (ZeroDivisionError, ValueError):
                self._display_var.set(MATH_ERROR)
                self.is_error = True
            except SyntaxError:
                self._display_var.set(SYNTAX_ERROR)
                self.is_error = True
            finally:
                # initialize expression and cursor position
                self.exp_stack = [(EXP_SEP, DIS_SEP)]
                self._cur_idx = 0