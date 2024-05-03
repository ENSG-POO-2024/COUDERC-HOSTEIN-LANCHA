class Red:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def deplacement(self,direction):
        if direction == "h" :
            self.y += 1
        elif direction == "d" :
            self.x += 1
        elif direction == "b" :
            self.y -= 1
        elif direction == "g" :
            self.x -= 1
    def __str__(self):
        return "Hey ! Moi, c'est Red"

class Carte:
    def __init__(self):
        pass