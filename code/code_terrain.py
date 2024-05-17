from random import randint
import matplotlib.pyplot as plt
import matplotlib.image as img
import os
import numpy as np
import pandas as pd

# les deux lignes sont écrites à cause d'un pb de chemin relatif
path = os.path.dirname(os.path.abspath(__file__))
print (path)

# ouverture du fichier contenant la liste des pokemon avec leur nom

list_pokemon = pd.read_csv(("../data/pokemon_first_gen.csv"), delimiter = ',')




class Vue:
    
    def __init__(self,carte,x0,y0): # A modifier (doit dependre de la pos de red)
        self.x = x0
        self.y = y0
        self.monde = carte
        self.biome_red = carte[x0,y0]
        self.combat = 0
        self.map_init = (os.path.join(path,"../data/init.png"))
        self.matrice = np.copy(self.monde[self.x - 4 : self.x + 5, self.y - 5 : self.y + 5])
        self.obstacle = [3,7,10,11,12,13,14,15]
    
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
        if self.biome_red == 1 or self.biome_red == 8:
            if randint(1, 15) == 5:
                return randint(1,151)
        return 0
    
    def deplacement(self,direction):
        x_max, y_max = self.monde.shape
        if direction == "b" and self.x + 5 < x_max :
            if self.matrice[5,4] not in self.obstacle :
                self.x += 1
            self.genere_terrain()
        elif direction == "d" and self.y + 5  < y_max :
            if self.matrice[4,5] not in self.obstacle :
                self.y += 1
            self.genere_terrain()
        elif direction == "h" and self.x -4 > 0 :
            if self.matrice[3,4] not in self.obstacle :
                self.x -= 1
            self.genere_terrain()
        elif direction == "g" and self.y -5 > 0 :
            if self.matrice[4,3] not in self.obstacle :
                self.y -= 1
            self.genere_terrain()
        self.combat = self.biome_red