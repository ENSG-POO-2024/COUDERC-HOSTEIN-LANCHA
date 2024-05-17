
import numpy as np
from random import randint,random
from pokemon import *





class Combat :
    
    def __init__(self, liste_pkmn):
        self.liste_pkmn = liste_pkmn
        self.current_pokemon = liste_pkmn.objets[0]
        self.combat_fini = False
        self.fuite = False
        self.tentatives_fuite = 0
        self.capture = False
        self.a = [0,randint(0,3)]


    def attaque_pokemon (self, wild_pokemon):
        if not self.combat_fini :
                
            #il faut un input de a
            #c'est une liste de deux int
            #le premier donne la nature de l'action, le deuxieme est specifique a chaque action
            #TEST
            self.current_pokemon = self.liste_pkmn.objets[0]
            print(self.a)
                
            if self.a[0] == 0:
                #0 indique d'attaquer
                #le deuxieme int donne quelle attaque choisir (0 à 3)
                if self.current_pokemon.checkstate_begin() :
                    # On effectue le test de statut de début de tour
                    capacite = self.current_pokemon.liste_capacites[self.a[1]]
                    self.current_pokemon.attaque(capacite,wild_pokemon)
                self.current_pokemon.checkstate_end(wild_pokemon)
            elif self.a[0] == 1:
                #1 indique de changer de pokemon
                #le deuxieme int donne le pokemon a echanger (1 à 5)
                #changer de pokemon
                # self.current_pokemon.checkstate_end(wild_pokemon)
                pass
            elif self.a[0] == 2:
                #2 indique une tentative de capture
                #le deuxième int donne le type de poké ball a utiliser
                #sa valeur (1, 1.5 ou 2) modifie la probabilité de capture
                c = (((3 * wild_pokemon.pv_max - 2 * wild_pokemon.pv) / (3 * wild_pokemon.pv_max)) * wild_pokemon.catchrate * self.a[1]) / 255
                #La probabilité de capturer un pokémon dépend de ses points de vie maximum, de ses points de vie actuels, de son taux de capture
                #et du type de ball utilisé pour tenter de le capturer
                print(c)
                if random() < c :
                    self.capture = True
                else :
                    self.capture = False
                    self.current_pokemon.checkstate_end(wild_pokemon)
                print(self.capture)
            elif self.a[0] == 3:
                #3 indique une tentative de fuite
                #Le calcul de celle-ci dépend de la vitesse du pokémon utilise, de la vitesse du pokemon sauvage, et du nombre de tentatives de fuites déjà effectuées
                F = ((self.current_pokemon.vit * 128) / wild_pokemon.vit) + (30 * self.tentatives_fuite)
                if randint(0,255) < F :
                    self.fuite = True
                else :
                    self.tentatives_fuite += 1
                    self.current_pokemon.checkstate_end(wild_pokemon)
                    #plus on essaie, plus on a de chances de fuir
            if self.current_pokemon.ko :
                print("koooooo")
                #si le pokemon actuel est ko, on change de pokemon, ou on tente une fuite
                self.combat_fini = True
            if wild_pokemon.ko or self.fuite or self.capture :
                #on verifie si le combat est fini
                self.combat_fini = True
            else :
                #Le pokémon sauvage a toujours le même comportement, il utilise une attaque au hasard
                if wild_pokemon.checkstate_begin():
                    wild_pokemon.attaque(wild_pokemon.liste_capacites[randint(0,3)],self.current_pokemon)
                wild_pokemon.checkstate_end(self.current_pokemon)
                print('yo')

    
    
