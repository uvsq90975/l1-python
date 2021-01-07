from tkinter import *

def touche(event):
    t=event.keysym
    print("Touche %s pressée" %t)

root = Tk()

root.bind('<Key>', touche)

root.mainloop()
