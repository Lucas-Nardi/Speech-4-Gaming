from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
#from Qt_forms.menu_forms2 import Ui_Menu
from Qt_forms.menu_forms3 import Ui_Menu
import os
from Speech_Recognition import voskAPI


class Menu_Screen(QtWidgets.QWidget):

    go_to_Edit = QtCore.pyqtSignal()
    which_game_im_will_use = None
    total_games = 0
    components_to_delete = list()
    play_button_component = list()
    playing = False

    play_icon = QtGui.QIcon()

    stop_playing_icon = QtGui.QIcon()



    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Menu()
        self.ui.setupUi(self)
        # speech_recognition = voskAPI()

        # Take each button that is on scrollArea and add click function

        i = 0
        self.total_games = len(self.ui.which_game)

        for QtWidgets in self.ui.scrollAreaWidgetContents.children():

            children = QtWidgets.children()


            if (len(QtWidgets.children()) > 0):


                delete_button = children[1]
                edit_button = children[2]
                play_button = children[3]
                self.components_to_delete.append(QtWidgets)
                self.play_button_component.append(play_button)

                if (i == 0):

                    delete_button.clicked.connect(lambda: self.delete_game(0, self.components_to_delete[0]))
                    edit_button.clicked.connect(lambda: self.edit(0))
                    play_button.clicked.connect(lambda: self.play(0,self.play_button_component[0]) )
                elif (i == 1):
                    delete_button.clicked.connect(lambda: self.delete_game(1,self.components_to_delete[1]))
                    edit_button.clicked.connect(lambda: self.edit(1))
                    play_button.clicked.connect(lambda: self.play(1,self.play_button_component[1]))
                elif (i == 2):
                    delete_button.clicked.connect(lambda: self.delete_game(2,self.components_to_delete[2]))
                    edit_button.clicked.connect(lambda: self.edit(2))
                    play_button.clicked.connect(lambda: self.play(2,self.play_button_component[2]))
                elif (i == 3):
                    delete_button.clicked.connect(lambda: self.delete_game(3,self.components_to_delete[3]))
                    edit_button.clicked.connect(lambda: self.edit(3))
                    play_button.clicked.connect(lambda: self.play(3,self.play_button_component[3]))
                elif (i == 4):
                    delete_button.clicked.connect(lambda: self.delete_game(4,self.components_to_delete[4]))
                    edit_button.clicked.connect(lambda: self.edit(4))
                    play_button.clicked.connect(lambda: self.play(4,self.play_button_component[4]))
                elif (i == 5):
                    delete_button.clicked.connect(lambda: self.delete_game(5,self.components_to_delete[5]))
                    edit_button.clicked.connect(lambda: self.edit(5))
                    play_button.clicked.connect(lambda: self.play(5,self.play_button_component[5]))
                elif (i == 6):
                    delete_button.clicked.connect(lambda: self.delete_game(6,self.components_to_delete[6]))
                    edit_button.clicked.connect(lambda: self.edit(6))
                    play_button.clicked.connect(lambda: self.play(6,self.play_button_component[6]))
                elif (i == 7):
                    delete_button.clicked.connect(lambda: self.delete_game(7,self.components_to_delete[7]))
                    edit_button.clicked.connect(lambda: self.edit(7))
                    play_button.clicked.connect(lambda: self.play(7,self.play_button_component[7]))
                elif (i == 8):
                    delete_button.clicked.connect(lambda: self.delete_game(8,self.components_to_delete[8]))
                    edit_button.clicked.connect(lambda: self.edit(8))
                    play_button.clicked.connect(lambda: self.play(8,self.play_button_component[8]))
                elif (i == 9):
                    delete_button.clicked.connect(lambda: self.delete_game(9,self.components_to_delete[9]))
                    edit_button.clicked.connect(lambda: self.edit(9))
                    play_button.clicked.connect(lambda: self.play(9,self.play_button_component[9]))

                i = i + 1


        self.ui.instructional_button.clicked.connect(self.instructional)
        self.ui.add_game_Button.clicked.connect(lambda: self.new_game("New Game"))

    def new_game(self,new_game):
        if(self.total_games <10):
            self.which_game_im_will_use = new_game
            self.go_to_Edit.emit()

    def delete_game(self,game_to_delete,component):

        _translate = QtCore.QCoreApplication.translate
        game_name = self.ui.which_game[game_to_delete] # Get the name of the csv file that need to be deleted

        self.total_games = self.total_games - 1
        game_path = "Games/" + game_name

        if (os.path.exists(game_path)):
            os.remove(game_path)

        self.ui.verticalLayout_2.removeWidget(component)
        game_count = str(self.total_games) + "/10"
        self.ui.games_number.setText(_translate("MainWindow", game_count))

        if(self.total_games == 0):
            self.ui.which_game.clear()



    def edit(self,which_game="New Game"):

        if(which_game != "New Game"):

            game_name = self.ui.which_game[which_game]
            self.which_game_im_will_use = game_name

        self.go_to_Edit.emit()

    def play(self,which_game,play_button_component):

        print(play_button_component)
        print(type(play_button_component))

        if(not self.playing): # I will play


            self.playing = True
            self.stop_playing_icon.addPixmap(QtGui.QPixmap("Images/stop_playing_icon.png"), QtGui.QIcon.Normal,QtGui.QIcon.Off)
            play_button_component.setIcon(self.stop_playing_icon)
            play_button_component.setIconSize(QtCore.QSize(70, 70))

            # game_name = self.ui.which_game[which_game]
            # self.which_game_im_will_use = game_name
            # self.speech_recognition.voice_commands(game_name)

        else: # I need to stop the recognition and change the Icon

            self.playing = False
            self.play_icon.addPixmap(QtGui.QPixmap("Images/play_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            play_button_component.setIcon(self.play_icon)
            play_button_component.setIconSize(QtCore.QSize(50, 50))

        #toDo Mudar o icone do play para o quadrado e fazer a função de parar o programa ao clicar 2 vezes

    def instructional(self):
        print("INSTRUÇÃO")
