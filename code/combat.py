import numpy as np
from random import randint
from pokemon import *


def combat(liste_pkmn,pkmn_sauvage):
    current_pokemon = liste_pkmn[0]
    combat_fini = False
    fuite = False
    capture = False
    while not combat_fini:
        a = [0,2] #on gerera ça plus tard avec qt
        #a est du type [int,int], le premier entier donne l'action a realiser (attaque,changer de pokemon,capture,fuite)
        #le second donne le detail de cette action (numero de l'attaque,du pokemon a changer)
        if a[0] == 0:
            print(0)
            capacite = current_pokemon.liste_capacites[a[1]]
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




    