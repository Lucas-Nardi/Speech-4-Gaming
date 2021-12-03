from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QCursor,QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Edit(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName("Menu")
        Menu.setWindowModality(Qt.NonModal)
        Menu.resize(885, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMaximumSize(QSize(885, 667))
        font = QFont()
        font.setFamilies(["Berlin Sans FB"])
        font.setPointSize(53)
        Menu.setFont(font)
        Menu.setCursor(QCursor(Qt.ArrowCursor))
        Menu.setAutoFillBackground(False)
        Menu.setStyleSheet("QWidget {	\n"
"\n"
"	\n"
"	background-color: rgb(26, 65, 90);\n"
"\n"
"}\n"
"/*\n"
"\n"
"background-image: linear-gradient(15deg, #13547a 0%, #80d0c7 100%);\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #13547a, stop: .5 #80d0c7);\n"
"background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.4 #13547a, stop: 0.8 #80d0c7);\n"
"			\n"
"\n"
"*/\n"
"\n"
"/* background-color: rgb(26, 65, 90); */\n"
"\n"
"\n"
"")
        self.Title_Screen = QLabel(Menu)
        self.Title_Screen.setObjectName("Title_Screen")
        self.Title_Screen.setGeometry(QRect(220, 0, 461, 61))
        font1 = QFont()
        font1.setFamilies(["Leelawadee"])
        font1.setPointSize(32)
        self.Title_Screen.setFont(font1)
        self.Title_Screen.setCursor(QCursor(Qt.PointingHandCursor))
        self.Title_Screen.setAutoFillBackground(False)
        self.Title_Screen.setStyleSheet("color: rgb(255, 255, 255);\n"
"boder:none;")
        self.Title_Screen.setFrameShape(QFrame.NoFrame)
        self.Title_Screen.setFrameShadow(QFrame.Raised)
        self.Title_Screen.setLineWidth(0)
        self.Title_Screen.setAlignment(Qt.AlignCenter)
        self.frame = QFrame(Menu)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(40, 203, 781, 391))
        self.frame.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
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
"\n"
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
"\n"
"\n"
"/* RESET ARROW */\n"
"\n"
"QScrollBar::up"
                        "-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     \n"
"	 background: none;\n"
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
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 10, 781, 371))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.scrollArea.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
"QScrollBar:vertical{\n"
"	background-color: rgb(31, 125, 108);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setLineWidth(0)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 767, 1640))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 10, 9, 0)
        self.key1 = QWidget(self.scrollAreaWidgetContents)
        self.key1.setObjectName("key1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.key1.sizePolicy().hasHeightForWidth())
        self.key1.setSizePolicy(sizePolicy3)
        self.key1.setMinimumSize(QSize(0, 55))
        self.key1.setMaximumSize(QSize(16777215, 90))
        self.key1.setCursor(QCursor(Qt.PointingHandCursor))
        self.key1.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command1 = QLineEdit(self.key1)
        self.game_command1.setObjectName("game_command1")
        self.game_command1.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.game_command1.sizePolicy().hasHeightForWidth())
        self.game_command1.setSizePolicy(sizePolicy4)
        self.game_command1.setMinimumSize(QSize(0, 43))
        self.game_command1.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamilies(["Berlin Sans FB"])
        font2.setPointSize(20)
        self.game_command1.setFont(font2)
        self.game_command1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command1.setMaxLength(17)
        self.game_command1.setAlignment(Qt.AlignCenter)
        self.game_command1.setReadOnly(False)
        self.key_1_name = QLabel(self.key1)
        self.key_1_name.setObjectName("key_1_name")
        self.key_1_name.setGeometry(QRect(336, 6, 108, 43))
        font3 = QFont()
        font3.setFamilies(["Berlin Sans FB"])
        font3.setPointSize(30)
        self.key_1_name.setFont(font3)
        self.key_1_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_1_name.setAlignment(Qt.AlignCenter)
        self.checkBoxW = QCheckBox(self.key1)
        self.checkBoxW.setObjectName("checkBoxW")
        self.checkBoxW.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxW.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  \n"
