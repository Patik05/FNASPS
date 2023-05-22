import pygame, sys, pygame, os
from pygame.locals import *
from random import randint

width = 800
height = 1050

#xList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
xList = [(300,560), "MD", (380,620), "MH", (140, 640), "2A", (180,700), "T5", (510,640), "T15", (160,790), "T2", (260,870), "HW1B", (260,820), "HW1A", (360,870), "HW2B", (360,820), "HW2A", (510, 750), "T16"]
#MainDoor MainHallway

def random_rects():
    rects = []
    tett = []
    for t in xList:
        #print(str(xList.index(t)))
        #w = textik(str(xList.index(t)), mensi_text_font, (255,255,255), t, t)
        if xList.index(t) % 2 == 0:
            r = t
            tett.append(r)
            r = Rect(t, (70, 48))
            rects.append(r)
        else:
            r = t
            tett.append(r)
    return rects, tett


pygame.init()
screen = pygame.display.set_mode((width, height))

mensi_text_font = pygame.font.Font(pygame.font.get_default_font(), 18)
def textik(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    #print(x,y)
    #print(x)
    screen.blit(img, (x,y))

running = True
kamka = 0
j = 0
op = 0
rects, tett = random_rects()
while running:

    mx, my = pygame.mouse.get_pos()
    rect = Rect(mx, my, 1, 1)
    klik = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                klik = True
    screen.fill((0, 0, 0))
    MpKm = pygame.draw.rect(screen, (255,255,255), [100, 1050 - 500, 500, 400], 2)
    #pygame.draw.rect(screen, (0,255,0), rect, 1)

    for r in rects:
        if kamka == rects.index(r):
            pygame.draw.rect(screen, (140,140,140), r, 0)
        if rect.colliderect(r) and klik:
            pygame.draw.rect(screen, (255,0,0), r, 5)
            kamka = rects.index(r)
        else:
            pygame.draw.rect(screen, (255,255,255), r, 3)
    
    for t in tett:
        if tett.index(t) % 2 == 0:
            op += 1
            l = t
        else:
            op += 1
            o = str(t)
        if op == 2:
            op = 0
            textik(o, mensi_text_font, (255,255,255), l[0]+5, l[1]+8)
            
    pygame.display.flip()
pygame.quit()
