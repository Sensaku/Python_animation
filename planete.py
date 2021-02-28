from tkinter import *
from random import randint
from math import cos,sin


class Anim_pluie(Tk):

    def __init__(self, w=500, h=500, r=20, grav=0.5, frot=0.95):
        super().__init__()
        (self.w, self.h) = (w, h)
        (self.x, self.y) = (w / 2, h / 4)
        self.canvas = Canvas(self, width=w, height=h, bg='#000000')
        self.planet = (w/2, h/2, 50)
        px, py, pr = self.planet
        self.lune = (100,20)
        ld, lr = self.lune
        self.angle = 0
        self.canvas.pack()
        self.canvas.create_oval(px - pr, py - pr, px + pr, py + pr, fill="blue", outline="white")
        self.id_lune = self.canvas.create_oval(
            px - lr,
            py - lr,
            px + lr,
            py + lr,
            fill="grey"
        )
        self.animation()

    def animation(self):
        if not self.fini():
            self.dessiner()
            self.suivant()
            self.after(30, self.animation)

    # un cercle (x,y,r)
    def dessiner(self):
        if(self.id_lune != 0):
            #self.canvas.delete(self.id_lune)
            print(self.id_lune)
        px,py,pr = self.planet
        ld, lr = self.lune
        self.canvas.moveto(self.id_lune, px-lr + ld * cos(self.angle), py-lr + ld * sin(self.angle))
        self.canvas.place()



    def suivant(self):
        self.angle += 0.05

    def fini(self):
        return False


if __name__ == '__main__':
    ROOT = Anim_pluie()
    ROOT.mainloop()
