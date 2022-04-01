##########
# 项目名称：Tri-Func-Calculator-CQU
# 最终版本：Tri-Func-Calculator-CQU
# 修订时间：2022年4月1日
# 小组成员：林康志、杜建建、钟豪、朱思宁、戚俊
# 程序说明: 计算器功能和GUI实现。
##########

from tkinter import *
from functools import partial
from my_button import *
from sin import sin
from cos import cos
from tan import tan
from asin import asin
from acos import acos
from atan import atan

class Calculator:
    """The gui of the calculator. The gui made of a rectangle screen, buttons,
    and a display banner that presents the current expression."""
    arithmetic = {POW: OP_POW, POW_3: OP_POW_3, POW_2: OP_POW_2,
                  DIVIDE: OP_DIVIDE, MUL: OP_MUL, PLUS: PLUS, MINUS: MINUS}
    extra_functions = {SQRT: OP_SQRT, SIN: OP_SIN, COS: OP_COS, TAN: OP_TAN, ASIN: OP_ASIN,
                       ACOS: OP_ACOS, ATAN: OP_ATAN}
    powers = {POW_2: POW_2_DIS, POW_3: POW_3_DIS, POW: POW_DIS}
    rounding = {L_FLOOR: OP_L_FLOOR, R_FLOOR: OP_R_FLOOR, L_CEIL: OP_L_CEIL,
                R_CEIL: OP_R_CEIL}
    # The buttons of the calculator. Each button is represented as a tuple,
    # in the following format: (<display_name>, <button_type>)
    # The buttons types can be found in constants.py
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
        """The constructor of the gui."""
        self.screen = tk.Tk()
        # A list representing the current expression typed by the user.
        # Each element of the list is a tuple, in the format (<expression>, <display>):
        # expression is the actual operand calculated by python
        # and display is the representation of the expression on the display banner.
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        # The previous answer calculated by the computer
        self.pre_ans = INIT_ANS
        # Boolean indicates if an error raised by the calculator.
        self.is_error = False
        # Boolean indicates that equals button has been pressed.
        self.is_answer = False
        # The current index of the cursor
        self._cur_idx = 0
        self._display_var = StringVar()
        self._init_screen()

    def _init_screen(self):
        """This method responsible for setting up the calculator screen."""
        self._set_background()
        self._set_labels()
        self._set_buttons()
        self._set_display_banner()
        self._display_exp()
        # Starting cursor action
        self.screen.after(CURSOR_BLINK, self._set_cursor)

    def _set_background(self):
        """Setting up the back of the screen, it's title, size and color."""
        self.screen.title(TITLE)
        self.screen.geometry(SCREEN_SIZE)
        self.screen.resizable(width=False, height=False)
        self.screen.configure(background=S_COLOR)

    def _set_labels(self):
        """Setting up the labels on the screen."""
        self.gen_label(NAME_S, NAME_T, NAME_FG, NAME_SIZE, NAME_LOC)
        self.gen_label(COMP_S, COMP_T, COMP_FG, COMP_SIZE, COMP_LOC)
        self.gen_label(MOD_S, MOD_T, MOD_FG, MOD_SIZE, MOD_LOC)

    def gen_label(self, text_size, text, fg, size, loc):
        """A helper function to set_labels, sets the given label on the screen"""
        label_font = font.Font(family=FONT, size=text_size, weight=font.BOLD)
        label = tk.Label(self.screen, text=text, bg=S_COLOR, font=label_font, fg=fg)
        label.pack()
        label.place(height=size[0], width=size[1], x=loc[0], y=loc[1])

    def _set_display_banner(self):
        """Setting up the display banner and place it on the screen"""
        display_font = font.Font(family=FONT, size=D_F_SIZE)
        display = Entry(self.screen, textvariable=self._display_var, bd=BORDER_SIZE,
                        bg=DISPLAY_BG, font=display_font, fg=DISPLAY_FG)
        display.pack()
        display.place(height=DISPLAY_H, width=DISPLAY_W, x=DISPLAY_X, y=DISPLAY_Y)

    def _set_cursor(self):
        """This method responsible for the cursor animation.
        every CURSOR_BLINK seconds this method will be called and switch the current
        cursor representation (from '|' to '')"""
        if not self.is_answer and not self.is_error:
            cursor = self.exp_stack[self._cur_idx]
            blink = [DIS_SEP, ""]
            self.exp_stack[self._cur_idx] = (EXP_SEP, blink[1 - blink.index(cursor[1])])
            self._display_exp()
        self.screen.after(CURSOR_BLINK, self._set_cursor)

    def _set_buttons(self):
        """This method responsible for the placement of the buttons on the screen"""
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
        """Given a grid size (rows,cols), this method place the buttons from
        self.buttons matrix at (i,j) index, on the desired location on the screen
        according to (x,y) parameters."""
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
        """Gets a button display name (key), and returns the function this button should
        execute."""
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
        """Given a button's key and type, the factory creates the relevant button object
        then placed it on the screen using 'create' shareable method."""
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
        """This method generates cur_display, which is a string that contains the
        display representation of the current expression the user typed. Then placed
        it in the display banner."""
        cur_display = "".join(elem[1] for elem in self.exp_stack)
        self._display_var.set(cur_display)

    def _add_elem(self, exp_elem, dis_elem):
        """
        Adds new element to the current expression array.
        :param exp_elem: The actual expression python execute.
        :param dis_elem: The representation of the expression on the display banner.
        """
        self.exp_stack = self.exp_stack[:self._cur_idx] + [(exp_elem, dis_elem)] \
                         + [(EXP_SEP, DIS_SEP)] + self.exp_stack[self._cur_idx + 1:]
        self._cur_idx += 1

    def _remove_elem(self):
        """Removes an element according to the cursor position. The element that is
        before the cursor will be deleted."""
        self.exp_stack = self.exp_stack[:self._cur_idx - 1] + self.exp_stack[self._cur_idx:]
        self._cur_idx -= 1

    # def print_exp(self):
    #     exp = "".join(elem[0] for elem in self.exp_stack)
    #     dis = "".join(elem[1] for elem in self.exp_stack)
    #     print("Exp: ", exp, "\t", "Dis: ", dis)

    def get_exp(self, key):
        """Gets a string which appears on a button and return the expression this key
        represent."""
        if key in self.arithmetic:
            return self.arithmetic.get(key)
        elif key in self.extra_functions:
            return self.extra_functions.get(key)
        elif key in self.rounding:
            return self.rounding.get(key)
        return key

    def get_dis(self, key):
        """Gets a string which appears on a button and return the display name of this
        key, as appears in the display banner"""
        if key in self.extra_functions:
            return key + L_PAR
        elif key in self.powers:
            return self.powers.get(key)
        else:
            return key

    def _arrow_func(self, direction):
        """This method responsible for the action of the arrows keys."""
        if not self.is_error and \
                not ((direction == L and self._cur_idx == 0) or
                     (direction == R and self._cur_idx == len(self.exp_stack) - 1)):
            self.is_answer = False
            self.exp_stack[self._cur_idx] = self.exp_stack[self._cur_idx + direction]
            self.exp_stack[self._cur_idx + direction] = (EXP_SEP, DIS_SEP)
            self._display_exp()
            self._cur_idx += direction

    def _check_power(self):
        """In actual scientific calculator, one can place only one power char after
        some number. This method returns True in case the user tries to put power element
        in a sequence."""
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
        """This method responsible for the action of most buttons, except for special
        buttons which are: AC,DEL,Ans,Arrows and equals."""
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
        """This method responsible for the action of 'Ans' button"""
        if not self.is_error:
            self.is_answer = False
            if self.pre_ans == INIT_ANS:
                # in case there is no pre answer, and however the user try using it:
                self.pre_ans = "0"
            self._add_elem(self.pre_ans, ANS)
            self._display_exp()

    def _del_func(self):
        """This method responsible for the action of 'DEL' button"""
        if not self.is_error and len(self.exp_stack) != 1:
            self.is_answer = False
            self._remove_elem()
            self._display_exp()

    def _ac_func(self):
        """This method responsible for the action of 'AC' button"""
        if self.is_error:
            # in case an error occurred, only pressing AC button will continue the run
            self.is_error = False
            self.pre_ans = INIT_ANS
        self.is_answer = False
        self.exp_stack = [(EXP_SEP, DIS_SEP)]
        self._cur_idx = 0
        self._display_exp()

    def _calc_expression(self):
        """This method generates expression, which is a string that contains the
        current expression the user typed, calculates it's value and returns it."""
        expression = "".join(elem[0] for elem in self.exp_stack)
        return str(eval(expression))[:MAX_CHARS_NUM]

    def _equals_func(self):
        """This method responsible for the action of '=' button"""
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
