import threading

from PySide6 import QtCore, QtWidgets
from qt_forms.instruction_forms import Ui_Instruction

class Instruction_Screen(QtWidgets.QWidget):

    go_to_Menu = QtCore.Signal()

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Instruction()
        self.ui.setupUi(self)

        self.ui.menu_button.clicked.connect(self.menu)

    def menu(self):
        self.go_to_Menu.emit()
