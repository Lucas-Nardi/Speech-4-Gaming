# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Menu2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Menu(object):

    which_game = []

    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.setWindowModality(QtCore.Qt.ApplicationModal)
        Menu.resize(885, 667)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(49)
        Menu.setFont(font)
        Menu.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        Menu.setAutoFillBackground(False)
        Menu.setStyleSheet("QWidget {    \n"
"     background-color: rgb(26, 65, 90); \n"
"    \n"
"}\n"
"/*\n"
"\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.4 #13547a, stop: 0.8 #80d0c7);\n"
"    \n"
"\n"
"*/\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.Title_Software = QtWidgets.QLabel(Menu)
        self.Title_Software.setGeometry(QtCore.QRect(220, 10, 471, 81))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(41)
        self.Title_Software.setFont(font)
        self.Title_Software.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Title_Software.setAutoFillBackground(False)
        self.Title_Software.setStyleSheet("color: rgb(255, 255, 255);\n"
"boder:none;\n"
"background-color: none")
        self.Title_Software.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Title_Software.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title_Software.setLineWidth(0)
        self.Title_Software.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_Software.setObjectName("Title_Software")
        self.add_game_Button = QtWidgets.QPushButton(Menu)
        self.add_game_Button.setGeometry(QtCore.QRect(40, 80, 61, 51))
        self.add_game_Button.setStyleSheet("background-color: None;\n"
"border:none;\n"
"border-width:0px;\n"
"\n"
"")
        self.add_game_Button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Images/add_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_game_Button.setIcon(icon)
        self.add_game_Button.setIconSize(QtCore.QSize(51, 49))
        self.add_game_Button.setDefault(False)
        self.add_game_Button.setObjectName("add_game_Button")
        self.frame = QtWidgets.QFrame(Menu)
        self.frame.setEnabled(True)
        self.frame.setGeometry(QtCore.QRect(120, 175, 681, 451))
        self.frame.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
"QScrollBar:vertical{\n"
"    boder: none;\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius:10px;\n"
"    background-color: rgb(31, 125, 108);\n"
"}\n"
"\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"    border-radius:4px;\n"
"    min-height:15px;\n"
"    background-color: rgb(31, 79, 108);\n"
"}\n"
"\n"
"/* BUTTON TOP - SCROLLBAR*/\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    border:none;    \n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius:5px;\n"
"    subcontrol-position:top;\n"
"    subcontrol-origin: margin;\n"
"    \n"
"}\n"
"\n"
"\n"
"\n"
"/* BUTTON BOTTOM - SCROLLBAR*/\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    border:none;    \n"
"    background-color: rgb(255, 255, 255);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius:5px;\n"
"    subcontrol-position:bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"\n"
"\n"
"/* RESET ARROW */\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     \n"
"     background: none;\n"
"}\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical {\n"
"background: none;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(0)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(-1, 0, 681, 451))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollArea.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
"QScrollBar:vertical{\n"
"    background-color: rgb(31, 125, 108);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 690, 77))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        self.scrollAreaWidgetContents.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setContentsMargins(0, 10, 9, 0)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Images/edit_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Images/play_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        games_dir = "./Games/"  # Enter Directory of all images
        i = 0
        _translate = QtCore.QCoreApplication.translate

        self.which_game.clear()

        for fl in os.listdir(games_dir):

                if (fl.endswith(".csv")):

                        self.which_game.append(fl)

                        name = "jogo" + str(i + 1)
                        name1 = "game_name" + str(i + 1)
                        name2 = "edit_button" + str(i + 1)
                        name3 = "play_button" + str(i + 1)
                        game_name_writting = fl.split(".")

                        jogo_background = QtWidgets.QWidget(self.scrollAreaWidgetContents)
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(jogo_background.sizePolicy().hasHeightForWidth())
                        jogo_background.setSizePolicy(sizePolicy)
                        jogo_background.setMinimumSize(QtCore.QSize(681, 67))
                        jogo_background.setMaximumSize(QtCore.QSize(16777215, 90))
                        jogo_background.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        jogo_background.setStyleSheet("background-color: rgb(30, 217, 89);\n"
                                                      "border-radius:15px;")
                        jogo_background.setObjectName(name)
                        game_name = QtWidgets.QLabel(jogo_background)
                        game_name.setGeometry(QtCore.QRect(18, 1, 500, 61))
                        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                                           QtWidgets.QSizePolicy.Preferred)
                        sizePolicy.setHorizontalStretch(0)
                        sizePolicy.setVerticalStretch(0)
                        sizePolicy.setHeightForWidth(game_name.sizePolicy().hasHeightForWidth())
                        game_name.setSizePolicy(sizePolicy)
                        game_name.setMaximumSize(QtCore.QSize(500, 90))
                        font = QtGui.QFont()
                        font.setFamily("Berlin Sans FB")
                        font.setPointSize(36)
                        game_name.setFont(font)
                        game_name.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                        game_name.setStyleSheet("color: rgb(255, 255, 255);")
                        game_name.setObjectName(name1)
                        game_name.setText(_translate("Menu", game_name_writting[0]))

                        edit_button = QtWidgets.QPushButton(jogo_background)
                        edit_button.setGeometry(QtCore.QRect(520, 8, 51, 51))
                        edit_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                        edit_button.setText("")
                        edit_button.setIcon(icon1)
                        edit_button.setIconSize(QtCore.QSize(50, 50))
                        edit_button.setObjectName(name2)

                        play_button = QtWidgets.QPushButton(jogo_background)
                        play_button.setGeometry(QtCore.QRect(588, 11, 51, 51))
                        play_button.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
                        play_button.setText("")
                        play_button.setIcon(icon2)
                        play_button.setIconSize(QtCore.QSize(50, 50))
                        play_button.setObjectName(name3)

                        self.verticalLayout_2.addWidget(jogo_background)
                        i = i + 1





        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.instructional_button = QtWidgets.QPushButton(Menu)
        self.instructional_button.setGeometry(QtCore.QRect(790, 80, 61, 51))
        self.instructional_button.setStyleSheet("border:none;\n"
"border-width:0px;\n"
"\n"
"background-color: none;")
        self.instructional_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Images/instructional_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.instructional_button.setIcon(icon3)
        self.instructional_button.setIconSize(QtCore.QSize(53, 54))
        self.instructional_button.setDefault(False)
        self.instructional_button.setObjectName("instructional_button")
        self.games_number = QtWidgets.QLabel(Menu)
        self.games_number.setGeometry(QtCore.QRect(112, 80, 61, 51))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(23)
        self.games_number.setFont(font)
        self.games_number.setStyleSheet("background-color: None;\n"
"color: rgb(255, 255, 255);")
        self.games_number.setObjectName("games_number")

        total_games = str(i) + "/10"
        self.games_number.setText(_translate("Menu", total_games))
        self.frame.raise_()
        self.Title_Software.raise_()
        self.add_game_Button.raise_()
        self.instructional_button.raise_()
        self.games_number.raise_()

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.Title_Software.setText(_translate("Menu", "Speech 4 Gaming"))



