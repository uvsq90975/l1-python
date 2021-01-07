from tkinter import Tk, Canvas

root = Tk()
cnv = Canvas(root, width=200, height=200)
cnv.pack()

cnv.create_rectangle(50, 50, 150, 150, fill='gray')

def mouvement(event):
    if 50< event.x <150 and 50< event.y <150:
        print("INside")
    else:
        print("OUTside")

cnv.bind("<Motion>",mouvement)

root.mainloop()