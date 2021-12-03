from PySide6.QtCore import (QCoreApplication,
    QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont, QIcon, QPixmap)
from PySide6.QtWidgets import (QFrame, QLabel, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Instruction(object):
    def setupUi(self, Menu):
        if not Menu.objectName():
            Menu.setObjectName("Menu")
        Menu.setWindowModality(Qt.ApplicationModal)
        Menu.resize(885, 677)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Menu.sizePolicy().hasHeightForWidth())
        Menu.setSizePolicy(sizePolicy)
        Menu.setMaximumSize(QSize(885, 667))
        font = QFont()
        font.setFamilies([u"Berlin Sans FB"])
        font.setPointSize(49)
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
        font1.setFamilies([u"Leelawadee"])
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
        self.frame.setGeometry(QRect(28, 69, 831, 511))
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
"	background-color: transparent;\n"
"\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Plain)
        self.frame.setLineWidth(0)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 831, 511))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 817, 2074))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContents.setSizePolicy(sizePolicy2)
        self.scrollAreaWidgetContents.setCursor(QCursor(Qt.PointingHandCursor))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 10, 9, 0)
        self.slide1 = QLabel(self.scrollAreaWidgetContents)
        self.slide1.setObjectName("slide1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.slide1.sizePolicy().hasHeightForWidth())
        self.slide1.setSizePolicy(sizePolicy3)
        self.slide1.setMinimumSize(QSize(651, 501))
        self.slide1.setPixmap(QPixmap("image/Instrução_Slide_Menu.png"))
        self.slide1.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.slide1)

        self.slide1_4 = QLabel(self.scrollAreaWidgetContents)
        self.slide1_4.setObjectName("slide1_4")
        sizePolicy3.setHeightForWidth(self.slide1_4.sizePolicy().hasHeightForWidth())
        self.slide1_4.setSizePolicy(sizePolicy3)
        self.slide1_4.setMinimumSize(QSize(651, 501))
        self.slide1_4.setPixmap(QPixmap("image/Instrução_ReconhecimentoDeVoz_Slides.png"))
        self.slide1_4.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.slide1_4)

        self.slide1_2 = QLabel(self.scrollAreaWidgetContents)
        self.slide1_2.setObjectName("slide1_2")
        sizePolicy3.setHeightForWidth(self.slide1_2.sizePolicy().hasHeightForWidth())
        self.slide1_2.setSizePolicy(sizePolicy3)
        self.slide1_2.setMinimumSize(QSize(651, 501))
        self.slide1_2.setPixmap(QPixmap("image/Instrução_Slides_Edit_Screen01.png"))
        self.slide1_2.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.slide1_2)

        self.slide1_3 = QLabel(self.scrollAreaWidgetContents)
        self.slide1_3.setObjectName("slide1_3")
        sizePolicy3.setHeightForWidth(self.slide1_3.sizePolicy().hasHeightForWidth())
        self.slide1_3.setSizePolicy(sizePolicy3)
        self.slide1_3.setMinimumSize(QSize(651, 501))
        self.slide1_3.setPixmap(QPixmap("image/Instrução_Slides_Edit_Screen02.png"))
        self.slide1_3.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.slide1_3)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.menu_button = QPushButton(Menu)
        self.menu_button.setObjectName("menu_button")
        self.menu_button.setGeometry(QRect(30, 610, 125, 51))
        font2 = QFont()
        font2.setFamilies([u"Berlin Sans FB"])
        font2.setPointSize(16)
        self.menu_button.setFont(font2)
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
        self.frame.raise_()
        self.Title_Screen.raise_()
        self.menu_button.raise_()

        self.retranslateUi(Menu)

        QMetaObject.connectSlotsByName(Menu)
    # setupUi

    def retranslateUi(self, Menu):
        Menu.setWindowTitle(QCoreApplication.translate("Menu", "Menu", None))
        self.Title_Screen.setText(QCoreApplication.translate("Menu", "Instrução", None))
        self.slide1.setText("")
        self.slide1_4.setText("")
        self.slide1_2.setText("")
        self.slide1_3.setText("")
        self.menu_button.setText(QCoreApplication.translate("Menu", "Voltar", None))
    # retranslateUi

