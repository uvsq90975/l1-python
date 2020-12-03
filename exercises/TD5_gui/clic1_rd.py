# Clic

# Pixel au niveau du clic

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




# Début du code

root.bind("<Button-1>", aff_pixel)




# Fin du code

root.mainloop()
