# Couleurs (dégradés)

import tkinter as tk
import random

L = 256
WIDTH, HEIGHT = L, L
root = tk.Tk()

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg="black")
canvas.grid(column=1, row=0, rowspan = 7)

# Fonctions

def get_color(r, g, b):
    """ Retourne une couleur à partir de ses composantes r, g, b entre 0 et 255"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


def draw_pixel(i, j, color):
    """colorie un pixel"""
    pixel = canvas.create_line(i, j, i+1 , j, fill=color)


def ecran_aleatoire():
    for i in range(L):
        for j in range(L):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
            color = get_color(r, g, b)
            pixel = canvas.create_line(i, j, i+1 , j, fill=color)


def degrade_gris():
    for i in range(L):
        for j in range(L):
            color = get_color(i, i, i)
            draw_pixel(i, j, color)


def degrade_2D():
    for i in range(L):
        for j in range(L):
            color = get_color(i, 0, j)
            draw_pixel(i, j, color)


# Début du code

B_aleatoire = tk.Button(root, text="Aléatoire", fg="blue", font=("times new roman", "20"), padx=10, command=ecran_aleatoire)
B_aleatoire.grid(column = 0, row = 1)

B_degrade_gris = tk.Button(root, text="Dégradé gris", fg="blue", font=("times new roman", "20"), padx=10, command=degrade_gris)
B_degrade_gris.grid(column = 0, row = 3)

B_degrade_2D = tk.Button(root, text="Dégradé 2D", fg="blue", font=("times new roman", "20"), padx=10, command=degrade_2D)
B_degrade_2D.grid(column = 0, row = 5)

draw_pixel(L/2, L/2,"white")

# Fin du code

root.mainloop()
