import types_pkmn
import numpy as np
import pandas as pd
from random import randint



capacites = pd.read_csv("../data/abilities.csv")
all_pokemon = pd.read_csv("../data/pokemon_first_gen.csv")

class Pokemon:
    def __init__(self,name,pv,atk,atk_spe,dfs,dfs_spe,vit,liste_capacites,type1,type2 = "neutral"):
        #On a défini par défaut le 2nd type comme neutre mais le programme accepte 2 types distincts
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.pv_tot = pv
        self.atk = atk
        self.atk_spe = atk_spe
        self.dfs = dfs
        self.dfs_spe = dfs_spe
        self.vit = vit
        #On a choisi d'ajouter des statistiques multiplicatives d'attaque et de défense qui permettent
        #respectivement d'augmenter les dégâts infligés et de réduire les dégâts subis
        self.ko = False
        self.liste_capacites = liste_capacites
        #juste une liste de 4 int donnant l'indice de l'attaque
        self.iswild = False
        self.lvl = pv / 4
        #On n'utilise pas la mécanique de niveau, mais elle est nécessaire pr le calcul de dégats
        #on fait donc une approximation via les pv
        
    def __str__(self):
        return self.name
    
    def attaque(self,num,adv):
        type_atk = capacites["Type"][num]
        dmg = 2 * self.lvl
        dmg /= 5
        dmg += 2
        dmg *= capacites["Power"][num]
        if capacites["Nature"][num] == "phy":
            dmg *= self.atk
            dmg /= adv.dfs
        elif capacites["Nature"][num] == "spe":
            dmg *= self.atk_spe
            dmg /= adv.dfs_spe
        dmg +=2
        rnd = randint(217,255)
        rnd /= 255
        dmg *= rnd
        if self.type1 == type_atk or self.type2 == type_atk:
            #On a introduit le concept des attaques "STAB" : si le pokémon et son attaque sont de même type, celle-ci augmente de puissance
            if not type_atk == "neutral":
                #l'attaque neutre doit rester de puissance indépendante du type néanmoins
                dmg *= 1.5
        #les dégâts augmentent avec la statistique d'attaque du pokémon
        dmg *= types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type1]]
        dmg *= types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type2]]
        adv.degats(type_atk)
        print(self.name + " attaque " + capacites["Name"][num])
        
    def degats(self,type_atk,pui):
        if pui >= self.pv:
            self.pv = 0
            self.ko = True
            #Si l'attaque rend le pokemon KO, on met ses PV à 0 (pas de PV négatifs)
        else :
            self.pv = np.ceil(self.pv - pui)

class PokemonSauvage(Pokemon):
    #On crée une sous-classe spécifiquement pour les pokémon sauvages
    #ceux-ci disposent en plus d'un taux de capture
    def __init__(self,cap):
        super().__init__()
        self.cap = cap
        self.iswild = True