# Cible

import tkinter as tk
import random

# Variables globales

L = 700
WIDTH, HEIGHT = L, L
E = 30

# Création de l'interface et du canevas

root = tk.Tk()
root.title("Cible")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
canvas.grid()


# Début du code

coul = ["blue", "green", "black", "yellow", "magenta", "red"]

for i in range(int((L/2)/E)):
    x0, y0 = 0 + i*E, 0 + i*E
    x1, y1 = L - i*E, L - i*E
    cercle = canvas.create_oval(x0, y0, x1, y1, outline=coul[i%6], width=E)


# Fin du code
root.mainloop()