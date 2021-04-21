# This Python file uses the following encoding: utf-8
import sys
import os

from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QWidget)
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader


class Menu(QWidget):
    def __init__(self):
        super(Menu, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "./Ui files/Menu.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()


if __name__ == "__main__":
    app = QApplication([])
    widget = Menu()
    widget.show()
    sys.exit(app.exec_())
