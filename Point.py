class Point:

    def __init__(self):
        self.x = 23
        self.y = self.x + 5

    def affiche(self):
        self.z = 42
        print("({0},{1})".format(self.x, self.y))
