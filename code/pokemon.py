'''
Ce fichier gère la classe Pokemon et sa génération
'''


import types_pkmn
import numpy as np
import pandas as pd
from random import randint,random



capacites = pd.read_csv("../data/abilities.csv")
#On importe la liste de toutes les capacités sous forme de dataframe pandas
all_pokemon = pd.read_csv("../data/pokemon_first_gen.csv")
#On importe la liste de tous les pokémon en dataframe pandas
#celui-ci n'est utilisé que dans la fonction number_to_pokemon, mais celle-ci a vocation a être utilisée plusieurs fois, il est donc préférable
#de l'importer une fois au début et de réutiliser le même fichier ensuite puisqu'on ne le modifiera pas
all_pokemon["Type1"] = all_pokemon["Type1"].str.lower()
all_pokemon["Type2"] = all_pokemon["Type2"].str.lower()
#On convertit tous les types en bas-de-casse pour permettre une correspondance entre tous les fichiers

def number_to_pokemon(num):
    '''
    Donne un objet pokemon correspondant au numéro indiqué dans l'ordre du pokédex
    utilise le fichier "pokemon_first_gen.csv"
    :param num: numéro du pokémon dans le pokédex (de 1 à 151)
    :type num: int
    
    :return: pokémon ayant le numéro correspondant avec toutes ses statistiques initialisées comme dans "pokemon_first_gen.csv"
    :type return: objet Pokemon
    
    
    Pour le détail, on choisit chaque pokémon au niveau 100, et ses valeurs d'IV et d'EV sont toutes fixées à 0
    Autrement dit c'est le pokémon qu'on obtient si on est le plus malchanceux possible et qu'on ne l'a jamais utilisé en combat auparavant
    Tous les calculs sont basés sur la 3e génération de jeux pokémon
    '''
    if num == 0:
        return None
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
    
    #Ci-dessus, toute l'extraction des données depuis le dataframe
    
    if pd.isnull(liste_capacites[3]):
        liste_capacites[3] = 149
        if pd.isnull(liste_capacites[2]):
            liste_capacites[2] = 149
            if pd.isnull(liste_capacites[1]):
                liste_capacites[1] = 149
    
    #On gère le cas où les pokémon ne sont pas initialisés avec 4 attaques en leur donnant l'attaque, sans effet, "trempette à chaque emplacement vide
    
    pv = np.floor(((2 * pv * lvl) / 100) + lvl + 10)
    atk = np.floor(((2 * atk * lvl) / 100) + 5)
    atk_spe = np.floor(((2 * atk_spe * lvl) / 100) + 5)
    dfs = np.floor(((2 * dfs * lvl) / 100) + 5)
    dfs_spe = np.floor(((2 * dfs_spe * lvl) / 100) + 5)
    vit = np.floor(((2 * vit * lvl) / 100) + 5)
    
    #les formules assez imbuvables ci-dessus permettent le calcul des statistiques "réelles" du pokémon qui sont en réalité
    #bien différentes des statistiques de base du pokémon telles que données dans le fichier csv (sinon c'est pas drôle)
    
    return Pokemon(name, pv, atk, atk_spe, dfs, dfs_spe, vit, liste_capacites, catchrate, type1, type2)

