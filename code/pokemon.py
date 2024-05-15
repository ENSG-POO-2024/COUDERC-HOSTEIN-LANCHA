import types_pkmn
import numpy as np
import pandas as pd
from random import randint



capacites = pd.read_csv("../data/abilities.csv")
all_pokemon = pd.read_csv("../data/pokemon_first_gen.csv")
all_pokemon["Type1"] = all_pokemon["Type1"].str.lower()
all_pokemon["Type2"] = all_pokemon["Type2"].str.lower()

def number_to_pokemon(num):
    lvl = 100
    num -= 1
    name = all_pokemon.loc[num]["Name"]
    pv = all_pokemon.loc[num]["HP"]
    atk = all_pokemon.loc[num]["Attack"]
    atk_spe = all_pokemon.loc[num]["Sp. Atk"]
    dfs = all_pokemon.loc[num]["Defense"]
    dfs_spe = all_pokemon.loc[num]["Sp. Def"]
    vit = all_pokemon.loc[num]["Speed"]
    liste_capacites = [all_pokemon.loc[num]["Move1"],all_pokemon.loc[num]["Move2"],all_pokemon.loc[num]["Move3"],all_pokemon.loc[num]["Move4"]]
    type1 = all_pokemon.loc[num]["Type1"]
    if not pd.isnull(all_pokemon.loc[num]["Type2"]) :
        type2 = all_pokemon.loc[num]["Type2"]
    else :
        type2 = "neutral"
    pv = np.floor(((2 * pv * lvl) / 100) + lvl + 10)
    atk = np.floor(((2 * atk * lvl) / 100) + 5)
    atk_spe = np.floor(((2 * atk_spe * lvl) / 100) + 5)
    dfs = np.floor(((2 * dfs * lvl) / 100) + 5)
    dfs_spe = np.floor(((2 * dfs_spe * lvl) / 100) + 5)
    vit = np.floor(((2 * vit * lvl) / 100) + 5)
    return Pokemon(name, pv, atk, atk_spe, dfs, dfs_spe, vit, liste_capacites, type1, type2)

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
        self.lvl = 100
        #On n'utilise pas la mécanique de niveau, mais elle est nécessaire pr le calcul de dégats
        
    def __str__(self):
        return self.name
    
    def attaque(self,num,adv):
        print(num)
        type_atk = capacites["Type"][num]
        dmg = ((2 * self.lvl) / 5 + 2) * capacites["Power"][num]
        if capacites["Nature"][num] == "phy":
            dmg *= self.atk
            dmg /= adv.dfs
        elif capacites["Nature"][num] == "spe":
            dmg *= self.atk_spe
            dmg /= adv.dfs_spe
        dmg = (dmg / 50) + 2
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
        print(dmg)
        adv.degats(dmg)
        print(self.name + " utilise " + capacites["Name"][num])
        
    def degats(self,dmg):
        if dmg >= self.pv:
            self.pv = 0
            self.ko = True
            #Si l'attaque rend le pokemon KO, on met ses PV à 0 (pas de PV négatifs)
        else :
            self.pv = np.ceil(self.pv - dmg)

class PokemonSauvage(Pokemon):
    #On crée une sous-classe spécifiquement pour les pokémon sauvages
    #ceux-ci disposent en plus d'un taux de capture
    def __init__(self,cap):
        super().__init__()
        self.cap = cap
        self.iswild = True