# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:16:57 2024

@author: melanie
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys
from melanie import Sac
import pokemon as pk


class Interface_choix(object):
    
    def setupUi(self, Dialog, sac_pokemon):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 720)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(192, 50, 416, 30))
        self.label.setLineWidth(18)
        self.label.setObjectName("label")        
        
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 150, 200, 200))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../data/sprites/face/3.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_2.setScaledContents(True)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 150, 200, 200))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(300, 150, 200, 200))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../data/sprites/face/6.jpg"))
        self.label_3.setObjectName("label_3")
        self.label_3.setScaledContents(True)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 150, 200, 200))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton")
        
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(560, 150, 200, 200))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../data/sprites/face/9.jpg"))
        self.label_4.setObjectName("label_4")
        self.label_4.setScaledContents(True)
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(560, 150, 200, 200))
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton")
        
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 410, 200, 200))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../data/sprites/face/58.jpg"))
        self.label_5.setObjectName("label_4")
        self.label_5.setScaledContents(True)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 410, 200, 200))
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton")
        
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(300, 410, 200, 200))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../data/sprites/face/78.jpg"))
        self.label_6.setObjectName("label_4")
        self.label_6.setScaledContents(True)
        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(300, 410, 200, 200))
        self.pushButton_5.setFlat(True)
        self.pushButton_5.setObjectName("pushButton")
        
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(560, 410, 200, 200))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("../data/sprites/face/25.jpg"))
        self.label_7.setObjectName("label_4")
        self.label_7.setScaledContents(True)
        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(560, 410, 200, 200))
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton")
       
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "")) # "Florizar"
        self.pushButton_2.setText(_translate("Dialog","" )) # "Dracaufeu"
        self.pushButton_3.setText(_translate("Dialog", "")) # "Tortank"
        self.pushButton_4.setText(_translate("Dialog", "")) # "Caninos"
        self.pushButton_5.setText(_translate("Dialog", "" )) # "Galopa"
        self.pushButton_6.setText(_translate("Dialog", "")) # "Pikachu"
        self.label.setText(_translate("Dialog", "Choisissez 3 pokemon de départ : "))

    

        

class MyApp2(QMainWindow):

    def __init__(self, sac_pokemon):
        super().__init__()
        self.ui = Interface_choix()
        self.ui.setupUi(self, sac_pokemon)

        self.ui.pushButton.clicked.connect(self.choix_pokemon_1)
        self.ui.pushButton_2.clicked.connect(self.choix_pokemon_2)
        self.ui.pushButton_3.clicked.connect(self.choix_pokemon_3)
        self.ui.pushButton_4.clicked.connect(self.choix_pokemon_4)
        self.ui.pushButton_5.clicked.connect(self.choix_pokemon_5)
        self.ui.pushButton_6.clicked.connect(self.choix_pokemon_6)
        
    
    def choix_pokemon_1(self):
        pokemon_1 = pk.number_to_pokemon(3)
        sac_pokemon.objets.append(pokemon_1)
        
    def choix_pokemon_2(self):
        pokemon_2 = pk.number_to_pokemon(6)
        sac_pokemon.objets.append(pokemon_2)
        
    def choix_pokemon_3(self):
        pokemon_3 = pk.number_to_pokemon(9)
        sac_pokemon.objets.append(pokemon_3)
        
    def choix_pokemon_4(self):
        pokemon_4 = pk.number_to_pokemon(58)
        sac_pokemon.objets.append(pokemon_4)
        
    def choix_pokemon_5(self):
        pokemon_5 = pk.number_to_pokemon(78)
        sac_pokemon.objets.append(pokemon_5)
        
    def choix_pokemon_6(self):
        pokemon_6 = pk.number_to_pokemon(25)
        sac_pokemon.objets.append(pokemon_6)

        
 


if __name__ == "__main__":
    
    sac_pokemon = Sac()
    # pokemon1 = Pokemon("Sabelette", 0, 45, 48, [0, 1], "Ground")
    # pokemon2 = Pokemon("Pikachu", 0, 45, 48, [0, 1], "Fairy")
    # pokemon3 = Pokemon("Abo", 0, 45, 48, [0, 1], "Rock")
    # sac_pokemon.capture_pokemon(pokemon1)
    # sac_pokemon.capture_pokemon(pokemon2)
    # sac_pokemon.capture_pokemon(pokemon3)
    
    def run_app():
        app = QApplication(sys.argv)
        mainWin = MyApp2(sac_pokemon)
        mainWin.show()
        app.exec_()
        
    run_app()
    print(sac_pokemon)