"	  background-color:rgb(7, 113, 240)\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.checkBoxW.setIconSize(QSize(23, 28))
        self.checkBoxW.setCheckable(True)
        self.checkBoxW.setChecked(True)

        self.verticalLayout_2.addWidget(self.key1)

        self.key2 = QWidget(self.scrollAreaWidgetContents)
        self.key2.setObjectName("key2")
        sizePolicy3.setHeightForWidth(self.key2.sizePolicy().hasHeightForWidth())
        self.key2.setSizePolicy(sizePolicy3)
        self.key2.setMinimumSize(QSize(0, 55))
        self.key2.setMaximumSize(QSize(16777215, 90))
        self.key2.setCursor(QCursor(Qt.PointingHandCursor))
        self.key2.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command2 = QLineEdit(self.key2)
        self.game_command2.setObjectName("game_command2")
        self.game_command2.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command2.sizePolicy().hasHeightForWidth())
        self.game_command2.setSizePolicy(sizePolicy4)
        self.game_command2.setMinimumSize(QSize(0, 43))
        self.game_command2.setMaximumSize(QSize(16777215, 16777215))
        self.game_command2.setFont(font2)
        self.game_command2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command2.setMaxLength(16)
        self.game_command2.setAlignment(Qt.AlignCenter)
        self.key_2_name = QLabel(self.key2)
        self.key_2_name.setObjectName("key_2_name")
        self.key_2_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_2_name.setFont(font3)
        self.key_2_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_2_name.setAlignment(Qt.AlignCenter)
        self.checkBoxS = QCheckBox(self.key2)
        self.checkBoxS.setObjectName("checkBoxS")
        self.checkBoxS.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxS.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"   background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxS.setIconSize(QSize(23, 28))
        self.checkBoxS.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key2)

        self.key3 = QWidget(self.scrollAreaWidgetContents)
        self.key3.setObjectName("key3")
        sizePolicy3.setHeightForWidth(self.key3.sizePolicy().hasHeightForWidth())
        self.key3.setSizePolicy(sizePolicy3)
        self.key3.setMinimumSize(QSize(0, 55))
        self.key3.setMaximumSize(QSize(16777215, 90))
        self.key3.setCursor(QCursor(Qt.PointingHandCursor))
        self.key3.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command3 = QLineEdit(self.key3)
        self.game_command3.setObjectName("game_command3")
        self.game_command3.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command3.sizePolicy().hasHeightForWidth())
        self.game_command3.setSizePolicy(sizePolicy4)
        self.game_command3.setMinimumSize(QSize(0, 43))
        self.game_command3.setMaximumSize(QSize(16777215, 16777215))
        self.game_command3.setFont(font2)
        self.game_command3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command3.setMaxLength(16)
        self.game_command3.setAlignment(Qt.AlignCenter)
        self.key_3_name = QLabel(self.key3)
        self.key_3_name.setObjectName("key_3_name")
        self.key_3_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_3_name.setFont(font3)
        self.key_3_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_3_name.setAlignment(Qt.AlignCenter)
        self.checkBoxA = QCheckBox(self.key3)
        self.checkBoxA.setObjectName("checkBoxA")
        self.checkBoxA.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxA.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxA.setIconSize(QSize(23, 28))
        self.checkBoxA.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key3)

        self.key4 = QWidget(self.scrollAreaWidgetContents)
        self.key4.setObjectName("key4")
        sizePolicy3.setHeightForWidth(self.key4.sizePolicy().hasHeightForWidth())
        self.key4.setSizePolicy(sizePolicy3)
        self.key4.setMinimumSize(QSize(0, 55))
        self.key4.setMaximumSize(QSize(16777215, 90))
        self.key4.setCursor(QCursor(Qt.PointingHandCursor))
        self.key4.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command4 = QLineEdit(self.key4)
        self.game_command4.setObjectName("game_command4")
        self.game_command4.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command4.sizePolicy().hasHeightForWidth())
        self.game_command4.setSizePolicy(sizePolicy4)
        self.game_command4.setMinimumSize(QSize(0, 43))
        self.game_command4.setMaximumSize(QSize(16777215, 16777215))
        self.game_command4.setFont(font2)
        self.game_command4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command4.setMaxLength(16)
        self.game_command4.setAlignment(Qt.AlignCenter)
        self.key_4_name = QLabel(self.key4)
        self.key_4_name.setObjectName("key_4_name")
        self.key_4_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_4_name.setFont(font3)
        self.key_4_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_4_name.setAlignment(Qt.AlignCenter)
        self.checkBoxD = QCheckBox(self.key4)
        self.checkBoxD.setObjectName("checkBoxD")
        self.checkBoxD.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxD.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxD.setIconSize(QSize(23, 28))
        self.checkBoxD.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key4)

        self.key5 = QWidget(self.scrollAreaWidgetContents)
        self.key5.setObjectName("key5")
        sizePolicy3.setHeightForWidth(self.key5.sizePolicy().hasHeightForWidth())
        self.key5.setSizePolicy(sizePolicy3)
        self.key5.setMinimumSize(QSize(0, 55))
        self.key5.setMaximumSize(QSize(16777215, 90))
        self.key5.setCursor(QCursor(Qt.PointingHandCursor))
        self.key5.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command5 = QLineEdit(self.key5)
        self.game_command5.setObjectName("game_command5")
        self.game_command5.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command5.sizePolicy().hasHeightForWidth())
        self.game_command5.setSizePolicy(sizePolicy4)
        self.game_command5.setMinimumSize(QSize(0, 43))
        self.game_command5.setMaximumSize(QSize(16777215, 16777215))
        font4 = QFont()
        font4.setFamilies(["Berlin Sans FB"])
        font4.setPointSize(20)
        font4.setBold(False)
        self.game_command5.setFont(font4)
        self.game_command5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command5.setMaxLength(16)
        self.game_command5.setAlignment(Qt.AlignCenter)
        self.key_5_name = QLabel(self.key5)
        self.key_5_name.setObjectName("key_5_name")
        self.key_5_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_5_name.setFont(font3)
        self.key_5_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_5_name.setAlignment(Qt.AlignCenter)
        self.checkBox_Q = QCheckBox(self.key5)
        self.checkBox_Q.setObjectName("checkBox_Q")
        self.checkBox_Q.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox_Q.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox_Q.setIconSize(QSize(23, 28))
        self.checkBox_Q.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key5)

        self.key6 = QWidget(self.scrollAreaWidgetContents)
        self.key6.setObjectName("key6")
        sizePolicy3.setHeightForWidth(self.key6.sizePolicy().hasHeightForWidth())
        self.key6.setSizePolicy(sizePolicy3)
        self.key6.setMinimumSize(QSize(0, 55))
        self.key6.setMaximumSize(QSize(16777215, 90))
        self.key6.setCursor(QCursor(Qt.PointingHandCursor))
        self.key6.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command6 = QLineEdit(self.key6)
        self.game_command6.setObjectName("game_command6")
        self.game_command6.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command6.sizePolicy().hasHeightForWidth())
        self.game_command6.setSizePolicy(sizePolicy4)
        self.game_command6.setMinimumSize(QSize(0, 43))
        self.game_command6.setMaximumSize(QSize(16777215, 16777215))
        self.game_command6.setFont(font2)
        self.game_command6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command6.setMaxLength(16)
        self.game_command6.setAlignment(Qt.AlignCenter)
        self.key_6_name = QLabel(self.key6)
        self.key_6_name.setObjectName("key_6_name")
        self.key_6_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_6_name.setFont(font3)
        self.key_6_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_6_name.setAlignment(Qt.AlignCenter)
        self.checkBox_E = QCheckBox(self.key6)
        self.checkBox_E.setObjectName("checkBox_E")
        self.checkBox_E.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox_E.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox_E.setIconSize(QSize(23, 28))
        self.checkBox_E.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key6)

        self.key7 = QWidget(self.scrollAreaWidgetContents)
        self.key7.setObjectName("key7")
        sizePolicy3.setHeightForWidth(self.key7.sizePolicy().hasHeightForWidth())
        self.key7.setSizePolicy(sizePolicy3)
        self.key7.setMinimumSize(QSize(0, 55))
        self.key7.setMaximumSize(QSize(16777215, 90))
        self.key7.setCursor(QCursor(Qt.PointingHandCursor))
        self.key7.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command7 = QLineEdit(self.key7)
        self.game_command7.setObjectName("game_command7")
        self.game_command7.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command7.sizePolicy().hasHeightForWidth())
        self.game_command7.setSizePolicy(sizePolicy4)
        self.game_command7.setMinimumSize(QSize(0, 43))
        self.game_command7.setMaximumSize(QSize(16777215, 16777215))
        self.game_command7.setFont(font2)
        self.game_command7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command7.setMaxLength(16)
        self.game_command7.setAlignment(Qt.AlignCenter)
        self.key_7_name = QLabel(self.key7)
        self.key_7_name.setObjectName("key_7_name")
        self.key_7_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_7_name.setFont(font3)
        self.key_7_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_7_name.setAlignment(Qt.AlignCenter)
        self.checkBoxR_3 = QCheckBox(self.key7)
        self.checkBoxR_3.setObjectName("checkBoxR_3")
        self.checkBoxR_3.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxR_3.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxR_3.setIconSize(QSize(23, 28))
        self.checkBoxR_3.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key7)

        self.key8 = QWidget(self.scrollAreaWidgetContents)
        self.key8.setObjectName("key8")
        sizePolicy3.setHeightForWidth(self.key8.sizePolicy().hasHeightForWidth())
        self.key8.setSizePolicy(sizePolicy3)
        self.key8.setMinimumSize(QSize(0, 55))
        self.key8.setMaximumSize(QSize(16777215, 90))
        self.key8.setCursor(QCursor(Qt.PointingHandCursor))
        self.key8.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command8 = QLineEdit(self.key8)
        self.game_command8.setObjectName("game_command8")
        self.game_command8.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command8.sizePolicy().hasHeightForWidth())
        self.game_command8.setSizePolicy(sizePolicy4)
        self.game_command8.setMinimumSize(QSize(0, 43))
        self.game_command8.setMaximumSize(QSize(16777215, 16777215))
        self.game_command8.setFont(font2)
        self.game_command8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command8.setMaxLength(16)
        self.game_command8.setAlignment(Qt.AlignCenter)
        self.key_8_name = QLabel(self.key8)
        self.key_8_name.setObjectName("key_8_name")
        self.key_8_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_8_name.setFont(font3)
        self.key_8_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_8_name.setAlignment(Qt.AlignCenter)
        self.checkBoxT = QCheckBox(self.key8)
        self.checkBoxT.setObjectName("checkBoxT")
        self.checkBoxT.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxT.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxT.setIconSize(QSize(23, 28))
        self.checkBoxT.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key8)

        self.key9 = QWidget(self.scrollAreaWidgetContents)
        self.key9.setObjectName("key9")
        sizePolicy3.setHeightForWidth(self.key9.sizePolicy().hasHeightForWidth())
        self.key9.setSizePolicy(sizePolicy3)
        self.key9.setMinimumSize(QSize(0, 55))
        self.key9.setMaximumSize(QSize(16777215, 90))
        self.key9.setCursor(QCursor(Qt.PointingHandCursor))
        self.key9.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command9 = QLineEdit(self.key9)
        self.game_command9.setObjectName("game_command9")
        self.game_command9.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command9.sizePolicy().hasHeightForWidth())
        self.game_command9.setSizePolicy(sizePolicy4)
        self.game_command9.setMinimumSize(QSize(0, 43))
        self.game_command9.setMaximumSize(QSize(16777215, 16777215))
        self.game_command9.setFont(font2)
        self.game_command9.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command9.setMaxLength(16)
        self.game_command9.setAlignment(Qt.AlignCenter)
        self.key_9_name = QLabel(self.key9)
        self.key_9_name.setObjectName("key_9_name")
        self.key_9_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_9_name.setFont(font3)
        self.key_9_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_9_name.setTextFormat(Qt.PlainText)
        self.key_9_name.setPixmap(QPixmap("image/espace_Icon.png"))
        self.key_9_name.setScaledContents(True)
        self.key_9_name.setAlignment(Qt.AlignCenter)
        self.key_9_name.setWordWrap(False)
        self.checkBoxEspace = QCheckBox(self.key9)
        self.checkBoxEspace.setObjectName("checkBoxEspace")
        self.checkBoxEspace.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxEspace.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
