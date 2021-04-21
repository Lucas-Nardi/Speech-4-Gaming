from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
from Qt_forms.menu_forms import Ui_Menu


class Menu_Screen(QtWidgets.QWidget):

    go_to_Edit = QtCore.pyqtSignal()

    which_game = None

    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)

        # Take each button that is on scrollArea and add click function

        i = 0

        for QtWidgets in self.ui.scrollAreaWidgetContents.children():

            children = QtWidgets.children()

            if (len(QtWidgets.children()) > 0):
                edit_button = children[1]
                play_button = children[2]

                if (i == 0):
                    edit_button.clicked.connect(lambda: self.edit(0))
                    play_button.clicked.connect(lambda: self.play(0))
                elif (i == 1):
                    edit_button.clicked.connect(lambda: self.edit(1))
                    play_button.clicked.connect(lambda: self.play(1))
                elif (i == 2):
                    edit_button.clicked.connect(lambda: self.edit(2))
                    play_button.clicked.connect(lambda: self.play(2))
                elif (i == 3):
                    edit_button.clicked.connect(lambda: self.edit(3))
                    play_button.clicked.connect(lambda: self.play(3))
                elif (i == 4):
                    edit_button.clicked.connect(lambda: self.edit(4))
                    play_button.clicked.connect(lambda: self.play(4))
                elif (i == 5):
                    edit_button.clicked.connect(lambda: self.edit(5))
                    play_button.clicked.connect(lambda: self.play(5))
                elif (i == 6):
                    edit_button.clicked.connect(lambda: self.edit(6))
                    play_button.clicked.connect(lambda: self.play(6))
                elif (i == 7):
                    edit_button.clicked.connect(lambda: self.edit(7))
                    play_button.clicked.connect(lambda: self.play(7))
                elif (i == 8):
                    edit_button.clicked.connect(lambda: self.edit(8))
                    play_button.clicked.connect(lambda: self.play(8))
                elif (i == 9):
                    edit_button.clicked.connect(lambda: self.edit(9))
                    play_button.clicked.connect(lambda: self.play(9))

                i = i + 1



        self.ui.instructional_button.clicked.connect(self.instructional)
        self.ui.add_game_Button.clicked.connect(lambda: self.edit())


    def edit(self,which_game="Novo Game"):
        print("EDITANDO")

        if(which_game != "Novo Game"):
            game_name = self.ui.which_game[which_game]
            self.which_game = game_name
        else:
            print("CRIANDO UM NOVO GAME")
        self.go_to_Edit.emit()

    def play(self,which_game):
        print("JOGANDO")
        game_name = self.ui.which_game[which_game]
        self.which_game = game_name
        print(game_name)

    def instructional(self):
        print("INSTRUÇÃO")
