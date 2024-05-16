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
import melanie

path = os.path.dirname(os.path.abspath(__file__))
print (path)




class ImageWindow(QMainWindow):
    """
    Classe définissant la fenêtre principale de jeu
    """
    
    
    def __init__(self, vue):
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
        self.combat = 0     #Initialisation du combat

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
        
        # Génération des fenetre terrain et combat        
        self.terrain= c.Carte(self, self.vue)        
        
        self.terrain.show_map()
        self.fight = c.inter_combat(self, 25, 137)
        
        # Génération du sac
        
        self.sac = melanie.Sac()
        
        # On n'est pas en phase de combat, donc cacher l'interface
        self.fight.hide()
        
        
        # boutons du combat
        
        self.fight.pushButton_4.clicked.connect(self.fuir)
        # self.fight.pushButton_3.clicked.connect(self.sac)s
        
        
    def fuir(self):
        self.combat = 0
        self.setupUI()
        

                
        
    def keyPressEvent(self, event):
        """
        définit les evts associés à la pression des touches

        """
        if self.combat == 0 :  # si on n'est pas en phase de combat
            
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
                
                if key == 83 :
                    self.terrain.hide()
                    self.sac.show()
                
                self.terrain.show_map()
                self.combat = self.terrain.combat
            else :
                pass
        else :
            # print(self.combat)
            self.terrain.hide()
            print(self.combat)
            self.fight.show(25, self.combat)


class Red:
    def __init__(self,x,y, terrain):
        self.x = x
        self.y = y
        self.biome = terrain

    def __str__(self):
        return "Hey ! Moi, c'est Red"
    
    def chg_biome (self,x,y):
        pass


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

    MAPP = Vue(matrix,15,15)
    app = QtWidgets.QApplication(sys.argv)
    ui = ImageWindow(MAPP)
    ui.setupUI()
    ui.show()
    sys.exit(app.exec_())


