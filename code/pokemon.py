import types_pkmn
import numpy as np
import pandas as pd
from random import randint,random



capacites = pd.read_csv("../data/abilities.csv")
all_pokemon = pd.read_csv("../data/pokemon_first_gen.csv")
all_pokemon["Type1"] = all_pokemon["Type1"].str.lower()
all_pokemon["Type2"] = all_pokemon["Type2"].str.lower()

def number_to_pokemon(num):
    if num == 0:
        return None
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
    catchrate = all_pokemon.loc[num]["Catchrate"]
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
    
    return Pokemon(name, pv, atk, atk_spe, dfs, dfs_spe, vit, liste_capacites, catchrate, type1, type2)

class Pokemon:
    def __init__(self,name,pv,atk,atk_spe,dfs,dfs_spe,vit,liste_capacites,catchrate,type1,type2 = "neutral"):
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
        self.catchrate = catchrate
        self.ko = False
        self.liste_capacites = liste_capacites
        #La liste des capacités des pokémon est une liste de 4 entiers, chacun donnant l'indice d'une attaque dans le dataframe "capacites"
        #lui-même obtenu à partir du fichier "abilities.csv"
        self.iswild = False
        self.lvl = 100
        #On n'utilise pas réellement la mécanique de niveau, mais elle est nécessaire au le calcul de dégâts
        self.state = "normal"
        self.status_duration = 0
        self.seeded = False
        
    def __str__(self):
        return self.name
    
    def checkstate_begin(self):
        #Cette fonction gère le statut du pokémon au début du tour
        #Elle renvoie True si le pokémon peut jouer, False sinon
        if self.state == "asleep":
            #dans le cas où le pokémon est endormi, l'endormissement dure au plus 4 tours, au minimum 1
            if self.status_duration == 0:
                #Si les 4 tours sont écoulés, le pokémon joue
                self.state = "normal"
                return True
            elif self.status_duration == 4:
                #Si le pokémon vient de s'endormir, il ne joue pas
                self.status_duration -= 1
                return False
            else :
                #Si le pokémon s'est endormi il y a plus d'un tour et moins de 4, on vérifie s'il
                #se réveille, cela a une chance sur deux d'arriver
                if random() < 0.5:
                    self.status_duration -= 1
                    return False
                    #S'il ne se réveille pas, on fait avancer de 1 le compteur de réveil
                else :
                    self.state = "normal"
                    self.status_duration = 0
                    return True
                    #S'il se réveille, on met le compteur à 0, et on remet le statut du pokémon à "normal"
        elif self.state == "paralyzed":
            #Dans le cas de la paralysie, le pokémon a une chance sur 4 de ne pas jouer
            #Il ne peut pas se défaire de cet effet néanmoins
            if random() < 0.25 :
                return False
            else :
                return True
        elif self.state == "frozen":
            #Si le pokémon est gelé, il a une chance sur 5 de dégeler, et c'est le seul cas
            #où il pourra jouer
            if random() < 0.2:
                self.state = "normal"
                return True
            else :
                return False
        elif self.state == "confused":
            #Si le pokémon est confus, la confusion dure 1 à 4 tours
            #À chaque tour, le pokémon a 1 chance sur 2 de repasser à l'état normal
            #S'il reste confus, il a une chance sur deux de s'infliger des dégâts et de ne pas pouvoir
            #jouer, et une chance sur deux de jouer normalement
            if self.status_duration == 0:
                #Quand le compteur est à 0, le pokémon repasse à l'état normal
                self.state = "normal"
                return True
            elif self.status_duration == 4:
                #Quand le compteur est à 4, le pokémon reste confus, on vérifie s'il joue
                if random() < 0.5:
                    self.degats(self.pv_max / 8)
                    return False
                else :
                    return True
                self.status_duration -= 1
            else :
                #Sinon, on vérifie si le pokémon quitte sa confusion
                if random() < 0.5:
                    #S'il reste confus, on vérifie s'il joue
                    self.status_duration -= 1
                    if random() < 0.5:
                        self.degats(self.pv_max / 8)
                        return False
                    else :
                        return True
                else :
                    #Sinon, il joue normalement
                    self.state = "normal"
                    self.status_duration = 0
                    return True
        else:
            #Si le pokémon n'est sous l'effet d'aucun état actif en début de tour, il joue normalement
            return True
    
    def checkstate_end(self,adv):
        #Cette fonction gère le statut du pokémon à la fin du tour
        if self.seeded == True :
            #Si le pokémon a subi l'attaque vampigraine, le pokémon adverse vole 1/8 de sa vie
            lifesteal = self.degats(np.ceil(self.pv_max / 8))
            adv.heal(lifesteal)
        if self.state == "poisoned" and not self.ko :
            #Si le pokémon est empoisonné, il perd un quart de sa vie maximale
            self.pv -= np.ceil(self.pv_max / 8)
            if self.pv <= 0:
                self.pv = 0
                self.ko = True
        elif self.state == "burnt" and not self.ko :
            #Si le pokémon est brûlé, il perd un quart de sa vie maximale aussi
            self.pv -= np.ceil(self.pv_max / 8)
            if self.pv <= 0:
                self.pv = 0
                self.ko = True
            
    
    def attaque(self,num,adv):
        #La méthode qui permet à un pokémon d'en attaquer un autre
        	#num correspond à l'indice de l'attaque dans le dataframe "capacites"
        #Le calcul est assez laborieux, la formule est basée sur la page poképédia "calcul des dégâts", on utilise la mécanique de la 1ère génération
        
        print(self.name + " utilise " + capacites["Name"][num])
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
        if capacites["repeat"] :
            #Certaines capacités peuvent être lancées aléatoirement 2 à 5 fois
            #Dans ce cas, on multiplie simplement les dégâts infligés par un nombre
            #entre 2 et 5
            r = random()
            if r < 0.375:
                dmg *= 2
            elif r < 0.75:
                dmg *= 3
            elif r < 0.875:
                dmg *= 4
            else :
                dmg *= 5
        if randint(0,99) < capacites["Precision"][num]:
            #On vérifie que l'attaque se lance, cela dépend de la précision de l'attaque
            #une précision de 70 par exemple signifie que l'attaque a 70% de chances de réussir
            condition = True
            if capacites["condition"][num] == "asleep":
                #Cette condition permet de vérifier que si l'attaque est Dévorêve, elle
                #se lance uniquement si le pokémon adverse est endormi
                if not adv.state == "asleep":
                    condition = False
            if condition and capacites["Power"][num] != 0:
                #si l'attaque a une puissance, elle inflige des dégâts
                dmg = adv.degats(dmg)
                #On change la valeur de dmg en la remplaçant par les dégâts réellement subis
                #c'est utile dans le calcul du vol de vie
            if capacites["seed"][num]:
                #Si l'attaque est vampigraine, elle place le pokémon adverse dans l'état infecté
                adv.seeded = True
            if capacites["SD"][num] != 0:
                #Certaines attaques infligent des dégâts au lanceur
                #Les dégâts en question dépendent des pv max du lanceur, ils sont soient égaux
                #à un quart, soit à la totalité de ceux-ci, et "capacites["SD"][num]" vaut 0,1 ou 4
                self.degats(capacites["SD"][num] * self.pv_max / 4)
            if capacites["LS"][num]:
                #Certaines attaques soignent le lanceur de la moitié des dégâts infligés
                self.heal(np.ceil(dmg / 2))
            if capacites["newstatus"][num] != "normal" and adv.state == "normal" and randint(0,99) < capacites["precision_status"][num]:
                #certaines attaques changent le statut du pokemon adverse
                #la probabilité de changer de statut est liée à une autre variable située dans
                #la colonne "precision_status"
                adv.state = capacites["newstatus"][num]
                #si le changement de statut réussit, il est appliqué au pokemon adverse
                if capacites["newstatus"][num] == "asleep":
                    #dans le cas d'une attaque endormant l'adversaire, il faut aussi mettre son compteur
                    #de statut à 4, puisque l'endormissement dure 4 tours au maximum
                    adv.status_duration = 4
                if capacites["newstatus"][num] == "confused":
                    #idem pour la confusion
                    adv.status_duration = 4
            if capacites["heal"][num]:
                self.heal(self.pv_max / 2)
        else:
            print(self.name + " rate son attaque !")
            #TEST
        
    def degats(self,dmg):
        #Une méthode, distincte de "attaque" pour gérer les dégâts
        #la différencier de la méthode attaque est utile notamment dans le cas où le
        #pokémon subit des dégâts liés à un autre effet
        #elle renvoie les dégâts subis, ce qui peut servir pour les attaques ayant du vol de vie par exemple
        if dmg >= self.pv:
            dmg = self.pv
            self.pv = 0
            self.ko = True
            #Si l'attaque rend le pokemon KO, on met ses PV à 0 (pas de PV négatifs)
        else :
            dmg = np.floor(dmg)
            self.pv = self.pv - dmg
        return dmg
    
    def heal(self,amount):
        self.pv += np.floor(amount)
        if self.pv > self.pv_max:
            self.pv = self.pv_max
