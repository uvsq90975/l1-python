from tkinter import *

WIDTH=800
HEIGHT=800
COTE=40

root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, background="ivory")
cnv.pack()

DIR={'Left':(-1,0),'Right':(1,0),'Up':(0,-1),'Down':(0,1)}

def bouge(event):
    key=event.keysym
    dx, dy=DIR[key]
    a,b, segment=pile[-1]
    if len(pile)>=2 and a+dx==pile[-2][0] and b+dy==pile[-2][1] :
            pile.pop()
            print("back")
            cnv.delete(segment)
    else:
        segment=cnv.create_line(a*COTE+COTE//2, b*COTE+COTE//2,
                                a*COTE+COTE//2+dx*COTE,
                                b*COTE+COTE//2+dy*COTE,
                                fill='blue', width=4, capstyle=ROUND)
        pile.append([a+dx, b+dy, segment])

    cnv.move("perso", dx*COTE, dy*COTE)

perso=cnv.create_rectangle(0, 0,COTE, COTE, fill="blue",
                           outline='', tag='perso')
pile=[(0,0, perso)]

for key in ["<Left>", "<Right>", "<Up>", "<Down>"]:
    root.bind(key, bouge)

root.mainloop()

