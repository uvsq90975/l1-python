# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    return temps[0]*24*60*60 + temps[1]*60*60 + temps[2]*60 + temps[3]


temps = (2, 23, 1, 34)
print(type(temps))
print(temps)
print(tempsEnSeconde(temps), "secondes")   


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    j = seconde // (24*60*60)
    h = (seconde % (24*60*60)) // (60*60)
    m = ((seconde % (24*60*60)) % (60*60)) // 60
    s = ((seconde % (24*60*60)) % (60*60)) % 60
    temps = (j, h, m, s)
    return temps

    
temps = secondeEnTemps(tempsEnSeconde(temps))
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")
print()


# fonction auxiliaire ici

def affichePluriel(mot, nbre):
    if nbre == 0:
        print("", end="")
    elif nbre == 1:
        print(nbre, mot, end=" ")
    elif nbre > 1:
        print(nbre, mot + "s", end=" ")


def afficheTemps(temps):
    affichePluriel("jour", temps[0])
    affichePluriel("heure", temps[1])
    affichePluriel("minute", temps[2])
    affichePluriel("seconde", temps[3])
    print()

    
afficheTemps((1, 0, 14, 23))


def demandeTemps():
    print()
    j = int(input("Entrer un nombre de jours : "))
    if j == -1:
        exit()    # sortie du programme
    
    h = int(input("Entrer un nombre d'heures < 24 : "))
    while h >= 24:
        h = int(input("Entrer un nombre d'heures < 24 : "))

    m = int(input("Entrer un nombre de minutes < 60 : "))
    while m >= 60:    
        m = int(input("Entrer un nombre de minutes < 60 :"))

    s = int(input("Entrer un nombre de secondes < 60 :"))
    while s >=60:    
        s = int(input("Entrer un nombre de secondes < 60 :"))
    
    temps = (j, h, m, s)
    return temps

#afficheTemps(demandeTemps())



def sommeTemps(temps1,temps2):
    s1 = tempsEnSeconde(temps1)
    s2 = tempsEnSeconde(temps2)
    s = s1 + s2
    temps = secondeEnTemps(s)
    print()
    print(temps1, "+", temps2, "=", temps)
    print()
    return temps

sommeTemps((2,3,4,25),(5,22,57,1))



def proportionTemps(temps,proportion):
    if type(temps) == float :
        temps, proportion = proportion, temps
    s = tempsEnSeconde(temps)
    r = int(proportion * s)
    tempsR = secondeEnTemps(r)
    print(100*proportion, "% de ", end="")
    afficheTemps(temps)
    print("= ", end = "")
    afficheTemps(tempsR)
    return tempsR

afficheTemps(proportionTemps((2,0,36,0), 0.5))

#appeler la fonction en échangeant l'ordre des arguments
print()
afficheTemps(proportionTemps(0.5, (2,0,36,0)))
print()



def tempsEnDate(ref, temps):
    seconde = tempsEnSeconde(temps)
    a = seconde // (365*24*60*60)
    a = a + ref
    j = (seconde % (365*24*60*60)) // (24*60*60)
    h = ((seconde % (365*24*60*60)) % (24*60*60)) // (60*60)
    m = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) // 60
    s = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) % 60
    date = (a, j, h, m, s)
    return date


def afficheDate(date):
    affichePluriel("annee", date[0])
    affichePluriel("jour", date[1])
    affichePluriel("heure", date[2])
    affichePluriel("minute", date[3])
    affichePluriel("seconde", date[4])
    print()
    

temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(1970, temps))
#afficheDate()
print()

import time


seconde = int(time.time())
print(seconde)
print()
temps = secondeEnTemps(seconde)
date = tempsEnDate(1970, temps)
afficheDate(date)
print()

s = time.gmtime(0)
print(s)
print()
date = (s[0], s[2], s[3], s[4], s[5])
afficheDate(date)
print()



def bisextile(ref, jour):
    a = jour // (365)
    for i in range (ref, ref+a+1) :
      if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) :
        print(i)
       
        
bisextile(2020, 200000)
print()

def nombreBisextile(ref, jour):
    a = jour // (365)
    bis = 0
    for i in range (ref, ref+a+1) :
      if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) :
        bis = bis + 1
    return bis

def tempsEnDateBisextile(ref, temps):
    seconde = tempsEnSeconde(temps)
    jour = seconde // (60*60*24)
    bis = nombreBisextile(ref, jour)
    print("Nombre d'annees bissextiles = ", bis)
    seconde = seconde + bis*(60*60*24)
    tempsBis = secondeEnTemps(seconde)
    dateBis = tempsEnDate(ref, tempsBis)
    return dateBis 
   

