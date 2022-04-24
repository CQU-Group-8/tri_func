# ##################################
# #界面设计第二版
# 成员：杨欣，胡邦涛，钟轶伟，卢静雯，刘子钰
# ###################################
import sys
import math
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QComboBox, QHBoxLayout, QVBoxLayout, QPushButton, \
    QLineEdit, QLabel
from sin import *
from cos import *
from tan import *
from asin import *
from acos import *
from atan import *

class Interface_method:

    def sin(self, value):   #调用sin计算公式mySin
        return sin(value)
        # return math.sin(value)

    def arcsin(self, value): #调用arcsin计算公式asin
        return asin(value)
        # return math.asin(value)

    def cos(self, value):  #调用cos计算公式myCos
        return cos(value)
        # return math.cos(value)
    def arccos(self, value):  #调用acos计算公式
        return acos(value)

    def tan(self, value):  #调用tan计算公式
        return tan(value)

    def arctan(self, value):   #调用arctan计算公式atan
        return atan(value)
        # return math.atan(value)

    def get_func_name(self):
        return sorted(self.valueFunctions.keys())

###################选择功能############################
    def get_func_result(self, name, value, isdeg):
        if isdeg == True:
            if "arc" in name:
                return math.degrees(self.valueFunctions[name](value))
            else:
                return self.valueFunctions[name](math.radians(value))
        else:
            return self.valueFunctions[name](value)

####################-选择计算功能-#######################
    def __init__(self):
        self.valueFunctions = {
            'sin': self.sin,
            'arcsin': self.arcsin,
            'cos': self.cos,
            'arccos': self.arccos,
            'tan': self.tan,
            'arctan': self.arctan,
        }

###################-界面设计-#########################
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.method = Interface_method()
        self.initUI()

    def initUI(self):
        # adaptive screen resolution
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()
        self.setFixedSize(int(self.width * 0.2), int(self.width * 0.2 * 0.3))

        self.center()
        self.setWindowTitle('计算器')

        self.btn_Calc = QPushButton('计算', self)
        self.btn_Calc.clicked.connect(self.btn_Calc_on_click)

        self.cb_method = QComboBox(self)
        self.cb_method.addItems(self.method.get_func_name())
        self.cb_method.currentIndexChanged.connect(self.cb_method_changed)

        self.btn_format_input = QPushButton('deg', self)
       # self.btn_format_input.clicked.connect(self.btn_format_on_click)
        self.btn_format_input.setEnabled(True)

        #self.btn_format_output = QPushButton('deg', self)
        self.btn_format_output = QPushButton('deg', self)
        #self.btn_format_output.clicked.connect(self.btn_format_on_click) #点击更换

        self.qle_input = QLineEdit(self)
        self.qle_input.textEdited.connect(self.input_format_check)
        self.qle_input.returnPressed.connect(self.btn_Calc_on_click)

        self.qle_output = QLineEdit(self)
        self.qle_output.setFocusPolicy(Qt.NoFocus)

        self.qlb_result = QLabel('result', self)

        self.hbox_input = QHBoxLayout()
        self.hbox_output = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.hbox_input.addWidget(self.cb_method, 1)
        self.hbox_input.addWidget(self.qle_input, 4)
        self.hbox_input.addWidget(self.btn_format_input, 1)

        self.hbox_output.addWidget(self.qlb_result, 1, Qt.AlignCenter)
        self.hbox_output.addWidget(self.qle_output, 4)
        self.hbox_output.addWidget(self.btn_format_output, 1)

        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_output)
        self.vbox.addWidget(self.btn_Calc)
        # vbox.setContentsMargins(0,0,0,0)
        self.setLayout(self.vbox)
        self.show()

    # set window location at the center of screen
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
######################-输入数据检查格式-##############################
    def input_format_check(self):
        try:
            str_input = self.qle_input.text().strip();
            self.method.get_func_result(self.cb_method.currentText(), float(eval(str_input)),
                                        self.btn_format_input.text() == "red" and self.btn_format_input.isEnabled()
                                        or self.btn_format_output.text() == "red" and self.btn_format_output.isEnabled())
        except:
            self.qle_input.setStyleSheet("color: red;")
            self.btn_Calc.setEnabled(False)
        else:
            self.qle_input.setStyleSheet("color: black;")
            self.btn_Calc.setEnabled(True)

    flag = 0
    ###################-输入输出格式选择-######################
    def cb_method_changed(self):
        if "arc" in self.cb_method.currentText(): #反三角函数，输出可选择格式，输入不可
            self.btn_format_input.setEnabled(False)
            self.btn_format_output.setEnabled(True)
            # self.flag = 0
        else:                                      #输入可选择格式，输出不可
            self.btn_format_input.setEnabled(True)
            self.btn_format_output.setEnabled(False)
            # self.flag = 1
        self.input_format_check()

    def btn_format_on_click(self):
        sender = self.sender()
        text = sender.text()
        sender.setText("deg" if text == "red" else "red")
##################-计算结果-###########################
    def btn_Calc_on_click(self):
        str_input = self.qle_input.text().strip();
        if (str_input == ''):
            return
        try:
            self.qle_output.setText(
                str(self.method.get_func_result(self.cb_method.currentText(), float(eval(str_input)),
                                                self.btn_format_input.text() == "red" and self.btn_format_input.isEnabled()
                                                or self.btn_format_output.text() == "red" and self.btn_format_output.isEnabled())))
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
