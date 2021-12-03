from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)
import os

class Ui_Menu(object):

    which_game = []

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(885, 667)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(885, 667))
        icon = QIcon("Speech_4_Gaming.ico")
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setMinimumSize(QSize(885, 667))
        self.centralwidget.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
"QScrollBar:vertical{\n"
"	boder: none;\n"
"	width: 14px;\n"
"	margin: 15px 0 15px 0;\n"
"	border-radius:10px;\n"
"	background-color: rgb(31, 125, 108);\n"
"}\n"
"\n"
"/* HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {\n"
"	border-radius:4px;\n"
"	min-height:15px;\n"
"	background-color: rgb(31, 79, 108);\n"
"}\n"
"\n"
"/* BUTTON TOP - SCROLLBAR*/\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"	border:none;	\n"
"	background-color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-top-left-radius: 5px;\n"
"	border-top-right-radius:5px;\n"
"	subcontrol-position:top;\n"
"	subcontrol-origin: margin;\n"
"	\n"
"}\n"
"\n"
"/* BUTTON BOTTOM - SCROLLBAR*/\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"	border:none;	\n"
"	background-color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-bottom-left-radius: 5px;\n"
"	border-bottom-right-radius:5px;\n"
"	subcontrol-position:bottom;\n"
"	subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* RESET ARROW */\n"
"\n"
"QScrollBar::up-arrow:vertical, QSc"
                        "rollBar::down-arrow:vertical {     \n"
