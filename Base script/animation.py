from tkinter import *
from random import randint
class Anim_pluie(Tk):

    def __init__(self, w=500, h=500, r=20, grav=0.5, frot=0.95):
        super().__init__()
        (self.w, self.h) = (w, h)
        (self.x, self.y) = (w/2, h/4)
        self.canvas = Canvas(self, width=w, height=h, bg='#B0C4DE')
        self.canvas.pack()
        self.animation()

    def animation(self):
        if not self.fini():
            self.dessiner()
            self.suivant()
            self.after(30, self.animation)
            
    def dessiner(self):
        pass

    def suivant(self):
        pass

    def fini(self):
        return False
            
if __name__ == '__main__':
    ROOT = Anim_pluie()
    ROOT.mainloop()
