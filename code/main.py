from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QPixmap
import numpy as np
import time as tm
import os
import carte_combat as c
from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as img
import fenetre1 as sac_inter
from melanie import *
from PyQt5.Qt import Qt
import pandas as pd
import essai_combat as cb
import pokemon as pk
from PyQt5.QtCore import QEventLoop, QTimer

path = os.path.dirname(os.path.abspath(__file__))
print (path)



list_pokemon = pd.read_csv(("../data/pokemon_first_gen.csv"), delimiter = ',')

class ImageWindow(QMainWindow):
    """
    Classe définissant la fenêtre principale de jeu
    """
    
    
    def __init__(self, vue, sac_pokemon):
        """
        

        Parameters
        ----------
        vue : Vue
            La map de jeu, de type Vue, qui contient les informations de terrain

        Returns
        -------
        None.

        """
        super().__init__()
        self.vue = vue
        self.sac_pokemon = sac_pokemon
        self.combat = 0     #Initialisation du combat
        self.menu = 0
        self.type_attaque = [0,0]
        
        
    def setupUI(self):
        """
        Initialise le jeu, en définissant les nouveaux attributs de la fenetre que sont les parties du jeu

        Returns
        -------
        None.

        """
        self.setWindowTitle('Pokemon')
        self.setGeometry(150, 150, 900, 820)

        self.start = tm.time()
        self.pok1 = pk.number_to_pokemon(25)
        self.pok2 = pk.number_to_pokemon(13)
        # Génération des fenetre terrain et combat        
        self.terrain= c.Carte(self, self.vue)        
        
        self.terrain.show_map()
        self.fight = c.inter_combat(self, self.pok1, self.pok2)
        self.attaque_p = cb.Combat(self.sac_pokemon)
        self.wild_pokemon = self.pok1
        
        # Génération du sac
        
        self.sac = sac_inter.Interface_sac(self, self.sac_pokemon)
        self.sac.hide()
        
        # On n'est pas en phase de combat, donc cacher l'interface
        self.fight.hide()
        
        
        # boutons du combat
        self.setFocusPolicy(Qt.StrongFocus)
        self.button_action()
        
        
    def fuir(self):
        self.combat = 0
        self.fight.hide()
        self.terrain.show_map()
        self.menu = 0
        

    def close_sac(self):
        self.sac.hide()
        if self.combat == 0:
            self.terrain.show_map()
        else:
            self.fight.show(self.sac_pokemon.objets[0], self.wild_pokemon)
        self.menu = 0
    
    def open_sac(self):
        self.fight.att_hide()
        self.fight.hide()
        self.sac.show()
        self.menu = 1
    
    def show_fight(self):
        self.fight.att_show(self.sac_pokemon.objets[0], self.wild_pokemon)
    
    def keyPressEvent(self, event):
        """
        définit les evts associés à la pression des touches

        """
        if self.combat == 0 and self.menu == 0 :  # si on n'est pas en phase de combat
            
            key = event.key()
            print(f"Touche pressée : {key}")
            if tm.time() - self.start > 0.01 :
                key = event.key()
                if key == 16777235 :
                    self.terrain.map.deplacement("h")
                    self.start = tm.time()
                if key == 16777237 :
                    self.terrain.map.deplacement("b")
                    self.start = tm.time()
                if key == 16777234 :
                    self.terrain.map.deplacement("g")
                    self.start = tm.time()
                if key == 16777236:
                    self.terrain.map.deplacement("d")
                    self.start = tm.time()
                self.img = "../data/map.jpg"
                
                self.terrain.show_map()
                
                if key == 83 :
                    self.terrain.hide()
                    self.sac.show()
                    self.menu = 1
                    
                
                
                self.combat = self.terrain.combat
        else :
            if self.menu == 0:
                # print(self.combat)
                self.terrain.hide()
                # print(self.combat)
                self.wild_pokemon = pk.number_to_pokemon(self.combat)
                self.attaque_p = cb.Combat(self.sac_pokemon)
                self.fight.show(self.sac_pokemon.objets[0], pk.number_to_pokemon(self.combat))
                # self.combat_pok()
            
            
    def monter(self):
         rang_selectionnes = [index.row() for index in self.sac.listWidget.selectedIndexes()]
         for rang in rang_selectionnes :
             if rang > 0:
                 nouveau_rang = rang - 1
                 self.sac.listWidget.insertItem(nouveau_rang, self.sac.listWidget.takeItem(rang))
                 self.sac.listWidget.setCurrentRow(nouveau_rang)
                 sac_pokemon.changer_place(sac_pokemon.objets[rang], nouveau_rang)
                 #print(sac_pokemon)
                 
        
    def descendre(self):        
         rang_selectionnes = [index.row() for index in self.sac.listWidget.selectedIndexes()]
         for rang in reversed(rang_selectionnes) :
             if rang < self.sac.listWidget.count()-1 :
                 nouveau_rang = rang+1
                 self.sac.listWidget.insertItem(nouveau_rang, self.sac.listWidget.takeItem(rang))
                 self.sac.listWidget.setCurrentRow(nouveau_rang) 
                 sac_pokemon.changer_place(sac_pokemon.objets[rang], nouveau_rang)
                 #print(sac_pokemon)
    
    def button_action(self):
        
        # self.fight.pushButton_4.clicked.connect(self.fuir)
        self.sac.pushButton_1.clicked.connect(self.monter)
        self.sac.pushButton_2.clicked.connect(self.descendre)
        self.sac.pushButton_3.clicked.connect(self.close_sac)
        
        self.fight.pushButton.clicked.connect(self.combat_pok)
        self.fight.pushButton_3.clicked.connect(self.open_sac)
        self.fight.pushButton_2.clicked.connect(self.capt_pok)
        self.fight.pushButton_4.clicked.connect(self.fuite_pok)
        
        self.fight.att1.clicked.connect(lambda: self.set_value_fight([0,0]))
        self.fight.att2.clicked.connect(lambda: self.set_value_fight([0,1]))
        self.fight.att3.clicked.connect(lambda: self.set_value_fight([0,2]))
        self.fight.att4.clicked.connect(lambda: self.set_value_fight([0,3]))
        
        
        # self.fight.pushButton_3.clicked.connect(self.open_sac)
        # self.fight.pushButton.clicked.connect(self.combat_pok)
    
    def fuite_pok(self):
        self.type_attaque = [3,0]
        self.attaque_p.a = self.type_attaque
        self.attaque_p.attaque_pokemon(self.wild_pokemon)
        if self.attaque_p.fuite or self.attaque_p.combat_fini:
            self.fuir()
        else:
            pass
    
    def capt_pok (self):
        print("ici, c'est bon !")
        self.type_attaque = [2,1]
        self.attaque_p.a = self.type_attaque
        self.attaque_p.attaque_pokemon(self.wild_pokemon)
        if self.wild_pokemon.pv <= 0 or self.attaque_p.capture:
            self.sac_pokemon.capture_pokemon(self.wild_pokemon)
            # self.sac.hide()
            print(self.sac_pokemon)
            self.fight.hide()
            self.combat = 0 
            self.menu = 0
            self.terrain.show_map()
            
    
    
    
    
    def combat_pok (self):
        print(self.combat)
    
        
        if not self.attaque_p.combat_fini :
            self.fight.att_show(self.sac_pokemon.objets[0], self.wild_pokemon)

            self.waitForButtonClick()
            self.attaque_p.a = self.type_attaque
            self.attaque_p.attaque_pokemon(self.wild_pokemon)
            
            self.fight.show(self.sac_pokemon.objets[0], self.wild_pokemon)

            print(self.wild_pokemon.pv)
            print(self.sac_pokemon.objets[0].pv)
            
            if self.attaque_p.combat_fini :
                self.fight.pushButton.hide()
                self.combat = 0
        else :
            print("combat fini")
                

        
    def waitForButtonClick(self):
         loop = QEventLoop()
         self.fight.att1.clicked.connect(loop.quit)
         self.fight.att2.clicked.connect(loop.quit)
         self.fight.att3.clicked.connect(loop.quit)
         self.fight.att4.clicked.connect(loop.quit)
         self.fight.pushButton.clicked.connect(loop.quit)
         self.fight.pushButton_4.clicked.connect(loop.quit)
         self.fight.pushButton_3.clicked.connect(loop.quit)
         self.fight.pushButton_2.clicked.connect(loop.quit)
         loop.exec_()
    
    def set_value_fight(self,val):
        if not self.attaque_p.combat_fini:
            self.type_attaque = val
    
    
    
    
    
    
    
    
    
    
    
    
    
    















