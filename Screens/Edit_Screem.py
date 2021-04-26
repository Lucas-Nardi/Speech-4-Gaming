import PyQt5
from PyQt5 import QtCore, QtWidgets,QtGui
from Qt_forms.edit_game_forms2 import Ui_Edit
import os
import threading
import time

class EditScreen(QtWidgets.QWidget):

    go_to_Menu = QtCore.pyqtSignal()
    file_data = []
    repeated_commands = None

    def __init__(self, game_commands_file_name):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Edit()
        self.ui.setupUi(self)

        if(game_commands_file_name != "New Game"):  # Need to create a new game

            # Currect Directory = ../Speech 4 Gaming/
            self.fill_Screen(game_commands_file_name)


        self.repeated_commands = [False] * len(self.ui.scrollAreaWidgetContents.children())

        #  threading.Thread(target=self.apply_changes(game_commands_file_name) ).start()
        self.ui.apply_button.clicked.connect(lambda:self.apply_changes(game_commands_file_name))
        self.ui.menu_button.clicked.connect(self.back_to_menu)


    def error_message(self, repeated_command):

        print("ERROR MESSAGE")

        _translate = QtCore.QCoreApplication.translate

        error_warning = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents2)
        error_warning.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(error_warning.sizePolicy().hasHeightForWidth())
        error_warning.setSizePolicy(sizePolicy)
        error_warning.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(17)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        error_warning.setFont(font)
        error_warning.setMouseTracking(False)
        error_warning.setStyleSheet("background-color: rgb(255, 55, 48);\n" "color: rgb(255, 255, 255);")
        error_warning.setInputMethodHints(QtCore.Qt.ImhLowercaseOnly)
        error_warning.setAlignment(QtCore.Qt.AlignCenter)
        error_warning.setObjectName("error_warning")
        error_warning.setText(_translate("Menu", repeated_command))
        self.ui.verticalLayout_4.addWidget(error_warning)

    def apply_changes(self, game_path):

        self.file_data.clear()

        errors = list()

        for QtWidgets in self.ui.scrollAreaWidgetContents2.children():

            if(type(QtWidgets) == PyQt5.QtWidgets.QLabel):
                errors.append(QtWidgets)

        for x in range(len(errors)):

            com = errors.pop(0)
            self.ui.verticalLayout_2.removeWidget(com)
            print("--------------------------------------------------------")


        file_data = "Command 1,Command 2,key,Press key\n"
        self.file_data.append(file_data)
        exist_commands = list()
        file_data = ""
        commands_number = len(self.ui.scrollAreaWidgetContents.children())
        which_command_im_in = 1
        command_1_repeated = False

        for QtWidgets in self.ui.scrollAreaWidgetContents.children():

            children = QtWidgets.children()

            if (len(QtWidgets.children()) > 0):

                commands_ui = children[0]
                key_ui = children[1]
                check_box_ui = children[2]

                commands = commands_ui.text()
                commands = str(commands)
                commands = commands.lower()

                if (commands.find("/") != -1):  # Has more the one command

                    commad = commands.split("/")

                    if (not commad[0] in exist_commands):  # This command 1  is unique

                        exist_commands.append(commad[0])
                        file_data = commad[0] + ","
                        if(self.repeated_commands[which_command_im_in] == True):

                            self.command_1_repeated = False
                            self.repeated_commands[which_command_im_in] = False
                            commands_ui.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')

                    else: # command 1 already exist

                        file_data = commad[0] + ","
                        commands_ui.setStyleSheet('background-color: rgb(255, 55, 48); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')
                        self.repeated_commands[which_command_im_in] = True
                        self.error_message(commad[0])
                        command_1_repeated = True

                    if (not commad[1] in exist_commands):  # This command 2 is unique

                        exist_commands.append(commad[1])

                        if(which_command_im_in == 9):  # Space key
                            file_data = file_data + commad[1] + ",Space,"
                        elif(which_command_im_in == 11): # Shift key
                            file_data = file_data + commad[1] + ",Shift,"
                        else:
                            file_data = file_data + commad[1] + "," + key_ui.text() + ","

                        if (command_1_repeated == False and self.repeated_commands[which_command_im_in] == True):

                            self.repeated_commands[which_command_im_in] = False
                            commands_ui.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')

                    else: # command 2 already exist

                        if (which_command_im_in == 9):  # Space key
                            file_data = file_data + commad[1] + ",Space,"
                        elif (which_command_im_in == 11):  # Shift key
                            file_data = file_data + commad[1] + ",Shift,"
                        else:
                            file_data = file_data + commad[1] + "," + key_ui.text() + ","


                        commands_ui.setStyleSheet('background-color: rgb(255, 55, 48); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')
                        self.repeated_commands[which_command_im_in] = True
                        self.error_message(commad[1])

                else: # There is only 1 command

                    if (len(commands) > 0 and not commands.isspace()):  # This command is not a space character

                        if (not commands in exist_commands):  # This command  is unique

                            exist_commands.append(commands)

                            if (which_command_im_in == 9):  # Space key
                                file_data = commands + ",-,Space,"
                            elif (which_command_im_in == 11):  # Shift key
                                file_data = commands + ",-,Shift,"
                            else:
                                file_data = commands + ",-," + key_ui.text() + ","

                            if (self.repeated_commands[which_command_im_in] == True):

                                self.repeated_commands[which_command_im_in] = False
                                commands_ui.setStyleSheet('background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')

                        else: # This command already exist

                            if (which_command_im_in == 9):  # Space key
                                file_data = commands + ",-,Space,"
                            elif (which_command_im_in == 11):  # Shift key
                                file_data = commands + ",-,Shift,"
                            else:
                                file_data = commands + ",-," + key_ui.text() + ","

                            commands_ui.setStyleSheet('background-color: rgb(255, 55, 48); color: rgb(0, 0, 0); border-style: solid; border-width: 2px; border-color: black;')
                            self.repeated_commands[which_command_im_in] = True
                            self.error_message(commands)

                    else: # This command is a space character

                        if (which_command_im_in == 9):  # Space key
                            file_data = "-,-," + "Space,"
                        elif (which_command_im_in == 11):  # Shift key
                            file_data = "-,-," + "Shift,"
                        else:
                            file_data = "-,-," + key_ui.text() + ","

                        check_box_ui.setChecked(False)
                        self.repeated_commands[which_command_im_in] = False

                if (check_box_ui.isChecked()):

                    if ((commands_number - 1) == which_command_im_in):
                        file_data = file_data + "yes"
                    else:
                        file_data = file_data + "yes\n"
                else:
                    if ((commands_number - 1) == which_command_im_in):  # last command do not need \n
                        file_data = file_data + "no"
                    else:
                        file_data = file_data + "no\n"

                self.file_data.append(file_data)
                which_command_im_in = which_command_im_in + 1

        self.save_changes_on_File(game_path)

    def save_changes_on_File(self,game_path):

        if( not True in self.repeated_commands):  # Não tem nehum comando repetido

            game_name = game_path.split(".")
            game_commands_file_path = "Games/" + self.ui.game_name_area.text() + ".csv"
            game_commands_file = open(game_commands_file_path, "w+")
            print(game_commands_file_path)

            for line in self.file_data:
                print(line)
                game_commands_file.write(line)

            game_commands_file.close()

            if (os.path.exists(game_commands_file_path) and game_name[0] != self.ui.game_name_area.text()):  # The game name changed

                original_path = "Games/" + game_path
                os.remove(original_path)

    def fill_Screen(self, game_path):

        game_name = game_path.split(".")
        game_commands_file_path = "Games/" + game_path
        exist_file = os.path.exists(game_commands_file_path)

        if (exist_file):
            _translate = QtCore.QCoreApplication.translate
            self.ui.game_name_area.setText(_translate("Menu", game_name[0]))

            game_commands_file = open(game_commands_file_path, "r")
            data = game_commands_file.readline()  # read the columns names

        for QtWidgets in self.ui.scrollAreaWidgetContents.children():

            children = QtWidgets.children()

            if (len(QtWidgets.children()) > 0):

                commands_ui = children[0]
                check_box_ui = children[2]

                commands = game_commands_file.readline()

                data = commands.split(",")
                command1 = data[0]
                command2 = data[1]
                check_box = data[3]

                command = ""

                if (command1 != "-" and command2 != "-"):
                    command = command1 + "/" + command2
                elif (command1 != "-" and command2 == "-"):
                    command = command1
                elif (command1 == "-" and command2 != "-"):
                    command = command2

                commands_ui.setText(_translate("Menu", command))

                if (check_box == "yes\n" or check_box == "yes"):
                    check_box_ui.setChecked(True)

        game_commands_file.close()

    def back_to_menu(self):
        self.go_to_Menu.emit()