from tkinter import Tk, Canvas
from random import randrange

SIDE=200

root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack(padx=10, pady=10)
cnv.focus_set()

def dessiner(event):
    n=int(event.keysym[0])
    for i in range(n):
        a=randrange(SIDE)
        b=randrange(SIDE)
        cnv. create_rectangle(a, b, a+20, b+20, fill="red")

cnv.bind('<Key-1>', dessiner)
cnv.bind('<Key-2>', dessiner)
cnv.bind('<Key-3>', dessiner)

root.mainloop()