"	 background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
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
"QWidget {\n"
"\n"
"	background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.4 #13547a, stop: 0.8 		  #80d0c7);\n"
"}\n"
"\n"
"\n"
"")
        self.instructional_button = QPushButton(self.centralwidget)
        self.instructional_button.setObjectName("instructional_button")
        self.instructional_button.setGeometry(QRect(791, 80, 61, 51))
        self.instructional_button.setStyleSheet("border:none;\n"
"border-width:0px;\n"
"\n"
"background-color: none;")
        icon = QIcon()
        icon.addFile("image/instructional_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.instructional_button.setIcon(icon)
        self.instructional_button.setIconSize(QSize(53, 54))
        self.instructional_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.games_number = QLabel(self.centralwidget)
        self.games_number.setObjectName("games_number")
        self.games_number.setGeometry(QRect(113, 80, 61, 51))
        font = QFont()
        font.setFamilies(["Berlin Sans FB"])
        font.setPointSize(23)
        self.games_number.setFont(font)
        self.games_number.setStyleSheet("background-color: None;\n"
"color: rgb(255, 255, 255);")
        self.Title_Software = QLabel(self.centralwidget)
        self.Title_Software.setObjectName("Title_Software")
        self.Title_Software.setGeometry(QRect(221, 10, 471, 81))
        font1 = QFont()
        font1.setFamilies(["MS Shell Dlg 2"])
        font1.setPointSize(41)
        self.Title_Software.setFont(font1)
        self.Title_Software.setCursor(QCursor(Qt.PointingHandCursor))
        self.Title_Software.setAutoFillBackground(False)
        self.Title_Software.setStyleSheet("color: rgb(255, 255, 255);\n"
"boder:none;\n"
"background-color: none")
        self.Title_Software.setFrameShape(QFrame.NoFrame)
        self.Title_Software.setFrameShadow(QFrame.Raised)
        self.Title_Software.setLineWidth(0)
        self.Title_Software.setAlignment(Qt.AlignCenter)
        self.add_game_Button = QPushButton(self.centralwidget)
        self.add_game_Button.setObjectName("add_game_Button")
        self.add_game_Button.setGeometry(QRect(41, 80, 61, 51))
        self.add_game_Button.setStyleSheet("background-color: None;\n"
"border:none;\n"
"border-width:0px;\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile("image/add_button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_game_Button.setIcon(icon1)
        self.add_game_Button.setIconSize(QSize(51, 49))
        self.add_game_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(120, 170, 681, 451))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.scrollArea.setStyleSheet("QScrollBar:vertical{\n"
"    background-color:rgb(31, 125, 108);\n"
"}\n"
"\n"
"QScrollArea{\n"
"     background-color: transparent\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 667, 537))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContents.setCursor(QCursor(Qt.PointingHandCursor))
        self.scrollAreaWidgetContents.setStyleSheet("background-color: transparent;")
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 9, 0)


        icon1 = QIcon()
        icon1.addPixmap(QPixmap("image/edit_button.png"), QIcon.Normal, QIcon.Off)
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("image/play_button.png"), QIcon.Normal, QIcon.Off)

        icon4 = QIcon()
        icon4.addPixmap(QPixmap("image/delete_icon.png"), QIcon.Normal, QIcon.Off)

        games_dir = "./games/"  # Enter Directory of all images
        i = 0
        _translate = QCoreApplication.translate

        self.which_game.clear()

        for fl in os.listdir(games_dir):

            if (fl.endswith(".csv")):
                self.which_game.append(fl)

                name = "jogo" + str(i + 1)
                name1 = "game_name" + str(i + 1)
                name2 = "edit_button" + str(i + 1)
                name3 = "play_button" + str(i + 1)
                name4 = "delete_button" + str(i + 1)
                game_name_writting = fl.split(".")

                jogo_background = QWidget(self.scrollAreaWidgetContents)
                sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(jogo_background.sizePolicy().hasHeightForWidth())
                jogo_background.setSizePolicy(sizePolicy)
                jogo_background.setMinimumSize(QSize(655, 67))
                jogo_background.setMaximumSize(QSize(655, 90))
                jogo_background.setCursor(QCursor(Qt.PointingHandCursor))
                jogo_background.setStyleSheet("background-color: rgb(30, 217, 89); border-radius: 15px;")
                jogo_background.setObjectName(name)
                game_name = QLabel(jogo_background)
                game_name.setGeometry(QRect(18, 1, 421, 61))
                sizePolicy = QSizePolicy(QSizePolicy.Preferred,
                                                   QSizePolicy.Preferred)
                sizePolicy.setHorizontalStretch(0)
                sizePolicy.setVerticalStretch(0)
                sizePolicy.setHeightForWidth(game_name.sizePolicy().hasHeightForWidth())
                game_name.setSizePolicy(sizePolicy)
                game_name.setMaximumSize(QSize(500, 90))
                font = QFont()
                font.setFamily("Berlin Sans FB")
                font.setPointSize(32)
                game_name.setFont(font)
                game_name.setCursor(QCursor(Qt.PointingHandCursor))
                game_name.setStyleSheet("color: rgb(255, 255, 255); background-color: transparent")
                game_name.setObjectName(name1)
                game_name.setText(_translate("Menu", game_name_writting[0]))

                delete_button = QPushButton(jogo_background)
                delete_button.setGeometry(QRect(460, 8, 51, 51))
                delete_button.setCursor(QCursor(Qt.PointingHandCursor))
                delete_button.setIcon(icon4)
                delete_button.setIconSize(QSize(50, 50))
                delete_button.setObjectName(name4)
                delete_button.setStyleSheet("background-color: transparent")

                edit_button = QPushButton(jogo_background)
                edit_button.setGeometry(QRect(528, 8, 51, 51))
                edit_button.setCursor(QCursor(Qt.PointingHandCursor))
                edit_button.setIcon(icon1)
                edit_button.setIconSize(QSize(50, 50))
                edit_button.setObjectName(name2)
                edit_button.setStyleSheet("background-color: transparent")

                play_button = QPushButton(jogo_background)
                play_button.setGeometry(QRect(588, 11, 51, 51))
                play_button.setCursor(QCursor(Qt.PointingHandCursor))
                play_button.setIcon(icon2)
                play_button.setIconSize(QSize(50, 50))
                play_button.setObjectName(name3)
                play_button.setStyleSheet("background-color: transparent")

                self.verticalLayout_2.addWidget(jogo_background)
                i = i + 1
        game_count = str(i) + "/10"
        self.games_number.setText(_translate("MainWindow", game_count))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(MainWindow)

        self.instructional_button.setDefault(False)
        self.add_game_Button.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Speech 4 Gaming"))
        self.Title_Software.setText(_translate("MainWindow", "Speech 4 Gaming"))
    # retranslateUi

