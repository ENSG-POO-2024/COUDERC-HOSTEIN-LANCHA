import numpy as np

efficiencies = np.array([
    [0.5,1  ,1  ,0.5,0.5,0.5,2  ,2  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,1  ,1  ],
    [2  ,1  ,1  ,1  ,1  ,1  ,0.5,2  ,0.5,2  ,1  ,0.5,0.5,2  ,1  ,0  ,2  ,0.5,1  ],
    [0.5,1  ,2  ,1  ,1  ,1  ,0  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,0.5,2  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,0.5,2  ,1  ,0.5,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ],
    [2  ,1  ,0.5,0.5,0.5,1  ,1  ,2  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [0.5,2  ,2  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,2  ,1  ,1  ],
    [0.5,1  ,2  ,0.5,0.5,1  ,1  ,0.5,1  ,1  ,2  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,1  ],
    [0.5,0.5,1  ,1  ,0.5,1  ,0.5,1  ,1  ,1  ,2  ,0.5,2  ,1  ,1  ,0.5,2  ,0.5,1  ],
    [0.5,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,0  ,1  ,1  ,1  ],
    [0.5,1  ,0.5,2  ,0.5,1  ,1  ,1  ,0.5,1  ,0.5,0.5,1  ,2  ,2  ,1  ,1  ,0.5,1  ],
    [0  ,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,1  ,2  ,0.5,1  ,0.5,0.5,0.5,1  ,1  ,1  ],
    [0.5,2  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,2  ,0.5,1  ,1  ,1  ,0  ,1  ,1  ],
    [0.5,0.5,1  ,1  ,2  ,1  ,1  ,2  ,2  ,1  ,1  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ],
    [2  ,1  ,1  ,1  ,2  ,2  ,1  ,1  ,0.5,1  ,0.5,2  ,1  ,2  ,1  ,1  ,1  ,0  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,0  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [1  ,0.5,1  ,1  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ,2  ,1  ,1  ,2  ,0.5,1  ,1  ],
    [0.5,2  ,1  ,1  ,1  ,0.5,1  ,1  ,2  ,1  ,2  ,1  ,1  ,0.5,1  ,1  ,1  ,1  ,1  ],
    [1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ,1  ]
    ])
#On a défini la table des classes à l'aide d'un array numpy.
#la 19e ligne/colonne correspond au "type" neutre qui est utile pour définir deux types ou pour l'attaque neutre
types_dict = {"steel":0,"fighting":1,"dragon":2,"water":3,"electric":4,"fire":5,"fairy":6,"ice":7,"bug":8,"normal":9,"grass":10,"poison":11,"psychic":12,"rock":13,"ground":14,"ghost":15,"dark":16,"flying":17,"neutral":18}
#l'utilisation d'un dictionnaire avec des indices correspondant au tableau permet une correspondance entre types et efficacités des attaques

class Pokemon:
    def __init__(self,pv,atk,dfs,type1,type2 = "neutral"):
        #On a défini par défaut le 2nd type comme neutre mais le programme accepte 2 types distincts
        self.type1 = type1
        self.type2 = type2
        self.pv = pv
        self.atk = atk
        self.dfs = dfs
        #On a choisi d'ajouter des statistiques multiplicatives d'attaque et de défense qui permettent
        #respectivement d'augmenter les dégâts infligés et de réduire les dégâts subis
        self.ko = False
    def attaque(self,type_atk,pui,adv):
        #On utilise d'abord une fonction attaque dans le pokémon attaquant pour appliquer les éventuels modificateurs de dégâts liés au pokémon
        if self.type1 == type_atk or self.type2 == type_atk:
            #On a introduit le concept des attaques "STAB" : si le pokémon et son attaque sont de même type, celle-ci augmente de puissance
            if not type_atk == "neutral":
                #l'attaque neutre doit rester de puissance indépendante du type néanmoins
                pui *= 1.5
        pui *= self.atk
        #les dégâts augmentent avec la statistique d'attaque du pokémon
        adv.degats(type_atk,pui)
    def degats(self,type_atk,pui):
        pui *= self.dfs
        #les dégâts sont réduits par la statistique de défense
        pui *= efficiencies[types_dict[type_atk],types_dict[self.type1]]
        pui *= efficiencies[types_dict[type_atk],types_dict[self.type2]]
        #On calcule l'efficacité de l'attaque reçue en fonction des types du pokémon
        if pui >= self.pv:
            self.pv = 0
            self.ko = True
            #Si l'attaque rend le pokemon KO, on met ses PV à 0 (pas de PV négatifs)
        else :
            self.pv = np.ceil(self.pv - pui)

class combat:
    def __init__(self,liste_pkmn,pkmn_sauvage):
        pass
    def tour_joueur(self):