from tkinter import *
from random import randint
class Anim_pluie(Tk):

    def __init__(self, w=500, h=500, r=20, grav=0.5, frot=0.95):
        super().__init__()
        (self.w, self.h) = (w, h)
        (self.x, self.y) = (w/2, h/4)
        self.gouttes = []
        self.canvas = Canvas(self, width=w, height=h, bg='#B0C4DE')
        self.canvas.pack()
        self.animation()

    def animation(self):
        if not self.fini():
            self.dessiner()
            self.suivant()
            self.after(30, self.animation)
    # un cercle (x,y,r)
    def dessiner(self):
        self.canvas.delete(ALL)
        for x,y,r,rmax in self.gouttes:
            self.canvas.create_oval(x-r, y-r, r+x, y+r, outline='#1E90FF')

    def suivant(self):
        particules = []
        for x,y,r,rmax in self.gouttes:
            if r > rmax:
                continue
            else:
                particules.append((x,y,r+1,rmax))
        particules.append((randint(0, self.w), randint(0, self.h), randint(0,10),randint(3,25)))
        particules.append((randint(0, self.w), randint(0, self.h), randint(0,10),randint(3,25)))
        particules.append((randint(0, self.w), randint(0, self.h), randint(0, 10), randint(3, 25)))
        particules.append((randint(0, self.w), randint(0, self.h), randint(0, 10), randint(3, 25)))
        particules.append((randint(0, self.w), randint(0, self.h), randint(0, 10), randint(3, 25)))
        self.gouttes = particules

    def fini(self):
        return False
            
if __name__ == '__main__':
    ROOT = Anim_pluie()
    ROOT.mainloop()
