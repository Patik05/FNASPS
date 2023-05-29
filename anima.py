import math, pygame, os, random
from pygame.locals import *

class animatronik(object):
    def __init__(self, c):
        #self.dostupnost = ex
        self.cesta = c
        self.pozice = self.cesta[0]
        self.start_pozice = 1
    def pohyb(self, pozica, NemuzeDovnitr, bjump):
        bald = pozica
        aaaa = random.choice([0, 1])
        bbbb = random.choice([0, 1])
        if pozica + 1 <= len(self.cesta):
            if aaaa == 0:
                if bbbb == 0:
                    pozica = self.cesta[pozica]
            else:
                bald -= 1
                pozica = self.cesta[pozica]
        elif NemuzeDovnitr:
            bald = 1
            pozica = self.cesta[self.start_pozice] 
        else:
            pozica = 100
            bald = 100
        return pozica, bald
    def naZpatek(self, pozica):
        pozica = self.cesta[1]
        return pozica
        
def flip(img,boolean=True):
    return pygame.transform.flip(img,boolean,False)
