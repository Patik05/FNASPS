import sys, pygame,anima as e
from pygame import *

def terminace():
    pygame.quit()
    sys.exit()

def audio(p, bo):
    pygame.mixer.init()
    pygame.mixer.music.load(p)
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play()
    pygame.mixer.music.unpause()
    bo = False
    return bo

def KmFnce():
    KmLt = []
    tett = []
    for t in xList:
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

txKm = pygame.font.Font(pygame.font.get_default_font(), 18)
mensi_text_font = pygame.font.Font(pygame.font.get_default_font(), 24)
text_font = pygame.font.SysFont('lucida_sans_typewriter', 36) #tahoma
vetsi_text_font = pygame.font.SysFont('lucida_sans_typewriter', 72) #orc_a papyrus stencil
def textik(text, font, text_col, x,y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x,y))

n = 1

sq = 0
sj = 0

pp = False

if n == 0:
    Sn = pygame.image.load('MainMenu/real.png')
else:
    Sn = pygame.image.load('MainMenu/real1.png')
    sk = e.animatronik([9,5,8,7,6,20])
    pp = True
    Ses = pygame.image.load('MainMenu/hwSe.png')
    SrO = pygame.image.load('MainMenu/SvSe.png')
    #ss = ["", "", "", "", "", Sr5, Sr6, Sr7, Sr8, ""]
LLLL = ""

AuBox = "MuBo.mp3"
POOP = pygame.image.load('MainMenu/kl.png')
Sl = pygame.image.load('MainMenu/SvL.png')
Sr = pygame.image.load('MainMenu/SvR.png')
Sdl = pygame.image.load('MainMenu/DdL.png')
Sdr = pygame.image.load('MainMenu/DdR.png')
St = pygame.image.load('MainMenu/static.png')
St1 = pygame.image.load('MainMenu/static1.png')
Sp = pygame.image.load('MainMenu/sipecka.png')
Tx = pygame.image.load('MainMenu/text.png')
KLKM = pygame.image.load('MainMenu/Spsmap.png')
Ikonka = pygame.image.load('MainMenu/icon.png')
ImgPG = pygame.image.load('MainMenu/pg.png')
Novi = pygame.image.load('MainMenu/noviny.png')
Et = pygame.image.load('MainMenu/entr.png')
OF = pygame.image.load('MainMenu/G1.png')
Ckamka0 = pygame.image.load('MainMenu/K0.png')
Ckamka1 = pygame.image.load('MainMenu/K1.png')
Ckamka2 = pygame.image.load('MainMenu/K2.png')
Ckamka3 = pygame.image.load('MainMenu/K3.png')
Ckamka4 = pygame.image.load('MainMenu/K4.png')
Ckamka5 = pygame.image.load('MainMenu/K5.png')
Ckamka6 = pygame.image.load('MainMenu/K6.png')
Ckamka7 = pygame.image.load('MainMenu/K7.png')
Ckamka8 = pygame.image.load('MainMenu/K8.png')
Ckamka9 = pygame.image.load('MainMenu/K9.png')
Ckamka = [Ckamka0,Ckamka1,Ckamka2,Ckamka3,Ckamka4,Ckamka5,Ckamka6,Ckamka7,Ckamka8,Ckamka9]

Brs = pygame.image.load('MainMenu/hwBr.png')
BrO = pygame.image.load('MainMenu/SvBr.png')
HoO = pygame.image.load('MainMenu/SvHo.png')
FiO = pygame.image.load('MainMenu/SvFi.png')
#bb = ["", "", "", "", "", Br5, Br6, Br7, Br8, ""]
hh = ["", "", "", "", "", "", "", "", "", ""]
jj = ["", "", "", "", "", "", "", "", "", ""]
ff = ["", "", "", "", "", "", "", "", "", ""]
balding = e.animatronik([9,5,8,7,6,20])
ho = e.animatronik([7,5,3,5,2,6,20])
fl = e.animatronik([8,1,7,2,20])
bjump = 0
hj = 0
fj = 0
jj = 0
bald = 0
fq = 0
hq = 0

BtKm = pygame.image.load('MainMenu/KmBt.png')
#screen.blit(pygame.transform.scale(pic, (500, 500)), (0, 0))
# ----------------------------------- #
OknoSirka = 1680 #2480
OknoVyska = 1000
Okno_velikost = (OknoSirka,OknoVyska)
screen = pygame.display.set_mode(Okno_velikost,0,32)

display = pygame.Surface((300,200)) 

