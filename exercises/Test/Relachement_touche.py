from tkinter import Tk, Canvas
import os

os.system('xset r off')

root = Tk()
cnv = Canvas(root, width=400, height=100, bg="ivory")
cnv.pack()
cnv.focus_set()
x=0

def texte(event):
    global x
    cnv.create_text(x, 40, text =event.keysym, font="Arial 50 bold")
    x+=30

cnv.bind('<KeyRelease-a>', texte)

root.mainloop()
os.system('xset r on')