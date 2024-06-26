# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:16:57 2024

@author: melanie
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow 
import sys
from besace import Sac
import pokemon as pk
import interface_sac as int_s



class MyApp2(QMainWindow):

    def __init__(self, sac_pokemon):
        super().__init__()
        self.ui = int_s.Interface_choix()
        self.sac_pokemon = sac_pokemon
        self.ui.setupUi(self, self.sac_pokemon)

        self.ui.pushButton.clicked.connect(self.choix_pokemon_1)
        self.ui.pushButton_2.clicked.connect(self.choix_pokemon_2)
        self.ui.pushButton_3.clicked.connect(self.choix_pokemon_3)
        self.ui.pushButton_4.clicked.connect(self.choix_pokemon_4)
        self.ui.pushButton_5.clicked.connect(self.choix_pokemon_5)
        self.ui.pushButton_6.clicked.connect(self.choix_pokemon_6)
        
    
    def choix_pokemon_1(self):
        pokemon_1 = pk.number_to_pokemon(3)
        self.sac_pokemon.objets.append(pokemon_1)
            
    def choix_pokemon_2(self):
        pokemon_2 = pk.number_to_pokemon(6)
        self.sac_pokemon.objets.append(pokemon_2)
        
    def choix_pokemon_3(self):
        pokemon_3 = pk.number_to_pokemon(9)
        self.sac_pokemon.objets.append(pokemon_3)
        
    def choix_pokemon_4(self):
        pokemon_4 = pk.number_to_pokemon(58)
        self.sac_pokemon.objets.append(pokemon_4)
        
    def choix_pokemon_5(self):
        pokemon_5 = pk.number_to_pokemon(78)
        self.sac_pokemon.objets.append(pokemon_5)
        
    def choix_pokemon_6(self):
        pokemon_6 = pk.number_to_pokemon(25)
        self.sac_pokemon.objets.append(pokemon_6)

        
 


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
