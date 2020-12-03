# Début

import tkinter as tk

WIDTH, HEIGHT = 600, 400


root = tk.Tk()

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)

# Début de votre code

"""
#Ligne horizontale
x0 = 100
x1 = WIDTH - 100
y = HEIGHT / 2
canvas.create_line(x0, y, x1, y)
canvas.create_oval(x0 - 50, y - 50, x0 + 50, y + 50)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)

#canvas.create_line(0, 0, WIDTH, HEIGHT, fill="red", width=5)
"""

#Ligne verticale
y0 = 100
y1 = HEIGHT - 100
x = WIDTH / 2
canvas.create_line(x, y0, x, y1)
canvas.create_oval(x-50, y0-50, x+50, y0+50)
canvas.create_oval(x-50, y1-50, x+50, y1+50)
canvas.create_oval(x-50, (y0+y1)/2-50, x+50, (y0+y1)/2+50)


# Fin de votre code

canvas.grid()
root.mainloop()
