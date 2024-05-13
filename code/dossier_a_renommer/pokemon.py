import types
import numpy as np

class Pokemon:
    def __init__(self,pv,atk,dfs,liste_capacites,type1,type2 = "neutral"):
        #On a défini par défaut le 2nd type comme neutre mais le programme accepte 2 types distincts
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
        pui *= types.efficiencies[types.dic[type_atk],types.dic[self.type1]]
        pui *= types.efficiencies[types.dic[type_atk],types.dic[self.type2]]
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