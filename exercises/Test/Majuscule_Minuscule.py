from tkinter import Tk, Canvas

root = Tk()
cnv = Canvas(root, width=400, height=100, bg="ivory")
cnv.pack()
cnv.focus_set()
x=0

def texte(event):
    global x
    cnv.create_text(x, 40, text =event.keysym, font="Arial 50 bold")
    x+=30

cnv.bind('<Key-a>', texte)
cnv.bind('<Key-B>', texte)

root.mainloop()