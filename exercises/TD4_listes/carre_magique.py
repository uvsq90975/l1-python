carre_mag = [[4, 14, 15, 1], [9, 7, 6, 12], [5, 11, 10, 8], [16, 2, 3, 13]]
print(carre_mag)

carre_pas_mag = [list(l) for l in carre_mag] # attention, on ne peut pas seulement copier la liste
carre_pas_mag[3][2] = 7

def afficheCarre(carre):
    """ Affiche la liste à 2 dimensions carre comme un carré"""
    for l in carre:
        print(l)
    print()

afficheCarre(carre_mag)
afficheCarre(carre_pas_mag)

def testLignesEgales(carre):
    """ Renvoie la somme des éléments d'une ligne de la liste 2D carre si toutes les lignes ont la même somme, et -1 sinon """
    som = sum(carre[0])
    for l in carre:
        if sum(l) != som:
            return -1
    return som

print(testLignesEgales(carre_mag))
print(testLignesEgales(carre_pas_mag))

def testColonnesEgales(carre):
    """ Renvoie la somme des éléments d'une colonne de la liste 2D carre si toutes les colonnes ont la même somme, et -1 sinon """
    col = [l[0] for l in carre]
    som = sum(col)
    for i in range(1, len(carre)):
        col = [l[i] for l in carre]
        if sum(col) != som:
            return -1
    return som

print(testColonnesEgales(carre_mag))
print(testColonnesEgales(carre_pas_mag))

def testDiagonalesEgales(carre):
    """ Renvoie la somme des éléments d'une diagonale de la liste 2D carre si les 2 diagonales ont la même somme, et -1 sinon """
    n = len(carre)
    diag = [carre[i][i] for i in range(n)]
    anti_diag = [carre[i][n - 1 - i] for i in range(n)]
    som = sum(diag)
    if som == sum(anti_diag):
        return som
    else:
        return -1

print(testDiagonalesEgales(carre_mag))
print(testDiagonalesEgales(carre_pas_mag))

def estCarreMagique(carre):
    """ Renvoie True si c'est un carre magique et False sinon"""
    return testLignesEgales(carre) ==  testColonnesEgales(carre) \
        and testLignesEgales(carre) == testDiagonalesEgales(carre) \
        and testLignesEgales(carre) != -1

print(estCarreMagique(carre_mag))
print(estCarreMagique(carre_pas_mag))

def estNormal(carre):
    """ Retourne True si contient toutes les valeurs de 1 à n^2 où n est la taille 
        du carré, et False sinon """
    n = len(carre)
    nombres = list(range(1, n * n + 1))
    for i in range(n):
        for j in range(n):
            if carre[i][j] in nombres: #on teste d'abord pour pas générer d'erreur avec remove
                nombres.remove(carre[i][j])
    return len(nombres) == 0

print(estNormal(carre_mag))
print(estNormal(carre_pas_mag))
