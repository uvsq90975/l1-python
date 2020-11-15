# temps[0] : jours, temps[1]: heures, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en seconde de temps\
         donné comme jour, heure, minute, seconde."""
    return temps[3] + temps[2]*60 + temps[1]*60*60 + temps[0]*60*60*24


def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) \
        qui correspond au nombre de seconde passé en argument"""
    j = seconde // (24*60*60)
    h = (seconde % (24*60*60)) // (60*60)
    m = ((seconde % (24*60*60)) % (60*60)) // 60
    s = ((seconde % (24*60*60)) % (60*60)) % 60
    temps = (j, h, m, s)
    return temps


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


####################################################################

temps = (3, 0, 1, 34)
print() 
print(type(temps))
seconde = tempsEnSeconde(temps)
print(seconde, "secondes")
print()

temps = secondeEnTemps(seconde)
print(temps[0], "jours", temps[1], "heures", temps[2], "minutes", temps[3], "secondes")

afficheTemps(temps)
print()


