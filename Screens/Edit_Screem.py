from PyQt5 import QtGui
from PyQt5 import QtCore, QtWidgets
from Qt_forms.edit_game_forms import Ui_Edit


class EditScreen(QtWidgets.QWidget):

    go_to_Menu = QtCore.pyqtSignal()

    def __init__(self, game_commands=None):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edit()
        self.ui.setupUi(self)
        if(game_commands != None):
            print("ESTOU NA TELA DE EDIÇÃO PORRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print(game_commands)

        self.ui.menu_button.clicked.connect(self.back_to_menu)


    def back_to_menu(self):
        self.go_to_Menu.emit()

    def exit(self):
        print("Mudar de tela")