from tkinter import Tk, Canvas

root = Tk()

def press(event):
    print("press:", event.keysym)

def release(event):
    print("release:", event.keysym)

root.bind('<KeyPress>', press)
root.bind('<KeyRelease>', release)
root.mainloop()