" background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxEspace.setIconSize(QSize(23, 28))
        self.checkBoxEspace.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key9)

        self.key10 = QWidget(self.scrollAreaWidgetContents)
        self.key10.setObjectName("key10")
        sizePolicy3.setHeightForWidth(self.key10.sizePolicy().hasHeightForWidth())
        self.key10.setSizePolicy(sizePolicy3)
        self.key10.setMinimumSize(QSize(0, 55))
        self.key10.setMaximumSize(QSize(16777215, 90))
        self.key10.setCursor(QCursor(Qt.PointingHandCursor))
        self.key10.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command10 = QLineEdit(self.key10)
        self.game_command10.setObjectName("game_command10")
        self.game_command10.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command10.sizePolicy().hasHeightForWidth())
        self.game_command10.setSizePolicy(sizePolicy4)
        self.game_command10.setMinimumSize(QSize(0, 43))
        self.game_command10.setMaximumSize(QSize(16777215, 16777215))
        self.game_command10.setFont(font2)
        self.game_command10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command10.setMaxLength(16)
        self.game_command10.setAlignment(Qt.AlignCenter)
        self.key_10_name = QLabel(self.key10)
        self.key_10_name.setObjectName("key_10_name")
        self.key_10_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_10_name.setFont(font3)
        self.key_10_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_10_name.setAlignment(Qt.AlignCenter)
        self.checkBoxCtrl = QCheckBox(self.key10)
        self.checkBoxCtrl.setObjectName("checkBoxCtrl")
        self.checkBoxCtrl.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxCtrl.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"   \n"
