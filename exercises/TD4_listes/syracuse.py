def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """
    l = []
    l.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        l.append(n)
    return l


#print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    test = True
    for n in range(2,n_max+1):
        l = syracuse(n)
        print(l)
        
        if l[-1] != 1:
            test = False
            print("False")
        else:
            print("True")
    
    print("Test terminé")
    return test



print(testeConjecture(10))



    def tempsVol(n):
    """ Retourne le temps de vol de n """
    l = []
    l.append(n)
    cpt = 0
    while n != 1:
        if n % 2 == 0:
            n = n//2
        else:
            n = n*3+1
        l.append(n)
        cpt += 1
    return cpt


def tempsVol2(n):
    """ Retourne le temps de vol de n """
    l = syracuse(n)
    return len(l)-1


n = 3
print("Le temps de vol de", n, "est", tempsVol(n))
print("Le temps de vol de", n, "est", tempsVol2(n))


def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    l = []
    for n in range(1, n_max + 1):
        l.append(tempsVol2(n))
    return l

l = tempsVolListe(10000)
#print(l)

maxi = max(l)
print("Temsp de vol maxi :", maxi)
val = l.index(maxi) + 1
print("Valeur :", val)


def altMax(n):
    """ Retourne la plus grande valeur par laquelle passe n au cours de son vol"""
    l = syracuse(n)
    return max(l)


def altMaxListe(n_max):
    l = []
    for n in range(1, n_max + 1):
        l.append(altMax(n))
    return l


n = 10000
l = altMaxListe(n)
#print(l)

maxi = max(l)
print("Altitude maxi :", maxi)
val = l.index(maxi) + 1
print("Valeur :", val)