pygame.display.set_icon(Ikonka)

KameStat = pygame.image.load('MainMenu/stat.png')
KameStat = pygame.transform.scale(KameStat, (OknoSirka, OknoVyska))
Sn = pygame.transform.scale(Sn,  (810, 1000))

kill = ""
#Kolikátá noc
PNoc = 0
#Pro správné počítaní času
rozdil = 0

nahoru = False
dolu = False
MenuBool = True
IntermiseBool = False
Lose = False
Win = False

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
            
            screen.blit(Sn, (OknoSirka - 780,0))
            screen.blit(Sw, (0,0))
            screen.blit(Sq, (0,0))
            
            # -------- Pro epilepsii -------- #
            if Sw == St:
                jump_allowed = False
                Sw = St1
            else:
                Sw = St

            screen.blit(Tx, (220, 150))
            screen.blit(Sp, (120,sipecky_Y))
            #screen.blit(Tx1, (20, OknoVyska - 100))
            #screen.blit(Tx2, (OknoSirka - 350, OknoVyska - 100))
            textik("V 0.01", text_font, (255,255,255), 60, OknoVyska - 100)
            textik("©️ Patron Service, Poland", text_font, (255,255,255), OknoSirka - 650, OknoVyska - 100)  
            pygame.display.update()
            hodiny.tick(40)


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
                hodiny.tick(40)
        else:
            IntermiseBool = False
            GameBool = True 
                
    # -------- Hlavní traktor --------- #
    if GameBool:
        rozdil = pygame.time.get_ticks() / 1000
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
        k = ""
        BoolSWKamera = False
        #Logika rozmístění a přepínání kamer
        MPoz = OknoVyska - 540 #530
        xList = [(540,MPoz), "ŘE", (440,MPoz + 120), "SCHO", (160, MPoz + 140), "HW1B", (200,MPoz), "KAB", (540,MPoz + 80), "SEK1", (340,MPoz + 140), "HW1A", (80,MPoz + 280), "T17B", (360,MPoz + 280), "T16", (410,MPoz + 370), "T15", (490, MPoz + 270), "SEK2"]#MainDoor MainHallway
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
        odecet = 0.2
        zdroj = 1
        nace = 0
        naze = 0
        nape = 0
        
        xxxx = 300
        deme = False
        keke = False
        cunter = 0     
        while running:

            rect = Rect(mx, my, 1, 1)
            mx, my = pygame.mouse.get_pos()
            screen.fill((0,0,0))
            Vteriny = round((pygame.time.get_ticks() / 1000) - rozdil)
            Minivteriny = round((pygame.time.get_ticks() / 100 - rozdil / 100))
            strtVteriny = Vteriny - 60 * Minu
            Rano = Vteriny // 45
            
            
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
                if pygame.mouse.get_pressed()[0]:
                    try:
                        keke = True
                    except AttributeError:
                        pass
                else:
                    keke = False  
            
            
            if Rano < 1:
                Rano = 12
            elif Rano >= 6:
                Win = True
                running = False
                GameBool = False

            if strtVteriny < 10:
                strtVteriny = "0"+str(strtVteriny)
            elif strtVteriny >= 60:
                Minu += 1
        
            if naze + 4 < Vteriny:
                #POHYB ŠEL INTEGROVAT DO ANIMATRONIKŮ (self.pohybCislo), ALE NECHCI TO UŽ MĚNIT
                naze += 4
                bald += 1
                hq += 1
                fq += 1
                sq += 1
                #Average agrese
                bjump, bald = balding.pohyb(bald, BoolRD, bjump, 5)
                #Menší agrese
                hj, hq = ho.pohyb(hq, BoolRD, hj, 3)
                #Vyšší agrese
                fj, fq = fl.pohyb(fq, BoolLD, fj, 7)
                if n == 1:
                    #Agrese (90% na pohyb)
                    sj, sq = sk.pohyb(sq, BoolRD, sj, 9)  
                
                
            if nace < Vteriny:
                Proc = round(Proc - odecet * zdroj, 1)
                nace += 1                  
                                    
            #Aby jsme nešli až moc daleko s power drainingem
            zdroj = 1
            #Rect/hitboxy kamery (mimo kvůli vypínání a zapínání kamery
            KM = Rect(350, OknoVyska - 140, OknoSirka-700, 100)
            #KM = pygame.draw.rect(screen, (0,0,255), [350, OknoVyska - 100, OknoSirka-700, 100], 4)
            
            
            #ONO BY TO ŠLO UDĚLAT NA GLOBÁLNÍ PROMĚNOU, ALE NECHCE SE MI
            if bjump > 90:
                LLLL = BrO
                kill = "Brian"
                Lose = True
                running = False
                GameBool = False
            elif hj > 90:
                LLLL = HoO
                kill = "Honza"
                Lose = True
                running = False
                GameBool = False
            elif fj > 90:
                LLLL = FiO
                kill = "Filip"
                Lose = True
                running = False
                GameBool = False
            elif sj > 90:
                LLLL = SrO
                kill = "Snejkyr"
                Lose = True
                running = False
                GameBool = False
            elif xxxx < 0:
                LLLL = POOP
                kill = "Casovy limit music boxu smrade"
                Lose = True
                running = False
                GameBool = False                
            
            if not keke:
                if Vteriny % 4 == 0 and not deme:
                    xxxx -= 20
                    deme = True
                elif Vteriny % 4 != 0:
                    deme =  False        
                      
            if not BoolKm:
                screen.blit(OF, (dX - 210,0))
                                    
                #Rect/hitboxy tlačítek
                LD = Rect(dX + -76, 330, 100, 120)
                LL = Rect(dX + -76, 480, 100, 120)
                RD = Rect(dX + OknoSirka, 340, 90, 110)
                RL = Rect(dX + OknoSirka, 490, 90, 100)
                
                #Rect/hitboxy otáčení
                #LS = pygame.draw.rect(screen, (0,0,255), [0, 0, 200, OknoVyska], 4)
                #PS = pygame.draw.rect(screen, (0,0,255), [OknoSirka - 200, 0, 200, OknoVyska], 4)
                LS = Rect(0, 0, 200, OknoVyska)
                PS = Rect(OknoSirka - 200, 0, 200, OknoVyska)
            
                if PS.collidepoint((mx, my)) and dX >= -200:
                    dX -= 20
                elif LS.collidepoint((mx, my)) and dX <= 200:
                    dX += 20
                    
                #Dalo by se dát and místo více if, né když stačí ale ověřit jednu proměnnou
                if klik and Proc > 0:
                    if LL.collidepoint((mx, my)):
                        BoolLL = not BoolLL
                    elif RL.collidepoint((mx, my)):
                        BoolRL = not BoolRL
                    elif LD.collidepoint((mx,my)):
                        BoolLD = not BoolLD
                    elif RD.collidepoint((mx,my)):
                        BoolRD = not BoolRD
                
                if Proc < 0:
                    BoolLL = False
                    BoolRL = False
                    BoolLD = False
                    BoolRD = False
                
                if BoolLL == True:
                    screen.blit(Sl, (dX - 52, 216))
                if BoolRL == True:
                    screen.blit(Sr, (dX + OknoSirka - 416, 230))

                if bjump == 20 and BoolRL:
                    screen.blit(BrO, (dX + OknoSirka - 416, 230))
                if hj == 20 and BoolRL:
                    screen.blit(HoO, (dX + OknoSirka - 416, 230))
                if fj == 20 and BoolLL:
                    screen.blit(FiO, (dX - 52, 216))
                if sj == 20 and BoolRL:
                    screen.blit(SrO, (dX + OknoSirka - 416, 216))
                
                
                if BoolRD == True:
                    screen.blit(Sdr, (dX + OknoSirka - 416, 230)) 
                if BoolLD == True:
                    screen.blit(Sdl, (dX - 52, 216))

                pygame.mixer.music.pause()
            # -------- Na kameře -------- #
            else:
                #Vykreslení záznamu kamery live WOWOWOWOWO
                zdroj += 1
                screen.blit(Ckamka[kamka], (0,0))
                pygame.draw.rect(screen, (255,255,255), [40, 40, OknoSirka - 60, OknoVyska - 60], 2)
                
                if bjump == kamka:
                    screen.blit(Brs, (OknoSirka / 2,OknoVyska / 2))
                    
                if sj == kamka:
                    screen.blit(Ses, (OknoSirka / 2- 400,OknoVyska / 2 - 200))
                    #screen.blit(ss[kamka], (OknoSirka / 2,OknoVyska / 2))
                
                if BoolPG:
                    #Phone Guy
                    screen.blit(ImgPG, (OknoSirka - 400, OknoVyska - 300))
                    PG = Rect([1460, 820, 70, 60])
                    if rect.colliderect(PG) and klik:
                        BoolPG = False
                
                if (Vteriny - PrepMaediator) < 0.5:
                    screen.blit(KameStat, (0,0))
                else:
                    screen.blit(KLKM, (100,MPoz))                
                    for r in KmLt:
                        if rect.colliderect(r) and klik and BoolSWKamera == False and kamka != KmLt.index(r):
                            kamka = KmLt.index(r)
                            #print(kamka)
                            #Ckamka = Ckamka + str(kamka)
                            PrepMaediator = Vteriny
                        elif kamka == KmLt.index(r):
                            pygame.draw.rect(screen, (140,140,140), r, 0)
                            pygame.draw.rect(screen, (150,200,255), r, 5)
                        else:
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

                #Epilepsie kamer
                if Sw == St:
                    jump_allowed = False
                    Sw = St1
                else:
                    Sw = St

                if kamka == 4:
                    if nape + 25 < Vteriny:
                        k = ""
                    if k == "":
                        k = audio(AuBox, k)
                        nape = Vteriny
                    else:
                        pygame.mixer.music.unpause()
                    pygame.draw.rect(screen, (0,0,0), [100, MPoz - 200, 320, 120], 0)
                    textik("Music box", text_font, (255,255,255), 110, MPoz - 190)
                    pygame.draw.rect(screen, (0,0,0), [100, MPoz - 130, 320, 120], 0)
                    sssss = pygame.draw.rect(screen, (100,100,100), [110, MPoz - 120, 300, 100], 0)
                    sussy = pygame.draw.rect(screen, (255,255,255), [110, MPoz - 120, xxxx, 100], 0)

                    if (rect.colliderect(sssss) or rect.colliderect(sussy)) and keke and xxxx < 300 and Minivteriny >= cunter + 10:
                        cunter = Minivteriny
                        xxxx += 20
                else:
                    pygame.mixer.music.pause()
                            
            if BoolRD == True:
                zdroj += 1            
            if BoolLD == True:
                zdroj += 1
            if BoolLL == True:
                zdroj += 1            
            if BoolRL == True:
                zdroj += 1   
            screen.blit(BtKm, (350, OknoVyska - 140))
            textik(str(Rano) + "AM", vetsi_text_font, (255,255,255), OknoSirka - 250, 40)
            textik(str(Minu) + ":" + str(strtVteriny), mensi_text_font, (200,200,200), OknoSirka - 140, 120)
            textik("Noc " + str(PNoc), text_font, (255,255,255), OknoSirka - 200, 160)
            textik("Energie:" + str(Proc) + "%", text_font, (255,255,255), 60, 60)  
            textik("Využití:" + str(zdroj), mensi_text_font, (255,255,255), 60, 120)
            
            if xxxx <= 120 and xxxx > 60:
                pygame.draw.rect(screen, (255,255,0), [OknoSirka - 320, OknoVyska - 140, 200, 100],0)
                textik("Music box!", mensi_text_font, (0,0,0), OknoSirka - 300, OknoVyska - 120)
            elif xxxx <= 60:
                pygame.draw.rect(screen, (255,0,0), [OknoSirka - 320, OknoVyska - 140, 200, 100],0)
                textik("Music box!!!!", mensi_text_font, (255,255,255), OknoSirka - 300, OknoVyska - 120)
            
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
                                
            pygame.display.update()
            hodiny.tick(40)
        
    # -------- Noviny na začítku hry -------- #
    if Win:
        klik = False
        PNoc += 1
        running = True
        while running:
            #Průhlednost
            screen.fill((0,0,0))
            textik("6 AM!Yayayayaya!!!!!!", vetsi_text_font, (255,255,255), OknoSirka/2 - 200, OknoVyska /2)
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
                hodiny.tick(40)
        else:
            IntermiseBool = False
            GameBool = True
            
    if Lose:
        running = True
        while running:
            #Průhlednost
            screen.fill((0,0,0))
            screen.blit(LLLL,(OknoSirka/2 - 300, 200))
            textik("Zabil tebe " + kill + "!!!!", vetsi_text_font, (255,255,255), OknoSirka/2 - 400, OknoVyska /2)
            textik("Esc to escape this", mensi_text_font, (255,255,255), OknoSirka/2 - 400, OknoVyska /2 + 200)
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminace()
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        terminace()

                pygame.display.update()
                hodiny.tick(40)
        else:
            IntermiseBool = False
            GameBool = True 
    screen.blit(pygame.transform.scale(display,Okno_velikost),(0,0))
