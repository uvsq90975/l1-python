# Dessin

import tkinter as tk
import random

# Variables globales

WIDTH, HEIGHT = 500, 500

# Définitions des fonctions

def aff_cercle():
    #coul = "blue"
    global coul
    x = random.randint(0+50, WIDTH-50)
    y = random.randint(0+50, HEIGHT-50)
    cercle = canvas.create_oval(x-50, y-50, x+50, y+50, fill=coul)


def aff_carre():
    #coul = "red"
    global coul
    x = random.randint(0+50, WIDTH-50)
    y = random.randint(0+50, HEIGHT-50)
    carre = canvas.create_rectangle(x-50, y-50, x+50, y+50, fill=coul)


def aff_croix():
    #coul = "yellow"
    global coul
    x = random.randint(0+50, WIDTH-50)
    y = random.randint(0+50, HEIGHT-50)
    ligne1 = canvas.create_line(x-50, y-50, x+50, y+50, fill=coul)
    ligne2 = canvas.create_line(x-50, y+50, x+50, y-50, fill=coul)


coul = "blue"

def choix_couleur():
    global coul
    coul = input("Ecrire votre couleur :")


# Début du code

root = tk.Tk()
root.title("Mon dessin")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", border=10, relief="groove")
canvas.grid(column=1, row=1, rowspan=10)


B_choix_couleur = tk.Button(root, text="Choisir une couleur", bg="dark grey", fg="red", font=("20"), padx=50, command=choix_couleur)
B_choix_couleur.grid(column=1, row=0)


B_cercle = tk.Button(root, text="Cercle", command=aff_cercle)
B_cercle.grid(column=0, row=3)

B_carre = tk.Button(root, text="Carré", command=aff_carre)
B_carre.grid(column=0, row=6)

B_croix = tk.Button(root, text="Croix", command=aff_croix)
B_croix.grid(column=0, row=9)


# Fin du code
root.mainloop()