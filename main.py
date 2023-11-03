import os
import sys
import json
import time
# import screeninfo
import numpy as np
import serial.tools.list_ports


from PyQt6 import QtWidgets, QtCore, QtGui, uic
from PyQt6.uic import loadUi
from PyQt6.QtCore import Qt, QTimer, QThread, pyqtSignal, QCoreApplication, QByteArray, QEventLoop, QProcess
from PyQt6.QtGui import QIcon, QImage, QPixmap, QGuiApplication
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow, QStackedWidget, QMessageBox, QTextEdit, QFileDialog
from PyQt6.QtNetwork import QLocalSocket, QLocalServer
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTextEdit, QVBoxLayout, QWidget)
# from cam import *

# from tool_screen import *
# from mainWindow import Ui_MainWindow as mainUI
# from res_rc import *

# Import UI files

ui_folder = os.path.join("UI")
# mainUI, _ = uic.loadUiType(os.path.join(ui_folder, "mainWindow_1080p_1.1.ui"))
# mainUi = uic.loadUi(os.path.join(ui_folder, "mainWindow_1080p_1.1.ui"))


"""
UI File
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1389, 865)
        MainWindow.setMinimumSize(QSize(0, 865))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u":/icon/Assets/icon/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(210, 210, 210, 255));\n"
"border:0px\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 #A0A0A0, stop:0 rgba(240, 240, 240, 255));\n"
"border:0px")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.centralwidget)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setStyleSheet(u"background:rgba(240, 240, 240, 255);")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_scanType = QLabel(self.frame_title)
        self.label_scanType.setObjectName(u"label_scanType")
        self.label_scanType.setMinimumSize(QSize(208, 0))
        font = QFont()
        font.setFamilies([u"Segoe UI Semibold"])
        font.setPointSize(16)
        font.setBold(True)
        self.label_scanType.setFont(font)
        self.label_scanType.setStyleSheet(u"background:rgba(240, 240, 240, 255);")
        self.label_scanType.setLineWidth(0)
        self.label_scanType.setAlignment(Qt.AlignCenter)
        self.label_scanType.setMargin(20)

        self.horizontalLayout_5.addWidget(self.label_scanType)

        self.horizontalSpacer_2 = QSpacerItem(751, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.button_setting = QPushButton(self.frame_title)
        self.button_setting.setObjectName(u"button_setting")
        self.button_setting.setMinimumSize(QSize(220, 60))
        self.button_setting.setMaximumSize(QSize(240, 16777215))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.button_setting.setFont(font1)
        self.button_setting.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"	border-radius: 12px\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(210,223,233);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:  rgba(170, 170, 170, 255);\n"
"	\n"
"}\n"
"")
        self.button_setting.setIconSize(QSize(40, 40))
        self.button_setting.setCheckable(True)
        self.button_setting.setChecked(False)

        self.horizontalLayout_5.addWidget(self.button_setting)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_content = QFrame(self.centralwidget)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setMinimumSize(QSize(0, 120))
        self.frame_content.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 #A0A0A0, stop:0 rgba(240, 240, 240, 255));")
        self.frame_content.setFrameShape(QFrame.StyledPanel)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_content)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.frame_content)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setMinimumSize(QSize(440, 700))
        self.frame_menu.setMaximumSize(QSize(16777215, 16777215))
        self.frame_menu.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(240, 240, 240, 255), stop:1 rgba(210, 210, 210, 255));\n"
"border:0px\n"
"\n"
"")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_Intro_Scan_Pattern = QFrame(self.frame_menu)
        self.frame_Intro_Scan_Pattern.setObjectName(u"frame_Intro_Scan_Pattern")
        self.frame_Intro_Scan_Pattern.setMaximumSize(QSize(16777215, 50))
        palette = QPalette()
        self.frame_Intro_Scan_Pattern.setPalette(palette)
        self.frame_Intro_Scan_Pattern.setStyleSheet(u"background-color: rgba()")
        self.frame_Intro_Scan_Pattern.setFrameShape(QFrame.StyledPanel)
        self.frame_Intro_Scan_Pattern.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_Intro_Scan_Pattern)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 10)
        self.label_4 = QLabel(self.frame_Intro_Scan_Pattern)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 40))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_4.setFont(font2)

        self.horizontalLayout_4.addWidget(self.label_4)


        self.verticalLayout.addWidget(self.frame_Intro_Scan_Pattern)

        self.frame_7 = QFrame(self.frame_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background:rgba(0,0,0,0);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_s_lr = QLabel(self.frame_7)
        self.label_s_lr.setObjectName(u"label_s_lr")
        self.label_s_lr.setMaximumSize(QSize(102, 16777215))
        font3 = QFont()
        font3.setFamilies([u"Consolas"])
        font3.setPointSize(20)
        self.label_s_lr.setFont(font3)
        self.label_s_lr.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_s_lr)

        self.label_s_ud = QLabel(self.frame_7)
        self.label_s_ud.setObjectName(u"label_s_ud")
        self.label_s_ud.setMaximumSize(QSize(102, 16777215))
        self.label_s_ud.setFont(font3)
        self.label_s_ud.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_s_ud)

        self.label_s_fb = QLabel(self.frame_7)
        self.label_s_fb.setObjectName(u"label_s_fb")
        self.label_s_fb.setMaximumSize(QSize(102, 16777215))
        self.label_s_fb.setFont(font3)
        self.label_s_fb.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_s_fb)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame = QFrame(self.frame_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 460))
        self.frame.setStyleSheet(u"background:rgba(0,0,0,0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(11, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(102, 0))
        self.frame_2.setMaximumSize(QSize(102, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_2)
        self.verticalLayout_13.setSpacing(7)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(11, 11, 11, 11)
        self.button_speed_plus_lr = QPushButton(self.frame_2)
        self.button_speed_plus_lr.setObjectName(u"button_speed_plus_lr")
        self.button_speed_plus_lr.setMinimumSize(QSize(80, 53))
        self.button_speed_plus_lr.setMaximumSize(QSize(80, 53))
        font4 = QFont()
        font4.setFamilies([u"Consolas"])
        font4.setPointSize(20)
        font4.setBold(True)
        self.button_speed_plus_lr.setFont(font4)
        self.button_speed_plus_lr.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.button_speed_plus_lr)

        self.verticalSlider_LeftRight = QSlider(self.frame_2)
        self.verticalSlider_LeftRight.setObjectName(u"verticalSlider_LeftRight")
        self.verticalSlider_LeftRight.setMinimumSize(QSize(82, 0))
        self.verticalSlider_LeftRight.setMaximumSize(QSize(16777215, 16777215))
        self.verticalSlider_LeftRight.setStyleSheet(u".QSlider {\n"
"    min-Width: 80px;\n"
"    /*max-height: 80px;*/\n"
"	background:rgba(0,0,0,0);\n"
"	border: 1px solid rgba(0,0,0,0);\n"
"}\n"
"\n"
".QSlider::groove:vertical {\n"
"    border: 1px solid  rgb(180,180,180);\n"
"	border-radius: 4px;\n"
"    width: 7px;\n"
"    background: rgb(140,140,140);\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));\n"
"	border: 1px solid rgba(205,205,205,100);\n"
"	width: 50px;\n"
"    height: 50px;\n"
"    margin: -2px -36px;\n"
"}\n"
"\n"
".QSlider::handle:vertical::hover {\n"
"    background: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QSlider::handle:vertical::pressed {\n"
"    background: rgba(205, 205, 205, 255);\n"
"}")
        self.verticalSlider_LeftRight.setOrientation(Qt.Vertical)

        self.verticalLayout_13.addWidget(self.verticalSlider_LeftRight)

        self.button_speed_minus_lr = QPushButton(self.frame_2)
        self.button_speed_minus_lr.setObjectName(u"button_speed_minus_lr")
        self.button_speed_minus_lr.setMinimumSize(QSize(80, 53))
        self.button_speed_minus_lr.setMaximumSize(QSize(80, 53))
        self.button_speed_minus_lr.setFont(font4)
        self.button_speed_minus_lr.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_13.addWidget(self.button_speed_minus_lr)


        self.horizontalLayout_15.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(102, 0))
        self.frame_3.setMaximumSize(QSize(102, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.button_speed_plus_ud = QPushButton(self.frame_3)
        self.button_speed_plus_ud.setObjectName(u"button_speed_plus_ud")
        self.button_speed_plus_ud.setMinimumSize(QSize(80, 53))
        self.button_speed_plus_ud.setMaximumSize(QSize(80, 53))
        self.button_speed_plus_ud.setFont(font4)
        self.button_speed_plus_ud.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.button_speed_plus_ud)

        self.verticalSlider_UpDown = QSlider(self.frame_3)
        self.verticalSlider_UpDown.setObjectName(u"verticalSlider_UpDown")
        self.verticalSlider_UpDown.setMinimumSize(QSize(82, 0))
        self.verticalSlider_UpDown.setMaximumSize(QSize(16777215, 16777215))
        self.verticalSlider_UpDown.setStyleSheet(u".QSlider {\n"
"    min-Width: 80px;\n"
"    /*max-height: 80px;*/\n"
"	background:rgba(0,0,0,0);\n"
"	border: 1px solid rgba(0,0,0,0);\n"
"}\n"
"\n"
".QSlider::groove:vertical {\n"
"    border: 1px solid  rgb(180,180,180);\n"
"	border-radius: 4px;\n"
"    width: 7px;\n"
"    background: rgb(140,140,140);\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));\n"
"	border: 1px solid rgba(205,205,205,100);\n"
"	width: 50px;\n"
"    height: 50px;\n"
"    margin: -2px -36px;\n"
"}\n"
"\n"
".QSlider::handle:vertical::hover {\n"
"    background: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QSlider::handle:vertical::pressed {\n"
"    background: rgba(205, 205, 205, 255);\n"
"}")
        self.verticalSlider_UpDown.setOrientation(Qt.Vertical)

        self.verticalLayout_14.addWidget(self.verticalSlider_UpDown)

        self.button_speed_minus_ud = QPushButton(self.frame_3)
        self.button_speed_minus_ud.setObjectName(u"button_speed_minus_ud")
        self.button_speed_minus_ud.setMinimumSize(QSize(80, 53))
        self.button_speed_minus_ud.setMaximumSize(QSize(80, 53))
        self.button_speed_minus_ud.setFont(font4)
        self.button_speed_minus_ud.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_14.addWidget(self.button_speed_minus_ud)


        self.horizontalLayout_15.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(102, 0))
        self.frame_4.setMaximumSize(QSize(102, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.button_speed_plus_fb = QPushButton(self.frame_4)
        self.button_speed_plus_fb.setObjectName(u"button_speed_plus_fb")
        self.button_speed_plus_fb.setMinimumSize(QSize(80, 53))
        self.button_speed_plus_fb.setMaximumSize(QSize(80, 53))
        self.button_speed_plus_fb.setFont(font4)
        self.button_speed_plus_fb.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.button_speed_plus_fb)

        self.verticalSlider_ForwardBack = QSlider(self.frame_4)
        self.verticalSlider_ForwardBack.setObjectName(u"verticalSlider_ForwardBack")
        self.verticalSlider_ForwardBack.setMinimumSize(QSize(82, 0))
        self.verticalSlider_ForwardBack.setMaximumSize(QSize(16777215, 16777215))
        self.verticalSlider_ForwardBack.setStyleSheet(u".QSlider {\n"
"    min-Width: 80px;\n"
"    /*max-height: 80px;*/\n"
"	background:rgba(0,0,0,0);\n"
"	border: 1px solid rgba(0,0,0,0);\n"
"}\n"
"\n"
".QSlider::groove:vertical {\n"
"    border: 1px solid  rgb(180,180,180);\n"
"	border-radius: 4px;\n"
"    width: 7px;\n"
"    background: rgb(140,140,140);\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:vertical {\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));\n"
"	border: 1px solid rgba(205,205,205,100);\n"
"	width: 50px;\n"
"    height: 50px;\n"
"    margin: -2px -36px;\n"
"}\n"
"\n"
".QSlider::handle:vertical::hover {\n"
"    background: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QSlider::handle:vertical::pressed {\n"
"    background: rgba(205, 205, 205, 255);\n"
"}")
        self.verticalSlider_ForwardBack.setOrientation(Qt.Vertical)

        self.verticalLayout_15.addWidget(self.verticalSlider_ForwardBack)

        self.button_speed_minus_fb = QPushButton(self.frame_4)
        self.button_speed_minus_fb.setObjectName(u"button_speed_minus_fb")
        self.button_speed_minus_fb.setMinimumSize(QSize(80, 53))
        self.button_speed_minus_fb.setMaximumSize(QSize(80, 53))
        self.button_speed_minus_fb.setFont(font4)
        self.button_speed_minus_fb.setStyleSheet(u"QPushButton {\n"
"	color:  rgb(100,100,100);;\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.verticalLayout_15.addWidget(self.button_speed_minus_fb)


        self.horizontalLayout_15.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_menu)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 0))
        self.frame_6.setMaximumSize(QSize(16777215, 91))
        self.frame_6.setStyleSheet(u"background:rgab(0,0,0,0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(102, 0))
        self.label_5.setMaximumSize(QSize(102, 16777215))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(120, 0))
        self.label_6.setMaximumSize(QSize(102, 16777215))
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_57.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(102, 0))
        self.label_7.setMaximumSize(QSize(102, 16777215))
        self.label_7.setFont(font5)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.label_7)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_5 = QFrame(self.frame_menu)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 60))
        self.frame_5.setStyleSheet(u"background:rgab(0,0,0,0);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.button_save_spd = QPushButton(self.frame_5)
        self.button_save_spd.setObjectName(u"button_save_spd")
        self.button_save_spd.setMinimumSize(QSize(0, 60))
        self.button_save_spd.setMaximumSize(QSize(16777215, 60))
        self.button_save_spd.setFont(font1)
        self.button_save_spd.setLayoutDirection(Qt.LeftToRight)
        self.button_save_spd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	height: 70px;\n"
"	border-radius: 12px\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/Assets/icon/U_H.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_save_spd.setIcon(icon1)
        self.button_save_spd.setIconSize(QSize(35, 35))
        self.button_save_spd.setCheckable(True)
        self.button_save_spd.setChecked(False)

        self.horizontalLayout_18.addWidget(self.button_save_spd)

        self.button_undo_spd = QPushButton(self.frame_5)
        self.button_undo_spd.setObjectName(u"button_undo_spd")
        self.button_undo_spd.setMinimumSize(QSize(0, 60))
        self.button_undo_spd.setMaximumSize(QSize(16777215, 60))
        self.button_undo_spd.setFont(font1)
        self.button_undo_spd.setLayoutDirection(Qt.LeftToRight)
        self.button_undo_spd.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 100);\n"
"	height: 70px;\n"
"	border-radius: 12px\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	\n"
"}\n"
"")
        self.button_undo_spd.setIcon(icon1)
        self.button_undo_spd.setIconSize(QSize(35, 35))
        self.button_undo_spd.setCheckable(True)
        self.button_undo_spd.setChecked(False)

        self.horizontalLayout_18.addWidget(self.button_undo_spd)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_menu)

        self.frame_option = QFrame(self.frame_content)
        self.frame_option.setObjectName(u"frame_option")
        self.frame_option.setMinimumSize(QSize(0, 0))
        self.frame_option.setStyleSheet(u"background-color: white")
        self.frame_option.setFrameShape(QFrame.StyledPanel)
        self.frame_option.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_option)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_option)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Page_main = QWidget()
        self.Page_main.setObjectName(u"Page_main")
        self.verticalLayout_3 = QVBoxLayout(self.Page_main)
        self.verticalLayout_3.setSpacing(7)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(7, 0, 7, 0)
        self.frame_8 = QFrame(self.Page_main)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_lrud = QFrame(self.frame_8)
        self.frame_lrud.setObjectName(u"frame_lrud")
        self.frame_lrud.setFrameShape(QFrame.StyledPanel)
        self.frame_lrud.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_lrud)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_9 = QFrame(self.frame_lrud)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.button_move_up = QPushButton(self.frame_9)
        self.button_move_up.setObjectName(u"button_move_up")
        self.button_move_up.setMinimumSize(QSize(180, 180))
        self.button_move_up.setMaximumSize(QSize(180, 180))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI Semibold"])
        font6.setPointSize(18)
        font6.setBold(True)
        self.button_move_up.setFont(font6)
        self.button_move_up.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_up.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.button_move_up)


        self.verticalLayout_16.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_lrud)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.button_move_left = QPushButton(self.frame_10)
        self.button_move_left.setObjectName(u"button_move_left")
        self.button_move_left.setMinimumSize(QSize(180, 180))
        self.button_move_left.setMaximumSize(QSize(180, 180))
        self.button_move_left.setFont(font6)
        self.button_move_left.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_left.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.button_move_left)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.button_move_right = QPushButton(self.frame_10)
        self.button_move_right.setObjectName(u"button_move_right")
        self.button_move_right.setMinimumSize(QSize(180, 180))
        self.button_move_right.setMaximumSize(QSize(180, 180))
        self.button_move_right.setFont(font6)
        self.button_move_right.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_right.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.horizontalLayout_8.addWidget(self.button_move_right)


        self.verticalLayout_16.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_lrud)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.button_move_down = QPushButton(self.frame_11)
        self.button_move_down.setObjectName(u"button_move_down")
        self.button_move_down.setMinimumSize(QSize(180, 180))
        self.button_move_down.setMaximumSize(QSize(180, 180))
        self.button_move_down.setFont(font6)
        self.button_move_down.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_down.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.horizontalLayout_7.addWidget(self.button_move_down)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_lrud)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.button_main_connect = QPushButton(self.frame_12)
        self.button_main_connect.setObjectName(u"button_main_connect")
        self.button_main_connect.setMinimumSize(QSize(180, 49))
        self.button_main_connect.setMaximumSize(QSize(180, 49))
        self.button_main_connect.setFont(font2)
        self.button_main_connect.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_main_connect.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_19.addWidget(self.button_main_connect)


        self.verticalLayout_16.addWidget(self.frame_12)


        self.horizontalLayout_9.addWidget(self.frame_lrud)

        self.frame_fb = QFrame(self.frame_8)
        self.frame_fb.setObjectName(u"frame_fb")
        self.frame_fb.setMaximumSize(QSize(206, 16777215))
        self.frame_fb.setFrameShape(QFrame.StyledPanel)
        self.frame_fb.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_fb)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.button_move_fwd = QPushButton(self.frame_fb)
        self.button_move_fwd.setObjectName(u"button_move_fwd")
        self.button_move_fwd.setMinimumSize(QSize(180, 180))
        self.button_move_fwd.setMaximumSize(QSize(180, 180))
        self.button_move_fwd.setFont(font6)
        self.button_move_fwd.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_fwd.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.button_move_fwd)

        self.button_move_bwd = QPushButton(self.frame_fb)
        self.button_move_bwd.setObjectName(u"button_move_bwd")
        self.button_move_bwd.setMinimumSize(QSize(180, 180))
        self.button_move_bwd.setMaximumSize(QSize(180, 180))
        self.button_move_bwd.setFont(font6)
        self.button_move_bwd.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_move_bwd.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 30px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);;\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.verticalLayout_10.addWidget(self.button_move_bwd)


        self.horizontalLayout_9.addWidget(self.frame_fb)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.Page_main)
        self.Page1 = QWidget()
        self.Page1.setObjectName(u"Page1")
        self.verticalLayout_4 = QVBoxLayout(self.Page1)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(7, 0, 7, 0)
        self.stackedWidget.addWidget(self.Page1)
        self.Page_Horizontal = QWidget()
        self.Page_Horizontal.setObjectName(u"Page_Horizontal")
        self.verticalLayout_5 = QVBoxLayout(self.Page_Horizontal)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(7, 0, 7, 0)
        self.sub_frame_speed_show_h = QFrame(self.Page_Horizontal)
        self.sub_frame_speed_show_h.setObjectName(u"sub_frame_speed_show_h")
        self.sub_frame_speed_show_h.setMaximumSize(QSize(16777215, 110))
        self.sub_frame_speed_show_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_speed_show_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.sub_frame_speed_show_h)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_scanSpeed_h = QLabel(self.sub_frame_speed_show_h)
        self.label_scanSpeed_h.setObjectName(u"label_scanSpeed_h")
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(15)
        font7.setBold(False)
        self.label_scanSpeed_h.setFont(font7)
        self.label_scanSpeed_h.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_scanSpeed_h.setMargin(20)

        self.horizontalLayout_13.addWidget(self.label_scanSpeed_h)

        self.label_scanSpeed_val_h_2 = QLabel(self.sub_frame_speed_show_h)
        self.label_scanSpeed_val_h_2.setObjectName(u"label_scanSpeed_val_h_2")
        self.label_scanSpeed_val_h_2.setMinimumSize(QSize(270, 0))
        self.label_scanSpeed_val_h_2.setMaximumSize(QSize(270, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Consolas"])
        font8.setPointSize(26)
        self.label_scanSpeed_val_h_2.setFont(font8)
        self.label_scanSpeed_val_h_2.setLayoutDirection(Qt.LeftToRight)
        self.label_scanSpeed_val_h_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_scanSpeed_val_h_2.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_scanSpeed_val_h_2)

        self.label_scanSpeed_val_h = QLabel(self.sub_frame_speed_show_h)
        self.label_scanSpeed_val_h.setObjectName(u"label_scanSpeed_val_h")
        self.label_scanSpeed_val_h.setMinimumSize(QSize(0, 0))
        self.label_scanSpeed_val_h.setMaximumSize(QSize(16777215, 16777215))
        self.label_scanSpeed_val_h.setFont(font8)
        self.label_scanSpeed_val_h.setLayoutDirection(Qt.LeftToRight)
        self.label_scanSpeed_val_h.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_scanSpeed_val_h.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_scanSpeed_val_h)

        self.label_scanSpeed_val_h_actual = QLabel(self.sub_frame_speed_show_h)
        self.label_scanSpeed_val_h_actual.setObjectName(u"label_scanSpeed_val_h_actual")
        self.label_scanSpeed_val_h_actual.setMinimumSize(QSize(156, 0))
        self.label_scanSpeed_val_h_actual.setMaximumSize(QSize(156, 16777215))
        font9 = QFont()
        font9.setFamilies([u"Consolas"])
        font9.setPointSize(10)
        self.label_scanSpeed_val_h_actual.setFont(font9)
        self.label_scanSpeed_val_h_actual.setLayoutDirection(Qt.LeftToRight)
        self.label_scanSpeed_val_h_actual.setStyleSheet(u"color:#909090;")
        self.label_scanSpeed_val_h_actual.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_scanSpeed_val_h_actual.setMargin(0)

        self.horizontalLayout_13.addWidget(self.label_scanSpeed_val_h_actual)

        self.sub_frame_studyID_h = QFrame(self.sub_frame_speed_show_h)
        self.sub_frame_studyID_h.setObjectName(u"sub_frame_studyID_h")
        self.sub_frame_studyID_h.setMinimumSize(QSize(267, 64))
        self.sub_frame_studyID_h.setMaximumSize(QSize(267, 64))
        self.sub_frame_studyID_h.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgb(170,170,170);\n"
"\n"
"")
        self.sub_frame_studyID_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_studyID_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.sub_frame_studyID_h)
        self.horizontalLayout_44.setSpacing(7)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(7, 0, 7, 0)
        self.label_scanID_h = QLabel(self.sub_frame_studyID_h)
        self.label_scanID_h.setObjectName(u"label_scanID_h")
        font10 = QFont()
        font10.setFamilies([u"Segoe UI Semibold"])
        font10.setPointSize(14)
        font10.setBold(False)
        self.label_scanID_h.setFont(font10)
        self.label_scanID_h.setStyleSheet(u"border: 0px; background:rgba(0,0,0,0);")
        self.label_scanID_h.setMargin(20)

        self.horizontalLayout_44.addWidget(self.label_scanID_h)

        self.frame_studyID_h = QFrame(self.sub_frame_studyID_h)
        self.frame_studyID_h.setObjectName(u"frame_studyID_h")
        self.frame_studyID_h.setMaximumSize(QSize(16777215, 38))
        font11 = QFont()
        font11.setFamilies([u"Segoe UI"])
        self.frame_studyID_h.setFont(font11)
        self.frame_studyID_h.setStyleSheet(u"	border-radius: 14px; \n"
"	color: black;\n"
"	background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 rgba(255,255,255,255), stop:0 rgba(245,245,245,255));\n"
"/*qradialgradient(cx:0,cy:0,radius:1,fx:0.5,fy:0.5,stop:1 rgba(205, 205, 205, 205), stop:0 rgba(170, 170, 170, 255));*/\n"
"	border: 1px solid rgb(170,170,170);")
        self.frame_studyID_h.setFrameShape(QFrame.StyledPanel)
        self.frame_studyID_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_studyID_h)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(20, 2, 20, 5)
        self.textEdit_studyID_h = QTextEdit(self.frame_studyID_h)
        self.textEdit_studyID_h.setObjectName(u"textEdit_studyID_h")
        font12 = QFont()
        font12.setFamilies([u"Segoe UI Semibold"])
        font12.setPointSize(14)
        self.textEdit_studyID_h.setFont(font12)
        self.textEdit_studyID_h.setStyleSheet(u"	border-radius: 10px; \n"
"	background-color: rgba(0,0,0,0);\n"
"	border-radius: 20px;\n"
"	/*background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:1 rgba(205, 205, 205, 205), stop:0 rgba(170, 170, 170, 255));*/\n"
"	border: 0px solid rgb(170,170,170);")
        self.textEdit_studyID_h.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_studyID_h.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_43.addWidget(self.textEdit_studyID_h)


        self.horizontalLayout_44.addWidget(self.frame_studyID_h)


        self.horizontalLayout_13.addWidget(self.sub_frame_studyID_h)


        self.verticalLayout_5.addWidget(self.sub_frame_speed_show_h)

        self.sub_frame_speed_adjust_h = QFrame(self.Page_Horizontal)
        self.sub_frame_speed_adjust_h.setObjectName(u"sub_frame_speed_adjust_h")
        self.sub_frame_speed_adjust_h.setMaximumSize(QSize(16777215, 110))
        self.sub_frame_speed_adjust_h.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgb(170,170,170);\n"
"\n"
"")
        self.sub_frame_speed_adjust_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_speed_adjust_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.sub_frame_speed_adjust_h)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 11, -1, -1)
        self.button_speed_minus_h = QPushButton(self.sub_frame_speed_adjust_h)
        self.button_speed_minus_h.setObjectName(u"button_speed_minus_h")
        self.button_speed_minus_h.setMinimumSize(QSize(53, 53))
        self.button_speed_minus_h.setMaximumSize(QSize(53, 53))
        self.button_speed_minus_h.setFont(font4)
        self.button_speed_minus_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.button_speed_minus_h)

        self.slider_speed_h = QSlider(self.sub_frame_speed_adjust_h)
        self.slider_speed_h.setObjectName(u"slider_speed_h")
        self.slider_speed_h.setMinimumSize(QSize(0, 82))
        self.slider_speed_h.setMaximumSize(QSize(16777215, 82))
        self.slider_speed_h.setStyleSheet(u".QSlider {\n"
"    min-height: 80px;\n"
"    max-height: 80px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 1px solid rgba(0,0,0,0);\n"
"}\n"
"\n"
".QSlider::groove:horizontal {\n"
"    border: 1px solid  rgb(180,180,180);\n"
"	border-radius: 4px;\n"
"    height: 7px;\n"
"    background: rgb(140,140,140);\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal {\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));\n"
"	border: 1px solid rgba(205,205,205,100);\n"
"	width: 50px;\n"
"    height: 120px;\n"
"    margin: -24px -12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal::hover {\n"
"    background: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QSlider::handle:horizontal::pressed {\n"
"    background: rgba(205, 205, 205, 255);\n"
"}")
        self.slider_speed_h.setOrientation(Qt.Horizontal)

        self.horizontalLayout_12.addWidget(self.slider_speed_h)

        self.button_speed_plus_h = QPushButton(self.sub_frame_speed_adjust_h)
        self.button_speed_plus_h.setObjectName(u"button_speed_plus_h")
        self.button_speed_plus_h.setMinimumSize(QSize(53, 53))
        self.button_speed_plus_h.setMaximumSize(QSize(53, 53))
        self.button_speed_plus_h.setFont(font4)
        self.button_speed_plus_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.button_speed_plus_h)


        self.verticalLayout_5.addWidget(self.sub_frame_speed_adjust_h)

        self.line_2_h = QFrame(self.Page_Horizontal)
        self.line_2_h.setObjectName(u"line_2_h")
        font13 = QFont()
        font13.setKerning(True)
        self.line_2_h.setFont(font13)
        self.line_2_h.setStyleSheet(u"	color: rgba(255,255,255,0);\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));*/\n"
"")
        self.line_2_h.setLineWidth(0)
        self.line_2_h.setFrameShape(QFrame.HLine)
        self.line_2_h.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_2_h)

        self.sub_frame_dist_show_h = QFrame(self.Page_Horizontal)
        self.sub_frame_dist_show_h.setObjectName(u"sub_frame_dist_show_h")
        self.sub_frame_dist_show_h.setMaximumSize(QSize(16777215, 110))
        self.sub_frame_dist_show_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_dist_show_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.sub_frame_dist_show_h)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_scanDist_h = QLabel(self.sub_frame_dist_show_h)
        self.label_scanDist_h.setObjectName(u"label_scanDist_h")
        self.label_scanDist_h.setFont(font7)
        self.label_scanDist_h.setMargin(20)

        self.horizontalLayout_14.addWidget(self.label_scanDist_h)

        self.label_scanDist_val_h = QLabel(self.sub_frame_dist_show_h)
        self.label_scanDist_val_h.setObjectName(u"label_scanDist_val_h")
        self.label_scanDist_val_h.setFont(font8)
        self.label_scanDist_val_h.setLayoutDirection(Qt.LeftToRight)
        self.label_scanDist_val_h.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_scanDist_val_h.setMargin(0)

        self.horizontalLayout_14.addWidget(self.label_scanDist_val_h)

        self.label_scanDist_filler_h = QLabel(self.sub_frame_dist_show_h)
        self.label_scanDist_filler_h.setObjectName(u"label_scanDist_filler_h")

        self.horizontalLayout_14.addWidget(self.label_scanDist_filler_h)


        self.verticalLayout_5.addWidget(self.sub_frame_dist_show_h)

        self.sub_frame_dist_adjust_h = QFrame(self.Page_Horizontal)
        self.sub_frame_dist_adjust_h.setObjectName(u"sub_frame_dist_adjust_h")
        self.sub_frame_dist_adjust_h.setMaximumSize(QSize(16777215, 110))
        self.sub_frame_dist_adjust_h.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	border-radius: 20px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgb(170,170,170);\n"
"\n"
"")
        self.sub_frame_dist_adjust_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_dist_adjust_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.sub_frame_dist_adjust_h)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.button_dist_minus_h = QPushButton(self.sub_frame_dist_adjust_h)
        self.button_dist_minus_h.setObjectName(u"button_dist_minus_h")
        self.button_dist_minus_h.setMinimumSize(QSize(53, 53))
        self.button_dist_minus_h.setMaximumSize(QSize(53, 53))
        self.button_dist_minus_h.setFont(font4)
        self.button_dist_minus_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.button_dist_minus_h)

        self.slider_dist_h = QSlider(self.sub_frame_dist_adjust_h)
        self.slider_dist_h.setObjectName(u"slider_dist_h")
        self.slider_dist_h.setMinimumSize(QSize(0, 82))
        self.slider_dist_h.setMaximumSize(QSize(16777215, 82))
        self.slider_dist_h.setStyleSheet(u".QSlider {\n"
"    min-height: 80px;\n"
"    max-height: 80px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 1px solid rgba(0,0,0,0);\n"
"}\n"
"\n"
".QSlider::groove:horizontal {\n"
"    border: 1px solid  rgb(180,180,180);\n"
"	border-radius: 4px;\n"
"    height: 7px;\n"
"    background: rgb(140,140,140);\n"
"    margin: 0 12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal {\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(255, 255, 255, 255), stop:1 rgba(245, 245, 245, 255));\n"
"	border: 1px solid rgba(205,205,205,100);\n"
"	width: 50px;\n"
"    height: 120px;\n"
"    margin: -24px -12px;\n"
"}\n"
"\n"
".QSlider::handle:horizontal::hover {\n"
"    background: rgb(224, 238, 249);\n"
"}\n"
"\n"
".QSlider::handle:horizontal::pressed {\n"
"    background: rgba(205, 205, 205, 255);\n"
"}")
        self.slider_dist_h.setOrientation(Qt.Horizontal)

        self.horizontalLayout_11.addWidget(self.slider_dist_h)

        self.button_dist_plus_h = QPushButton(self.sub_frame_dist_adjust_h)
        self.button_dist_plus_h.setObjectName(u"button_dist_plus_h")
        self.button_dist_plus_h.setMinimumSize(QSize(53, 53))
        self.button_dist_plus_h.setMaximumSize(QSize(53, 53))
        self.button_dist_plus_h.setFont(font4)
        self.button_dist_plus_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 10px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255205), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.05,fy:0.05,stop:0 rgba(205, 205, 205, 0), stop:1 rgba(170, 170, 170, 0));\n"
"	border: 1px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.button_dist_plus_h)


        self.verticalLayout_5.addWidget(self.sub_frame_dist_adjust_h)

        self.line_3_h = QFrame(self.Page_Horizontal)
        self.line_3_h.setObjectName(u"line_3_h")
        self.line_3_h.setLineWidth(-1)
        self.line_3_h.setFrameShape(QFrame.HLine)
        self.line_3_h.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_3_h)

        self.sub_frame_direction_h = QFrame(self.Page_Horizontal)
        self.sub_frame_direction_h.setObjectName(u"sub_frame_direction_h")
        self.sub_frame_direction_h.setMaximumSize(QSize(16777215, 200))
        self.sub_frame_direction_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_direction_h.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.sub_frame_direction_h)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_gazedir_h_filler = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h_filler.setObjectName(u"label_gazedir_h_filler")
        font14 = QFont()
        font14.setFamilies([u"Segoe UI"])
        font14.setPointSize(12)
        font14.setBold(False)
        self.label_gazedir_h_filler.setFont(font14)
        self.label_gazedir_h_filler.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h_filler, 0, 0, 2, 1)

        self.button_gazedir_h_1 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_1.setObjectName(u"button_gazedir_h_1")
        self.button_gazedir_h_1.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_1.setMaximumSize(QSize(112, 40))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI Semibold"])
        font15.setPointSize(10)
        font15.setBold(True)
        self.button_gazedir_h_1.setFont(font15)
        self.button_gazedir_h_1.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_1, 0, 1, 2, 1)

        self.button_gazedir_h_2 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_2.setObjectName(u"button_gazedir_h_2")
        self.button_gazedir_h_2.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_2.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_2.setFont(font15)
        self.button_gazedir_h_2.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_2, 0, 2, 2, 1)

        self.button_gazedir_h_3 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_3.setObjectName(u"button_gazedir_h_3")
        self.button_gazedir_h_3.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_3.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_3.setFont(font15)
        self.button_gazedir_h_3.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_3, 0, 3, 2, 1)

        self.label_gazedir_h_filler_3 = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h_filler_3.setObjectName(u"label_gazedir_h_filler_3")
        self.label_gazedir_h_filler_3.setFont(font14)
        self.label_gazedir_h_filler_3.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h_filler_3, 0, 4, 1, 1)

        self.label_gazedir_h_filler_4 = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h_filler_4.setObjectName(u"label_gazedir_h_filler_4")
        self.label_gazedir_h_filler_4.setFont(font14)
        self.label_gazedir_h_filler_4.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h_filler_4, 1, 4, 2, 1)

        self.label_gazedir_h = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h.setObjectName(u"label_gazedir_h")
        self.label_gazedir_h.setFont(font14)
        self.label_gazedir_h.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h, 2, 0, 2, 1)

        self.button_gazedir_h_4 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_4.setObjectName(u"button_gazedir_h_4")
        self.button_gazedir_h_4.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_4.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_4.setFont(font15)
        self.button_gazedir_h_4.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_4, 2, 1, 2, 1)

        self.button_gazedir_h_5 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_5.setObjectName(u"button_gazedir_h_5")
        self.button_gazedir_h_5.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_5.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_5.setFont(font15)
        self.button_gazedir_h_5.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_5, 2, 2, 2, 1)

        self.button_gazedir_h_6 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_6.setObjectName(u"button_gazedir_h_6")
        self.button_gazedir_h_6.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_6.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_6.setFont(font15)
        self.button_gazedir_h_6.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_6, 2, 3, 2, 1)

        self.label_gazedir_h_filler_5 = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h_filler_5.setObjectName(u"label_gazedir_h_filler_5")
        self.label_gazedir_h_filler_5.setFont(font14)
        self.label_gazedir_h_filler_5.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h_filler_5, 3, 4, 2, 1)

        self.label_gazedir_h_filler_2 = QLabel(self.sub_frame_direction_h)
        self.label_gazedir_h_filler_2.setObjectName(u"label_gazedir_h_filler_2")
        self.label_gazedir_h_filler_2.setFont(font14)
        self.label_gazedir_h_filler_2.setMargin(0)

        self.gridLayout_3.addWidget(self.label_gazedir_h_filler_2, 4, 0, 1, 1)

        self.button_gazedir_h_7 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_7.setObjectName(u"button_gazedir_h_7")
        self.button_gazedir_h_7.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_7.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_7.setFont(font15)
        self.button_gazedir_h_7.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_7, 4, 1, 1, 1)

        self.button_gazedir_h_8 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_8.setObjectName(u"button_gazedir_h_8")
        self.button_gazedir_h_8.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_8.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_8.setFont(font15)
        self.button_gazedir_h_8.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_8, 4, 2, 1, 1)

        self.button_gazedir_h_9 = QPushButton(self.sub_frame_direction_h)
        self.button_gazedir_h_9.setObjectName(u"button_gazedir_h_9")
        self.button_gazedir_h_9.setMinimumSize(QSize(112, 40))
        self.button_gazedir_h_9.setMaximumSize(QSize(112, 40))
        self.button_gazedir_h_9.setFont(font15)
        self.button_gazedir_h_9.setStyleSheet(u"QPushButton {\n"
"	color: black;\n"
"	border-radius: 14px;\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(252,252,252,255), stop:1 rgba(240,240,240,255));\n"
"	border: 0px solid rgba(170,170,170, 100);\n"
"}\n"
"")

        self.gridLayout_3.addWidget(self.button_gazedir_h_9, 4, 3, 1, 1)


        self.verticalLayout_5.addWidget(self.sub_frame_direction_h)

        self.sub_frame_buttons_h = QFrame(self.Page_Horizontal)
        self.sub_frame_buttons_h.setObjectName(u"sub_frame_buttons_h")
        self.sub_frame_buttons_h.setMaximumSize(QSize(16777215, 110))
        self.sub_frame_buttons_h.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_buttons_h.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.sub_frame_buttons_h)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.button_saveSetting_h = QPushButton(self.sub_frame_buttons_h)
        self.button_saveSetting_h.setObjectName(u"button_saveSetting_h")
        self.button_saveSetting_h.setMinimumSize(QSize(96, 49))
        self.button_saveSetting_h.setMaximumSize(QSize(96, 49))
        self.button_saveSetting_h.setFont(font2)
        self.button_saveSetting_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.button_saveSetting_h)

        self.button_restoreSetting_h = QPushButton(self.sub_frame_buttons_h)
        self.button_restoreSetting_h.setObjectName(u"button_restoreSetting_h")
        self.button_restoreSetting_h.setMinimumSize(QSize(96, 49))
        self.button_restoreSetting_h.setMaximumSize(QSize(96, 49))
        self.button_restoreSetting_h.setFont(font2)
        self.button_restoreSetting_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_16.addWidget(self.button_restoreSetting_h)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_6)

        self.button_start_scan_h = QPushButton(self.sub_frame_buttons_h)
        self.button_start_scan_h.setObjectName(u"button_start_scan_h")
        self.button_start_scan_h.setMinimumSize(QSize(145, 49))
        self.button_start_scan_h.setMaximumSize(QSize(145, 49))
        self.button_start_scan_h.setFont(font2)
        self.button_start_scan_h.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_start_scan_h.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}")

        self.horizontalLayout_16.addWidget(self.button_start_scan_h)


        self.verticalLayout_5.addWidget(self.sub_frame_buttons_h)

        self.stackedWidget.addWidget(self.Page_Horizontal)
        self.Page_About = QWidget()
        self.Page_About.setObjectName(u"Page_About")
        self.verticalLayout_7 = QVBoxLayout(self.Page_About)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_softInfo = QFrame(self.Page_About)
        self.frame_softInfo.setObjectName(u"frame_softInfo")
        self.frame_softInfo.setMinimumSize(QSize(0, 320))
        self.frame_softInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_softInfo.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_softInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_logo = QLabel(self.frame_softInfo)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(0, 0))
        self.label_logo.setPixmap(QPixmap(u":/icon/Assets/icon/logo.png"))

        self.gridLayout.addWidget(self.label_logo, 0, 0, 2, 1)

        self.label_softInfo_1 = QLabel(self.frame_softInfo)
        self.label_softInfo_1.setObjectName(u"label_softInfo_1")
        font16 = QFont()
        font16.setFamilies([u"Segoe UI Semibold"])
        font16.setPointSize(24)
        self.label_softInfo_1.setFont(font16)
        self.label_softInfo_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_softInfo_1, 0, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 1, 1, 1)

        self.label_softinfo_2 = QLabel(self.frame_softInfo)
        self.label_softinfo_2.setObjectName(u"label_softinfo_2")
        font17 = QFont()
        font17.setFamilies([u"Segoe UI"])
        font17.setPointSize(14)
        self.label_softinfo_2.setFont(font17)
        self.label_softinfo_2.setLayoutDirection(Qt.LeftToRight)
        self.label_softinfo_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_softinfo_2, 1, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 3, 1, 1)


        self.verticalLayout_7.addWidget(self.frame_softInfo)

        self.frame_connection_status = QFrame(self.Page_About)
        self.frame_connection_status.setObjectName(u"frame_connection_status")
        self.frame_connection_status.setMaximumSize(QSize(16777215, 120))
        self.frame_connection_status.setFrameShape(QFrame.StyledPanel)
        self.frame_connection_status.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_connection_status)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")

        self.verticalLayout_7.addWidget(self.frame_connection_status)

        self.frame_device_option = QFrame(self.Page_About)
        self.frame_device_option.setObjectName(u"frame_device_option")
        self.frame_device_option.setFrameShape(QFrame.StyledPanel)
        self.frame_device_option.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_device_option)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_about_back = QPushButton(self.frame_device_option)
        self.button_about_back.setObjectName(u"button_about_back")
        self.button_about_back.setMinimumSize(QSize(200, 70))
        self.button_about_back.setMaximumSize(QSize(200, 70))
        self.button_about_back.setFont(font2)
        self.button_about_back.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.button_about_back)


        self.verticalLayout_7.addWidget(self.frame_device_option)

        self.stackedWidget.addWidget(self.Page_About)
        self.Page_Output = QWidget()
        self.Page_Output.setObjectName(u"Page_Output")
        self.verticalLayout_6 = QVBoxLayout(self.Page_Output)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.stackedWidget.addWidget(self.Page_Output)
        self.Page_Setting = QWidget()
        self.Page_Setting.setObjectName(u"Page_Setting")
        self.verticalLayout_9 = QVBoxLayout(self.Page_Setting)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.sub_frame_setting_scanning_title = QFrame(self.Page_Setting)
        self.sub_frame_setting_scanning_title.setObjectName(u"sub_frame_setting_scanning_title")
        self.sub_frame_setting_scanning_title.setMinimumSize(QSize(0, 70))
        self.sub_frame_setting_scanning_title.setMaximumSize(QSize(16777215, 50))
        self.sub_frame_setting_scanning_title.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.sub_frame_setting_scanning_title)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_setting_scanning = QLabel(self.sub_frame_setting_scanning_title)
        self.label_setting_scanning.setObjectName(u"label_setting_scanning")
        self.label_setting_scanning.setFont(font7)
        self.label_setting_scanning.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_setting_scanning.setMargin(20)

        self.horizontalLayout_23.addWidget(self.label_setting_scanning)

        self.label_setting_scanning_filler_2 = QLabel(self.sub_frame_setting_scanning_title)
        self.label_setting_scanning_filler_2.setObjectName(u"label_setting_scanning_filler_2")
        self.label_setting_scanning_filler_2.setFont(font8)
        self.label_setting_scanning_filler_2.setLayoutDirection(Qt.LeftToRight)
        self.label_setting_scanning_filler_2.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.label_setting_scanning_filler_2.setMargin(0)

        self.horizontalLayout_23.addWidget(self.label_setting_scanning_filler_2)

        self.label_setting_scanning_filler = QLabel(self.sub_frame_setting_scanning_title)
        self.label_setting_scanning_filler.setObjectName(u"label_setting_scanning_filler")

        self.horizontalLayout_23.addWidget(self.label_setting_scanning_filler)


        self.verticalLayout_9.addWidget(self.sub_frame_setting_scanning_title)

        self.sub_frame_setting_scanning = QFrame(self.Page_Setting)
        self.sub_frame_setting_scanning.setObjectName(u"sub_frame_setting_scanning")
        self.sub_frame_setting_scanning.setMinimumSize(QSize(0, 244))
        self.sub_frame_setting_scanning.setMaximumSize(QSize(16777215, 244))
        self.sub_frame_setting_scanning.setStyleSheet(u"	border: 2px solid white;\n"
"	border-radius: 20px;")
        self.sub_frame_setting_scanning.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.sub_frame_setting_scanning)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, -1, 0, -1)
        self.sub_frame_setting_scanning_header = QFrame(self.sub_frame_setting_scanning)
        self.sub_frame_setting_scanning_header.setObjectName(u"sub_frame_setting_scanning_header")
        self.sub_frame_setting_scanning_header.setMinimumSize(QSize(0, 60))
        self.sub_frame_setting_scanning_header.setMaximumSize(QSize(16777215, 60))
        font18 = QFont()
        font18.setPointSize(4)
        self.sub_frame_setting_scanning_header.setFont(font18)
        self.sub_frame_setting_scanning_header.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	/*border-radius: 20px;\n"
"    background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 0px solid rgb(170,170,170);\n"
"	border-radius:0px;\n"
"    border-top-left-radius:20px;\n"
"    border-top-right-radius:20px;\n"
"\n"
"")
        self.sub_frame_setting_scanning_header.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.sub_frame_setting_scanning_header)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_set_scan_type = QLabel(self.sub_frame_setting_scanning_header)
        self.label_set_scan_type.setObjectName(u"label_set_scan_type")
        self.label_set_scan_type.setMinimumSize(QSize(220, 60))
        self.label_set_scan_type.setMaximumSize(QSize(220, 60))
        font19 = QFont()
        font19.setFamilies([u"Segoe UI Semibold"])
        font19.setPointSize(12)
        self.label_set_scan_type.setFont(font19)
        self.label_set_scan_type.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px;\n"
"border-top-left-radius:20px;")
        self.label_set_scan_type.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_set_scan_type)

        self.label_set_scan_spd_range = QLabel(self.sub_frame_setting_scanning_header)
        self.label_set_scan_spd_range.setObjectName(u"label_set_scan_spd_range")
        self.label_set_scan_spd_range.setMinimumSize(QSize(192, 60))
        self.label_set_scan_spd_range.setMaximumSize(QSize(192, 60))
        self.label_set_scan_spd_range.setFont(font19)
        self.label_set_scan_spd_range.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_scan_spd_range.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_set_scan_spd_range)

        self.label_set_spd_step = QLabel(self.sub_frame_setting_scanning_header)
        self.label_set_spd_step.setObjectName(u"label_set_spd_step")
        self.label_set_spd_step.setMinimumSize(QSize(0, 60))
        self.label_set_spd_step.setMaximumSize(QSize(16777215, 60))
        self.label_set_spd_step.setFont(font19)
        self.label_set_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_spd_step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_set_spd_step)


        self.verticalLayout_8.addWidget(self.sub_frame_setting_scanning_header)

        self.sub_frame_setting_scanning_radial = QFrame(self.sub_frame_setting_scanning)
        self.sub_frame_setting_scanning_radial.setObjectName(u"sub_frame_setting_scanning_radial")
        self.sub_frame_setting_scanning_radial.setMinimumSize(QSize(0, 60))
        self.sub_frame_setting_scanning_radial.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_setting_scanning_radial.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	/*border-radius: 20px;\\n    background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:rgb(230,230,230);\n"
"    border: 0px solid rgb(170,170,170);\n"
"	border-radius:0px;")
        self.sub_frame_setting_scanning_radial.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning_radial.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.sub_frame_setting_scanning_radial)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_set_radial = QLabel(self.sub_frame_setting_scanning_radial)
        self.label_set_radial.setObjectName(u"label_set_radial")
        self.label_set_radial.setMinimumSize(QSize(220, 60))
        self.label_set_radial.setMaximumSize(QSize(220, 60))
        self.label_set_radial.setFont(font19)
        self.label_set_radial.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_radial.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.label_set_radial)

        self.sub_frame_r_spd_range = QFrame(self.sub_frame_setting_scanning_radial)
        self.sub_frame_r_spd_range.setObjectName(u"sub_frame_r_spd_range")
        self.sub_frame_r_spd_range.setMinimumSize(QSize(192, 60))
        self.sub_frame_r_spd_range.setMaximumSize(QSize(192, 60))
        self.sub_frame_r_spd_range.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_r_spd_range.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_r_spd_range.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.sub_frame_r_spd_range)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 11, 0, 11)
        self.textEdit_lr_spd_range_max = QTextEdit(self.sub_frame_r_spd_range)
        self.textEdit_lr_spd_range_max.setObjectName(u"textEdit_lr_spd_range_max")
        self.textEdit_lr_spd_range_max.setMinimumSize(QSize(0, 0))
        self.textEdit_lr_spd_range_max.setMaximumSize(QSize(16777215, 60))
        font20 = QFont()
        font20.setFamilies([u"Consolas"])
        font20.setPointSize(14)
        self.textEdit_lr_spd_range_max.setFont(font20)
        self.textEdit_lr_spd_range_max.setStyleSheet(u"border:0px;")
        self.textEdit_lr_spd_range_max.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_lr_spd_range_max.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_25.addWidget(self.textEdit_lr_spd_range_max)

        self.textEdit_lr_spd_range_min = QTextEdit(self.sub_frame_r_spd_range)
        self.textEdit_lr_spd_range_min.setObjectName(u"textEdit_lr_spd_range_min")
        self.textEdit_lr_spd_range_min.setMinimumSize(QSize(0, 0))
        self.textEdit_lr_spd_range_min.setMaximumSize(QSize(16777215, 60))
        self.textEdit_lr_spd_range_min.setFont(font20)
        self.textEdit_lr_spd_range_min.setStyleSheet(u"border:0px;")
        self.textEdit_lr_spd_range_min.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_lr_spd_range_min.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_25.addWidget(self.textEdit_lr_spd_range_min)


        self.horizontalLayout_40.addWidget(self.sub_frame_r_spd_range)

        self.sub_frame_r_spd_step = QFrame(self.sub_frame_setting_scanning_radial)
        self.sub_frame_r_spd_step.setObjectName(u"sub_frame_r_spd_step")
        self.sub_frame_r_spd_step.setMinimumSize(QSize(237, 60))
        self.sub_frame_r_spd_step.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_r_spd_step.setFont(font20)
        self.sub_frame_r_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_r_spd_step.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_r_spd_step.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.sub_frame_r_spd_step)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 0, -1, 0)
        self.button_set_lr_spd_plus = QPushButton(self.sub_frame_r_spd_step)
        self.button_set_lr_spd_plus.setObjectName(u"button_set_lr_spd_plus")
        self.button_set_lr_spd_plus.setMinimumSize(QSize(45, 45))
        self.button_set_lr_spd_plus.setMaximumSize(QSize(45, 45))
        self.button_set_lr_spd_plus.setFont(font20)
        self.button_set_lr_spd_plus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_27.addWidget(self.button_set_lr_spd_plus)

        self.label_set_lr_spd_step = QLabel(self.sub_frame_r_spd_step)
        self.label_set_lr_spd_step.setObjectName(u"label_set_lr_spd_step")
        self.label_set_lr_spd_step.setFont(font20)
        self.label_set_lr_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:0px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_lr_spd_step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_set_lr_spd_step)

        self.button_set_lr_spd_minus = QPushButton(self.sub_frame_r_spd_step)
        self.button_set_lr_spd_minus.setObjectName(u"button_set_lr_spd_minus")
        self.button_set_lr_spd_minus.setMinimumSize(QSize(45, 45))
        self.button_set_lr_spd_minus.setMaximumSize(QSize(45, 45))
        self.button_set_lr_spd_minus.setFont(font20)
        self.button_set_lr_spd_minus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_27.addWidget(self.button_set_lr_spd_minus)


        self.horizontalLayout_40.addWidget(self.sub_frame_r_spd_step)


        self.verticalLayout_8.addWidget(self.sub_frame_setting_scanning_radial)

        self.sub_frame_setting_scanning_vertical = QFrame(self.sub_frame_setting_scanning)
        self.sub_frame_setting_scanning_vertical.setObjectName(u"sub_frame_setting_scanning_vertical")
        self.sub_frame_setting_scanning_vertical.setMinimumSize(QSize(0, 60))
        self.sub_frame_setting_scanning_vertical.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_setting_scanning_vertical.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	background:rgb(245,245,245);\n"
"    border: 0px solid rgb(170,170,170);\n"
"	border-radius:0px;")
        self.sub_frame_setting_scanning_vertical.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning_vertical.setFrameShadow(QFrame.Raised)
        self.sub_frame_setting_scanning_vertical.setLineWidth(1)
        self.horizontalLayout_39 = QHBoxLayout(self.sub_frame_setting_scanning_vertical)
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_set_vertical = QLabel(self.sub_frame_setting_scanning_vertical)
        self.label_set_vertical.setObjectName(u"label_set_vertical")
        self.label_set_vertical.setMinimumSize(QSize(220, 60))
        self.label_set_vertical.setMaximumSize(QSize(220, 60))
        self.label_set_vertical.setFont(font19)
        self.label_set_vertical.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px;\n"
"color:black;")
        self.label_set_vertical.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.label_set_vertical)

        self.sub_frame_v_spd_range = QFrame(self.sub_frame_setting_scanning_vertical)
        self.sub_frame_v_spd_range.setObjectName(u"sub_frame_v_spd_range")
        self.sub_frame_v_spd_range.setMinimumSize(QSize(192, 60))
        self.sub_frame_v_spd_range.setMaximumSize(QSize(192, 60))
        self.sub_frame_v_spd_range.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_v_spd_range.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_v_spd_range.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.sub_frame_v_spd_range)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 11, 0, 11)
        self.textEdit_ud_spd_range_max = QTextEdit(self.sub_frame_v_spd_range)
        self.textEdit_ud_spd_range_max.setObjectName(u"textEdit_ud_spd_range_max")
        self.textEdit_ud_spd_range_max.setMinimumSize(QSize(0, 0))
        self.textEdit_ud_spd_range_max.setMaximumSize(QSize(16777215, 60))
        self.textEdit_ud_spd_range_max.setFont(font20)
        self.textEdit_ud_spd_range_max.setStyleSheet(u"border:0px;")
        self.textEdit_ud_spd_range_max.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_ud_spd_range_max.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_29.addWidget(self.textEdit_ud_spd_range_max)

        self.textEdit_ud_spd_range_min = QTextEdit(self.sub_frame_v_spd_range)
        self.textEdit_ud_spd_range_min.setObjectName(u"textEdit_ud_spd_range_min")
        self.textEdit_ud_spd_range_min.setMinimumSize(QSize(0, 0))
        self.textEdit_ud_spd_range_min.setMaximumSize(QSize(16777215, 70))
        self.textEdit_ud_spd_range_min.setFont(font20)
        self.textEdit_ud_spd_range_min.setStyleSheet(u"border:0px;")
        self.textEdit_ud_spd_range_min.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_ud_spd_range_min.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_29.addWidget(self.textEdit_ud_spd_range_min)


        self.horizontalLayout_39.addWidget(self.sub_frame_v_spd_range)

        self.sub_frame_v_spd_step = QFrame(self.sub_frame_setting_scanning_vertical)
        self.sub_frame_v_spd_step.setObjectName(u"sub_frame_v_spd_step")
        self.sub_frame_v_spd_step.setMinimumSize(QSize(237, 60))
        self.sub_frame_v_spd_step.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_v_spd_step.setFont(font20)
        self.sub_frame_v_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_v_spd_step.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_v_spd_step.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.sub_frame_v_spd_step)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 0)
        self.button_set_ud_spd_plus = QPushButton(self.sub_frame_v_spd_step)
        self.button_set_ud_spd_plus.setObjectName(u"button_set_ud_spd_plus")
        self.button_set_ud_spd_plus.setMinimumSize(QSize(45, 45))
        self.button_set_ud_spd_plus.setMaximumSize(QSize(45, 45))
        self.button_set_ud_spd_plus.setFont(font20)
        self.button_set_ud_spd_plus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_30.addWidget(self.button_set_ud_spd_plus)

        self.label_set_ud_spd_step = QLabel(self.sub_frame_v_spd_step)
        self.label_set_ud_spd_step.setObjectName(u"label_set_ud_spd_step")
        self.label_set_ud_spd_step.setFont(font20)
        self.label_set_ud_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:0px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_ud_spd_step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_set_ud_spd_step)

        self.button_set_ud_spd_minus = QPushButton(self.sub_frame_v_spd_step)
        self.button_set_ud_spd_minus.setObjectName(u"button_set_ud_spd_minus")
        self.button_set_ud_spd_minus.setMinimumSize(QSize(45, 45))
        self.button_set_ud_spd_minus.setMaximumSize(QSize(45, 45))
        self.button_set_ud_spd_minus.setFont(font20)
        self.button_set_ud_spd_minus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_30.addWidget(self.button_set_ud_spd_minus)


        self.horizontalLayout_39.addWidget(self.sub_frame_v_spd_step)


        self.verticalLayout_8.addWidget(self.sub_frame_setting_scanning_vertical)

        self.sub_frame_setting_scanning_horizontal = QFrame(self.sub_frame_setting_scanning)
        self.sub_frame_setting_scanning_horizontal.setObjectName(u"sub_frame_setting_scanning_horizontal")
        self.sub_frame_setting_scanning_horizontal.setMinimumSize(QSize(0, 60))
        self.sub_frame_setting_scanning_horizontal.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_setting_scanning_horizontal.setStyleSheet(u"	color: rgb(255,255,255);\n"
"	background:rgb(230,230,230);\n"
"    border: 0px solid rgb(170,170,170);\n"
"	border-radius:0px;\n"
"    border-bottom-left-radius:20px;\n"
"    border-bottom-right-radius:20px;")
        self.sub_frame_setting_scanning_horizontal.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_scanning_horizontal.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.sub_frame_setting_scanning_horizontal)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_set_horiz = QLabel(self.sub_frame_setting_scanning_horizontal)
        self.label_set_horiz.setObjectName(u"label_set_horiz")
        self.label_set_horiz.setMinimumSize(QSize(220, 60))
        self.label_set_horiz.setMaximumSize(QSize(220, 60))
        self.label_set_horiz.setFont(font19)
        self.label_set_horiz.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px;\n"
"color:black;")
        self.label_set_horiz.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.label_set_horiz)

        self.sub_frame_h_spd_range = QFrame(self.sub_frame_setting_scanning_horizontal)
        self.sub_frame_h_spd_range.setObjectName(u"sub_frame_h_spd_range")
        self.sub_frame_h_spd_range.setMinimumSize(QSize(192, 60))
        self.sub_frame_h_spd_range.setMaximumSize(QSize(192, 60))
        self.sub_frame_h_spd_range.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_h_spd_range.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_h_spd_range.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.sub_frame_h_spd_range)
        self.horizontalLayout_37.setSpacing(0)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 11, 0, 11)
        self.textEdit_fb_spd_range_max = QTextEdit(self.sub_frame_h_spd_range)
        self.textEdit_fb_spd_range_max.setObjectName(u"textEdit_fb_spd_range_max")
        self.textEdit_fb_spd_range_max.setMinimumSize(QSize(0, 0))
        self.textEdit_fb_spd_range_max.setMaximumSize(QSize(16777215, 70))
        self.textEdit_fb_spd_range_max.setFont(font20)
        self.textEdit_fb_spd_range_max.setStyleSheet(u"border:0px;")
        self.textEdit_fb_spd_range_max.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_fb_spd_range_max.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_37.addWidget(self.textEdit_fb_spd_range_max)

        self.textEdit_fb_spd_range_min = QTextEdit(self.sub_frame_h_spd_range)
        self.textEdit_fb_spd_range_min.setObjectName(u"textEdit_fb_spd_range_min")
        self.textEdit_fb_spd_range_min.setMinimumSize(QSize(0, 0))
        self.textEdit_fb_spd_range_min.setMaximumSize(QSize(16777215, 70))
        self.textEdit_fb_spd_range_min.setFont(font20)
        self.textEdit_fb_spd_range_min.setStyleSheet(u"border:0px;")
        self.textEdit_fb_spd_range_min.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit_fb_spd_range_min.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.horizontalLayout_37.addWidget(self.textEdit_fb_spd_range_min)


        self.horizontalLayout_38.addWidget(self.sub_frame_h_spd_range)

        self.sub_frame_h_spd_step = QFrame(self.sub_frame_setting_scanning_horizontal)
        self.sub_frame_h_spd_step.setObjectName(u"sub_frame_h_spd_step")
        self.sub_frame_h_spd_step.setMinimumSize(QSize(237, 60))
        self.sub_frame_h_spd_step.setMaximumSize(QSize(16777215, 60))
        self.sub_frame_h_spd_step.setFont(font20)
        self.sub_frame_h_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:2px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.sub_frame_h_spd_step.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_h_spd_step.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.sub_frame_h_spd_step)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(-1, 0, -1, 0)
        self.button_set_fb_spd_plus = QPushButton(self.sub_frame_h_spd_step)
        self.button_set_fb_spd_plus.setObjectName(u"button_set_fb_spd_plus")
        self.button_set_fb_spd_plus.setMinimumSize(QSize(45, 45))
        self.button_set_fb_spd_plus.setMaximumSize(QSize(45, 45))
        self.button_set_fb_spd_plus.setFont(font20)
        self.button_set_fb_spd_plus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_33.addWidget(self.button_set_fb_spd_plus)

        self.label_set_fb_spd_step = QLabel(self.sub_frame_h_spd_step)
        self.label_set_fb_spd_step.setObjectName(u"label_set_fb_spd_step")
        self.label_set_fb_spd_step.setFont(font20)
        self.label_set_fb_spd_step.setStyleSheet(u"background:rgba(0,0,0,0);\n"
"color:black;\n"
"border:0px solid rgb(255,255,255);\n"
"border-radius:0px")
        self.label_set_fb_spd_step.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_set_fb_spd_step)

        self.button_set_fb_spd_minus = QPushButton(self.sub_frame_h_spd_step)
        self.button_set_fb_spd_minus.setObjectName(u"button_set_fb_spd_minus")
        self.button_set_fb_spd_minus.setMinimumSize(QSize(45, 45))
        self.button_set_fb_spd_minus.setMaximumSize(QSize(45, 45))
        self.button_set_fb_spd_minus.setFont(font20)
        self.button_set_fb_spd_minus.setStyleSheet(u"QPushButton {	\n"
"	color: black;\n"
"	border-radius: 10px;\n"
"	background:rgba(0,0,0,0);\n"
"	border: 0px solid rgba(170,170,170,0);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color:rgba(205, 205, 205, 255);\n"
"	color:white;\n"
"	\n"
"}")

        self.horizontalLayout_33.addWidget(self.button_set_fb_spd_minus)


        self.horizontalLayout_38.addWidget(self.sub_frame_h_spd_step)


        self.verticalLayout_8.addWidget(self.sub_frame_setting_scanning_horizontal)


        self.verticalLayout_9.addWidget(self.sub_frame_setting_scanning)

        self.frame_device_container_rpi = QFrame(self.Page_Setting)
        self.frame_device_container_rpi.setObjectName(u"frame_device_container_rpi")
        self.frame_device_container_rpi.setMaximumSize(QSize(16777215, 80))
        self.frame_device_container_rpi.setFrameShape(QFrame.StyledPanel)
        self.frame_device_container_rpi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_device_container_rpi)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button_editDevice = QPushButton(self.frame_device_container_rpi)
        self.button_editDevice.setObjectName(u"button_editDevice")
        self.button_editDevice.setMinimumSize(QSize(160, 48))
        self.button_editDevice.setMaximumSize(QSize(160, 48))
        self.button_editDevice.setFont(font2)
        self.button_editDevice.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_editDevice.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.button_editDevice)

        self.button_testConnection_ard = QPushButton(self.frame_device_container_rpi)
        self.button_testConnection_ard.setObjectName(u"button_testConnection_ard")
        self.button_testConnection_ard.setMinimumSize(QSize(176, 49))
        self.button_testConnection_ard.setMaximumSize(QSize(176, 49))
        self.button_testConnection_ard.setFont(font2)
        self.button_testConnection_ard.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_testConnection_ard.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"QPushButton::disable {\n"
"	background-color:rgba(170, 170, 170, 255);\n"
"}\n"
"")

        self.horizontalLayout_10.addWidget(self.button_testConnection_ard)

        self.comboBox_arduino = QComboBox(self.frame_device_container_rpi)
        self.comboBox_arduino.setObjectName(u"comboBox_arduino")
        self.comboBox_arduino.setMinimumSize(QSize(0, 48))
        self.comboBox_arduino.setMaximumSize(QSize(16777215, 48))
        self.comboBox_arduino.setFont(font12)
        self.comboBox_arduino.setStyleSheet(u"QComboBox\n"
"{\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    selection-background-color: #111;\n"
"    selection-color: yellow;\n"
"    color: white;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 rgba(170,170,170,255), stop:0 rgba(130,130,130,255));\n"
"    /*background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);*/\n"
"    border-style: solid;\n"
"    border: 2px solid white;\n"
"    border-radius:14px;\n"
"    padding: 1px 0px 1px 20px;\n"
"}\n"
"\n"
"\n"
"QComboBox:hover, QPushButton:hover\n"
"{\n"
"    border: 2px solid yellow;\n"
"    color: white;\n"
"}\n"
"\n"
"QComboBox:editable {\n"
"    background: red;\n"
"    color: pink;\n"
"}\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 0px;\n"
"    padding-left: 20px;\n"
"    color: white;\n"
"    /*background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1"
                        " #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);*/\n"
"	background-color:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 rgba(170,170,170,255), stop:0 rgba(130,130,130,255));\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox:!on\n"
"{\n"
"    color: white;\n"
"    /*background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);*/\n"
"	background-color:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:1 rgba(170,170,170,255), stop:0 rgba(130,130,130,255));\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"     color: black;\n"
"     border-left-width: 0px;\n"
"     border-le"
                        "ft-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
"     padding-left: 10px;\n"
" }\n"
"QComboBox::item {\n"
"    text-align: center;\n"
"}\n"
"QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow\n"
"{\n"
"     image: url(:/icons/down_arrow.png);\n"
"     width: 7px;\n"
"     height: 5px;\n"
"}")
        self.comboBox_arduino.setEditable(False)

        self.horizontalLayout_10.addWidget(self.comboBox_arduino)


        self.verticalLayout_9.addWidget(self.frame_device_container_rpi)

        self.sub_frame_setting_button = QFrame(self.Page_Setting)
        self.sub_frame_setting_button.setObjectName(u"sub_frame_setting_button")
        self.sub_frame_setting_button.setFrameShape(QFrame.StyledPanel)
        self.sub_frame_setting_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.sub_frame_setting_button)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_saveSetting_restore = QPushButton(self.sub_frame_setting_button)
        self.button_saveSetting_restore.setObjectName(u"button_saveSetting_restore")
        self.button_saveSetting_restore.setMinimumSize(QSize(200, 70))
        self.button_saveSetting_restore.setMaximumSize(QSize(200, 70))
        self.button_saveSetting_restore.setFont(font2)
        self.button_saveSetting_restore.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.button_saveSetting_restore)

        self.button_saveSetting_save = QPushButton(self.sub_frame_setting_button)
        self.button_saveSetting_save.setObjectName(u"button_saveSetting_save")
        self.button_saveSetting_save.setMinimumSize(QSize(200, 70))
        self.button_saveSetting_save.setMaximumSize(QSize(200, 70))
        self.button_saveSetting_save.setFont(font2)
        self.button_saveSetting_save.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.button_saveSetting_save)

        self.button_saveSetting_about = QPushButton(self.sub_frame_setting_button)
        self.button_saveSetting_about.setObjectName(u"button_saveSetting_about")
        self.button_saveSetting_about.setMinimumSize(QSize(200, 70))
        self.button_saveSetting_about.setMaximumSize(QSize(200, 70))
        self.button_saveSetting_about.setFont(font2)
        self.button_saveSetting_about.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255,255,255);\n"
"	border-radius: 14px;\n"
"    /*background:qlineargradient(spread:pad, x1:0, y2:1, x1:0, y2:1, stop:0 rgba(245, 245, 245, 255), stop:1 rgba(220, 220, 220, 255));*/\n"
"	background:qradialgradient(cx:0,cy:0,radius:1,fx:0.2,fy:0.2,stop:0 rgba(205, 205, 205, 205), stop:1 rgba(170, 170, 170, 255));\n"
"	border: 1px solid rgba(170,170,170, 100);\n"
"}\n"
"QPushButton::hover {\n"
"	background-color: rgb(224, 238, 249);\n"
"	color: rgb(100,100,100);\n"
"}\n"
"QPushButton::pressed {\n"
"	background-color: rgba(200, 200, 200, 255);\n"
"	color: rgb(255,255,255);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.button_saveSetting_about)


        self.verticalLayout_9.addWidget(self.sub_frame_setting_button)

        self.stackedWidget.addWidget(self.Page_Setting)
        self.Page_Record = QWidget()
        self.Page_Record.setObjectName(u"Page_Record")
        self.verticalLayout_12 = QVBoxLayout(self.Page_Record)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.stackedWidget.addWidget(self.Page_Record)

        self.verticalLayout_11.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame_option)


        self.verticalLayout_2.addWidget(self.frame_content)

        self.frame_status_bar = QFrame(self.centralwidget)
        self.frame_status_bar.setObjectName(u"frame_status_bar")
        self.frame_status_bar.setMinimumSize(QSize(0, 26))
        self.frame_status_bar.setStyleSheet(u"background-color:  rgba(210, 210, 210, 255);\n"
"border:0px")
        self.frame_status_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_status_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_status_bar)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(1050, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.label_disp_status = QLabel(self.frame_status_bar)
        self.label_disp_status.setObjectName(u"label_disp_status")
        self.label_disp_status.setMinimumSize(QSize(120, 0))
        font21 = QFont()
        font21.setFamilies([u"Segoe UI Semibold"])
        font21.setPointSize(9)
        self.label_disp_status.setFont(font21)
        self.label_disp_status.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_disp_status)


        self.verticalLayout_2.addWidget(self.frame_status_bar)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Eye Tech Lab AutoCap: Round Table Version", None))
        self.label_scanType.setText(QCoreApplication.translate("MainWindow", u"Chin Rest Controller", None))
        self.button_setting.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"  Speed Control", None))
        self.label_s_lr.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_s_ud.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_s_fb.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_speed_plus_lr.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_speed_minus_lr.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_speed_plus_ud.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_speed_minus_ud.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_speed_plus_fb.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_speed_minus_fb.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Left Right</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Up Down</p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Forward Back</p></body></html>", None))
        self.button_save_spd.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_undo_spd.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.button_move_up.setText(QCoreApplication.translate("MainWindow", u"\ufe3f\n"
"Up", None))
        self.button_move_left.setText(QCoreApplication.translate("MainWindow", u"\u3008 Left     ", None))
        self.button_move_right.setText(QCoreApplication.translate("MainWindow", u"    Right \u3009", None))
        self.button_move_down.setText(QCoreApplication.translate("MainWindow", u"Down\n"
" \ufe40", None))
        self.button_main_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.button_move_fwd.setText(QCoreApplication.translate("MainWindow", u" \ufe3d\n"
"Forward", None))
        self.button_move_bwd.setText(QCoreApplication.translate("MainWindow", u"Backword\n"
" \ufe3e", None))
        self.label_scanSpeed_h.setText(QCoreApplication.translate("MainWindow", u"Scan Speed", None))
        self.label_scanSpeed_val_h_2.setText("")
        self.label_scanSpeed_val_h.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_scanSpeed_val_h_actual.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.label_scanID_h.setText(QCoreApplication.translate("MainWindow", u"Study ID", None))
        self.textEdit_studyID_h.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI Semibold'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.button_speed_minus_h.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_speed_plus_h.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_scanDist_h.setText(QCoreApplication.translate("MainWindow", u"Scan Distance", None))
        self.label_scanDist_val_h.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_scanDist_filler_h.setText("")
        self.button_dist_minus_h.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_dist_plus_h.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_gazedir_h_filler.setText("")
        self.button_gazedir_h_1.setText(QCoreApplication.translate("MainWindow", u"Up Right", None))
        self.button_gazedir_h_2.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.button_gazedir_h_3.setText(QCoreApplication.translate("MainWindow", u"Up Left", None))
        self.label_gazedir_h_filler_3.setText("")
        self.label_gazedir_h_filler_4.setText("")
        self.label_gazedir_h.setText(QCoreApplication.translate("MainWindow", u"Gaze Direction", None))
        self.button_gazedir_h_4.setText(QCoreApplication.translate("MainWindow", u"Right", None))
        self.button_gazedir_h_5.setText(QCoreApplication.translate("MainWindow", u"Primary", None))
        self.button_gazedir_h_6.setText(QCoreApplication.translate("MainWindow", u"Left", None))
        self.label_gazedir_h_filler_5.setText("")
        self.label_gazedir_h_filler_2.setText("")
        self.button_gazedir_h_7.setText(QCoreApplication.translate("MainWindow", u"Down Right", None))
        self.button_gazedir_h_8.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.button_gazedir_h_9.setText(QCoreApplication.translate("MainWindow", u"Down Left", None))
        self.button_saveSetting_h.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.button_restoreSetting_h.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.button_start_scan_h.setText(QCoreApplication.translate("MainWindow", u"Start Scan", None))
        self.label_softInfo_1.setText(QCoreApplication.translate("MainWindow", u"Eye Tech Lab", None))
        self.label_softinfo_2.setText(QCoreApplication.translate("MainWindow", u"Gavin Herbert Eye Institute\n"
"Center for Translational Vision Research\n"
"University of California Irvine\n"
"", None))
        self.button_about_back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_setting_scanning.setText(QCoreApplication.translate("MainWindow", u"Speed Step Setting", None))
        self.label_setting_scanning_filler_2.setText("")
        self.label_setting_scanning_filler.setText("")
        self.label_set_scan_type.setText(QCoreApplication.translate("MainWindow", u"Control Type", None))
        self.label_set_scan_spd_range.setText(QCoreApplication.translate("MainWindow", u"Speed Range", None))
        self.label_set_spd_step.setText(QCoreApplication.translate("MainWindow", u"Speed Step", None))
        self.label_set_radial.setText(QCoreApplication.translate("MainWindow", u"Left - Right", None))
        self.textEdit_lr_spd_range_max.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.textEdit_lr_spd_range_min.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.button_set_lr_spd_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_set_lr_spd_step.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.button_set_lr_spd_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_set_vertical.setText(QCoreApplication.translate("MainWindow", u"Up - Down", None))
        self.textEdit_ud_spd_range_max.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.textEdit_ud_spd_range_min.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.button_set_ud_spd_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_set_ud_spd_step.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_set_ud_spd_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_set_horiz.setText(QCoreApplication.translate("MainWindow", u"Foward - Backward", None))
        self.textEdit_fb_spd_range_max.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.textEdit_fb_spd_range_min.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Consolas'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">500</p></body></html>", None))
        self.button_set_fb_spd_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.label_set_fb_spd_step.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.button_set_fb_spd_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_editDevice.setText(QCoreApplication.translate("MainWindow", u"Search Arduino", None))
        self.button_testConnection_ard.setText(QCoreApplication.translate("MainWindow", u"Test Connection", None))
        self.comboBox_arduino.setCurrentText("")
        self.button_saveSetting_restore.setText(QCoreApplication.translate("MainWindow", u"Restore Default", None))
        self.button_saveSetting_save.setText(QCoreApplication.translate("MainWindow", u"Save Setting", None))
        self.button_saveSetting_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_disp_status.setText("")
    # retranslateUi



"""
Stores or read the saved parameters
"""   
class UIParams:
    def __init__(self):
        # Initial Parameter
        self.leftRight_speed_range_lowerbound = 1000
        self.leftRight_speed_range_upperbound = 30000
        self.leftRight_speed_init_val = 10000
        self.leftRight_speed_step = 1000

        self.upDown_speed_range_lowerbound = 100
        self.upDown_speed_range_upperbound = 3000
        self.upDown_speed_init_val = 800
        self.upDown_speed_step = 100

        self.fwdBwd_speed_range_lowerbound = 1000
        self.fwdBwd_speed_range_upperbound = 30000
        self.fwdBwd_speed_init_val = 10000
        self.fwdBwd_speed_step = 1000

        self.device_arduino = ""

        
        # Check if there is saving parameters
        self.saving = os.path.join(os.getcwd(), "saving.json")
        
        if os.path.exists(self.saving):
            # Read the current saving file if there is
            with open(self.saving, "r") as f:
                param = json.load(f)
            self.__dict__.update(param)
        else:
            # Else, generate the new saving file
            with open(self.saving, "w") as f:
                json.dump(self.__dict__, f, indent = 4)
    
    # Save the current settings
    def save(self):
        with open(self.saving, "w") as f:
            json.dump(self.__dict__, f, indent = 4)
            
    # Restore Default
    def restore(self):
        self.leftRight_speed_range_lowerbound = 1000
        self.leftRight_speed_range_upperbound = 30000
        self.leftRight_speed_init_val = 10000
        self.leftRight_speed_step = 1000

        self.upDown_speed_range_lowerbound = 100
        self.upDown_speed_range_upperbound = 3000
        self.upDown_speed_init_val = 800
        self.upDown_speed_step = 100

        self.fwdBwd_speed_range_lowerbound = 1000
        self.fwdBwd_speed_range_upperbound = 30000
        self.fwdBwd_speed_init_val = 10000
        self.fwdBwd_speed_step = 1000

        self.device_arduino = ""


"""
UART Connection
"""   
class serial_connect():
    def __init__(self, device, baudrate = 9600, timeout = 1):
        self.device = device
        self.baudrate = baudrate
        self.timeout = 1
            
    def connect(self):
        try:
            self.send = serial.Serial(self.device, baudrate = self.baudrate, timeout = self.timeout)
            # Wait for 2 seconds
            start_time = time.time(); dtime = 0
            while dtime < 1.5:
                dtime = time.time() - start_time
            return True
        except serial.SerialException as e:
            return False
        
    def close_port(self):
        self.send.close()
        self.send = None
    
    # Move Motor:
    # Message Structure: "sd#00000e"
    # 's': Start
    # 'd': Direction (x, y, z)
    # '#': Direction Number (1, 2)
    # '00000': Motor Speed or Step Width
    # 'e': end
    
    def send_move(self, d, n, s):
        msg = str('s' + d + n + s + 'e')
        print(msg)
        self.send.write(msg.encode("utf-8"))


"""
Main UI
"""            
class main_ui(QMainWindow, Ui_MainWindow): #, mainUI):
    # Constructor
    def __init__(self):
        # Parameters
        self.setting = False
        self.connect = False
        self.params = UIParams()
        self.ctrl = None
        
        # Set up the ui
        super().__init__()
        # uic.loadUi("mainWindow.ui", self)
        self.setupUi(self)

        self.init_ctrller()
        self.init_button()
        self.init_text_disp()
        self.init_ui()
        self.show()
    
    '''
    Function to initializeadjuster
    '''
    
    def init_button(self):
        # Menu Buttons
        self.button_setting.clicked.connect(self.switch_setting)
        self.button_saveSetting_about.clicked.connect(lambda: (self.stackedWidget.setCurrentIndex(3), self.label_scanType.setText("About")))
        self.button_about_back.clicked.connect(       lambda: (self.stackedWidget.setCurrentIndex(5), self.label_scanType.setText("Setting")))
        
        # Setting page
            # Arduino Connection
        self.button_editDevice.clicked.connect(self.connection_edit_device_ard)
        self.button_testConnection_ard.clicked.connect(self.connection_check_ard)
        self.button_testConnection_ard.setEnabled(False)
            # Parameters
        self.button_saveSetting_restore.clicked.connect(lambda: (self.params.restore(), self.init_text_disp(), self.params.save(),
                                                                 self.init_ctrller(), self.button_testConnection_ard.setEnabled(False)))
        self.button_saveSetting_save.clicked.connect(self.set_save)
            # Speed Step
        self.button_set_lr_spd_plus.clicked.connect(self.set_lr_spd_plus);   self.button_set_lr_spd_minus.clicked.connect(self.set_lr_spd_minus)
        self.button_set_ud_spd_plus.clicked.connect(self.set_ud_spd_plus);   self.button_set_ud_spd_minus.clicked.connect(self.set_ud_spd_minus)
        self.button_set_fb_spd_plus.clicked.connect(self.set_fb_spd_plus);   self.button_set_fb_spd_minus.clicked.connect(self.set_fb_spd_minus)
        
        # Speed adjusting menu
        self.button_speed_plus_lr.clicked.connect(self.update_scanSpeed_minus_lr); self.button_speed_minus_lr.clicked.connect(self.update_scanSpeed_add_lr)
        self.button_speed_plus_ud.clicked.connect(self.update_scanSpeed_minus_ud); self.button_speed_minus_ud.clicked.connect(self.update_scanSpeed_add_ud)
        self.button_speed_plus_fb.clicked.connect(self.update_scanSpeed_minus_fb); self.button_speed_minus_fb.clicked.connect(self.update_scanSpeed_add_fb)
        self.button_save_spd.clicked.connect(lambda: self.save_settings(True, ""))
        self.button_undo_spd.clicked.connect(lambda: self.restore_settings(True))

        # Main page
        self.button_main_connect.clicked.connect(self.main_connect)
        self.button_move_up.pressed.connect(lambda: self.move_motor("z", "2", True))
        self.button_move_down.pressed.connect(lambda: self.move_motor("z", "1", True))
        self.button_move_left.pressed.connect(lambda: self.move_motor("y", "1", True))
        self.button_move_right.pressed.connect(lambda: self.move_motor("y", "2", True))
        self.button_move_fwd.pressed.connect(lambda: self.move_motor("x", "1", True))
        self.button_move_bwd.pressed.connect(lambda: self.move_motor("x", "2", True))
        
        self.button_move_up.released.connect(lambda: self.move_motor("z", "2", False))
        self.button_move_down.released.connect(lambda: self.move_motor("z", "1", False))
        self.button_move_left.released.connect(lambda: self.move_motor("y", "1", False))
        self.button_move_right.released.connect(lambda: self.move_motor("y", "2", False))
        self.button_move_fwd.released.connect(lambda: self.move_motor("x", "1", False))
        self.button_move_bwd.released.connect(lambda: self.move_motor("x", "2", False))

 

 
    
    def init_text_disp(self):
        # TODO: Add slider value

        # Setting Page
        self.textEdit_lr_spd_range_max.setPlainText(str(self.params.leftRight_speed_range_upperbound)); self.textEdit_lr_spd_range_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_lr_spd_range_min.setPlainText(str(self.params.leftRight_speed_range_lowerbound)); self.textEdit_lr_spd_range_min.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.textEdit_ud_spd_range_max.setPlainText(str(self.params.upDown_speed_range_upperbound)); self.textEdit_ud_spd_range_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_ud_spd_range_min.setPlainText(str(self.params.upDown_speed_range_lowerbound)); self.textEdit_ud_spd_range_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
                                                                                                                                                  
        self.textEdit_fb_spd_range_max.setPlainText(str(self.params.fwdBwd_speed_range_upperbound)); self.textEdit_fb_spd_range_max.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_fb_spd_range_min.setPlainText(str(self.params.fwdBwd_speed_range_lowerbound)); self.textEdit_fb_spd_range_min.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.label_set_lr_spd_step.setText(str(self.params.leftRight_speed_step))
        self.label_set_ud_spd_step.setText(str(self.params.upDown_speed_step))
        self.label_set_fb_spd_step.setText(str(self.params.fwdBwd_speed_step))
        
        self.comboBox_arduino.clear()
        if self.params.device_arduino != "":
            self.comboBox_arduino.addItem(self.params.device_arduino)

        self.label_disp_status.setText("")
        self.ctrl = None
    
    #TODO    
    def init_ctrller(self):
        # Slider for left right
        self.verticalSlider_LeftRight.setRange(self.params.leftRight_speed_range_lowerbound, self.params.leftRight_speed_range_upperbound)
        self.verticalSlider_LeftRight.setValue(self.params.leftRight_speed_init_val)
        self.verticalSlider_LeftRight.setSingleStep(self.params.leftRight_speed_step)
        self.verticalSlider_LeftRight.setPageStep(self.params.leftRight_speed_step)
        self.verticalSlider_LeftRight.setInvertedAppearance(True)
        self.label_s_lr.setText(str(self.params.leftRight_speed_init_val))
        self.verticalSlider_LeftRight.valueChanged.connect(self.update_scanSpeed_label_lr)
        
        # Slider for up down
        self.verticalSlider_UpDown.setRange(self.params.upDown_speed_range_lowerbound, self.params.upDown_speed_range_upperbound)
        self.verticalSlider_UpDown.setValue(self.params.upDown_speed_init_val)
        self.verticalSlider_UpDown.setSingleStep(self.params.upDown_speed_step)
        self.verticalSlider_UpDown.setPageStep(self.params.upDown_speed_step)
        self.verticalSlider_UpDown.setInvertedAppearance(True)
        self.label_s_ud.setText(str(self.params.upDown_speed_init_val))
        self.verticalSlider_UpDown.valueChanged.connect(self.update_scanSpeed_label_ud)
        
        # Slider for forward backward
        self.verticalSlider_ForwardBack.setRange(self.params.fwdBwd_speed_range_lowerbound, self.params.fwdBwd_speed_range_upperbound)
        self.verticalSlider_ForwardBack.setValue(self.params.fwdBwd_speed_init_val)
        self.verticalSlider_ForwardBack.setSingleStep(self.params.fwdBwd_speed_step)
        self.verticalSlider_ForwardBack.setPageStep(self.params.fwdBwd_speed_step)
        self.verticalSlider_ForwardBack.setInvertedAppearance(True)
        self.label_s_fb.setText(str(self.params.fwdBwd_speed_init_val))
        self.verticalSlider_ForwardBack.valueChanged.connect(self.update_scanSpeed_label_fb)
        
        self.ctrller_buttons(False)
        
    
    def init_ui(self):
        self.stackedWidget.setCurrentIndex(0)

    
    
    
    '''
    Button Functions
    '''
    # Toggle Switch
    def switch_setting(self):
        if not self.setting:
            self.setting = True
            self.stackedWidget.setCurrentIndex(5)
            self.label_scanType.setText("Setting")
            self.button_setting.setText("Back")
        else:
            self.setting = False
            self.stackedWidget.setCurrentIndex(0)
            self.label_scanType.setText("Chin Rest Controller")
            self.button_setting.setText("Setting")
        
    
    
    # Radial
    def update_scanSpeed_add_lr(self):
        current_speed = self.verticalSlider_LeftRight.value()
        if current_speed < self.params.leftRight_speed_range_upperbound:
            modVal = current_speed % self.params.leftRight_speed_step
            if modVal > 0:
                new_speed = current_speed + (self.params.leftRight_speed_step - modVal)
            else:
                new_speed = current_speed + self.params.leftRight_speed_step
            self.label_s_lr.setText(str(new_speed)) # update label
            self.verticalSlider_LeftRight.setValue(new_speed) # update speed
    
    def update_scanSpeed_minus_lr(self):
        current_speed = self.verticalSlider_LeftRight.value()
        if current_speed > self.params.leftRight_speed_range_lowerbound:
            modVal = current_speed % self.params.leftRight_speed_step
            if modVal > 0:
                new_speed = current_speed - modVal
            else:
                new_speed = current_speed - self.params.leftRight_speed_step
            self.label_s_lr.setText(str(new_speed))
            self.verticalSlider_LeftRight.setValue(new_speed) # update speed  
    
     
    # Vertical
    def update_scanSpeed_add_ud(self):
        current_speed = self.verticalSlider_UpDown.value()
        if current_speed < self.params.upDown_speed_range_upperbound:
            modVal = current_speed % self.params.upDown_speed_step
            if modVal > 0:
                new_speed = current_speed + (self.params.upDown_speed_step - modVal)
            else:
                new_speed = current_speed + self.params.upDown_speed_step
            self.label_s_ud.setText(str(new_speed)) # update label
            self.verticalSlider_UpDown.setValue(new_speed) # update speed
    
    def update_scanSpeed_minus_ud(self):
        current_speed = self.verticalSlider_UpDown.value()
        if current_speed > self.params.upDown_speed_range_lowerbound:
            modVal = current_speed % self.params.upDown_speed_step
            if modVal > 0:
                new_speed = current_speed - modVal
            else:
                new_speed = current_speed - self.params.upDown_speed_step
            new_text = str(new_speed)
            self.label_s_ud.setText(str(new_speed)) # update label
            self.verticalSlider_UpDown.setValue(new_speed) # update speed  
    
    # Horizontal
    def update_scanSpeed_add_fb(self):
        current_speed = self.verticalSlider_ForwardBack.value()
        if current_speed < self.params.fwdBwd_speed_range_upperbound:
            modVal = current_speed % self.params.fwdBwd_speed_step
            if modVal > 0:
                new_speed = current_speed + (self.params.fwdBwd_speed_step - modVal)
            else:
                new_speed = current_speed + self.params.fwdBwd_speed_step
            new_text = str(new_speed)
            self.label_s_fb.setText(str(new_speed)) # update label
            self.verticalSlider_ForwardBack.setValue(new_speed) # update speed
    
    def update_scanSpeed_minus_fb(self):
        current_speed = self.verticalSlider_ForwardBack.value()
        if current_speed > self.params.fwdBwd_speed_range_lowerbound:
            modVal = current_speed % self.params.fwdBwd_speed_step
            if modVal > 0:
                new_speed = current_speed - modVal
            else:
                new_speed = current_speed - self.params.fwdBwd_speed_step
            new_text = str(new_speed)
            self.label_s_fb.setText(str(new_speed)) # update label
            self.verticalSlider_ForwardBack.setValue(new_speed) # update speed  
    
    
    # Main page
    def main_connect(self):
        if not self.connect:
            self.ctrl = serial_connect(self.comboBox_arduino.currentText())
            if self.ctrl.connect():
                print(self.comboBox_arduino.currentText())
                self.label_disp_status.setText("Connected")
                self.label_disp_status.setStyleSheet("color:#404040")
            else:
                self.label_disp_status.setText("Failed")
                self.label_disp_status.setStyleSheet("color:#F04148")
                self.showMsg("warning", "Connection Failed! Check Arduino Connection.")
                self.ctrl = None
                return
            
            self.connect = True
            self.button_main_connect.setText("Disconnect")
            self.ctrller_buttons(True)
        else:
            self.ctrl = None
            self.connect = False
            self.label_disp_status.setText("Disconnected")
            self.label_disp_status.setStyleSheet("color:#404040")
            self.button_main_connect.setText("Connect")
            self.ctrller_buttons(False)
            

    # main page buttons
    def ctrller_buttons(self, status):
        self.button_move_up.setEnabled(status)
        self.button_move_down.setEnabled(status)
        self.button_move_left.setEnabled(status)
        self.button_move_right.setEnabled(status)
        self.button_move_fwd.setEnabled(status)
        self.button_move_bwd.setEnabled(status)
        
    def move_motor(self, axis, num, pressed):
        # x1: Forward
        # x2: Backward
        # y1: Right
        # y2: Left
        # z1: Down
        # z2: Up
        if axis == "x": speed = self.verticalSlider_ForwardBack.value()
        elif axis == "y": speed = self.verticalSlider_LeftRight.value()
        elif axis == "z": speed = self.verticalSlider_UpDown.value()
        
        spdstr = str(speed).zfill(5)
        self.ctrl.send_move(axis, num, spdstr)
        
       
    def start_scan_pure(self, type): 
        # Set label and lock the button:
        self.label_disp_status.setText("Preparing")
        self.label_disp_status.setStyleSheet("color:#808080")
        self.send = serial_connect(self.comboBox_arduino.currentText())
        QApplication.processEvents()
        
        # Check if valid
        if self.send.connect():
            print(self.comboBox_arduino.currentText())
            self.send.close_port()
        else:
            self.label_disp_status.setText("Failed")
            self.label_disp_status.setStyleSheet("color:#F04148")
            self.showMsg("warning", "Connection Failed! Check Arduino Connection.")
            return 0
        
        # Choose scan type
        if type == 'r':
            type_detail = "Radial" 
            self.button_start_scan_r.setEnabled(False)

            # Calculate the actual step: At the current 1/8 setting, 1600 = 1 rev; since 1/180 ratio, a full rotation is 180*1600 = 288,000
            # step = int((200*8*32/27) * (self.slider_dist_r.value()) / 360)
            step = int(self.slider_dist_r.value() * (1600/2))
            
            self.send.connect()
            self.send.scan_controls_only(type, self.params.direction, self.slider_speed_r.value(), step)
            self.button_start_scan_r.setEnabled(True)  
        elif type == 'v':
            type_detail = "Vertical" 
            self.button_start_scan_v.setEnabled(False)
            
            self.send.connect()
            self.send.scan_controls_only(type, self.params.direction, self.slider_speed_v.value(), self.slider_dist_v.value())
            self.button_start_scan_v.setEnabled(True)  
        elif type == 'h':
            type_detail = "Horizontal" 
            self.button_start_scan_h.setEnabled(False)

            self.send.connect()
            self.send.scan_controls_only(type, self.params.direction, self.slider_speed_h.value(), self.slider_dist_h.value())
            self.button_start_scan_h.setEnabled(True)   

        # Restore Button
        self.showMsg("information", "The scan is complete.")
        self.label_disp_status.setText("Scan Complete")
        self.label_disp_status.setStyleSheet("color:#43D85D")

    # Connection Check
    def connection_check_ard(self):
        # QTimer.singleShot(2000, lambda: self.label_disp_status.setText("Testing"))
        self.button_testConnection_ard.setEnabled(False)
        QApplication.processEvents()
        
        self.send = serial_connect(self.comboBox_arduino.currentText())
        
        if self.send.connect():
            self.showMsg("information", "Connect successful")
            self.send.close_port()
        else:
            self.showMsg("information", "Unable to connect")
        
        self.button_testConnection_ard.setEnabled(True)
    
    def connection_edit_device_ard(self):
        self.button_testConnection_ard.setEnabled(True)
        self.comboBox_arduino.clear()
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.comboBox_arduino.addItem(p.name)
        self.params.device_arduino = self.comboBox_arduino.currentText()
        self.params.save()        

    # Setting Page    
    def set_lr_spd_plus(self):
        current_step = self.params.leftRight_speed_step
        if current_step < self.params.leftRight_speed_range_upperbound:
            new_step = current_step + 100
            new_text = str(new_step)
            self.params.leftRight_speed_step = new_step # update value
            self.label_set_lr_spd_step.setText(new_text) # update label
    
    def set_lr_spd_minus(self):
        current_step = self.params.leftRight_speed_step
        if current_step > 100:
            new_step = current_step - 100
            new_text = str(new_step)
            self.params.leftRight_speed_step = new_step # update value
            self.label_set_lr_spd_step.setText(new_text) # update label
    
    def set_ud_spd_plus(self):
        current_step = self.params.upDown_speed_step
        if current_step < self.params.upDown_speed_range_upperbound:
            new_step = current_step + 100
            new_text = str(new_step)
            self.params.upDown_speed_step = new_step # update value
            self.label_set_ud_spd_step.setText(new_text) # update label
    
    def set_ud_spd_minus(self):
        current_step = self.params.upDown_speed_step
        if current_step > 100:
            new_step = current_step - 100
            new_text = str(new_step)
            self.params.upDown_speed_step = new_step # update value
            self.label_set_ud_spd_step.setText(new_text) # update label
    
    def set_fb_spd_plus(self):
        current_step = self.params.fwdBwd_speed_step
        if current_step < self.params.fwdBwd_speed_range_upperbound:
            new_step = current_step + 100
            new_text = str(new_step)
            self.params.fwdBwd_speed_step = new_step # update value
            self.label_set_fb_spd_step.setText(new_text) # update label
    
    def set_fb_spd_minus(self):
        current_step = self.params.fwdBwd_speed_step
        if current_step > 100:
            new_step = current_step - 100
            new_text = str(new_step)
            self.params.fwdBwd_speed_step = new_step # update value
            self.label_set_fb_spd_step.setText(new_text) # update label
    
        
    def set_save(self):
        try:
            self.params.leftRight_speed_range_upperbound = int(self.textEdit_lr_spd_range_max.toPlainText())
            self.params.leftRight_speed_range_lowerbound = int(self.textEdit_lr_spd_range_min.toPlainText())
            self.params.leftRight_speed_step = int(self.label_set_lr_spd_step.text())
            
            self.params.upDown_speed_range_upperbound = int(self.textEdit_ud_spd_range_max.toPlainText())
            self.params.upDown_speed_range_lowerbound = int(self.textEdit_ud_spd_range_min.toPlainText())
            self.params.upDown_speed_step = int(self.label_set_ud_spd_step.text())

            self.params.fwdBwd_speed_range_upperbound = int(self.textEdit_fb_spd_range_max.toPlainText())
            self.params.fwdBwd_speed_range_lowerbound = int(self.textEdit_fb_spd_range_min.toPlainText())
            self.params.upDown_speed_step = int(self.label_set_fb_spd_step.text())

            self.params.save()
            self.init_ctrller(); self.init_text_disp()
        except ValueError:
            self.showMsg("warning", "Please Check if Invalid Number is Entered")
        

    # Other:
    def restore_settings(self, msgFlag):
        # Slider for left right
        self.label_s_lr.setText(str(self.params.leftRight_speed_init_val))
        self.verticalSlider_LeftRight.setValue(self.params.leftRight_speed_init_val)
        
        # Slider for up down
        self.label_s_ud.setText(str(self.params.upDown_speed_init_val))
        self.verticalSlider_UpDown.setValue(self.params.upDown_speed_init_val)

        # Slider for forward backward
        self.label_s_fb.setText(str(self.params.fwdBwd_speed_init_val))
        self.verticalSlider_ForwardBack.setValue(self.params.fwdBwd_speed_init_val)
    
    
    def save_settings(self, msgFlag, IDFlag):
        self.params.leftRight_speed_init_val = self.verticalSlider_LeftRight.value()
        self.params.upDown_speed_init_val = self.verticalSlider_UpDown.value()
        self.params.fwdBwd_speed_init_val = self.verticalSlider_ForwardBack.value()
        
        self.params.save()
        if msgFlag:
            self.showMsg("information", "Parameters Saved")
    
    
    '''
    Function that update info
    '''
    # Left Right
    def update_scanSpeed_label_lr(self, value):
        self.label_s_lr.setText(str(value))
    
    # Up Down
    def update_scanSpeed_label_ud(self, value):
        self.label_s_ud.setText(str(value))
    
    # Forward Backward   
    def update_scanSpeed_label_fb(self, value):
        self.label_s_fb.setText(str(value))
   

    
    '''
    Other Function
    '''              
    def showMsg(self, title, info):
        # NOTE:
        # Add Icon after QMessageBox
        # StandardButton for okay
        title_type = {"information":QMessageBox.Icon.Information, "warning":QMessageBox.Icon.Warning}
        msg = QMessageBox()
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.setIcon(title_type[title])
        # msg.resize(1000, 200)
        msg.setWindowTitle(title)
        msg.setText(info)
        msg.exec()        

def main():
    app = QApplication(sys.argv)
    win = main_ui()
    win.show()
    sys.exit(app.exec())
    
if __name__ == '__main__':
    main()
    