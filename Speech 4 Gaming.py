import sys

from Screens.Menu import Menu_Screen
from Screens.Edit_Screem import EditScreen

from PyQt5 import QtWidgets


# from Screens.Telaedition import Telaedition

class Controller:

    def __init__(self):
        self.Menu = None
        self.edit = None
        self.instruction = None

    def show_menu(self):
        self.Menu = Menu_Screen()

        if (self.edit != None and self.edit.isVisible()):
            self.edit.close()

        if (self.instruction != None and self.instruction.isVisible()):
            self.instruction.close()

        self.Menu.go_to_Edit.connect(lambda: self.show_edit_screen(self.Menu.which_game))
        # self.Menu.exitScreen.connect(self.exit)
        self.Menu.show()

    def show_edit_screen(self,game_commands=None):

        self.edit = EditScreen(game_commands)

        if (self.Menu != None and self.Menu.isVisible()):
            self.Menu.close()

        self.edit.go_to_Menu.connect(self.show_menu)
        self.edit.show()

    # def show_instruction(self):
    #   self.edition = Telaedition()
    #  self.edition.voltando.connect(self.show_paint_screen)
    # self.edition.initialScreen.connect(self.show_initial)
    # self.paint.close()
    # self.edition.show()

    def exit(self):
        if (self.initial != None and self.initial.isVisible()):
            self.initial.close()
            sys.exit()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_menu()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()