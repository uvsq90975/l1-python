import tkinter as tk
import random

WIDTH, HEIGHT = 400, 400

root = tk.Tk()

root.title("Mon dessin")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", borderwidth=10, relief="groove")
canvas.grid(column=1, row=1, rowspan=11)


# Variables globales

coul = "blue"
objet = []


# Définitions des Fonctions

def choix_couleur():
    global coul
    coul = input("Choisir une couleur parmi : white, black, red, green, blue, cyan, yellow.")


def aff_cercle():
    #global coul
    coul = "blue"
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    cercle = canvas.create_oval(x-50, y-50, x+50, y+50, fill=coul)
    global objet
    objet.append(cercle)


def aff_carre():
    #global coul
    coul = "red"
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50)
    carre = canvas.create_rectangle(x-50, y-50, x+50, y+50, fill=coul)
    global objet
    objet.append(carre)


def aff_croix():
    #global coul
    coul = "yellow"
    x = random.randint(50, WIDTH-50)
    y = random.randint(50, HEIGHT-50) 
    ligne1 = canvas.create_line(x-50, y-50, x+50, y+50, fill=coul)
    ligne2 = canvas.create_line(x-50, y+50, x+50, y-50, fill=coul)
    global objet
    objet.append(ligne1)
    objet.append(ligne2)


def undo():
    global objet
    if len(objet) > 0:
        if canvas.type(objet[-1]) == "line":
            canvas.delete(objet[-1])
            canvas.delete(objet[-2])
            del objet[-1]
            del objet[-1]
        else:
            canvas.delete(objet[-1])        # effacer de l'affichage
            del objet[-1]                   # effacer de la liste objet[]


# Début du code

B_undo = tk.Button(root, text="Undo", command=undo, bg="yellow")
B_undo.grid(column=0, row=0)

B_couleur = tk.Button(root, text="Choisir une couleur", padx=50, bg="dark grey", fg="red", font=("30"), command=choix_couleur)
B_couleur.grid(column=1, row=0)

B_cercle = tk.Button(root, text="Cercle", command=aff_cercle)
B_cercle.grid(column=0, row=3)

B_carre = tk.Button(root, text="Carré", command=aff_carre)
B_carre.grid(column=0, row=6)

B_croix = tk.Button(root, text="Croix", command=aff_croix)
B_croix.grid(column=0, row=9)


# Fin du code

canvas.grid()
root.mainloop()
