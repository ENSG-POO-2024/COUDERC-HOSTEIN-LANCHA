

class Personnage :

    def __init__(self,px,py):
        self.px = px
        self.py + py

    # def deplacement(self, direction):
    #     if direction == "haut":
    #         self.py += 1
    #     if direction == "bas":
    #         self.py -= 1
    #     if direction == "gauche":
    #         self.px -= 1
    #     if direction == "droite":
    #         self.py += 1

    # sac = [] # le sac contient les pokemon que le personnage a au départ

    def decouverte_pokemon(self):
        # si self.position est à une distance d du pokemon alors on peut le voir et le combat commence
        pass

    def fuite(self):
        #on refuse le combat
        pass

    def attaque(self):
        #faire que notre pokemon attaque celui en face
        #le pokemon qui doit attaquer est le premier dans le sac
        pass

    def changer_pokemon(self):
        pass

    def capture_pokemon(self):
        pass





class Sac:

    def __init__(self):
        self.objets = []

    def __str__(self):
        txt = "Le sac contient : " + str(self.objets)
        return txt


    def changer_place(self, pokemon, nouvelle_place):
        # pour changer la place d'un pokemon dans le sac(attention la place du début est 0)
        if pokemon not in self.objets:
            print("Ce Pokémon n'est pas dans le sac !")
        else:
            self.objets[self.objets.index(pokemon)], self.objets[nouvelle_place] = self.objets[nouvelle_place], self.objets[self.objets.index(pokemon)]


    def changer_pokemon(self):
        #on veut changer de pokemon durant le combat
        pass

    def capture_pokemon(self, pokemon):
        # on ne peut capturer le pokemon que si le combat a été gagné
        # if pokemon.pv == 0:
        #     self.objets.append(pokemon)
        self.objets.append(pokemon)






if __name__ == "__main__":

    pokemon1 = "Pikachu"
    pokemon2 = "Luxray"
    pokemon3 = "Salameche"

    sac_pokemon = Sac()
    sac_pokemon.capture_pokemon(pokemon1)
    sac_pokemon.capture_pokemon(pokemon2)
    print(sac_pokemon)
    sac_pokemon.changer_place(pokemon1,1)
    print(sac_pokemon)
    sac_pokemon.changer_place(pokemon3, 1)
    sac_pokemon.capture_pokemon(pokemon3)
    print(sac_pokemon)
    sac_pokemon.changer_place(pokemon2, 2)
    print(sac_pokemon)