"	background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxCtrl.setIconSize(QSize(23, 28))
        self.checkBoxCtrl.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key10)

        self.key11 = QWidget(self.scrollAreaWidgetContents)
        self.key11.setObjectName("key11")
        sizePolicy3.setHeightForWidth(self.key11.sizePolicy().hasHeightForWidth())
        self.key11.setSizePolicy(sizePolicy3)
        self.key11.setMinimumSize(QSize(0, 55))
        self.key11.setMaximumSize(QSize(16777215, 90))
        self.key11.setCursor(QCursor(Qt.PointingHandCursor))
        self.key11.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command11 = QLineEdit(self.key11)
        self.game_command11.setObjectName("game_command11")
        self.game_command11.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command11.sizePolicy().hasHeightForWidth())
        self.game_command11.setSizePolicy(sizePolicy4)
        self.game_command11.setMinimumSize(QSize(0, 43))
        self.game_command11.setMaximumSize(QSize(16777215, 16777215))
        self.game_command11.setFont(font2)
        self.game_command11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command11.setMaxLength(16)
        self.game_command11.setAlignment(Qt.AlignCenter)
        self.key_11_name = QLabel(self.key11)
        self.key_11_name.setObjectName("key_11_name")
        self.key_11_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_11_name.setFont(font3)
        self.key_11_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;\n"
"")
        self.key_11_name.setPixmap(QPixmap("image/shitf_icon.png"))
        self.key_11_name.setScaledContents(True)
        self.key_11_name.setAlignment(Qt.AlignCenter)
        self.checkBoxShift = QCheckBox(self.key11)
        self.checkBoxShift.setObjectName("checkBoxShift")
        self.checkBoxShift.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxShift.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"	background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxShift.setIconSize(QSize(23, 28))
        self.checkBoxShift.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key11)

        self.key12 = QWidget(self.scrollAreaWidgetContents)
        self.key12.setObjectName("key12")
        sizePolicy3.setHeightForWidth(self.key12.sizePolicy().hasHeightForWidth())
        self.key12.setSizePolicy(sizePolicy3)
        self.key12.setMinimumSize(QSize(0, 55))
        self.key12.setMaximumSize(QSize(16777215, 90))
        self.key12.setCursor(QCursor(Qt.PointingHandCursor))
        self.key12.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command12 = QLineEdit(self.key12)
        self.game_command12.setObjectName("game_command12")
        self.game_command12.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command12.sizePolicy().hasHeightForWidth())
        self.game_command12.setSizePolicy(sizePolicy4)
        self.game_command12.setMinimumSize(QSize(0, 43))
        self.game_command12.setMaximumSize(QSize(16777215, 16777215))
        self.game_command12.setFont(font2)
        self.game_command12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command12.setMaxLength(16)
        self.game_command12.setAlignment(Qt.AlignCenter)
        self.key_12_name = QLabel(self.key12)
        self.key_12_name.setObjectName("key_12_name")
        self.key_12_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_12_name.setFont(font3)
        self.key_12_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_12_name.setScaledContents(False)
        self.key_12_name.setAlignment(Qt.AlignCenter)
        self.checkBoxTab = QCheckBox(self.key12)
        self.checkBoxTab.setObjectName("checkBoxTab")
        self.checkBoxTab.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxTab.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
