


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import numpy as np
import time as tm
import pandas as pd
import pokemon as pk
import time as tm
import os


list_pokemon = pd.read_csv(("../data/pokemon_first_gen.csv"), delimiter = ',')
position_pokemon = pd.read_csv(("../data/pokemon_coordinates.csv"), delimiter =',')
capacites = pd.read_csv("../data/abilities.csv")




class Carte():
    
    def __init__(self, MainWindow, vue):
        self.map= vue
        self.carte = QtWidgets.QLabel(MainWindow)
        pixmap = QPixmap(self.map.map_init)
        self.carte.setPixmap(pixmap)
        self.carte.setGeometry(30, 40, 721, 581)
        self.carte.setScaledContents(True)
        self.carte.setGeometry(QtCore.QRect(50, 50, 800, 720))



    def show_map(self):
                
        pixmap = QPixmap(self.map.map_init)
        self.carte.setPixmap(pixmap)
        self.carte.setGeometry(30, 40, 721, 581)
        self.carte.setScaledContents(True)
        self.carte.setGeometry(QtCore.QRect(50, 50, 800, 720))
        self.combat = self.map.hautes_herbes()
        self.carte.show()


    def hide(self):
        self.carte.hide()
        
        


class inter_combat ():
    def __init__(self, MainWindow, pok1, pok2):
        
        
        self.indx1 = str((list(list_pokemon.Name).index(pok1.name))+1)
        self.indx2 = str((list(list_pokemon.Name).index(pok2.name))+1)
        
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.P1_N = QtWidgets.QLabel(self.centralwidget)
        self.P1_N.setGeometry(QtCore.QRect(470, 310, 331, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P1_N.sizePolicy().hasHeightForWidth())
        self.P1_N.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.P1_N.setFont(font)
        self.P1_N.setTextFormat(QtCore.Qt.AutoText)
        self.P1_N.setScaledContents(False)
        self.P1_N.setAlignment(QtCore.Qt.AlignCenter)
        self.P1_N.setObjectName("P1_N")
        
        
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 520, 400, 230))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../data/img/combat/cadre.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        
        self.P1 = QtWidgets.QLabel(self.centralwidget)
        self.P1.setGeometry(QtCore.QRect(110, 260, 261, 261))
        self.P1.setText("")
        self.P1.setPixmap(QtGui.QPixmap("../data/sprites/dos/"+self.indx1+".jpg"))
        self.P1.setScaledContents(True)
        self.P1.setObjectName("P1")
        
        self.P2 = QtWidgets.QLabel(self.centralwidget)
        self.P2.setGeometry(QtCore.QRect(540, 70, 261, 261))
        self.P2.setText("")
        self.P2.setPixmap(QtGui.QPixmap("../data/sprites/face/"+self.indx2+".jpg"))
        self.P2.setScaledContents(True)
        self.P2.setObjectName("P2")
        
        self.P2_N = QtWidgets.QLabel(self.centralwidget)
        self.P2_N.setGeometry(QtCore.QRect(30, 50, 371, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.P2_N.sizePolicy().hasHeightForWidth())
        self.P2_N.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(19)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        
        self.P2_N.setFont(font)
        self.P2_N.setTextFormat(QtCore.Qt.AutoText)
        self.P2_N.setScaledContents(False)
        self.P2_N.setAlignment(QtCore.Qt.AlignCenter)
        self.P2_N.setObjectName("P2_N")
        
        
        self.PV1_2 = QtWidgets.QProgressBar(self.centralwidget)
        # self.PV1_2.setEnabled(True)
        self.PV1_2.setGeometry(QtCore.QRect(550, 405, 241, 21))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(12)
        # font.setBold(True)
        # font.setWeight(75)
        
        # self.PV1_2.setFont(font)
        # self.PV1_2.setToolTip("")
        self.PV1_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PV1_2.setStyleSheet("QProgressBar::chunk {\n"
"    /* Couleur de la barre de progression */\n"
"    background-color: rgb(0, 209, 0);\n"
"}\n"
"\n"
"")
        self.PV1_2.setProperty("value", int(pok1.pv))
        self.PV1_2.setMaximum(int(pok1.pv_max))
        self.PV1_2.setTextVisible(False)
        self.PV1_2.setOrientation(QtCore.Qt.Horizontal)
        self.PV1_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.PV1_2.setObjectName("PV1_2")
        
        
        
        self.PV1_3 = QtWidgets.QProgressBar(self.centralwidget)
        # self.PV1_3.setEnabled(True)
        self.PV1_3.setGeometry(QtCore.QRect(140, 150, 241, 21))
        # font = QtGui.QFont()
        # font.setFamily("Microsoft YaHei UI Light")
        # font.setPointSize(11)
        # font.setBold(True)
        # font.setWeight(75)
        # self.PV1_3.setFont(font)
        # self.PV1_3.setToolTip("")
        self.PV1_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PV1_3.setStyleSheet("QProgressBar::chunk {\n"
"    /* Couleur de la barre de progression */\n"
"    background-color: rgb(0, 209, 0);\n"
"}\n"
"\n"
"")
        
        self.PV1_3.setProperty("value", int(pok2.pv))
        self.PV1_3.setMaximum(int(pok2.pv_max))
        self.PV1_3.setTextVisible(False)
        self.PV1_3.setOrientation(QtCore.Qt.Horizontal)
        self.PV1_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.PV1_3.setObjectName("PV1_3")
        
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 141, 391, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../data/img/combat/HP2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(630, 435, 150, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light SemiCondensed")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(470, 650, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setIconSize(QtCore.QSize(80, 80))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(640, 650, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(640, 570, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(470, 570, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.att1 = QtWidgets.QPushButton(MainWindow)
        self.att1.setGeometry(QtCore.QRect(470, 650, 151, 51))
        self.att1.setObjectName("ATT1")
        self.att1.hide()
        
        
        self.att2 = QtWidgets.QPushButton(MainWindow)
        self.att2.setGeometry(QtCore.QRect(640, 650, 141, 51))
        self.att2.setObjectName("ATT2")
        self.att2.hide()
        
        self.att3 = QtWidgets.QPushButton(MainWindow)
        self.att3.setGeometry(QtCore.QRect(640, 570, 141, 51))
        self.att3.setObjectName("ATT3")
        self.att3.hide()
        
        self.att4 = QtWidgets.QPushButton(MainWindow)
        self.att4.setGeometry(QtCore.QRect(470, 570, 151, 51))
        self.att4.setObjectName("ATT4")
        self.att4.hide()
        

        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(430, 400, 391, 111))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../data/img/combat/HP_1.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 520, 450, 231))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../data/img/combat/cadre.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        
        

        self.txt_cadre = QtWidgets.QLabel(MainWindow)
        self.txt_cadre.setGeometry(QtCore.QRect(80, 580, 300, 151))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.txt_cadre.setFont(font)
        self.txt_cadre.setObjectName("label_2")


        self.P1_N.raise_()
        self.label_2.raise_()
        self.P1.raise_()
        self.P2.raise_()
        self.P2_N.raise_()
        self.PV1_2.raise_()
        self.PV1_3.raise_()
        self.label.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.txt_cadre.raise_()
        
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow, pok1, pok2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow, pok1, pok2):
        
        
        self.indx1 = str((list(list_pokemon.Name).index(pok1.name))+1)
        self.indx2 = str((list(list_pokemon.Name).index(pok2.name))+1)
        
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.P1_N.setText(_translate("MainWindow", pok1.name))
        self.P2_N.setText(_translate("MainWindow", pok2.name))
        self.PV1_2.setProperty("value", int(pok1.pv))
        self.PV1_3.setProperty("value", int(pok2.pv))
        self.label_4.setText(_translate("MainWindow", str(pok1.pv) + "/" + str(pok1.pv_max)))
        self.pushButton.setText(_translate("MainWindow", "FIGHT"))
        self.pushButton_2.setText(_translate("MainWindow", "CAPTURE"))
        self.pushButton_3.setText(_translate("MainWindow", "POKEMON"))
        self.pushButton_4.setText(_translate("MainWindow", "RUN"))
        self.txt_cadre.setText(_translate("MainWindow", ""))
        self.att1.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[0]]))
        self.att2.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[1]]))
        self.att3.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[2]]))
        self.att4.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[3]]))
        self.txt_cadre.show()
        
        


    def hide(self):
        
        self.P1.hide()
        self.P1_N.hide()
        self.P2.hide()
        self.P2_N.hide()
        self.PV1_2.hide()
        self.PV1_3.hide()
        self.centralwidget.hide()
        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.label_4.hide()
        self.pushButton.hide()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.label_5.hide()
        self.att1.hide()
        self.att2.hide()
        self.att3.hide()
        self.att4.hide()
        self.txt_cadre.hide()
    
    def show(self, pok1, pok2, at):
        # self.pok1 = pk.number_to_pokemon(pok1)
        # self.pok2 = pk.number_to_pokemon(pok2)
        
        self.indx1 = str((list(list_pokemon.Name).index(pok1.name))+1)
        self.indx2 = str((list(list_pokemon.Name).index(pok2.name))+1)
        
        
        
        _translate = QtCore.QCoreApplication.translate
        # print(list_pokemon.Name[pok2])
        self.P1.setPixmap(QtGui.QPixmap("../data/sprites/dos/"+ self.indx1 +".jpg"))
        self.P2.setPixmap(QtGui.QPixmap("../data/sprites/face/"+self.indx2 +".jpg"))
        if at != -1 :
            self.txt_cadre.setText(_translate("MainWindow", pok1.name + " Utilise " + capacites.Name[pok1.liste_capacites[at]]))
        else:
            self.txt_cadre.setText(_translate("MainWindow",""))

        self.txt_cadre.update()
        self.PV1_2.setMaximum(int(pok1.pv_max))
        self.PV1_3.setMaximum(int(pok2.pv_max))
        self.PV1_2.setProperty("value", int(pok1.pv))
        self.PV1_3.setProperty("value", int(pok2.pv))
        self.P1_N.setText(_translate("MainWindow", pok1.name))
        self.P2_N.setText(_translate("MainWindow", pok2.name))
        self.label_4.setText(_translate("MainWindow", str(pok1.pv) + "/" + str(pok1.pv_max)))
        self.P1.show()
        self.P1_N.show()
        self.P2.show()
        self.P2_N.show()
        self.PV1_2.show()
        self.PV1_3.show()
        self.centralwidget.show()
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.label_5.show()
        self.txt_cadre.show()
        self.att1.hide()
        self.att2.hide()
        self.att3.hide()
        self.att4.hide()

        # self.txt_cadre.hide()


    def att_hide(self):
        
        self.att1.hide()
        self.att2.hide()
        self.att3.hide()
        self.att4.hide()
        # self.txt_cadre.hide()
    
    def att_show(self, pok1,pok2):
        _translate = QtCore.QCoreApplication.translate
        
        self.indx1 = str((list(list_pokemon.Name).index(pok1.name))+1)
        self.indx2 = str((list(list_pokemon.Name).index(pok2.name))+1)
        
        self.att1.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[0]]))
        self.att2.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[1]]))
        self.att3.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[2]]))
        self.att4.setText(_translate("MainWindow", capacites.Name[pok1.liste_capacites[3]]))
        
        # self.txt_cadre.setText(_translate("MainWindow", ""))
            
        
        # print(list_pokemon.Name[pok2])
        self.P1.setPixmap(QtGui.QPixmap("../data/sprites/dos/"+ self.indx1 +".jpg"))
        self.P2.setPixmap(QtGui.QPixmap("../data/sprites/face/"+self.indx2 +".jpg"))
        self.PV1_2.setMaximum(int(pok1.pv_max))
        self.PV1_3.setMaximum(int(pok2.pv_max))
        self.PV1_2.setProperty("value", int(pok1.pv))
        self.PV1_3.setProperty("value", int(pok2.pv))
        self.P1_N.setText(_translate("MainWindow", pok1.name))
        self.P2_N.setText(_translate("MainWindow", pok2.name))
        self.label_4.setText(_translate("MainWindow", str(pok1.pv) + "/" + str(pok1.pv_max)))
        self.P1.show()
        self.P1_N.show()
        self.P2.show()
        self.P2_N.show()
        self.PV1_2.show()
        self.PV1_3.show()
        self.centralwidget.show()
        self.label.show()
        self.label_2.show()
        self.label_3.show()
        self.label_4.show()
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.label_5.show()
        self.att1.show()
        self.att2.show()
        self.att3.show()
        self.att4.show()
        # self.txt_cadre.show()
        
        

    
