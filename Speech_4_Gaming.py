import sys

from Screens.Menu import Menu_Screen
from Screens.Edit_Screem import EditScreen
from Screens.Instruction_Screen import Instruction_Screen
from PyQt5 import QtWidgets
import threading



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

        self.Menu.go_to_Edit.connect(lambda: self.show_edit_screen(self.Menu.which_game_i_will_use))
        self.Menu.go_to_Instruction.connect(lambda: self.show_instruction())
        threading.Thread(target=self.Menu.show()).start()

    def show_edit_screen(self,game_commands=None):

        self.edit = EditScreen(game_commands)

        if (self.Menu != None and self.Menu.isVisible()):
            self.Menu.close()

        self.edit.go_to_Menu.connect(self.show_menu)
        self.edit.show()

    def show_instruction(self):

        self.instruction = Instruction_Screen()

        if (self.Menu != None and self.Menu.isVisible()):
            self.Menu.close()

        self.instruction.go_to_Menu.connect(self.show_menu)
        self.instruction.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    threading.Thread(target=controller.show_menu()).start()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()