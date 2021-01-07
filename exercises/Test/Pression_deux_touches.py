from tkinter import *
from time import time

root = Tk()

def press(event):
    print("press:", event.keysym, time())

def release(event):
    print("release:", event.keysym, time())

for key in ["a", "z"]:
    root.bind('<KeyPress-%s>' %key, press)
    root.bind('<KeyRelease-%s>' %key, release)

root.mainloop()