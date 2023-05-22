import sys, pygame, os, random, time
import math
from pygame import *

def terminace():
    pygame.quit()
    sys.exit()

def KmFnce():
    KmLt = []
    tett = []
    for t in xList:
        #print(str(xList.index(t)))
        #w = textik(str(xList.index(t)), mensi_text_font, (255,255,255), t, t)
        #Pro lokaci
        if xList.index(t) % 2 == 0:
            r = t
            tett.append(r)
            r = Rect(t, (70, 48))
            KmLt.append(r)
        #Pro text
        else:
            r = t
            tett.append(r)
    return KmLt, tett

hodiny = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("FNASPS")

mensi_text_font = pygame.font.Font(pygame.font.get_default_font(), 18)
def textik(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

MnSc = pygame.image.load('MainMenu/BackGrnd.png')
Sn = pygame.image.load('MainMenu/real.png')
St = pygame.image.load('MainMenu/static.png')
St1 = pygame.image.load('MainMenu/static1.png')
Sp = pygame.image.load('MainMenu/sipecka.png')
#Fonty tu nejsou kvůli potřebě toto zabalit do .exe souboru (dělalo to problémy)
#Tedy alespoň to main menu
Tx = pygame.image.load('MainMenu/text.png')
Tx1 = pygame.image.load('MainMenu/text1.png')
Tx2 = pygame.image.load('MainMenu/text2.png')

Ikonka = pygame.image.load('MainMenu/icon.png')
# ----------------------------------- #
OknoSirka = 1680
OknoVyska = 1000
Okno_velikost = (OknoSirka,OknoVyska)
screen = pygame.display.set_mode(Okno_velikost,0,32)

display = pygame.Surface((300,200)) 

pygame.display.set_icon(Ikonka)

Pocatek = pygame.time.get_ticks()
CasPozadi = 0

nahoru = False
dolu = False
MenuBool = True
IntermiseBool = False
GameBool = False

sipecky_X = 120
sipecky_Y = 630

# -------Main Game------- #
while True:  
    # -------- Mimo, ať se neplete -------- #
    if MenuBool:
        #----- Hlavní Menu ----- #
        stage_sipecky = 0
        Sq = ""
        Sw = St
        klik = False
        running = True
        while running:
            mx, my = pygame.mouse.get_pos()
            Vteriny = (pygame.time.get_ticks()) / 1000
            jump_allowed = True
            jump_timer = pygame.event.custom_type()
            bg_ano = True
            bg_timer = pygame.event.custom_type()
            bg_ms = 800
            millisecond = 200
            loops = 1
            screen.blit(MnSc, (0,0))
            
            #print(Vteriny % 0.1)
            if Vteriny % 2 > 0.05 :
                Sq = St1
            else:
                Sq = St

            if stage_sipecky != 0:
                sipecky_Y = 758
            else:
                sipecky_Y = 648
            
            #print(my)
            B1 = pygame.draw.rect(screen, (255,0,0), [130, 620, 500, 100], 0)
            B2 = pygame.draw.rect(screen, (255,0,0), [130, 730, 500, 100], 0)
            if B1.collidepoint((mx, my)):
                stage_sipecky = 0
            if B2.collidepoint((mx, my)):
                stage_sipecky = 1
            
            if klik:
                MenuBool = False
                GameBool = True
                running = False
           
            klik = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminace()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        klik = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminace()
                    if event.key == pygame.K_RETURN:
                        # ------- Zatím to samé ------- #
                        if stage_sipecky == 0:
                            MenuBool = False
                            GameBool = True
                            running = False
                        else:
                            MenuBool = False
                            GameBool = True
                            running = False
                            
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        if stage_sipecky == 0:
                            stage_sipecky = 1
                        else:
                            stage_sipecky = 0                      
                    
            screen.blit(Sn, (OknoSirka / 2,0))
            screen.blit(Sw, (0,0))
            screen.blit(Sq, (0,0))
            
            # -------- Pro epilepsii -------- #
            if Sw == St:
                jump_allowed = False
                Sw = St1
                pygame.time.set_timer(jump_timer, millisecond, loops)
            else:
                Sw = St

            screen.blit(Tx, (220, 150))
            screen.blit(Sp, (sipecky_X,sipecky_Y))
            screen.blit(Tx1, (20, OknoVyska - 100))
            screen.blit(Tx2, (OknoSirka - 350, OknoVyska - 100))
            pygame.display.update()
            hodiny.tick(60)


    # -------- Noviny na začítku hry -------- #
    if IntermiseBool:
        running = True
        while running:
            screen.blit(MnSc, (0,0))
            pygame.display.update()
            hodiny.tick(60)
                
    # -------- Hlavní traktor --------- #
    if GameBool:
        #Mění se
        dX = 0
        #Kamera delay
        Mediator = 0
        #Světla
        BoolLL = False
        BoolRL = False
        BoolLD = False
        BoolRD = False
        klik = False
        #Logika rozmístění a přepínání kamer
        #xList = [(200,10), (240,40), (100, 80), (140,160), (300,120), (120,210), (180,240), (180,270), (260,240), (260,270), (310, 190)]
        MPoz = OknoVyska - 520 #530
        xList = [(300,MPoz+10), "MD", (380,MPoz + 30), "MH", (140, MPoz + 100), "2A", (180,700), "T5", (510,MPoz + 80), "T15", (160,MPoz + 160), "T2", (260,MPoz + 300), "HW1B", (260,MPoz +250), "HW1A", (360,MPoz + 300), "HW2B", (360,MPoz + 250), "HW2A", (510, MPoz + 180), "T16"]
        #MpKm = ([100, OknoVyska - 500, 500, 400])
        KmList = KmFnce()
        j = 0
        op = 0
        KmLt, tett = KmFnce()
        kamka = 0
        #Procenta
        #Taky si říkám
        
        BoolKm = False
        running = True
        while running:
            Proc = 100
            TxProc = str(Proc) + "%"
            rect = Rect(mx, my, 1, 1)
            screen.blit(MnSc, (0,0))
            mx, my = pygame.mouse.get_pos()
            Vteriny = (pygame.time.get_ticks()) / 1000
            #Rect/hitboxy kamery (mimo kvůli vypínání a zapínání kamery
            KM = pygame.draw.rect(screen, (0,0,255), [200, OknoVyska - 100, OknoSirka-400, 100], 4)
            if not BoolKm:
                #Rect/hitboxy tlačítek
                LL = pygame.draw.rect(screen, (255,0,0), [dX, 400, 50, 70], 0)
                LD = pygame.draw.rect(screen, (255,0,0), [dX, 490, 50, 70], 0)
                RL = pygame.draw.rect(screen, (255,0,0), [dX + OknoSirka - 50, 400, 50, 70], 0)
                RD = pygame.draw.rect(screen, (255,0,0), [dX + OknoSirka - 50, 490, 50, 70], 0)
                
                #Rect/hitboxy otáčení
                LS = pygame.draw.rect(screen, (0,0,255), [0, 0, 200, OknoVyska], 4)
                PS = pygame.draw.rect(screen, (0,0,255), [OknoSirka - 200, 0, 200, OknoVyska], 4)
                LS = Rect(0, 0, 200, OknoVyska)
                PS = Rect(OknoSirka - 200, 0, 200, OknoVyska)

                #Phone Guy
                PG = pygame.draw.rect(screen, (0,0,255), [300, 50, 200, 70], 4)
                
                if PS.collidepoint((mx, my)) and dX >= -100:
                    dX -= 10
                elif LS.collidepoint((mx, my)) and dX <= 100:
                    dX += 10
                    
                #Dalo by se dát and místo více if, né když stačí ale ověřit jednu proměnnou
                if klik:
                    if LL.collidepoint((mx, my)):
                        if not BoolLL:
                            BoolLL = True
                        else:
                            BoolLL = False
                    elif RL.collidepoint((mx, my)):
                        if not BoolRL:
                            BoolRL = True
                        else:
                            BoolRL = False
                    elif LD.collidepoint((mx,my)):
                        if not BoolLD:
                            BoolLD = True
                        else:
                            BoolLD = False
                    elif RD.collidepoint((mx,my)):
                        if not BoolRD:
                            BoolRD = True
                        else:
                            BoolRD = False
                
                if BoolLL == True:
                    SvetloL = pygame.draw.rect(screen, (255,255,255), [dX + 100, 200, 200, 600], 0)
                if BoolRL == True:
                    SvetloR = pygame.draw.rect(screen, (255,255,255), [dX + OknoSirka - 300, 200, 200, 600], 0)        
            # -------- Na kameře -------- #
            else:
                MpKm = pygame.draw.rect(screen, (255,255,255), [100, MPoz, 500, 400], 2)
                #Km = pygame.draw.rect(screen, (255,255,255), [100, OknoVyska - 800, 100, 50], 2)
                #tett
                #KmLt
                for r in KmLt:
                    if kamka == KmLt.index(r):
                        pygame.draw.rect(screen, (140,140,140), r, 0)
                    if rect.colliderect(r) and klik:
                        pygame.draw.rect(screen, (255,0,0), r, 5)
                        kamka = KmLt.index(r)
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
                    #print(Vteriny - Mediator)
                    
                    
            # ------- Delay pro kameru -------- #
            if klik and (Vteriny - Mediator) > 0.4:
                if KM.collidepoint((mx,my)):
                    if not BoolKm:
                        #Nastaví čas pro Mediator stejně jako celkové vteřiny
                        #Ale nezmění se, dokud nebudou funkce nahoře splněny
                        Mediator = Vteriny
                        BoolKm = True
                    else:
                        Mediator = Vteriny
                        BoolKm = False
            
            
            klik = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminace()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        klik = True
                if event.type == KEYDOWN: #Když držíme klávesu
                    if event.key == K_ESCAPE:
                        terminace()
                        
                        
            pygame.display.update()
            hodiny.tick(60)
        
    screen.blit(pygame.transform.scale(display,Okno_velikost),(0,0))
    pygame.display.update()
    hodiny.tick(60)
