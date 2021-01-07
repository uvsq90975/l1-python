from tkinter import *

WIDTH = 800
HEIGHT = 500

root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()
cnv.focus_set()

SIDE = 30
UNIT = 2

rect = cnv.create_rectangle(
    (WIDTH / 2 - SIDE / 2, HEIGHT / 2 - SIDE / 2),
    (WIDTH / 2 + SIDE / 2, HEIGHT / 2 + SIDE / 2),
    fill="black",
)


def handler():
    unit = UNIT

    if sum(keys.values()) > 1:
        unit = UNIT/1.5

    for key in drn:
        if keys[key]:
            if key == "Up":
                cnv.move(rect, 0, -unit)
            elif key == "Right":
                cnv.move(rect, unit, 0)
            elif key == "Left":
                cnv.move(rect, -unit, 0)
            elif key == "Down":
                cnv.move(rect, 0, unit)

    root.after(20, handler)


def press(event):
    keys[event.keysym] = True


def release(event):
    keys[event.keysym] = False


drn = ["Up", "Right", "Left", "Down"]
keys = dict.fromkeys(drn, False)

for key in drn:
    cnv.bind("<KeyPress-%s>" % key, press)
    cnv.bind("<KeyRelease-%s>" % key, release)

handler()

root.mainloop()