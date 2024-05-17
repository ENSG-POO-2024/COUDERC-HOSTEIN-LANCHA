from PyQt5 import QtWidgets
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QEventLoop
import numpy as np
import time as tm
import os
import interface_carte_combat as c
import interface_sac as sac_inter
from besace import *
from PyQt5.Qt import Qt
import pandas as pd
import essai_combat as cb
import pokemon as pk
import code_chosir_pokemon as ccp
import code_terrain as ct



# les deux lignes sont écrites à cause d'un pb de chemin relatif
path = os.path.dirname(os.path.abspath(__file__))

# ouverture du fichier contenant la liste des pokemon avec leur nom

list_pokemon = pd.read_csv(("../data/pokemon_first_gen.csv"), delimiter = ',')

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
        self.sac_pokemon = Sac()                        # On crée un objet de type Sac vide
        self.vue = vue                                  # On met le terrain visualisé en attribut
        self.combat = 0                                 # Initialisation du combat
        self.menu = 0                                   # cet attribut permet de controler quand est ce que les fleches engendrent des actions :
                                                        # elles ne doivent pas dans les menus 
        self.type_attaque = [0,0]                       # Cf combat : definit l'action a faire
        self.setFocusPolicy(Qt.StrongFocus)             # cet attribut permet entre autres de ne pas "sortir" de la fonction qui assigne une action aux touches
        self.deja_comb = -1                             # gere si on a deja attaqué dans la phase de combat actuelle : -1 = non
        
    def setupUI(self):
        """
        Initialise le jeu, en définissant les nouveaux attributs de la fenetre que sont les parties du jeu

        Returns
        -------
        None.

        """
        
        # Définition de notre fenêtre de jeu
        
        app = QApplication(sys.argv)
        mainWin = ccp.MyApp2(self.sac_pokemon)
        mainWin.show()
        app.exec_()
        
        self.setWindowTitle('Pokemon')
        self.setGeometry(150, 150, 900, 820)

        self.start = tm.time()
        self.pok1 = pk.number_to_pokemon(25)
        self.pok2 = pk.number_to_pokemon(13)
        
        
        # Génération des fenetre terrain et combat        
        self.terrain= c.Carte(self, self.vue)        
        self.terrain.show_map()
        self.fight = c.inter_combat(self, self.pok1, self.pok2)
        
        # Initialisation de la phase d'attaque
        
        self.attaque_p = cb.Combat(self.sac_pokemon)
        
        # Attribut gérant le pokemon sauvage attaqué
        self.wild_pokemon = self.pok1
        
        # Génération du sac
        
        self.sac = sac_inter.Interface_sac(self, self.sac_pokemon)
        self.sac.hide()
        
        # On n'est pas en phase de combat, donc cacher l'interface
        self.fight.hide()
        
        
        # boutons du combat
        # self.setFocusPolicy(Qt.StrongFocus)
        self.button_action()
        
        
        
    def fuir(self):
        """
            Fonction gérant la fuite lors de l'attaque'
        """
        self.combat = 0
        self.fight.hide()
        self.terrain.show_map()
        self.menu = 0
        

    def close_sac(self):
        
        """
            Fonction gérant la fermeture du sac'
        """
        
        self.sac.hide()
        
        # On regarde quelle fenêtre ouvrir selon si on a ouvert le sac en phase d'attaque ou d'exploration
        if self.combat == 0:
            self.terrain.show_map()
        else:
            self.deja_comb = -1 
            self.fight.show(self.sac_pokemon.objets[0], self.wild_pokemon, self.deja_comb)
        self.menu = 0
    
    def open_sac(self):
        """
        ouverture du sac
        """
        self.fight.att_hide()
        self.fight.hide()
        self.sac.show()
        self.menu = 1           # les fleches perdent leur effet
    
    
    def keyPressEvent(self, event):
        """
        définit les evts associés à la pression des touches

        """
        if self.combat == 0 and self.menu == 0 :  # si on n'est pas en phase de combat
            
            key = event.key()
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
                
                if key == 83 :                  #Si S presse, ouvrir le sac
                    self.terrain.hide()
                    self.sac.show()
                    self.menu = -1
                    
                self.combat = self.terrain.combat  #renvoie 0 si pas de combat et un chiffre entre 1 et 151 correspondant au pokemon attaqué s'il y a un combat
        else :
            
            # Si on est en phase de combat et que le menu n'est pas ouvert
            if self.menu == 0:
                self.deja_comb = -1
                self.terrain.hide() # on cache l'interface d'attaque
                self.wild_pokemon = pk.number_to_pokemon(self.combat)    # On change la valeur de wild_pokemon pour lui donner celle du pok qu'on combat
                self.attaque_p = cb.Combat(self.sac_pokemon)            # on maj l'attaque
                self.fight.show(self.sac_pokemon.objets[0], pk.number_to_pokemon(self.combat), -1)  # On ouvre l'interface de combat
            
            
    def monter(self):
        # cette fonction gère position du pokemon dans le sac lorsque l'on clique sur "monter". Elle modifie l'ordre du sac
         rang_selectionnes = [index.row() for index in self.sac.listWidget.selectedIndexes()]
         for rang in rang_selectionnes :
             if rang > 0:
                 nouveau_rang = rang - 1
                 self.sac.listWidget.insertItem(nouveau_rang, self.sac.listWidget.takeItem(rang))
                 self.sac.listWidget.setCurrentRow(nouveau_rang)
                 self.sac_pokemon.changer_place(self.sac_pokemon.objets[rang], nouveau_rang)
                 
        
    def descendre(self):        
        # ette fonction gère position du pokemon dans le sac lorsque l'on clique sur "descendre". Elle modifie l'ordre du sac
         rang_selectionnes = [index.row() for index in self.sac.listWidget.selectedIndexes()]
         for rang in reversed(rang_selectionnes) :
             if rang < self.sac.listWidget.count()-1 :
                 nouveau_rang = rang+1
                 self.sac.listWidget.insertItem(nouveau_rang, self.sac.listWidget.takeItem(rang))
                 self.sac.listWidget.setCurrentRow(nouveau_rang) 
                 self.sac_pokemon.changer_place(self.sac_pokemon.objets[rang], nouveau_rang)
    
    def button_action(self):
        
        # Définit les actions associées aux boutons lors de l'attaque d'un pokemon
        
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
        

    
    def fuite_pok(self):
        """
        Gère les tentatives de fuites : si fonctionne, active la fonction fuir
        """
        self.type_attaque = [3,0]
        self.attaque_p.a = self.type_attaque
        self.attaque_p.attaque_pokemon(self.wild_pokemon)
        if self.attaque_p.fuite or self.attaque_p.combat_fini:
            self.fuir()                                                 # fuite réussie
        else:
            pass
    
    def capt_pok (self):
        """
        Gère les tentatives de capture 
        """
        
        self.type_attaque = [2,1]
        self.attaque_p.a = self.type_attaque
        self.attaque_p.attaque_pokemon(self.wild_pokemon)
        if self.attaque_p.capture:
            self.combat = 0 
            self.sac_pokemon.capture_pokemon(self.wild_pokemon)
            # self.sac.hide()
            self.fight.hide()
            self.menu = 0
            self.terrain.show_map()
        else:
            self.fight.show(self.sac_pokemon.objets[0], self.wild_pokemon, self.deja_comb)
            
    
    
    
    def combat_pok (self):
        # Fonction gérant les différentes attaques, l'affichage des interfaces de combat

        if not self.attaque_p.combat_fini :             # On arrête le combat sinon
    
            self.fight.att_show(self.sac_pokemon.objets[0], self.wild_pokemon)      # affichage des 4 attaques
            self.waitForButtonClick(0)                                              # attendre la selection d'une attaque
            
            self.attaque_p.a = self.type_attaque
            self.attaque_p.attaque_pokemon(self.wild_pokemon)                       # appliquer l'attaque choisie
            
            # print(self.wild_pokemon.pv)
            # print(self.sac_pokemon.objets[0].pv)
            
            self.deja_comb = self.type_attaque[1]
            self.fight.show(self.sac_pokemon.objets[0], self.wild_pokemon, self.deja_comb)


            # si le combat se termine, cacher les boutons inutiles
            if self.attaque_p.combat_fini :
                self.fight.hide()
                self.combat = 0
                self.terrain.show_map()
        else :
            print("combat fini")
                
        
                

    def waitForButtonClick(self,a):
        # fonction qui gère l'attente d'un bouton cliqué
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
        # donne la valeur à type_attaque en fct du bouton
        if not self.attaque_p.combat_fini:
            self.type_attaque = val


if __name__ == '__main__':

    matrix = np.genfromtxt((os.path.join(path,"../data/terrain.csv")), delimiter=';',dtype=int)
    
    
    # sac_pokemon = Sac()
    # pokemon1 = pk.number_to_pokemon(25)
    # pokemon2 = pk.number_to_pokemon(30)
    # pokemon3 = pk.number_to_pokemon(40)
    # sac_pokemon.capture_pokemon(pokemon1)
    # sac_pokemon.capture_pokemon(pokemon2)
    # sac_pokemon.capture_pokemon(pokemon3)
    
    MAPP = ct.Vue(matrix,30,15)
    app = QtWidgets.QApplication(sys.argv)
    ui = ImageWindow(MAPP)
    ui.setupUI()
    ui.show()
    sys.exit(app.exec_())


