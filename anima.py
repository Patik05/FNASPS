import math, pygame, os
from pygame.locals import *

class animatronik(object):
    def __init__(self, c):
        #self.dostupnost = ex
        self.cesta = c
        self.pozice = self.cesta[0]
        self.start_pozice = self.cesta[0]
    def pohyb(self, pozica, muzeDovnitr):
        if pozica + 1 <= len(self.cesta):
            pozica = self.cesta[pozica]
            #print(len(self.cesta))
            #print (pozica)
        else:
            pozica = 0
        return pozica
        
def flip(img,boolean=True):
    return pygame.transform.flip(img,boolean,False)