class Pokemon:
    '''
    La classe pokemon
    Les objets pokemon sont actifs tout au long de la partie et conservent leurs attributs d'un combat à l'autre
    si aucune modification extérieure n'est effectuée
    '''
    def __init__(self,name,pv,atk,atk_spe,dfs,dfs_spe,vit,liste_capacites,catchrate,type1,type2 = "neutral"):
        '''
        :param name: nom du pokémon
        :param pv: nombre de points de vie max du pokémon
        :param atk: statistique d'attaque du pokémon
        :param atk_spe: statistique d'attaque du pokémon
        :param dfs: statistique d'attaque du pokémon
        :param dfs_spe: statistique d'attaque du pokémon
        :param vit: statistique d'attaque du pokémon
        :param liste_capacites: liste des capacités du pokémon sous forme d'indices
        :param catchrate: taux de capture du pokémon
        :param type1: premier type du pokémon
        :param type2: deuxième type du pokémon, initialisé à "neutral" si aucune valeur n'est fournie (en pratique on la fournit toujours)
        
        :type name: str
        :type pv: int
        :type atk: int
        :type atk_spe: int
        :type dfs: int
        :type dfs_spe: int
        :type vit: int
        :type liste_capacites: list
        :type catchrate: int
        :type type1: str
        :type type2: str
        
        
        
        '''
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.pv = int(pv)
        self.pv_max = int(pv)
        self.atk = atk
        self.atk_spe = atk_spe
        self.dfs = dfs
        self.dfs_spe = dfs_spe
        self.vit = vit
        self.catchrate = catchrate
        self.liste_capacites = liste_capacites
        #La liste des capacités des pokémon est une liste de 4 entiers, chacun donnant l'indice d'une attaque dans le dataframe "capacites"
        #lui-même obtenu à partir du fichier "abilities.csv"
        
        
        self.lvl = 100
        #On n'utilise pas réellement la mécanique de niveau, mais elle est nécessaire au le calcul de dégâts
        
        
        self.ko = False
        
        
        self.state = "normal"
        self.status_duration = 0
        self.seeded = False
        #les attributs ci-dessus servent pendant le déroulement du combat, ils déterminent si le pokémon est affecté
        #par un statut négatif (endormi,paralysé...) 
        #ou bien s'il est infecté (seeded)
        
        
    def __str__(self):
        '''
        rien de bien folichon par ici
        '''
        return self.name
    
    def checkstate_begin(self):
        '''
        Cette méthode gère les statuts actifs en début de tour
        elle renvoie True si le pokémon peut agir et False s'il ne peut pas (s'il est endormi par exemple)
        on profite du fait que le pokémon soit un objet pour éventuellement modifier sont statut de début de tour
        
        :return: True si le pokémon peut jouer, False s'il ne peut pas
        :type return: bool
        '''
        if self.state == "asleep":
            #Cas où le pokémon est endormi
            #L'endormissement dure au minimum 1 tour, au maximum 4
            #À partir du 2e tour d'endormissement, le pokémon a une chance sur deux de se réveiller
            #Quand le pokémon dort, il ne joue pas
            #La durée d'endormissement est gérée par l'attribut status_duration
            
            if self.status_duration == 0:
                #Au bout de 4 tours, le pokémon se réveille
                self.state = "normal"
                print(self.name + "se réveille !")
                return True
            
            elif self.status_duration == 4:
                #Au premier tour, le pokémon ne joue pas
                self.status_duration -= 1
                print(self.name +" est endormi")
                return False
            
            else :
                #Si le pokémon s'est endormi il y a plus d'un tour et moins de 4, on vérifie s'il
                #se réveille, cela a une chance sur deux d'arriver
                if random() < 0.5:
                    self.status_duration -= 1
                    print(self.name +" est endormi")
                    return False
                
                else :
                    self.state = "normal"
                    self.status_duration = 0
                    print(self.name + " se réveille !")
                    return True
        
        
        elif self.state == "paralyzed":
            #Cas où le pokémon est paralysé
            #Dans ce cas, le pokémon a une chance sur 4 de ne pas pouvoir attaquer (hors tous calculs)
            #Cet état est permanent s'il n'est pas soigné manuellement
            
            if random() < 0.25 :
                print(self.name + " est totalement paralysé !")
                return False
            
            else :
                return True
            
            
        elif self.state == "frozen":
            #Cas où le pokémon est gelé
            #Quand il est gelé, le pokémon ne peut pas combattre
            #Il a une chance sur 5 de dégeler, et s'il dégèle, il peut combattre le tour même
            
            if random() < 0.2:
                self.state = "normal"
                print(self.name + " est dégelé !")
                return True
            
            else :
                print(self.name +" est totalement gelé")
                return False
        
        
        elif self.state == "confused":
            #Cas où le pokémon est confus
            #C'est la modification de statut la plus complexe
            #La durée de la confusion est gérée comme celle du sommeil
            #De la même façon, il a une chance sur deux de cesser d'être confus au 2e et 3e tour de confusion
            #Lorsqu'il est confus, le pokémon a une chance sur deux d'échouer son attaque (hors tous calculs)
            #De plus, s'il échoue à cause de la confusion, il subit des dégâts à hauteur d'un huitième de ses pv max
            
            if self.status_duration == 0:
                #Au bout de 4 tours, le pokémon repasse à l'état normal
                self.state = "normal"
                return True
            
            elif self.status_duration == 4:
                #Au premier tour, le pokémon ne peut pas revenir à l'état normal
                if random() < 0.5:
                    self.degats(self.pv_max / 8)
                    return False
                
                else :
                    return True
                
                self.status_duration -= 1
                
            else :
                #au 2e et 3e tour, le pokémon a une chance sur deux de quitter l'état de confusion
                if random() < 0.5:
                    #Cas où le pokémon reste confus
                    self.status_duration -= 1
                    
                    if random() < 0.5:
                        self.degats(self.pv_max / 8)
                        return False
                    
                    else :
                        return True
                    
                else :
                    #Cas où il perd l'état
                    self.state = "normal"
                    self.status_duration = 0
                    return True
        
        
        else:
            #Si le pokémon n'est sous l'effet d'aucun état actif en début de tour, il joue normalement
            return True
    
    def checkstate_end(self,adv):
        '''
        Cette méthode gère les statuts actifs en fin de tour
        Contrairement aux statuts de fin de tour, ils ne peuvent pas empêcher le pokémon d'attaquer
        mais ils peuvent lui faire perdre de la vie par exemple
        Cette méthode ne renvoie rien
        
        :param adv: pokémon adverse
        :type adv: objet Pokemon
        '''
        
        if self.seeded == True :
            #Cas où le pokémon est infecté (effet de la capacité vampigraine)
            #C'est un effet de statut indépendant des autres, le pokémon peut être infecté et endormi par exemple
            lifesteal = self.degats(np.ceil(self.pv_max / 8))
            print(self.name +" est infecté")
            adv.heal(lifesteal)
            
        if self.state == "poisoned" and not self.ko :
            #Cas où le pokémon est empoisonné
            #Un pokémon empoisonné perd un huitième des ses pv max à chaque fin de tour
            self.degats(self.pv_max / 8)
            print(self.name +" est empoisonné")
            
        elif self.state == "burnt" and not self.ko :
            #Cas où le pokémon est brûlé
            #L'effet est exactement le même que l'empoisonnement
            self.degats(self.pv_max / 8)
            print(self.name +" est brûlé")
            
    
    def attaque(self,num,adv):
        '''
        Cette méthode permet au pokémon d'attaquer
        Elle est assez complexe car elle prend en compte tous les cas d'attaques qu'on a implantés
        Cette méthode ne renvoie rien
        
        :param num: indice de l'attaque utilisée dans le fichier abilities.csv
        :param adv: pokémon cible
        :type num: int
        :type adv: objet Pokemon
        '''
        
        print(self.name + " utilise " + capacites["Name"][num])
        
        
        #Ci-dessous le calcul de base des dégâts, comme effectué dans les jeux de la 1ere génération
        
        dmg = ((2 * self.lvl) / 5 + 2) * capacites["Power"][num]
        
        if capacites["Nature"][num] == "phy":
            #Les capacités physiques sont affectés par la statistiques attack du pokémon
            dmg *= self.atk
            dmg /= adv.dfs
            
        elif capacites["Nature"][num] == "spe":
            #Les capacités physiques sont affectés par la statistiques special_attack du pokémon
            dmg *= self.atk_spe
            dmg /= adv.dfs_spe
        
        dmg = (dmg / 50) + 2

        rnd = randint(217,255)
        rnd /= 255
        dmg *= rnd
        #Les dégâts ont une petite composante aléatoire
        
        
        
        type_atk = capacites["Type"][num]
        if self.type1 == type_atk or self.type2 == type_atk:
            #Les capacités du même type que le pokémon qui les utilise on un bonus multiplicatif de dégâts de 1.5
            if not type_atk == "neutral":
                #l'attaque neutre (Lutte) doit rester de même puissance indépendamment du type néanmoins
                dmg *= 1.5
        
        coef1 = types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type1]]
        coef2 = types_pkmn.efficiencies[types_pkmn.dic[type_atk],types_pkmn.dic[adv.type2]]
        dmg *= coef1
        dmg *= coef2
        
        if coef1*coef2 == 0 :
            print("Aucun effet !")
        elif coef1*coef2 == 0.25:
            print("Très peu efficace !")
        elif coef1*coef2 == 0.5:
            print("Peu efficace !")
        elif coef1*coef2 == 2:
            print("Très efficace !")
        elif coef1*coef2 == 4:
            print("Extrêmement efficace !")
        #On calcule les effets des types (résistances et faiblesses) sur chacune des attaques
        
        
        if capacites["repeat"][num] :
            #Certaines capacités peuvent être lancées aléatoirement 2 à 5 
            #On a 3 chances sur 8 que l'attaque se lance 2 fois
            #3 chances cur 8 que l'attaque se lance 3 fois
            #1 chances cur 8 que l'attaque se lance 4 fois
            #1 chances cur 8 que l'attaque se lance 5 fois
            #Dans ce cas, on multiplie simplement les dégâts infligés par un nombre entre 2 et 5
            
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
            #Chaque attaque dispose d'une précision qui donne le pourcentage de chances de réussite de la capacité
            
            condition = True
            #Ce booléen sert uniquement pour le cas des capacités avec une condition d'utilisation
            
            
            if capacites["condition"][num] == "asleep":
                #Une capacité a pour condition que le pokémon adverse soit endormi, si c'est celle-ci, on
                #vérifie qu'elle peut se lancer
                if not adv.state == "asleep":
                    condition = False
                    
            if condition and capacites["Power"][num] != 0:
                #si l'attaque a une puissance, elle inflige des dégâts
                #Cela permet d'éviter toute erreur dans le cas où l'attaque a une puissance de 0 mais que
                #le calcul de dégâts donne un nombre plus grand
                dmg = adv.degats(dmg)
                
                #on garde la valeur des dégâts réellements subis dans la variable dmg, cela sert dans certains cas
                #utiliser la méthode de cette façon permet à la fois d'appliquer réellement la méthode et de sauvegarder la valeur
                
            if capacites["seed"][num]:
                #Dans le cas de l'attaque vampigraine, on place le pokémon adverse dans l'état infecté
                adv.seeded = True
                print(adv.name + " est infecté !")
                
            if capacites["SD"][num] != 0:
                #Certaines attaques infligent des dégâts au lanceur
                #Les dégâts en question dépendent des pv max du lanceur, ils sont soient égaux
                #à un quart, soit à la totalité de ceux-ci, et "capacites["SD"][num]" vaut 0,1 ou 4
                self.degats(capacites["SD"][num] * self.pv_max / 4)
                print(self.name + " se blesse en attaquant !")
                
            if capacites["LS"][num]:
                #Certaines attaques soignent le lanceur de la moitié des dégâts infligés
                self.heal(np.ceil(dmg / 2))
                print(self.name + " vole de la vie !")
                
            if capacites["newstatus"][num] != "normal" and adv.state == "normal" and randint(0,99) < capacites["precision_status"][num]:
                #Certaines attaques changent le statut du pokemon adverse
                #la probabilité de changer de statut est liée à une autre variable située dans
                #la colonne "precision_status"
                adv.state = capacites["newstatus"][num]
                #si le changement de statut réussit, il est appliqué au pokemon adverse
                
                if capacites["newstatus"][num] == "burnt":
                    print(adv.name + " est brûlé !")
                if capacites["newstatus"][num] == "poisoned":
                    print(adv.name + " est empoisonné !")
                if capacites["newstatus"][num] == "frozen":
                    print(adv.name + " est gelé !")
                    
                if capacites["newstatus"][num] == "asleep":
                    #dans le cas d'une attaque endormant l'adversaire, il faut aussi mettre son compteur
                    #de statut à 4, puisque l'endormissement dure 4 tours au maximum
                    adv.status_duration = 4
                    print(adv.name + " s'endort !")
                    
                if capacites["newstatus"][num] == "confused":
                    #idem pour la confusion
                    adv.status_duration = 4
                    print(adv.name + " devient confus !")
                    
            if capacites["heal"][num]:
                self.heal(self.pv_max / 2)
                print(self.name + " se soigne !")
        else:
            print(self.name + " rate son attaque !")
        
    def degats(self,dmg):
        '''
        Cette méthode sert à gérer les dégâts subis par un pokémon
        elle renvoie les dégâts réellement subis, c'est à dire après passage à la partie entière ou réduction
        dans le cas où elle ferait plus de dégâts que le pokémon n'a encore de pv
        
        :param dmg: dégâts théoriques subis
        :type dmg: float
        
        :return: dégâts réellement subis
        :type return: int
        '''
        
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
        '''
        Cette méthode sert à gérer les soins subis par un pokémon
        elle ne renvoie rien
        
        :param amount: soins théoriques subis
        :type amount: float
        '''
        self.pv += np.floor(amount)
        if self.pv > self.pv_max:
            self.pv = self.pv_max
            #On vérifie que le pokémon ne se soigne pas plus que ses PV maximum