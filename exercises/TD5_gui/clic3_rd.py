# Clic

# Lignes bleues ou rouges

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


x = []
y = []

def aff_ligne(event):
    global x
    global y
    x.append(event.x)
    y.append(event.y)
    if len(x) == 1:
        pass
    elif len(x) == 2:
        if (x[0] < L/2 and x[1] < L/2) or (x[0] > L/2 and x[1] > L/2):
            coul="blue"
        else:
            coul="red"
        cercle = canvas.create_line(x[0], y[0], x[1], y[1], fill=coul)
        del x[-1]
        del x[-1]
        del y[-1]
        del y[-1]


# Début du code

ligne = canvas.create_line(L/2, 0, L/2, L, fill="white")

root.bind("<Button-1>", aff_ligne)



# Fin du code

root.mainloop()
