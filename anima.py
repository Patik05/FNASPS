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
        
        
        
    
#Z mého minulého projektíku
class PhysicsObject(object):
    def __init__(self,x,y,w,h):
        self.width = w
        self.height = h
        self.rect = pygame.Rect(x,y,self.width,self.height)
    def Move(self,Movement,platforms):
        collisions = [False,False,False,False]
        self.rect.x += [0]
        block_hit_list = CollisionTest(self.rect,platforms)
        for block in block_hit_list:
            if Movement[0] > 0:
                collisions[2] = True
                self.rect.right = block.left
            elif Movement[0] < 0:
                collisions[3] = True
                self.rect.left = block.right
        self.rect.y += Movement[1]
        block_hit_list = CollisionTest(self.rect,platforms)
        for block in block_hit_list:
            if Movement[1] > 0:
                collisions[0] = True
                self.rect.bottom = block.top
            elif Movement[1] < 0:
                collisions[1] = True
                self.rect.top = block.bottom
            self.change_y = 0
        return collisions
    def Draw(self):
        pygame.draw.rect(screen,(0,0,255),self.rect)
    def CollisionItem(self):
        CollisionInfo = [self.rect.x,self.rect.y,self.width,self.height]
        return CollisionInfo

def flip(img,boolean=True):
    return pygame.transform.flip(img,boolean,False)
