# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:02:15 2024

@author: melanie
"""



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

from fenetre1 import Ui_Dialog
from fenetre1 import Ui_Dialog2

import sys
import numpy as np
from random import randint


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

def combat(liste_pkmn,pkmn_sauvage):
    current_pokemon = liste_pkmn[0]
    combat_fini = False
    fuite = False
    capture = False
    while not combat_fini:
        a = [0,1] #on gerera ça plus tard avec qt
        #a est du type [int,int], le premier entier donne l'action a realiser (attaque,changer de pokemon,capture,fuite)
        #le second donne le detail de cette action (numero de l'attaque,du pokemon a changer)
        if a[0] == 0:
            print(0)
            capacite = toutes_capacites[a[1]]
            print("a")
            print(capacite)
            print("b")
            current_pokemon.attaque(capacite,pkmn_sauvage)
        elif a[0] == 1:
            print(1)
            #changer de pokemon
            pass
        elif a[0] == 2:
            print(2)
            capture = True
        elif a[0] == 3:
            print(3)
            fuite = True
        if pkmn_sauvage.ko or fuite or capture :
            print(4)
            combat_fini = True
        else :
            print(5)
            pkmn_sauvage.attaque(pkmn_sauvage.liste_capacites[randint(0,1)],current_pokemon)
        if current_pokemon.ko :
            print(6)
            combat_fini = True



class Pokemon:
    def __init__(self,nom,pv,atk,dfs,liste_capacites,type1,type2 = "neutral"):
        #On a défini par défaut le 2nd type comme neutre mais le programme accepte 2 types distincts
        self.nom = nom
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.pv_tot = pv
        self.atk = atk
        self.dfs = dfs
        #On a choisi d'ajouter des statistiques multiplicatives d'attaque et de défense qui permettent
        #respectivement d'augmenter les dégâts infligés et de réduire les dégâts subis
        self.ko = False
        self.liste_capacites = liste_capacites
        
    def attaque(self,capacite,adv):
        #On utilise d'abord une fonction attaque dans le pokémon attaquant pour appliquer les éventuels modificateurs de dégâts liés au pokémon
        pui = capacite[1]
        print(pui)
        if self.type1 == capacite[2] or self.type2 == capacite[2]:
            #On a introduit le concept des attaques "STAB" : si le pokémon et son attaque sont de même type, celle-ci augmente de puissance
            if not capacite[2] == "neutral":
                #l'attaque neutre doit rester de puissance indépendante du type néanmoins
                pui *= 1.5
        pui *= self.atk
        #les dégâts augmentent avec la statistique d'attaque du pokémon
        adv.degats(capacite[2],pui)
    def degats(self,type_atk,pui):
        pui *= self.dfs
        #les dégâts sont réduits par la statistique de défense
        pui *= efficiencies[types_dict[type_atk],types_dict[self.type1]]
        pui *= efficiencies[types_dict[type_atk],types_dict[self.type2]]
        #On calcule l'efficacité de l'attaque reçue en fonction des types du pokémon
        if pui >= self.pv:
            self.pv = 0
            self.ko = True
            #Si l'attaque rend le pokemon KO, on met ses PV à 0 (pas de PV négatifs)
        else :
            self.pv = np.ceil(self.pv - pui)

class PokemonSauvage(Pokemon):
    #On crée une sous-classe spécifiquement pour les pokémon sauvages
    #ceux-ci disposent en plus d'un taux de capture, et leur sprite est différent
    def __init__(self):
        super().__init__()
    

class Sac:

    def __init__(self):
        Clefairy = Pokemon("Clefairy", 70, 45, 48, [0, 1], "Fairy")
        Vulpix = Pokemon("Vulpix", 38, 41, 40, [0, 1], "Fire")
        Seel = Pokemon("Seel", 65, 45, 55, [0, 1], "Water")
        self.objets = [Clefairy, Vulpix, Seel]


    def __str__(self):
        txt = "Le sac contient : "
        for obj in self.objets:
            txt += str(obj.nom)
            txt += " "
        return txt


    def changer_place(self, pokemon, nouvelle_place):
        # pour changer la place d'un pokemon dans le sac(attention la place du début est 0)
        if pokemon not in self.objets:
            print("Ce Pokémon n'est pas dans le sac !")
        else:
            self.objets[self.objets.index(pokemon)], self.objets[nouvelle_place] = self.objets[nouvelle_place], self.objets[self.objets.index(pokemon)]


    def changer_pokemon(self):
        #on veut changer de pokemon durant le combat
        pass

    def capture_pokemon(self, pokemon):
        # on ne peut capturer le pokemon que si le combat a été gagné
        capture = False
        if pokemon.pv == 0:
             self.objets.append(pokemon)
             capture = True
        return capture




class MyApp(QMainWindow):

    def __init__(self, sac_pokemon):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self, sac_pokemon)
        
        # pour que quand on clique sur un bouton, une nouvelle fenêtre s'affiche
        self.ui.pushButton.clicked.connect(self.affich)
        self.ui.pushButton_2.clicked.connect(self.affich)
        self.ui.pushButton_3.clicked.connect(self.affich)
        self.ui.pushButton_4.clicked.connect(self.affich)
        self.ui.pushButton_5.clicked.connect(self.affich)
        self.ui.pushButton_6.clicked.connect(self.affich)
        
        # on veut ensuite que quand on a clique sur le pokemon
        # il soit à cet endroit dans la liste 
        
        
        
        
        
    def affich(self):
        mainWin = XXXXDlg(self, sac_pokemon)
        mainWin.exec()

    # def reject(self):
    #     super().reject()
        
    # def accept(self):
    #     super().accept()
        
        
class XXXXDlg(QDialog):

    def __init__(self, parent=None, sac_pokemon=None):
        super().__init__(parent)
        self.ui = Ui_Dialog2()
        self.ui.setupUi(self, sac_pokemon)
        
    # def accept(self):
    #     super().accept()        
        
        
        

if __name__ == "__main__":
    
    sac_pokemon = Sac()
    pokemon1 = Pokemon("Ponita", 0, 45, 48, [0, 1], "Fire")
    pokemon2 = Pokemon("Dratini", 0, 45, 48, [0, 1], "Fairy")
    pokemon3 = Pokemon("Magmar", 0, 45, 48, [0, 1], "Rock")
    sac_pokemon.capture_pokemon(pokemon1)
    sac_pokemon.capture_pokemon(pokemon2)
    sac_pokemon.capture_pokemon(pokemon3)
    
    def run_app():
        app = QApplication(sys.argv)
        mainWin = MyApp(sac_pokemon)
        mainWin.show()
        app.exec_()
        
    run_app()

    '''
    def run_dlg():
        dlg = QApplication(sys.argv)
        mainWin = XXXXDlg(sac_pokemon)
        mainWin.show()
        dlg.exec_()
        
    run_dlg()
    '''
        

 













































