import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import tkinter as tk

list_pokemon = pd.read_csv("../data/pokemon_first_gen.csv", delimiter = ',')
position_pokemon = pd.read_csv("../data/pokemon_coordinates.csv", delimiter =',')


class Red:
    def __init__(self,x,y, terrain):
        self.x = x
        self.y = y
        self.biome = terrain
    
    # def deplacement(self,direction):
    #     if direction == "h" :
    #         self.y += 1
    #     elif direction == "d" :
    #         self.x += 1
    #     elif direction == "b" :
    #         self.y -= 1
    #     elif direction == "g" :
    #         self.x -= 1
    def __str__(self):
        return "Hey ! Moi, c'est Red"
    
    def chg_biome (self,x,y):
        pass
    
    


class Pokemon_S :
    
    def __init__(self,x,y,etat,nom):
        self.x = x
        self.y = y
        self.etat = etat
        self.nom = nom
    
    def dist_perso (self, perso):
        return np.sqrt ((self.x - perso.x)**2 + (self.y - perso.y)**2)
    

    
    def montrer (self):
        self.etat = 1
    
    def cacher(self):
        self.etat = 0   
        
    def est_proche(self, perso, d):

        if self.dist_perso(perso) < d :
            self.etat = 1
            return True
        return False
    
    
    def __str__(self):
        return self.nom



class Carte :
    def __init__(self,matrice):
        self.map = matrice   



class Vue:
    def __init__(self,carte,x0,y0):
        self.x = x0
        self.y = y0
        self.monde = carte
        self.tuiles =  os.listdir("../data/img/")
    
    
    def genere_matrice(self):
        
        matrice  = np.copy(self.monde[self.x - 4 : self.x + 5, self.y - 5 : self.y + 5])
        matrice[4,4] = 2
        return matrice
    
    def genere_terrain (self):
        result = np.zeros((16*9, 16 * 10, 4)) # vue vierge
        matrice = self.genere_matrice()
        for i in range(matrice.shape[0]):
            for j in range(matrice.shape[1]):
                result[i*16:(i+1)*16, j*16:(j+1)*16,:] =  img.imread("../data/img/"+ self.tuiles[matrice[i, j]])# A terme utiliser un DICO avec les img reliees aux nb dans la matrice


        plt.imshow(result)
        plt.axis('off')
        plt.show()
    
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


if __name__ == "__main__":
    
    
    
    # h = img.imread("../data/img/0.png")
    # p = img.imread("../data/img/1.png")
    
    # plt.imshow(h)
    # plt.show()
    
    # plt.imshow(p)
    # plt.show()
    
    
    
    # img_conc = np.concatenate((h,p), axis=1)
    # plt.imshow(img_conc)
    # plt.axis('off')
    # plt.show()
    
    
    
    # def conc (img1,img2,ax):
    #     return np.concatenate((img1,img2),axis = 0)
    
    

    
    matrix = np.array([
        [0, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 4, 4, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
        [0, 4, 4, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 4, 4, 3, 0, 0, 3, 3, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [0, 0, 0, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 4, 4, 3, 0, 0, 3, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1],
        [0, 0, 0, 4, 4, 4, 3, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 4, 3, 3, 0, 1, 1, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 3, 3, 3, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3],
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 4, 4, 4, 4, 4, 4, 4, 0, 0, 4, 4, 4, 4, 4],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ])
    
    #IMG Vide
    terrain_complet = np.zeros((16 * matrix.shape[0], 16 * matrix.shape[1], 4))
    #on parcourt et on concatene
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            terrain_complet[i*16:(i+1)*16, j*16:(j+1)*16,:] =  img.imread("../data/img/"+ str(matrix[i, j]) + ".png")
    
    plt.imshow(terrain_complet)
    plt.axis('off')
    plt.show()
    
    
    
    MAPP = Vue(matrix,15,15)
    window=tk.Tk()

    
    KEYS_PRESSED=set()
    
    def keypress_on(event):
        KEYS_PRESSED.add(event.keysym)
    
    
    def keypress_off(event):
        KEYS_PRESSED.discard(event.keysym)
    
    window.bind("<KeyPress>", keypress_on)
    window.bind("<KeyRelease>", keypress_off)
    
    def tache():
        if KEYS_PRESSED == {'Right'}:
            MAPP.deplacement("d")
        if KEYS_PRESSED == {'Left'}:
            MAPP.deplacement("g")
        if KEYS_PRESSED == {'Down'}:
            MAPP.deplacement("b")
        if KEYS_PRESSED == {'Up'}:
            MAPP.deplacement("h")
        window.after(100,tache)
    window.after(10,tache)
    window.mainloop()
    
    