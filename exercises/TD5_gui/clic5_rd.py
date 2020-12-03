# Clic

# Cercles changent de couleur

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


cpt = 0

def carre_plein_vide(event):
    global cpt
    if cpt != 10:
        if cpt % 2 == 0:
            coul = "black"
        else:
            coul = "white"
        canvas.create_rectangle(100, 100, 400, 400, fill=coul, width=5, outline="white")
        cpt += 1
    else:
        root.destroy()


cercle = []

def cercle_change_couleur(event):
    global cpt
    cpt += 1
    if cpt <= 8:
        cercle.append(canvas.create_oval(event.x-50, event.y-50, event.x+50, event.y+50, fill="red"))
    elif cpt == 9:
        for i in range(8):
            canvas.itemconfigure(cercle[i], fill="yellow")
    elif cpt == 10:
        cpt = 0
        for i in range(8):
            canvas.delete(cercle[i])
        for i in range(8):
            del cercle[-1]


# Début du code

root.bind("<Button-1>", cercle_change_couleur)



# Fin du code

root.mainloop()
