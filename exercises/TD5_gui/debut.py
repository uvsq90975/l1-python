# Début

import tkinter as tk

WIDTH, HEIGHT = 800, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)

# Début de votre code
x0 = 100
x1 = WIDTH - 100
y = HEIGHT / 2
canvas.create_line(x0, y, x1, y)
canvas.create_oval(x0 - 50, y - 50, x0 + 100, y + 200)
canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
# Fin de votre code
canvas.grid()
root.mainloop()
