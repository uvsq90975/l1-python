from tkinter import *

root = Tk()
cnv = Canvas(root, width=300, height=300, bg="ivory")
cnv.pack()

def clic(event):
    x, y = event.x, event.y
    print(x, y)
    cnv.create_oval(x-3, y-3, x+3, y+3,
                    fill='red', outline='')

cnv.bind("<Button-1>", clic)
root.mainloop()