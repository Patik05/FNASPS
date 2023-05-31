import pygame, sys, pygame, os
from pygame.locals import *
from random import randint

width = 800
height = 1050

#xList = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
MPoz = 1050 - 520 #530
xList = [(540,MPoz), "ŘE", (440,MPoz + 120), "SCHO", (160, MPoz + 140), "HW1B", (200,MPoz), "KAB", (540,MPoz + 80), "SEK1", (340,MPoz + 140), "HW1A", (80,MPoz + 280), "T17B", (210,MPoz +280), "T17A", (360,MPoz + 280), "T16", (410,MPoz + 370), "T15", (490, MPoz + 270), "SEK2"]#MainDoor MainHallway

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

KLKM = pygame.image.load('MainMenu/Spsmap.png')

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

xxxx = 300
deme = False
keke = False
cunter = 0

rects, tett = random_rects()
while running:
    mx, my = pygame.mouse.get_pos()
    rect = Rect(mx, my, 1, 1)
                
    screen.fill((0, 0, 0))
    
    Vteriny = round((pygame.time.get_ticks() / 1000))     
    klik = False
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                klik = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                xxxx += 30
            elif event.key == pygame.K_DOWN:
                xxxx -= 30
        if pygame.mouse.get_pressed()[0]:
            try:
                keke = True
            except AttributeError:
                pass
        else:
            keke = False    
    
    if Vteriny % 2 == 0 and not deme:
        xxxx -= 30
        deme = True
    elif Vteriny % 2 != 0 and deme and cunter <= 0:
        deme =  False
    sssss = pygame.draw.rect(screen, (100,100,100), [110, MPoz - 120, 300, 100], 0)
    sussy = pygame.draw.rect(screen, (255,255,255), [110, MPoz - 120, xxxx, 100], 0)
    
    cunter -= 2
    
    if (rect.colliderect(sssss) or rect.colliderect(sussy)) and keke and xxxx < 300 and cunter <= 0:
        cunter = 500
        xxxx += 30
        
    pygame.display.flip()
pygame.quit()
