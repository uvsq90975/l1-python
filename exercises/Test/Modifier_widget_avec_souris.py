from tkinter import *

root = Tk()
side=350
pad=100
cnv = Canvas(root, width=side, height=side, bg="black")
cnv.pack(padx=pad, pady=pad)

def go_in(event):
    cnv['bg']="pink"

def go_out(event):
    cnv['bg']="royal blue"

cnv.bind("<Enter>", go_in)
cnv.bind("<Leave>", go_out)

root.mainloop()