" background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxTab.setIconSize(QSize(23, 28))
        self.checkBoxTab.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key12)

        self.key13 = QWidget(self.scrollAreaWidgetContents)
        self.key13.setObjectName("key13")
        sizePolicy3.setHeightForWidth(self.key13.sizePolicy().hasHeightForWidth())
        self.key13.setSizePolicy(sizePolicy3)
        self.key13.setMinimumSize(QSize(0, 55))
        self.key13.setMaximumSize(QSize(16777215, 90))
        self.key13.setCursor(QCursor(Qt.PointingHandCursor))
        self.key13.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command13 = QLineEdit(self.key13)
        self.game_command13.setObjectName("game_command13")
        self.game_command13.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command13.sizePolicy().hasHeightForWidth())
        self.game_command13.setSizePolicy(sizePolicy4)
        self.game_command13.setMinimumSize(QSize(0, 43))
        self.game_command13.setMaximumSize(QSize(16777215, 16777215))
        self.game_command13.setFont(font2)
        self.game_command13.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command13.setMaxLength(16)
        self.game_command13.setAlignment(Qt.AlignCenter)
        self.key_13_name = QLabel(self.key13)
        self.key_13_name.setObjectName("key_13_name")
        self.key_13_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_13_name.setFont(font3)
        self.key_13_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_13_name.setAlignment(Qt.AlignCenter)
        self.checkBoxZ = QCheckBox(self.key13)
        self.checkBoxZ.setObjectName("checkBoxZ")
        self.checkBoxZ.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxZ.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxZ.setIconSize(QSize(23, 28))
        self.checkBoxZ.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key13)

        self.key14 = QWidget(self.scrollAreaWidgetContents)
        self.key14.setObjectName("key14")
        sizePolicy3.setHeightForWidth(self.key14.sizePolicy().hasHeightForWidth())
        self.key14.setSizePolicy(sizePolicy3)
        self.key14.setMinimumSize(QSize(0, 55))
        self.key14.setMaximumSize(QSize(16777215, 90))
        self.key14.setCursor(QCursor(Qt.PointingHandCursor))
        self.key14.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command14 = QLineEdit(self.key14)
        self.game_command14.setObjectName("game_command14")
        self.game_command14.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command14.sizePolicy().hasHeightForWidth())
        self.game_command14.setSizePolicy(sizePolicy4)
        self.game_command14.setMinimumSize(QSize(0, 43))
        self.game_command14.setMaximumSize(QSize(16777215, 16777215))
        self.game_command14.setFont(font2)
        self.game_command14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command14.setMaxLength(16)
        self.game_command14.setAlignment(Qt.AlignCenter)
        self.key_14_name = QLabel(self.key14)
        self.key_14_name.setObjectName("key_14_name")
        self.key_14_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_14_name.setFont(font3)
        self.key_14_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_14_name.setAlignment(Qt.AlignCenter)
        self.checkBoxX = QCheckBox(self.key14)
        self.checkBoxX.setObjectName("checkBoxX")
        self.checkBoxX.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxX.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.checkBoxX.setIconSize(QSize(23, 28))
        self.checkBoxX.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key14)

        self.key15 = QWidget(self.scrollAreaWidgetContents)
        self.key15.setObjectName("key15")
        sizePolicy3.setHeightForWidth(self.key15.sizePolicy().hasHeightForWidth())
        self.key15.setSizePolicy(sizePolicy3)
        self.key15.setMinimumSize(QSize(0, 55))
        self.key15.setMaximumSize(QSize(16777215, 90))
        self.key15.setCursor(QCursor(Qt.PointingHandCursor))
        self.key15.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command15 = QLineEdit(self.key15)
        self.game_command15.setObjectName("game_command15")
        self.game_command15.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command15.sizePolicy().hasHeightForWidth())
        self.game_command15.setSizePolicy(sizePolicy4)
        self.game_command15.setMinimumSize(QSize(0, 43))
        self.game_command15.setMaximumSize(QSize(16777215, 16777215))
        self.game_command15.setFont(font2)
        self.game_command15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command15.setMaxLength(16)
        self.game_command15.setAlignment(Qt.AlignCenter)
        self.key_15_name = QLabel(self.key15)
        self.key_15_name.setObjectName("key_15_name")
        self.key_15_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_15_name.setFont(font3)
        self.key_15_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_15_name.setAlignment(Qt.AlignCenter)
        self.checkBoxC = QCheckBox(self.key15)
        self.checkBoxC.setObjectName("checkBoxC")
        self.checkBoxC.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxC.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxC.setIconSize(QSize(23, 28))
        self.checkBoxC.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key15)

        self.key16 = QWidget(self.scrollAreaWidgetContents)
        self.key16.setObjectName("key16")
        sizePolicy3.setHeightForWidth(self.key16.sizePolicy().hasHeightForWidth())
        self.key16.setSizePolicy(sizePolicy3)
        self.key16.setMinimumSize(QSize(0, 55))
        self.key16.setMaximumSize(QSize(16777215, 90))
        self.key16.setCursor(QCursor(Qt.PointingHandCursor))
        self.key16.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command16 = QLineEdit(self.key16)
        self.game_command16.setObjectName("game_command16")
        self.game_command16.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command16.sizePolicy().hasHeightForWidth())
        self.game_command16.setSizePolicy(sizePolicy4)
        self.game_command16.setMinimumSize(QSize(0, 43))
        self.game_command16.setMaximumSize(QSize(16777215, 16777215))
        self.game_command16.setFont(font2)
        self.game_command16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command16.setMaxLength(16)
        self.game_command16.setAlignment(Qt.AlignCenter)
        self.key_16_name = QLabel(self.key16)
        self.key_16_name.setObjectName("key_16_name")
        self.key_16_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_16_name.setFont(font3)
        self.key_16_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_16_name.setAlignment(Qt.AlignCenter)
        self.checkBoxV = QCheckBox(self.key16)
        self.checkBoxV.setObjectName("checkBoxV")
        self.checkBoxV.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxV.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxV.setIconSize(QSize(23, 28))
        self.checkBoxV.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key16)

        self.key17 = QWidget(self.scrollAreaWidgetContents)
        self.key17.setObjectName("key17")
        sizePolicy3.setHeightForWidth(self.key17.sizePolicy().hasHeightForWidth())
        self.key17.setSizePolicy(sizePolicy3)
        self.key17.setMinimumSize(QSize(0, 55))
        self.key17.setMaximumSize(QSize(16777215, 90))
        self.key17.setCursor(QCursor(Qt.PointingHandCursor))
        self.key17.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command17 = QLineEdit(self.key17)
        self.game_command17.setObjectName("game_command17")
        self.game_command17.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command17.sizePolicy().hasHeightForWidth())
        self.game_command17.setSizePolicy(sizePolicy4)
        self.game_command17.setMinimumSize(QSize(0, 43))
        self.game_command17.setMaximumSize(QSize(16777215, 16777215))
        self.game_command17.setFont(font2)
        self.game_command17.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command17.setMaxLength(16)
        self.game_command17.setAlignment(Qt.AlignCenter)
        self.key_17_name = QLabel(self.key17)
        self.key_17_name.setObjectName("key_17_name")
        self.key_17_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_17_name.setFont(font3)
        self.key_17_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_17_name.setAlignment(Qt.AlignCenter)
        self.checkBoxF = QCheckBox(self.key17)
        self.checkBoxF.setObjectName("checkBoxF")
        self.checkBoxF.setGeometry(QRect(600, 2, 51, 51))
        self.checkBoxF.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