class Vue:
    
    def __init__(self,carte,x0,y0): # A modifier (doit dependre de la pos de red)
        self.x = x0
        self.y = y0
        self.monde = carte
        self.biome_red = carte[x0,y0]
        self.combat = 0
        self.tuiles =  os.listdir(os.path.join(path,"../data/img/"))
        self.map_init = (os.path.join(path,"../data/init.png"))
        self.matrice = np.copy(self.monde[self.x - 4 : self.x + 5, self.y - 5 : self.y + 5])
    
    def genere_matrice(self):
        
        matrice  = np.copy(self.monde[self.x - 4 : self.x + 5, self.y - 5 : self.y + 5])
        self.biome_red = matrice[4,4]
        matrice[4,4] = int(str(99) + str(self.biome_red))
        self.matrice = matrice
        return matrice
    
    def genere_terrain (self):
        result = np.zeros((16*9, 16 * 10, 4)) # vue vierge
        matrice = self.genere_matrice()
        for i in range(matrice.shape[0]):
            for j in range(matrice.shape[1]):
                result[i*16:(i+1)*16, j*16:(j+1)*16,:] =  img.imread((os.path.join(path,"../data/img/"))+ str(matrice[i,j])+".png")# A terme utiliser un DICO avec les img reliees aux nb dans la matrice

        
        plt.imsave((os.path.join(path,"../data/map.jpg")), result)
        self.map_init = (os.path.join(path,"../data/map.jpg"))
    
    def hautes_herbes(self):
        if self.biome_red == 1 :
            if randint(1, 15) == 5:
                return randint(1,151)
        return 0
    
    def deplacement(self,direction):
        x_max, y_max = self.monde.shape
        if direction == "b" and self.x + 5 < x_max :
            if self.matrice[5,4] != 3 :
                self.x += 1
            self.genere_terrain()
        elif direction == "d" and self.y + 5  < y_max :
            if self.matrice[4,5] != 3 :
                self.y += 1
            self.genere_terrain()
        elif direction == "h" and self.x -4 > 0 :
            if self.matrice[3,4] != 3 :
                self.x -= 1
            self.genere_terrain()
        elif direction == "g" and self.y -5 > 0 :
            if self.matrice[4,3] != 3 :
                self.y -= 1
            self.genere_terrain()
        self.combat = self.biome_red


