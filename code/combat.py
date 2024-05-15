import numpy as np
from random import randint
from pokemon import *


def combat(liste_pkmn,pkmn_sauvage):
    current_pokemon = liste_pkmn[0]
    combat_fini = False
    fuite = False
    capture = False
    while not combat_fini:
        #il faut un input de a
        #c'est une liste de deux int
        #le premier donne la nature de l'action, le deuxieme est specifique a chaque action
        if a[0] == 0:
            #0 indique d'attquer
            print(0)
            capacite = current_pokemon.liste_capacites[a[1]]
            #le deuxieme int donne quelle attaque choisir (0 à 3)
            print("a")
            print(capacite)
            print("b")
            current_pokemon.attaque(capacite,pkmn_sauvage)
        elif a[0] == 1:
            #1 indique de changer de pokemon
            #le deuxieme int donne le pokemon a echanger (1 à 5)
            print(1)
            #changer de pokemon
            pass
        elif a[0] == 2:
            #2 indique une tentative de capture (le deuxieme int n'intervient pas)
            print(2)
            capture = True
        elif a[0] == 3:
            #3 indique une tentative de fuite (le deuxieme int n'intervient pas)
            print(3)
            fuite = True
        if current_pokemon.ko :
            #si le pokemon actuel est ko, on change de pokemon, ou on tente une fuite
            print(6)
            combat_fini = True
        if pkmn_sauvage.ko or fuite or capture :
            #on verifie si le combat est fini
            print(4)
            combat_fini = True
        else :
            print(5)
            pkmn_sauvage.attaque(pkmn_sauvage.liste_capacites[randint(0,1)],current_pokemon)




    