" background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBoxF.setIconSize(QSize(23, 28))
        self.checkBoxF.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key17)

        self.key18 = QWidget(self.scrollAreaWidgetContents)
        self.key18.setObjectName("key18")
        sizePolicy3.setHeightForWidth(self.key18.sizePolicy().hasHeightForWidth())
        self.key18.setSizePolicy(sizePolicy3)
        self.key18.setMinimumSize(QSize(0, 55))
        self.key18.setMaximumSize(QSize(16777215, 90))
        self.key18.setCursor(QCursor(Qt.PointingHandCursor))
        self.key18.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command18 = QLineEdit(self.key18)
        self.game_command18.setObjectName("game_command18")
        self.game_command18.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command18.sizePolicy().hasHeightForWidth())
        self.game_command18.setSizePolicy(sizePolicy4)
        self.game_command18.setMinimumSize(QSize(0, 43))
        self.game_command18.setMaximumSize(QSize(16777215, 16777215))
        self.game_command18.setFont(font2)
        self.game_command18.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command18.setMaxLength(16)
        self.game_command18.setAlignment(Qt.AlignCenter)
        self.key_18_name = QLabel(self.key18)
        self.key_18_name.setObjectName("key_18_name")
        self.key_18_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_18_name.setFont(font3)
        self.key_18_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_18_name.setAlignment(Qt.AlignCenter)
        self.checkBox1 = QCheckBox(self.key18)
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox1.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox1.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"   background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox1.setIconSize(QSize(23, 28))
        self.checkBox1.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key18)

        self.key19 = QWidget(self.scrollAreaWidgetContents)
        self.key19.setObjectName("key19")
        sizePolicy3.setHeightForWidth(self.key19.sizePolicy().hasHeightForWidth())
        self.key19.setSizePolicy(sizePolicy3)
        self.key19.setMinimumSize(QSize(0, 55))
        self.key19.setMaximumSize(QSize(16777215, 90))
        self.key19.setCursor(QCursor(Qt.PointingHandCursor))
        self.key19.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command19 = QLineEdit(self.key19)
        self.game_command19.setObjectName("game_command19")
        self.game_command19.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command19.sizePolicy().hasHeightForWidth())
        self.game_command19.setSizePolicy(sizePolicy4)
        self.game_command19.setMinimumSize(QSize(0, 43))
        self.game_command19.setMaximumSize(QSize(16777215, 16777215))
        self.game_command19.setFont(font2)
        self.game_command19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command19.setMaxLength(16)
        self.game_command19.setAlignment(Qt.AlignCenter)
        self.key_19_name = QLabel(self.key19)
        self.key_19_name.setObjectName("key_19_name")
        self.key_19_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_19_name.setFont(font3)
        self.key_19_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_19_name.setAlignment(Qt.AlignCenter)
        self.checkBox2 = QCheckBox(self.key19)
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox2.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox2.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"   background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox2.setIconSize(QSize(23, 28))
        self.checkBox2.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key19)

        self.key20 = QWidget(self.scrollAreaWidgetContents)
        self.key20.setObjectName("key20")
        sizePolicy3.setHeightForWidth(self.key20.sizePolicy().hasHeightForWidth())
        self.key20.setSizePolicy(sizePolicy3)
        self.key20.setMinimumSize(QSize(0, 55))
        self.key20.setMaximumSize(QSize(16777215, 90))
        self.key20.setCursor(QCursor(Qt.PointingHandCursor))
        self.key20.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command20 = QLineEdit(self.key20)
        self.game_command20.setObjectName("game_command20")
        self.game_command20.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command20.sizePolicy().hasHeightForWidth())
        self.game_command20.setSizePolicy(sizePolicy4)
        self.game_command20.setMinimumSize(QSize(0, 43))
        self.game_command20.setMaximumSize(QSize(16777215, 16777215))
        self.game_command20.setFont(font2)
        self.game_command20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command20.setMaxLength(16)
        self.game_command20.setAlignment(Qt.AlignCenter)
        self.key_20_name = QLabel(self.key20)
        self.key_20_name.setObjectName("key_20_name")
        self.key_20_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_20_name.setFont(font3)
        self.key_20_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_20_name.setAlignment(Qt.AlignCenter)
        self.checkBox3 = QCheckBox(self.key20)
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox3.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox3.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox3.setIconSize(QSize(23, 28))
        self.checkBox3.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key20)

        self.key21 = QWidget(self.scrollAreaWidgetContents)
        self.key21.setObjectName("key21")
        sizePolicy3.setHeightForWidth(self.key21.sizePolicy().hasHeightForWidth())
        self.key21.setSizePolicy(sizePolicy3)
        self.key21.setMinimumSize(QSize(0, 55))
        self.key21.setMaximumSize(QSize(16777215, 90))
        self.key21.setCursor(QCursor(Qt.PointingHandCursor))
        self.key21.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command21 = QLineEdit(self.key21)
        self.game_command21.setObjectName("game_command21")
        self.game_command21.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command21.sizePolicy().hasHeightForWidth())
        self.game_command21.setSizePolicy(sizePolicy4)
        self.game_command21.setMinimumSize(QSize(0, 43))
        self.game_command21.setMaximumSize(QSize(16777215, 16777215))
        self.game_command21.setFont(font2)
        self.game_command21.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command21.setMaxLength(16)
        self.game_command21.setAlignment(Qt.AlignCenter)
        self.key_21_name = QLabel(self.key21)
        self.key_21_name.setObjectName("key_21_name")
        self.key_21_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_21_name.setFont(font3)
        self.key_21_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_21_name.setAlignment(Qt.AlignCenter)
        self.checkBox4 = QCheckBox(self.key21)
        self.checkBox4.setObjectName("checkBox4")
        self.checkBox4.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox4.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"   background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox4.setIconSize(QSize(23, 28))
        self.checkBox4.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key21)

        self.key22 = QWidget(self.scrollAreaWidgetContents)
        self.key22.setObjectName("key22")
        sizePolicy3.setHeightForWidth(self.key22.sizePolicy().hasHeightForWidth())
        self.key22.setSizePolicy(sizePolicy3)
        self.key22.setMinimumSize(QSize(0, 55))
        self.key22.setMaximumSize(QSize(16777215, 90))
        self.key22.setCursor(QCursor(Qt.PointingHandCursor))
        self.key22.setStyleSheet("background-color: rgb(30, 217, 89);\n"
"")
        self.game_command22 = QLineEdit(self.key22)
        self.game_command22.setObjectName("game_command22")
        self.game_command22.setGeometry(QRect(10, 6, 251, 43))
        sizePolicy4.setHeightForWidth(self.game_command22.sizePolicy().hasHeightForWidth())
        self.game_command22.setSizePolicy(sizePolicy4)
        self.game_command22.setMinimumSize(QSize(0, 43))
        self.game_command22.setMaximumSize(QSize(16777215, 16777215))
        self.game_command22.setFont(font2)
        self.game_command22.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.game_command22.setMaxLength(16)
        self.game_command22.setAlignment(Qt.AlignCenter)
        self.key_22_name = QLabel(self.key22)
        self.key_22_name.setObjectName("key_22_name")
        self.key_22_name.setGeometry(QRect(336, 6, 108, 43))
        self.key_22_name.setFont(font3)
        self.key_22_name.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: black;")
        self.key_22_name.setAlignment(Qt.AlignCenter)
        self.checkBox5 = QCheckBox(self.key22)
        self.checkBox5.setObjectName("checkBox5")
        self.checkBox5.setGeometry(QRect(600, 2, 51, 51))
        self.checkBox5.setStyleSheet("QCheckBox::indicator {\n"
"     width: 40px;\n"
"     height: 40px;\n"
"	border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: black;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: rgb(7, 113, 240);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.checkBox5.setIconSize(QSize(23, 28))
        self.checkBox5.setCheckable(True)

        self.verticalLayout_2.addWidget(self.key22)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.name_title = QLabel(Menu)
        self.name_title.setObjectName("name_title")
        self.name_title.setGeometry(QRect(20, 88, 91, 51))
        font5 = QFont()
        font5.setFamilies(["Berlin Sans FB"])
        font5.setPointSize(18)
        self.name_title.setFont(font5)
        self.name_title.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius:7px;\n"
"border-bottom-left-radius: 7px;")
        self.name_title.setAlignment(Qt.AlignCenter)
        self.game_name_area = QLineEdit(Menu)
        self.game_name_area.setObjectName("game_name_area")
        self.game_name_area.setGeometry(QRect(110, 88, 411, 52))
        sizePolicy4.setHeightForWidth(self.game_name_area.sizePolicy().hasHeightForWidth())
        self.game_name_area.setSizePolicy(sizePolicy4)
        self.game_name_area.setMinimumSize(QSize(0, 52))
        self.game_name_area.setMaximumSize(QSize(16777215, 16777215))
        self.game_name_area.setFont(font2)
        self.game_name_area.setCursor(QCursor(Qt.PointingHandCursor))
        self.game_name_area.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-left:0px;\n"