def tempsEnDateMois(ref, temps):
    seconde = tempsEnSeconde(temps)
    a = seconde // (365*24*60*60)
    a = a + ref

    #annee bisextile si bis = 1  
    bis = 0
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) :
        bis = 1
    else :
        bis = 0  

    j = (seconde % (365*24*60*60)) // (24*60*60)

    M = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    m = ""
    if 1 <= j and j <= M[0]:
        m = "janvier"

    elif M[0]+1 <= j and j <= bis+M[0]+M[1]:
        m = "fevrier"
        j = j - (M[0])

    elif bis+M[0]+M[1]+1 <= j and j <= bis+M[0]+M[1]+M[2]:
        m = "mars"
        j = j - (bis+M[0]+M[1])

    elif bis+M[0]+M[1]+M[2]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]:
        m = "avril"
        j = j - (bis+M[0]+M[1]+M[2])

    elif bis+M[0]+M[1]+M[2]+M[3]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]:
        m = "mai"
        j = j - (bis+M[0]+M[1]+M[2]+M[3])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]:
        m = "juin"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]:
        m = "juillet"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]:
        m = "aout"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6])

    elif j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+1 <= j and j <= j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]:
        m = "septembre"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]:
        m = "octobre"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]:
        m = "novembre"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]+M[11]:
        m = "decembre"
        j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]) 

    h = ((seconde % (365*24*60*60)) % (24*60*60)) // (60*60)
    min = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) // 60
    s = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) % 60

    date = (a, m, j, h, min, s)
    return date


def tempsEnDateMoisBisextile(ref, temps):
    seconde = tempsEnSeconde(temps)
    a = seconde // (365*24*60*60)
    a = a + ref

    #annee bisextile si bis = 1  
    bis = 0
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0) :
        bis = 1
    else :
        bis = 0

    nbre_bis = 0
    for i in range (ref, a) :
      if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0) :
        nbre_bis = nbre_bis + 1    

    j = (seconde % (365*24*60*60)) // (24*60*60)
    j = j - nbre_bis

    M = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    m = ""
    if 1 <= j and j <= M[0] :
      m = "janvier"

    elif M[0]+1 <= j and j <= bis+M[0]+M[1] :
      m = "fevrier"
      j = j - (M[0])

    elif bis+M[0]+M[1]+1 <= j and j <= bis+M[0]+M[1]+M[2] :
      m = "mars"
      j = j - (bis+M[0]+M[1])

    elif bis+M[0]+M[1]+M[2]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3] :
      m = "avril"
      j = j - (bis+M[0]+M[1]+M[2])

    elif bis+M[0]+M[1]+M[2]+M[3]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4] :
      m = "mai"
      j = j - (bis+M[0]+M[1]+M[2]+M[3])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5] :
      m = "juin"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6] :
      m = "juillet"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7] :
      m = "aout"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6])

    elif j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+1 <= j and j <= j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8] :
      m = "septembre"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9] :
      m = "octobre"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10] :
      m = "novembre"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9])

    elif bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]+1 <= j and j <= bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]+M[11] :
      m = "decembre"
      j = j - (bis+M[0]+M[1]+M[2]+M[3]+M[4]+M[5]+M[6]+M[7]+M[8]+M[9]+M[10]) 

    h = ((seconde % (365*24*60*60)) % (24*60*60)) // (60*60)
    min = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) // 60
    s = (((seconde % (365*24*60*60)) % (24*60*60)) % (60*60)) % 60

    # heure hiver h = h + 1
    h = h + 1

    date = (a, m, j, h, min, s)
    return date



def afficheDateMois(date):
    print(date[2], date[1], date[0], end=" : ")
    affichePluriel("heure", date[3])
    affichePluriel("minute", date[4])
    affichePluriel("seconde", date[5])
    print()

# time{} commence en 1970 janvier 1 jour  00:00:00
# il faut ajouter 1 jour en secondes
temps = secondeEnTemps(int(time.time()) + 24*60*60)
afficheTemps(temps)
print()

afficheDateMois(tempsEnDateMois(1970, temps))

afficheDateMois(tempsEnDateMoisBisextile(1970, temps))

seconde = tempsEnSeconde(temps)
jour = seconde // (60*60*24)
bis = nombreBisextile(1970, jour)
print("Nombre d'annees bissextiles = ", bis)
print()







