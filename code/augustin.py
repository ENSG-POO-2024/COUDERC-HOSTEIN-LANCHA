import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import fenetreQT
import sys
from random import randint

path = os.path.dirname(os.path.abspath(__file__))
print (path)

list_pokemon = pd.read_csv(os.path.join(path, "../data/pokemon_first_gen.csv"), delimiter = ',')
position_pokemon = pd.read_csv(os.path.join(path,"../data/pokemon_coordinates.csv"), delimiter =',')



class Red:
    def __init__(self,x,y, terrain):
        self.x = x
        self.y = y
        self.biome = terrain

    def __str__(self):
        return "Hey ! Moi, c'est Red"
    
    def chg_biome (self,x,y):
        pass
    

class Carte :
    def __init__(self,matrice):
        self.map = matrice   



class Vue:
    def __init__(self,carte,x0,y0): # A modifier (doit dependre de la pos de red)
        self.x = x0
        self.y = y0
        self.monde = carte
        self.biome_red = carte[x0,y0]
        self.tuiles =  os.listdir(os.path.join(path,"../data/img/"))
        self.map_init = (os.path.join(path,"../data/init.png"))
    
    
    def genere_matrice(self):
        
        matrice  = np.copy(self.monde[self.x - 4 : self.x + 5, self.y - 5 : self.y + 5])
        self.biome_red = matrice[4,4]
        matrice[4,4] = int(str(99) + str(self.biome_red))
        return matrice
    
    def genere_terrain (self):
        result = np.zeros((16*9, 16 * 10, 4)) # vue vierge
        matrice = self.genere_matrice()
        for i in range(matrice.shape[0]):
            for j in range(matrice.shape[1]):
                result[i*16:(i+1)*16, j*16:(j+1)*16,:] =  img.imread((os.path.join(path,"../data/img/"))+ str(matrice[i,j])+".png")# A terme utiliser un DICO avec les img reliees aux nb dans la matrice

        
        plt.imshow(result)
        plt.imsave((os.path.join(path,"../data/map.jpg")), result)
        self.map_init = (os.path.join(path,"../data/map.jpg"))
    
    def hautes_herbes(self):
        if self.biome_red == 1 :
            if randint(1, 7) == 5:
                return randint(1,151)
        return 0
    
    def deplacement(self,direction):
        x_max, y_max = self.monde.shape
        if direction == "b" and self.x + 5 < x_max:
            self.x += 1
            self.genere_terrain()
        elif direction == "d" and self.y + 5  < y_max:
            self.y += 1
            self.genere_terrain()
        elif direction == "h" and self.x -4 > 0 :
            self.x -= 1
            self.genere_terrain()
        elif direction == "g" and self.y -5 > 0 :
            self.y -= 1
            self.genere_terrain()
        else:
            print("limite terrain")




class Jouer () :
    
    def __init__(self, grille):
        self.terrain = Vue(grille, 15, 15)
        self.commencer()
    
    def commencer(self):
        app = fenetreQT.QApplication(sys.argv)
        mainWindow = fenetreQT.ImageWindow(self.terrain)
        mainWindow.initUI()
        sys.exit(app.exec_())

if __name__ == "__main__":
    
    
    
    matrix2 = np.array([
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

    matrix = np.genfromtxt("../data/terrain.csv", delimiter=';',dtype=int)
    
    #IMG Vide
    terrain_complet = np.zeros((16 * matrix.shape[0], 16 * matrix.shape[1], 4))
    #on parcourt et on concatene
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            terrain_complet[i*16:(i+1)*16, j*16:(j+1)*16,:] =  img.imread((os.path.join(path,"../data/img/"))+ str(matrix[i, j]) + ".png")
    
    plt.imshow(terrain_complet)
    plt.axis('off')
    plt.show()
    
    MAPP = Vue(matrix,15,15)

    A = Jouer(matrix)