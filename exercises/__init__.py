import tkinter as tk

root = tk.Tk()


def f(event):
    x = event.keysym
    print("Touche enfoncée :", x)

def g(event):
    x = event.x
    y = event.y
    print("Position de la souris :", x, y)



root.bind('<Key>', f)
root.bind('<Motion>', g)

root.mainloop()
