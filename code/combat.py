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
        a = [0,randint(0,3)]
        if a[0] == 0:
            #0 indique d'attquer
            capacite = current_pokemon.liste_capacites[a[1]]
            #le deuxieme int donne quelle attaque choisir (0 à 3)
            current_pokemon.attaque(capacite,pkmn_sauvage)
        elif a[0] == 1:
            #1 indique de changer de pokemon
            #le deuxieme int donne le pokemon a echanger (1 à 5)
            #changer de pokemon
            pass
        elif a[0] == 2:
            #2 indique une tentative de capture (le deuxieme int n'intervient pas)
            capture = True
        elif a[0] == 3:
            #3 indique une tentative de fuite (le deuxieme int n'intervient pas)
            fuite = True
        if current_pokemon.ko :
            #si le pokemon actuel est ko, on change de pokemon, ou on tente une fuite
            combat_fini = True
        if pkmn_sauvage.ko or fuite or capture :
            #on verifie si le combat est fini
            combat_fini = True
        else :
            pkmn_sauvage.attaque(pkmn_sauvage.liste_capacites[randint(0,3)],current_pokemon)




    