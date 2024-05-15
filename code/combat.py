import numpy as np
from random import randint,random
from pokemon import *


def combat(liste_pkmn,pkmn_sauvage):
    current_pokemon = liste_pkmn[0]
    combat_fini = False
    fuite = False
    tentatives_fuite = 0
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
            #2 indique une tentative de capture
            #le deuxième int donne le type de poké ball a utiliser
            #sa valeur (1, 1.5 ou 2) modifie la probabilité de capture
            a = ((3 * pkmn_sauvage.pv_max - 2 * pkmn_sauvage.pv) * pkmn_sauvage.catchrate * a[1]) / 255
            #La probabilité de capturer un pokémon dépend de ses points de vie maximum, de ses points de vie actuels, de son taux de capture
            #et du type de ball utilisé pour tenter de le catpturer
            if random() < a :
                capture = True
            else :
                capture = False
        elif a[0] == 3:
            #3 indique une tentative de fuite
            #Le calcul de celle-ci dépend de la vitesse du pokémon utilise, de la vitesse du pokemon sauvage, et du nombre de tentatives de fuites déjà effectuées
            F = ((current_pokemon.vit * 128) / pkmn_sauvage.vit) + (30 * tentatives_fuite)
            if randint(0,255) < F :
                fuite = True
            else :
                tentatives_fuite += 1
                #plus on essaie, plus on a de chances de fuir
        if current_pokemon.ko :
            #si le pokemon actuel est ko, on change de pokemon, ou on tente une fuite
            combat_fini = True
        if pkmn_sauvage.ko or fuite or capture :
            #on verifie si le combat est fini
            combat_fini = True
        else :
            pkmn_sauvage.attaque(pkmn_sauvage.liste_capacites[randint(0,3)],current_pokemon)




    