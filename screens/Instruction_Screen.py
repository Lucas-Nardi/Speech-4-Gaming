import threading

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from qt_forms.instruction_forms import Ui_Instruction
import os
from Speech_Recognition import voskAPI


class Instruction_Screen(QtWidgets.QWidget):

    go_to_Menu = QtCore.pyqtSignal()

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Instruction()
        self.ui.setupUi(self)

        self.ui.menu_button.clicked.connect(self.menu)

    def menu(self):
        self.go_to_Menu.emit()
