import numpy as np
import pandas as pd
import matplotlib.image as img


list_pokemon = pd.read_csv("../data/pokemon_first_gen.csv", delimiter = ',')
position_pokemon = pd.read_csv("../data/pokemon_coordinates.csv", delimiter =',')


a = img.imread('../data/carte.jpg')



class Red:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def deplacement(self,direction):
        if direction == "h" :
            self.y += 1
        elif direction == "d" :
            self.x += 1
        elif direction == "b" :
            self.y -= 1
        elif direction == "g" :
            self.x -= 1
    def __str__(self):
        return "Hey ! Moi, c'est Red"


class Pokemon_S :
    
    def __init__(self,x,y,etat,nom):
        self.x = x
        self.y = y
        self.etat = etat
        self.nom = nom
    
    def dist_perso (self, perso):
        return np.sqrt ((self.x - perso.x)**2 + (self.y - perso.y)**2)
    
    def est_proche(self, perso, d):
        return self.dist_perso(perso) < d
    
    def montrer (self):
        self.etat = 1
    
    def cacher(self):
        self.etat = 0   
    
    
    def __str__(self):
        return self.nom


class Carte :
    def __init__(self,file):
        
class Vue :
    def __init__(self,carte,x0,y0):
        self.x = x0
        self.y = y0
    
    
    def deplacement(self,direction):
        if direction == "h" :
            self.y += 1
        elif direction == "d" :
            self.x += 1
        elif direction == "b" :
            self.y -= 1
        elif direction == "g" :
            self.x -= 1
    
    
    def afficher(self):
        
    
    