"border-left-width:0px;")
        self.game_name_area.setMaxLength(25)
        self.comand_name = QLabel(Menu)
        self.comand_name.setObjectName("comand_name")
        self.comand_name.setGeometry(QRect(100, 162, 131, 41))
        font6 = QFont()
        font6.setFamilies(["Berlin Sans FB"])
        font6.setPointSize(23)
        self.comand_name.setFont(font6)
        self.comand_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.keys_name = QLabel(Menu)
        self.keys_name.setObjectName("keys_name")
        self.keys_name.setGeometry(QRect(370, 162, 131, 41))
        self.keys_name.setFont(font6)
        self.keys_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.keys_name.setAlignment(Qt.AlignCenter)
        self.keep_pressing = QLabel(Menu)
        self.keep_pressing.setObjectName("keep_pressing")
        self.keep_pressing.setGeometry(QRect(546, 162, 251, 41))
        self.keep_pressing.setFont(font6)
        self.keep_pressing.setStyleSheet("color: rgb(255, 255, 255);")
        self.keep_pressing.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.menu_button = QPushButton(Menu)
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setGeometry(QRect(30, 610, 125, 51))
        font7 = QFont()
        font7.setFamilies(["Berlin Sans FB"])
        font7.setPointSize(16)
        self.menu_button.setFont(font7)
        self.menu_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.menu_button.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    border-style: outset;\n"
