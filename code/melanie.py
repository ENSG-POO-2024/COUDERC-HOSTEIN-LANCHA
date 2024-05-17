# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:02:15 2024

@author: melanie
"""



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QListWidget

from fenetre1 import Interface_sac


import sys
import numpy as np
from random import randint
import pokemon as pk


toutes_capacites = np.array([
    ["charge"           ,1  ,"normal"   ,100],
    ["fouet lianes"     ,1  ,"grass"    ,100],
    ["écume"            ,1  ,"water"    ,100],
    ["flammèche"        ,1  ,"fire"     ,100]
    ])

efficiencies = np.array([
    [0.5,1  ,1  ,0.5,0.5,0.5,2  ,2  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ,1  ],
    [2  ,1  ,1  ,1  ,1  ,1  ,0.5,2  ,0.5,2  ,1  ,0.5,0.5,2  ,1  ,0  ,2  ,0.5,1  ],
    [0.5,1  ,2  ,1  ,1  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,0.5,1  ,2  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,2  ,0.5,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ],
    [2  ,1  ,0.5,0.5,1  ,0.5,1  ,2  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [0.5,2  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,2  ,1  ,1  ],
    [0.5,1  ,2  ,0.5,1  ,0.5,1  ,0.5,1  ,1  ,2  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,1  ],
    [0.5,0.5,1  ,1  ,1  ,0.5,0.5,1  ,1  ,1  ,2  ,0.5,2  ,1  ,1  ,0.5,2  ,0.5,1  ],
    [0.5,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,0  ,1  ,1  ,1  ],
    [0.5,1  ,0.5,2  ,1  ,0.5,1  ,1  ,0.5,1  ,0.5,0.5,1  ,2  ,2  ,1  ,1  ,0.5,1  ],
    [0  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5,0.5,0.5,1  ,1  ,1  ],
    [0.5,2  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ],
    [0.5,0.5,1  ,1  ,1  ,2  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ],
    [2  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,0.5,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,0  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [1  ,0.5,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [0.5,2  ,1  ,1  ,0.5,1  ,1  ,1  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ]
    ])
#On a défini la table des classes à l'aide d'un array numpy.
#la 19e ligne/colonne correspond au "type" neutre qui est utile pour définir deux types ou pour l'attaque neutre
types_dict = {"steel":0,"fighting":1,"dragon":2,"water":3,"electric":4,"fire":5,"fairy":6,"ice":7,"bug":8,"normal":9,"grass":10,"poison":11,"psychic":12,"rock":13,"ground":14,"ghost":15,"dark":16,"flying":17,"neutral":18}
#l'utilisation d'un dictionnaire avec des indices correspondant au tableau permet une correspondance entre types et efficacités des attaques
    

class Sac:

    def __init__(self):
        # on initialise le sac avec 3 pokemons 
        p1 = pk.number_to_pokemon(30)
        p2 = pk.number_to_pokemon(40)
        p3 = pk.number_to_pokemon(10)
        self.objets = [p1, p2, p3]


    def __str__(self):
        # afin d'afficher dans la console ce que le sac contient  
        txt = "Le sac contient : "
        for obj in self.objets:
            txt += str(obj.name)
            txt += " "
        return txt


    def changer_place(self, pokemon, nouvelle_place):
        # pour changer la place d'un pokemon dans le sac (attention la place du début est 0)
        if pokemon not in self.objets:
            print("Ce Pokémon n'est pas dans le sac !")
        else:
            self.objets[self.objets.index(pokemon)], self.objets[nouvelle_place] = self.objets[nouvelle_place], self.objets[self.objets.index(pokemon)]

    def capture_pokemon(self, pokemon):
        # permet d'ajouter le pokemon dans le sac 
        # en l'ajoutant dans le sac, on lui redonne tous ses pv (guérison)
        pokemon.pv = pokemon.pv_max
        self.objets.append(pokemon)



class MyApp(QMainWindow):

    def __init__(self, sac_pokemon):
        super().__init__()
        self.ui = Interface_sac()
        self.ui.setupUi(self, sac_pokemon)

        self.ui.pushButton_1.clicked.connect(self.monter)
        self.ui.pushButton_2.clicked.connect(self.descendre)
          
        
    def monter(self):
         rang_selectionnes = [index.row() for index in self.ui.listWidget.selectedIndexes()]
         for rang in rang_selectionnes :
             if rang > 0:
                 nouveau_rang = rang - 1
                 self.ui.listWidget.insertItem(nouveau_rang, self.ui.listWidget.takeItem(rang))
                 self.ui.listWidget.setCurrentRow(nouveau_rang)
                 sac_pokemon.changer_place(sac_pokemon.objets[rang], nouveau_rang)
                 #print(sac_pokemon)
                 
        
    def descendre(self):        
         rang_selectionnes = [index.row() for index in self.ui.listWidget.selectedIndexes()]
         for rang in reversed(rang_selectionnes) :
             if rang < self.ui.listWidget.count()-1 :
                 nouveau_rang = rang+1
                 self.ui.listWidget.insertItem(nouveau_rang, self.ui.listWidget.takeItem(rang))
                 self.ui.listWidget.setCurrentRow(nouveau_rang) 
                 sac_pokemon.changer_place(sac_pokemon.objets[rang], nouveau_rang)
                 #print(sac_pokemon)
        
        
        
        
       
        

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
        mainWin = MyApp(sac_pokemon)
        mainWin.show()
        app.exec_()
        
    run_app()



 













































