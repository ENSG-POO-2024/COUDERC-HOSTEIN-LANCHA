import types_pkmn
import numpy as np
import pandas as pd
from random import randint



capacites = pd.read_csv("../data/abilities.csv")
all_pokemon = pd.read_csv("../data/pokemon_first_gen.csv")
all_pokemon["Type1"] = all_pokemon["Type1"].str.lower()
all_pokemon["Type2"] = all_pokemon["Type2"].str.lower()

def number_to_pokemon(num):
    #permet d'obtenir un pokemon en donnant son numero pokedex
    #renvoie un objet "Pokemon" avec toutes les statistiques dont il dispose au niveau 100
    #pour les nerds : on a fixé ici tous les IVs et EVs du pokémon à 0, choisi une nature neutre pour toutes les statistiques
    #et on a utilisé la formule de calcul des statistiques de la 3e génération
    lvl = 100
    num -= 1
    #le numéro du pokédex commence à 1, notre dataframe est indexée à partir de 0
    name = all_pokemon.loc[num]["Name"]
    pv = all_pokemon.loc[num]["HP"]
    atk = all_pokemon.loc[num]["Attack"]
    atk_spe = all_pokemon.loc[num]["Sp. Atk"]
    dfs = all_pokemon.loc[num]["Defense"]
    dfs_spe = all_pokemon.loc[num]["Sp. Def"]
    vit = all_pokemon.loc[num]["Speed"]
    liste_capacites = [all_pokemon.loc[num]["Move1"],all_pokemon.loc[num]["Move2"],all_pokemon.loc[num]["Move3"],all_pokemon.loc[num]["Move4"]]
    #On a ajouté au jeu de données d'origine 4 colonnes, chacune correspondant à un numéro d'attaque dont le pokémon dispose
    #dans notre jeu, les attaques seront fixées, les pokémon ne pourront pas en apprendre de nouvelles ou en oublier
    type1 = all_pokemon.loc[num]["Type1"]
    
    if not pd.isnull(all_pokemon.loc[num]["Type2"]) :
        type2 = all_pokemon.loc[num]["Type2"]
        #On fait attention au cas où le pokémon n'aurait pas de second type
    else :
        type2 = "neutral"
        
    pv = np.floor(((2 * pv * lvl) / 100) + lvl + 10)
    atk = np.floor(((2 * atk * lvl) / 100) + 5)
    atk_spe = np.floor(((2 * atk_spe * lvl) / 100) + 5)
    dfs = np.floor(((2 * dfs * lvl) / 100) + 5)
    dfs_spe = np.floor(((2 * dfs_spe * lvl) / 100) + 5)
    vit = np.floor(((2 * vit * lvl) / 100) + 5)
    #les formules assez imbuvables ci-dessus proviennent de la page poképédia "calcul des statistiques"
    
    return Pokemon(name, pv, atk, atk_spe, dfs, dfs_spe, vit, liste_capacites, type1, type2)

class Pokemon:
    def __init__(self,name,pv,atk,atk_spe,dfs,dfs_spe,vit,liste_capacites,type1,type2 = "neutral"):
        #On a défini par défaut le 2nd type comme neutre mais le programme accepte 2 types distincts
        #Chaque statistique est définie comme dans les jeux Pokémon classiques (à partir de la 2e génération)
        #
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.pv_max = pv
        self.atk = atk
        self.atk_spe = atk_spe
        self.dfs = dfs
        self.dfs_spe = dfs_spe
        self.vit = vit
        self.ko = False
        self.liste_capacites = liste_capacites
        #La liste des capacités des pokémon est une liste de 4 entiers, chacun donnant l'indice d'une attaque dans le dataframe "capacites"
        #lui-même obtenu à partir du fichier "abilities.csv"
        self.iswild = False
        self.lvl = 100
        #On n'utilise pas réellement la mécanique de niveau, mais elle est nécessaire au le calcul de dégâts
        
    def __str__(self):
        return self.name
    
    def attaque(self,num,adv):
        #La méthode qui permet à un pokémon d'en attaquer un autre
        	#num correspond à l'indice de l'attaque dans le dataframe "capacites"
        #Le calcul est assez laborieux, la formule est basée sur la page poképédia "calcul des dégâts", on utilise la mécanique de la 1ère génération
        
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
                #l'attaque neutre (Lutte) doit rester de même puissance indépendamment du type néanmoins
                dmg *= 1.5
        #les dégâts augmentent avec la statistique d'attaque du pokémon
        dmg *= types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type1]]
        dmg *= types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type2]]
        #Les dégâts changent en fonction du type du pokémon adverse
        adv.degats(dmg)
        return str(self.name + " utilise " + capacites["Name"][num])
        #On renvoie la description de l'action (probablement à changer)
        
    def degats(self,dmg):
        #Une méthode, distincte de "attaque" pour gérer les dégâts
        #celle-ci peut être utile dans le cas où le pokémon subirait des dégâts liés à un autre effet
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