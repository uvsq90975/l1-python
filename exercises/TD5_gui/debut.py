# Début

import tkinter as tk

WIDTH, HEIGHT = 800, 600

root = tk.Tk()

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT)
canvas.grid()

# Début de votre code
x0, x1 = WIDTH / 2, WIDTH / 2
y0, y1 = 100, HEIGHT - 100
canvas.create_line(x0, y0, x1, y1)
canvas.create_oval(x0 - 50, y0 - 50, x0 + 50, y0 + 50)
canvas.create_oval(x1 - 50, y1 - 50, x1 + 50, y1 + 50)
canvas.create_oval(x0-50, (y0+y1)/2 - 50, x0 + 50, (y0+y1)/2 + 50)
    
# Fin de votre code

root.mainloop()
