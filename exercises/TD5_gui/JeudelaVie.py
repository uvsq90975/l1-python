import tkinter as tk
root = tk.Tk()

import random

# Variables globales

L = 700     # largeur écran
d = 10       # largeur de cellule
N = L//d      # nbre de cellules


T = [[0 for i in range(N)] for i in range(N)]

New = [[0 for i in range(N)] for i in range(N)]


# Fenêtre graphique

canvas = tk.Canvas(root, width=L, height=L, bg="white", borderwidth=5, relief="groove")
canvas.grid(column=0, row=1)


# Fonctions

def aff_damier():
    for i in range(N):
        canvas.create_line((0, i*d), (L, i*d), fill="black")
        canvas.create_line((i*d, 0), (i*d, L), fill="black")


def aff_cellule(i, j, col):
    canvas.create_rectangle((i*d, j*d), ((i+1)*d, (j+1)*d), fill=col)


def clic_cellule(event):
    i = int(event.x // d)
    j = int(event.y // d)
    if T[i][j] == 0:
        aff_cellule(i, j, "black")
        T[i][j] = 1
        New[i][j] = 1
    else:
        aff_cellule(i, j, "white")
        T[i][j] = 0
        New[i][j] = 0


def start(event):
        # Naissance et mort des cellules
        for i in range(N):
            for j in range(N):
                cpt = 0
                if i>0 and j>0 and T[i-1][j-1] == 1:
                    cpt += 1
                if j>0 and T[i][j-1] == 1:
                    cpt += 1
                if i<N-1 and j>0 and T[i+1][j-1] == 1:
                    cpt += 1
                if i<N-1 and T[i+1][j] == 1:
                    cpt += 1
                if i<N-1 and j<N-1 and T[i+1][j+1] == 1:
                    cpt += 1
                if j<N-1 and T[i][j+1] == 1:
                    cpt += 1
                if i>0 and j<N-1 and T[i-1][j+1] == 1:
                    cpt += 1
                if i>0 and T[i-1][j] == 1:
                    cpt += 1

                if (cpt == 2 or cpt == 3) and T[i][j] == 1 :     # survie d'une cellule (si 2 ou 3 voisines)
                    New[i][j] = 1
                else:
                    New[i][j] = 0          

                if (cpt == 3) and T[i][j] == 0 :                  # naissance d'une cellule (si 3 voisines)
                    New[i][j] = 1       

        # Affichage des cellules
        for i in range(N):
            for j in range(N):
                if T[i][j] != New[i][j]:
                    T[i][j] = New[i][j]
                    if T[i][j] == 1:
                        aff_cellule(i, j, "black")
                    else:
                        aff_cellule(i, j, "white")


# Début

aff_damier()

root.bind("<Button-1>", clic_cellule)

root.bind("<Return>", start)


# Fin
root.mainloop()