"    border-radius: 10px;    \n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(199, 199, 199);\n"
"    border-style: inset;\n"
"}")
        icon = QIcon()
        icon.addFile("image/left_arrow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_button.setIcon(icon)
        self.menu_button.setIconSize(QSize(35, 35))
        self.apply_button = QPushButton(Menu)
        self.apply_button.setObjectName("apply_button")
        self.apply_button.setGeometry(QRect(740, 610, 125, 51))
        self.apply_button.setFont(font7)
        self.apply_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.apply_button.setStyleSheet("QPushButton{\n"
"    background-color: white;\n"
"    border-style: outset;\n"
"    border-radius: 10px;    \n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"    \n"
"	background-color: rgb(199, 199, 199);\n"
"    border-style: inset;\n"
"}\n"
"\n"
"")
        self.apply_button.setIconSize(QSize(21, 21))
        self.repeated_commands = QFrame(Menu)
        self.repeated_commands.setObjectName("repeated_commands")
        self.repeated_commands.setGeometry(QRect(550, 70, 261, 91))
        self.repeated_commands.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
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
"\n"
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
"\n"
"\n"
"/* RESET ARROW */\n"
"\n"
"QScrollBar::up"
                        "-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     \n"
"	 background: none;\n"
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
        self.repeated_commands.setFrameShape(QFrame.NoFrame)
        self.repeated_commands.setFrameShadow(QFrame.Plain)
        self.repeated_commands.setLineWidth(0)
        self.scrollArea2 = QScrollArea(self.repeated_commands)
        self.scrollArea2.setObjectName("scrollArea2")
        self.scrollArea2.setGeometry(QRect(-1, 10, 262, 81))
        sizePolicy1.setHeightForWidth(self.scrollArea2.sizePolicy().hasHeightForWidth())
        self.scrollArea2.setSizePolicy(sizePolicy1)
        self.scrollArea2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.scrollArea2.setStyleSheet("/* VERTIVAL SCROLL BAR*/\n"
"QScrollBar:vertical{\n"
"	\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.scrollArea2.setFrameShape(QFrame.NoFrame)
        self.scrollArea2.setFrameShadow(QFrame.Plain)
        self.scrollArea2.setLineWidth(0)
        self.scrollArea2.setWidgetResizable(True)
        self.scrollArea2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents2 = QWidget()
        self.scrollAreaWidgetContents2.setObjectName("scrollAreaWidgetContents2")
        self.scrollAreaWidgetContents2.setGeometry(QRect(0, 0, 262, 16))
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents2.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents2.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents2.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents2)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 6, 9, 0)
        self.scrollArea2.setWidget(self.scrollAreaWidgetContents2)
        self.frame.raise_()
        self.Title_Screen.raise_()
        self.name_title.raise_()
        self.game_name_area.raise_()
        self.comand_name.raise_()
        self.keys_name.raise_()
        self.keep_pressing.raise_()
        self.menu_button.raise_()
        self.apply_button.raise_()
        self.repeated_commands.raise_()

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", "Menu", None))
        self.Title_Screen.setText(QCoreApplication.translate("Menu", "Configurações de jogo", None))
        self.key_1_name.setText(QCoreApplication.translate("Menu", "W", None))
        self.key_2_name.setText(QCoreApplication.translate("Menu", "S", None))
        self.key_3_name.setText(QCoreApplication.translate("Menu", "A", None))
        self.key_4_name.setText(QCoreApplication.translate("Menu", "D", None))
        self.key_5_name.setText(QCoreApplication.translate("Menu", "Q", None))
        self.key_6_name.setText(QCoreApplication.translate("Menu", "E", None))
        self.key_7_name.setText(QCoreApplication.translate("Menu", "R", None))
        self.key_8_name.setText(QCoreApplication.translate("Menu", "T", None))
        self.key_10_name.setText(QCoreApplication.translate("Menu", "Ctrl", None))
        self.key_12_name.setText(QCoreApplication.translate("Menu", "Tab", None))
        self.key_13_name.setText(QCoreApplication.translate("Menu", "Z", None))
        self.key_14_name.setText(QCoreApplication.translate("Menu", "X", None))
        self.key_15_name.setText(QCoreApplication.translate("Menu", "C", None))
        self.key_16_name.setText(QCoreApplication.translate("Menu", "V", None))
        self.key_17_name.setText(QCoreApplication.translate("Menu", "F", None))
        self.key_18_name.setText(QCoreApplication.translate("Menu", "1", None))
        self.key_19_name.setText(QCoreApplication.translate("Menu", "2", None))
        self.key_20_name.setText(QCoreApplication.translate("Menu", "3", None))
        self.key_21_name.setText(QCoreApplication.translate("Menu", "4", None))
        self.key_22_name.setText(QCoreApplication.translate("Menu", "5", None))

        self.name_title.setText(QCoreApplication.translate("Menu", "Nome:", None))
        self.comand_name.setText(QCoreApplication.translate("Menu", "Comando", None))
        self.keys_name.setText(QCoreApplication.translate("Menu", "Tecla", None))
        self.keep_pressing.setText(QCoreApplication.translate("Menu", "Manter Pressionado", None))
        self.menu_button.setText(QCoreApplication.translate("Menu", "Voltar", None))
        self.apply_button.setText(QCoreApplication.translate("Menu", "Aplicar", None))

