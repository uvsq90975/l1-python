# Cible

import tkinter as tk

L = 500     # Largeur du canevas
WIDTH, HEIGHT = L, L
E = 10      # Epaisseur des cercles

fenetre = tk.Tk()

canvas = tk.Canvas(fenetre, width = WIDTH, height = HEIGHT, bg = "black")
canvas.grid(column=0, row=0)


# Début du code

coul = ["blue", "green", "black", "yellow", "magenta", "red"]

for i in range(int(L/(2*E))):
    x0, y0 = 0 + i*E, 0 + i*E
    x1, y1 = L - i*E, L - i*E
    cercle = canvas.create_oval(x0, y0, x1, y1, outline=coul[i%6], width = E)


# Fin du code

fenetre.mainloop()
