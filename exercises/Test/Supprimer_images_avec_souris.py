from tkinter import *
from random import randrange

SIDE=400
root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="python64.gif")

for i in range(20):
    x, y= randrange(SIDE),randrange(SIDE)
    cnv.create_image(x, y, image=logo)

def clic(event):
    x=event.x
    y=event.y
    t=cnv.find_closest(x, y)
    if t:
        cnv.delete(t[0])

cnv.bind("<Button>",clic)

root.mainloop()