from tkinter import Tk, Canvas

root = Tk()
cnv = Canvas(root, width=300, height=200)
cnv.pack()

rect=cnv.create_rectangle(30, 30, 130, 130, fill="red", outline='')

old=[None, None]

def clic(event):
    old[0]=event.x
    old[1]=event.y

def glisser(event):
    cnv.move(rect, event.x-old[0], event.y-old[1])
    old[0]=event.x
    old[1]=event.y


cnv.bind("<B1-Motion>",glisser)
cnv.bind("<Button-1>",clic)

root.mainloop()