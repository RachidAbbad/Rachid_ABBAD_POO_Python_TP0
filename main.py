from Point import Point
from Vecteur2d import Vecteur2d
import StringFunctions

# Test Point :
print("-------- Test Point ------------")
point = Point()
point.affiche()

# Test Vecteur 2d
print("-------- Test Vecteur2d ------------")

print("Vecteur sans paramètres :")
vect = Vecteur2d()
vect.affiche()

print("Vecteur avec paramètres x=3 & y=9:")
vect2 = Vecteur2d(3, 9)
vect2.affiche()

print("L'addition des deux vecteurs (3,9) & (4,8)")
vect3 = Vecteur2d(4, 8)
sumVect = vect3 + vect2
sumVect.affiche();

# Test nb occurences
print("-------- Test nombres des occuences ------------")
print("Chaine de test :\"Salut Salut je suis suis je aussi\"")
chaine = "Salut Salut je suis suis je aussi"

dictMot = StringFunctions.motsOccurence(chaine)
print("Nombre d'occurence des mots :")
for mot in dictMot:
    print(mot + "-->" + str(dictMot[mot]) + " ", end='')

dictLettres = StringFunctions.lettresOccurence(chaine)
print("\nNombre d'occurence des lettres :")
for lettre in dictLettres:
    print(lettre + "-->" + str(dictLettres[lettre]) + "  ", end='')
