# Clic

# clic

# Cercles bleus ou rouges

import tkinter as tk

L = 500
WIDTH, HEIGHT = L, L

root = tk.Tk()

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg="black")
canvas.grid()


# Fonctions

def aff_pixel(event):
    x = event.x
    y = event.y
    pixel = canvas.create_line(x, y, x+1, y, fill="white")


def aff_cercle(event):
    x, y = event.x, event.y
    r = 50
    if x < L/2:
        coul = "blue"
    else:
        coul = "red"
    cercle = canvas.create_oval(x-r, y-r, x+r, y+r, fill=coul)


# Début du code

ligne = canvas.create_line(L/2, 0, L/2, L, fill="white")

root.bind("<Button-1>", aff_cercle)




# Fin du code

root.mainloop()