if __name__ == '__main__':
    matrix1 = np.array([
        [5, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [5, 4, 4, 5, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 1],
        [5, 4, 4, 5, 5, 5, 5, 5, 1, 1, 5, 1, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 1, 1],
        [5, 5, 4, 4, 3, 5, 5, 3, 3, 5, 5, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1],
        [5, 5, 5, 4, 4, 3, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1],
        [5, 5, 5, 4, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 5, 5, 1, 1],
        [5, 5, 5, 4, 4, 3, 5, 5, 3, 1, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 1],
        [5, 5, 5, 4, 4, 4, 3, 5, 5, 1, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 1],
        [5, 5, 5, 5, 4, 4, 3, 3, 5, 1, 1, 1, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5],
        [5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [1, 5, 1, 5, 5, 5, 5, 5, 3, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 3, 3],
        [1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4],
        [1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 5, 5, 4, 4, 4, 4, 4],
        [1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
        [1, 5, 5, 1, 5, 5, 5, 5, 5, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 5, 5],
        [1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1],
        [1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1],
        [1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 5, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 5, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ])
    matrix = np.genfromtxt((os.path.join(path,"../data/terrain.csv")), delimiter=';',dtype=int)
    
    
    
    sac_pokemon = Sac()
    # pokemon1 = pk.number_to_pokemon(25)
    # pokemon2 = pk.number_to_pokemon(30)
    # pokemon3 = pk.number_to_pokemon(40)
    # sac_pokemon.capture_pokemon(pokemon1)
    # sac_pokemon.capture_pokemon(pokemon2)
    # sac_pokemon.capture_pokemon(pokemon3)
    
    MAPP = Vue(matrix,30,15)
    app = QtWidgets.QApplication(sys.argv)
    ui = ImageWindow(MAPP, sac_pokemon)
    ui.setupUI()
    ui.show()
    sys.exit(app.exec_())


