import sys, pygame, os, random, time, math, anima as e
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

def flip(img,boolean=True):
    return pygame.transform.flip(img,boolean,False)

hodiny = pygame.time.Clock()
pygame.init()
pygame.display.set_caption("FNASPS")

txKm = pygame.font.Font(pygame.font.get_default_font(), 18)
mensi_text_font = pygame.font.Font(pygame.font.get_default_font(), 24)
text_font = pygame.font.SysFont('lucida_sans_typewriter', 36) #tahoma
vetsi_text_font = pygame.font.SysFont('lucida_sans_typewriter', 72) #orc_a papyrus stencil
def textik(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

Sn = pygame.image.load('MainMenu/real.png')
St = pygame.image.load('MainMenu/static.png')
St1 = pygame.image.load('MainMenu/static1.png')
Sp = pygame.image.load('MainMenu/sipecka.png')
Tx = pygame.image.load('MainMenu/text.png')
KLKM = pygame.image.load('MainMenu/Spsmap.png')
Ikonka = pygame.image.load('MainMenu/icon.png')
ImgPG = pygame.image.load('MainMenu/pg.png')
ImgPC = pygame.image.load('MainMenu/pcfr.png')

Novi = pygame.image.load('MainMenu/noviny.png')
Et = pygame.image.load('MainMenu/entr.png')

OF = pygame.image.load('MainMenu/G1.png')

Ckamka0 = pygame.image.load('MainMenu/K0.png')
Ckamka1 = pygame.image.load('MainMenu/K1.png')
Ckamka2 = pygame.image.load('MainMenu/K2.png')
Ckamka3 = pygame.image.load('MainMenu/K3.png')
Ckamka4 = pygame.image.load('MainMenu/G1.png')
Ckamka5 = pygame.image.load('MainMenu/K5.png')
Ckamka6 = pygame.image.load('MainMenu/G1.png')
Ckamka7 = pygame.image.load('MainMenu/G1.png')
Ckamka8 = pygame.image.load('MainMenu/G1.png')
Ckamka9 = pygame.image.load('MainMenu/K9.png')
Ckamka10 = pygame.image.load('MainMenu/G1.png')
Ckamka = [Ckamka0,Ckamka1,Ckamka2,Ckamka3,Ckamka4,Ckamka5,Ckamka6,Ckamka7,Ckamka8,Ckamka9,Ckamka10]

Br9 = pygame.image.load('MainMenu/pg.png')
Br5 = pygame.image.load('MainMenu/pg.png')
Br8 = pygame.image.load('MainMenu/pg.png')
Br7 = pygame.image.load('MainMenu/pg.png')
Br6 = pygame.image.load('MainMenu/pg.png')

BtKm = pygame.image.load('MainMenu/KmBt.png')
#screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
# ----------------------------------- #
OknoSirka = 1680 #2480
OknoVyska = 1000
Okno_velikost = (OknoSirka,OknoVyska)
screen = pygame.display.set_mode(Okno_velikost,0,32)

display = pygame.Surface((300,200)) 

pygame.display.set_icon(Ikonka)

KameStat = pygame.image.load('MainMenu/static.gif')
KameStat = pygame.transform.scale(KameStat, (OknoSirka, OknoVyska))

#Kolikátá noc
PNoc = 0
#Pro správné počítaní délky noci
rozdil = 0

nahoru = False
dolu = False
MenuBool = True
IntermiseBool = False
GameBool = False
#Bude vráceno animatroniky
GameOver = False
Win = False
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
            Vteriny = pygame.time.get_ticks() / 1000
            mx, my = pygame.mouse.get_pos()
            jump_allowed = True
            jump_timer = pygame.event.custom_type()
            bg_ano = True
            bg_timer = pygame.event.custom_type()
            screen.fill((0,0,0))

            #Důvody epilepsie
            if Vteriny % 2 > 0.05 :
                Sq = St1
            else:
                Sq = St

            if stage_sipecky != 0:
                sipecky_Y = 758
            else:
                sipecky_Y = 648
            
            #print(my)
            #B1 = pygame.draw.rect(screen, (255,0,0), [130, 620, 500, 100], -1)
            #B2 = pygame.draw.rect(screen, (255,0,0), [130, 730, 500, 100], -1)
            B1 = Rect(130, 620, 500, 100)
            B2 = Rect(130, 730, 500, 100)
            if B1.collidepoint((mx, my)):
                stage_sipecky = 0
            elif B2.collidepoint((mx, my)):
                stage_sipecky = 1
            
            if klik:
                MenuBool = False
                IntermiseBool = True
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
                        #Zatím to samé
                        MenuBool = False
                        IntermiseBool = True
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
            else:
                Sw = St

            screen.blit(Tx, (220, 150))
            screen.blit(Sp, (sipecky_X,sipecky_Y))
            #screen.blit(Tx1, (20, OknoVyska - 100))
            #screen.blit(Tx2, (OknoSirka - 350, OknoVyska - 100))
            textik("V 0.01", text_font, (255,255,255), 60, OknoVyska - 100)
            textik("©️ Patron Service, Poland", text_font, (255,255,255), OknoSirka - 650, OknoVyska - 100)  
            pygame.display.update()
            hodiny.tick(60)


    # -------- Noviny na začítku hry -------- #
    if IntermiseBool:
        if PNoc == 0:
            rozdil = pygame.time.get_ticks() / 1000
            alpha = 0
            klik = False
            running = True
            while running:
                #Průhlednost
                alpha = round((pygame.time.get_ticks() / 8) - rozdil)
                if alpha < 256:
                    Novi.set_alpha(alpha)
                screen.fill((0,0,0))
                screen.blit(Novi, (0,0))
                screen.blit(Et, (OknoSirka - 250, OknoVyska - 150))
                if klik:
                    GameBool = True
                    IntermiseBool = False
                    running = False
                    PNoc = 1
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
                            #Zatím to samé
                            IntermiseBool = False
                            GameBool = True
                            running = False
                            PNoc = 1

                pygame.display.update()
                hodiny.tick(60)
        else:
            IntermiseBool = False
            GameBool = True 
                
    # -------- Hlavní traktor --------- #
    if GameBool:
        rozdil = pygame.time.get_ticks() / 1000
        #Mění se
        xt = "0"
        dX = -100
        #Kamera delay
        Mediator = 0
        PrepMaediator = 0
        #Světla
        BoolLL = False
        BoolRL = False
        BoolLD = False
        BoolRD = False
        BoolPG = True
        klik = False
    
        
        BoolSWKamera = False
        #Logika rozmístění a přepínání kamer
        MPoz = OknoVyska - 540 #530
        xList = [(540,MPoz), "ŘE", (440,MPoz + 120), "SCHO", (160, MPoz + 140), "HW1B", (200,MPoz), "KAB", (540,MPoz + 80), "SEK1", (340,MPoz + 140), "HW1A", (80,MPoz + 280), "T17B", (210,MPoz +280), "T17A", (360,MPoz + 280), "T16", (410,MPoz + 370), "T15", (490, MPoz + 270), "SEK2"]#MainDoor MainHallway
        KmLt, tett = KmFnce()
        kamka = 0
        strtVteriny = 0
        Minu = 0
        BoolKm = False
        running = True
        kameY = 0
        Rano = 12
        #Procenta
        Proc = 100
        #9 5 8 7 6
        balding = e.animatronik([9,5,8,7,6,0])
        bald = 0
        #hugerCat = e.animatronik(11, 11, 8000,False,)
        #flaska = e.animatronik(  11, 11, 8000,False,)
        #zakar = e.animatronik(   11, 11, 8000,False,)
        while running:
            if GameOver:
                Win = True
                running = False
                GameBool = False
            rect = Rect(mx, my, 1, 1)
            mx, my = pygame.mouse.get_pos()
            screen.fill((0,0,0))
            Vteriny = round((pygame.time.get_ticks() / 1000) - rozdil)
            strtVteriny = Vteriny - 60 * Minu
            
            Rano = Vteriny // 45
            if Rano < 1:
                Rano = 12
            elif Rano >= 6:
                Win = True
                running = False
                GameBool = False

            if strtVteriny < 10:
                xt = "0"
            elif strtVteriny >= 60:
                Minu += 1
            else:
                xt = ""

            #Rect/hitboxy kamery (mimo kvůli vypínání a zapínání kamery
            KM = Rect(350, OknoVyska - 140, OknoSirka-700, 100)
            #KM = pygame.draw.rect(screen, (0,0,255), [350, OknoVyska - 100, OknoSirka-700, 100], 4)
            if not BoolKm:
                screen.blit(OF, (dX - 210,0))
                #Rect/hitboxy tlačítek
                LL = pygame.draw.rect(screen, (255,0,0), [dX + 20, 400, 50, 70], 0)
                LD = pygame.draw.rect(screen, (255,0,0), [dX + 20, 490, 50, 70], 0)
                RL = pygame.draw.rect(screen, (255,0,0), [dX + OknoSirka - 20, 400, 50, 70], 0)
                RD = pygame.draw.rect(screen, (255,0,0), [dX + OknoSirka - 20, 490, 50, 70], 0)
                
                #Rect/hitboxy otáčení
                #LS = pygame.draw.rect(screen, (0,0,255), [0, 0, 200, OknoVyska], 4)
                #PS = pygame.draw.rect(screen, (0,0,255), [OknoSirka - 200, 0, 200, OknoVyska], 4)
                LS = Rect(0, 0, 200, OknoVyska)
                PS = Rect(OknoSirka - 200, 0, 200, OknoVyska)
            
                if PS.collidepoint((mx, my)) and dX >= -200:
                    dX -= 10
                elif LS.collidepoint((mx, my)) and dX <= 200:
                    dX += 10
                    
                #Dalo by se dát and místo více if, né když stačí ale ověřit jednu proměnnou
                if klik:
                    if LL.collidepoint((mx, my)):
                        BoolLL = not BoolLL
                    elif RL.collidepoint((mx, my)):
                        BoolRL = not BoolRL
                    elif LD.collidepoint((mx,my)):
                        BoolLD = not BoolLD
                    elif RD.collidepoint((mx,my)):
                        BoolRD = not BoolRD
                
                if BoolLL == True:
                    SvetloL = pygame.draw.rect(screen, (255,255,255), [dX + 100, 200, 200, 600], 0)
                if BoolLD == True:
                    DoorL = pygame.draw.rect(screen, (255,0,0), [dX + 100, 200, 200, 600], 0)
                if BoolRL == True:
                    SvetloR = pygame.draw.rect(screen, (255,255,255), [dX + OknoSirka - 250, 200, 200, 600], 0)
                if BoolRD == True:
                    DoorR = pygame.draw.rect(screen, (255,0,0), [dX + OknoSirka - 250, 200, 200, 600], 0)
                    
                    
                    
            # -------- Na kameře -------- #
            else:
                #Vykreslení záznamu kamery live WOWOWOWOWO
                screen.blit(Ckamka[kamka], (0,0))
                
              #  if Br + jmpsc = 
                
                
                if BoolPG:
                    #Phone Guy
                    screen.blit(ImgPG, (OknoSirka - 400, OknoVyska - 300))
                    PG = Rect([1460, 820, 70, 60])
                    if rect.colliderect(PG) and klik:
                        BoolPG = False
                    #1680
                            
                if (Vteriny - PrepMaediator) < 0.5:
                    screen.blit(KameStat, (0,0))
                else:
                    screen.blit(KLKM, (100,MPoz))                
                    for r in KmLt:
                        if rect.colliderect(r) and klik and BoolSWKamera == False and kamka != KmLt.index(r):
                            kamka = KmLt.index(r)
                            #Ckamka = Ckamka + str(kamka)
                            print(kamka)
                            PrepMaediator = Vteriny
                        elif kamka == KmLt.index(r):
                            pygame.draw.rect(screen, (140,140,140), r, 0)
                            pygame.draw.rect(screen, (150,200,255), r, 5)
                        else:
                            #pygame.draw.rect(screen, (20,20,20), r, 0)
                            pygame.draw.rect(screen, (10,10,10), r, 0)
                            pygame.draw.rect(screen, (150,200,255), r, 5)
                    
                    op = 0
                    for t in tett:
                        if tett.index(t) % 2 == 0:
                            op += 1
                            l = t
                        else:
                            op += 1
                            o = str(t)
                        if op == 2:
                            op = 0
                            textik(o, txKm, (255,255,255), l[0]+5, l[1]+8)
                    
                screen.blit(ImgPC, (0,kameY))
                
            screen.blit(BtKm, (350, OknoVyska - 140))
            textik(str(Rano) + "AM", vetsi_text_font, (255,255,255), OknoSirka - 250, 40)
            textik(str(Minu) + ":" + xt + str(strtVteriny), mensi_text_font, (200,200,200), OknoSirka - 140, 120)
            textik("Noc " + str(PNoc), text_font, (255,255,255), OknoSirka - 200, 160)
            textik("Energie:" + str(Proc) + "%", text_font, (255,255,255), 60, 60)  
            textik("Využití: nemá lol", mensi_text_font, (255,255,255), 60, 120)
            
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
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        bald += 1
                        jumpsc = balding.pohyb(bald, BoolRD)
                        print(jumpsc)
                        
                        
            pygame.display.update()
            hodiny.tick(60)
        
    # -------- Noviny na začítku hry -------- #
    if Win:
        klik = False
        PNoc += 1
        running = True
        while running:
            #Průhlednost
            screen.fill((0,0,0))
            textik("6 AM!!!!!!!!!!!!!!!", vetsi_text_font, (255,255,255), OknoSirka/2 - 200, OknoVyska /2)
            if klik:
                GameBool = True
                Win = False
                running = False
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
                        #Zatím to samé
                        Win = False
                        GameBool = True
                        running = False
                        PNoc = 1

                pygame.display.update()
                hodiny.tick(60)
        else:
            IntermiseBool = False
            GameBool = True 
    screen.blit(pygame.transform.scale(display,Okno_velikost),(0,0))
