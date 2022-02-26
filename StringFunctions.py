def motsOccurence(chaine):
    nbOcc = {}
    listMots = chaine.split()

    # Compter le nombre d'occurences
    for mot in listMots:
        if mot in nbOcc:
            nbOcc[mot] += 1
        else:
            nbOcc[mot] = 1

    return nbOcc


def lettresOccurence(chaine):
    nbOcc = {}

    # Compter le nombre d'occurences
    for lettre in chaine:
        if lettre.lower() in nbOcc:
            nbOcc[lettre.lower()] += 1
        elif lettre == " ":
            continue
        else:
            nbOcc[lettre.lower()] = 1

    return nbOcc



