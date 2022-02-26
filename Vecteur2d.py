class Vecteur2d:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def affiche(self):
        print("x={0}, y={1}".format(self.x, self.y))

    def __add__(self, other):
        sumX = self.x + other.x
        sumY = self.y + other.y
        return Vecteur2d(sumX, sumY)
