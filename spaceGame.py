# Siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame
import time
import math
import random
import shelve

FPS = 140
wind_laius = 600
wind_kõrgus = 600
padding = 10
scoreboard_kõrgus = 100
font_size = 36

kiirus = 4.5
elud = 10
x = padding
y = wind_kõrgus-padding-scoreboard_kõrgus

kills_for_bonus = 0
killcount = 0

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
nice_b = (66, 126, 245)
background = (31, 31, 31)


# SETUP
pygame.init()
pygame.font.init()
pygame.mixer.init()
font = pygame.font.Font(pygame.font.get_default_font(), font_size)

window = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Spacers Invade")
aeg = pygame.time.Clock()


# Pilt
laev = pygame.image.load("img/playerShip2_green.png").convert()
laev.set_colorkey(BLACK)
laev = pygame.transform.scale(laev,(50,50))
laius = laev.get_width()
kõrgus = laev.get_height()

x = padding
y = wind_kõrgus-2*padding-scoreboard_kõrgus - kõrgus

# Heli
heli_tabamus = pygame.mixer.Sound("audio/hit.wav")
heli_valik = pygame.mixer.Sound("audio/menu.wav")
heli_laser = pygame.mixer.Sound("audio/laser.wav")
heli_menüüs = pygame.mixer.Sound("audio/menu.wav")

pygame.mixer.music.load("audio/DigitalZen.mp3")
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.3)

# Meteoriidid
meteoriit_image = []
meteoriitX = []
meteoriitY = []
meteoriitY_change = []
meteoriitide_arv = 5


# Laskmine
laser_image = pygame.image.load("img/laserBlue03.png").convert()
laser_image = pygame.transform.scale(laser_image,(9,32))
laserX = 0
laserY = y
laserY_change = 7
laser_state = "ready"

# Loodud selleks, et peale menüüsse minekut oleks paus,
# et menüüs liiklemine oleks mugavam, kuid saab kasutada ükskõik kus
def delay(n = 0.15):
    time.sleep(n)

# Joonistab a ja refreshib ekraani.
# Kutsuda välja viimase funktsioonina mängimise ajal!!!

def redraw():
    window.blit(laev,(x,y))
    pygame.display.update()


# SKOORI LUGEMISEGA SEOTUV MANT
def elus():
    global elud
    global pause
    global run_menu
    global kills_for_bonus
    global killcount
    global FPS
    
    if elud <= 0:
        d = shelve.open("score.txt")
        score = d["score"]
        if killcount > score:
            d["score"] = killcount
        d.close()
        draw_endgame(killcount)
        delay(3)
        pause = True
        run_menu = True
        elud = 10
        meteoriidid_reset()
        meteoriitide_genereerimine()
        kills_for_bonus = 0
        killcount = 0
        FPS = 120
    if kills_for_bonus >= 10:
        kills_for_bonus = 0
        elud += 2
        FPS += 5
     
    
def meteoriidid_reset():
    global meteoriit_image
    global meteoriitX
    global meteoriitY
    global meteoriitY_change
    
    meteoriit_image = []
    meteoriitX = []
    meteoriitY = []
    meteoriitY_change = []
    

def meteoriitide_genereerimine():
    global meteoriitide_arv
    global meteoriitX
    global meteoriitY
    global meteoriitY_change

    for i in range(meteoriitide_arv):
        meteoriit_image.append(pygame.image.load("img/asteroid.png").convert())
        meteoriitX.append (random.randint(0,530))
        meteoriitY.append (random.randint(-250,-50))
        meteoriitY_change.append (30)


def meteoriit(x,y,i):
    meteoriit_image[i].set_colorkey(BLACK)
    window.blit(meteoriit_image[i],(x,y))


# Meteoriitide liikumine
def meteoriitide_liikumine():
    global laserY
    global elud
    global kills_for_bonus
    global killcount
    
    for i in range(meteoriitide_arv):
        if meteoriitY[i] > wind_kõrgus - 2*padding - scoreboard_kõrgus - 30:
            pygame.mixer.Sound.play(heli_tabamus)
            elud -= 1
            meteoriitY[i] = random.randint(-250,-50)
            meteoriitX[i] = random.randint(0,530)
        meteoriitY [i]+= meteoriitY_change [i]
        
        if meteoriitY [i] > 0:
            meteoriitY_change[i] = 1
            kokkupõrge = collision(meteoriitX[i],meteoriitY[i],laserX,laserY)
            if kokkupõrge:
                pygame.mixer.Sound.play(heli_tabamus)
                laserY = -50 # SEE SIIN
                kills_for_bonus += 1
                killcount += 1
                laser_state = "ready"
                meteoriitX[i] = random.randint(0,560)
                meteoriitY[i] = random.randint(-250,-50)
                
        meteoriit(meteoriitX[i],meteoriitY[i], i)


def laskmine(x,y):
    global laser_state
    laser_state = "fire"
    window.blit(laser_image,(x+21,y+10)) # selle peaks panema x+20, et kuulid hakkaksid täpselt laeva ninast tulema, aga kui see see panna x+20 ss metoriitide hitboxsid lähevad valeks


def laseri_liikumine():
    global laserY
    global laser_state
    if laserY < 0:
        laserY = y
        laser_state = "ready"
    if laser_state is "fire":
        laskmine(laserX,laserY)
        laserY -= laserY_change


# Collision
def collision(meteoriitX,meteoriitY,laserX,laserY):
    vahemaa = math.sqrt((math.pow(meteoriitX-laserX,2))+(math.pow(meteoriitY-laserY,2)))
    if vahemaa < 23:
        return True
    else:
        return False

# SUHT CRAP INTRO TEST
def intro():
    global play_intro
    window.fill(RED)
    pygame.display.update()
    delay(2)
    window.fill(GREEN)
    pygame.display.update()
    delay(1)
    play_intro = False
    

# Joonistab tausta ning skooriga seonduva
def draw_elem():
    global elud
    global killcount
    global kills_for_bonus
    
    window.fill(RED)
    pygame.draw.rect(window, background, (padding/2, 0, wind_laius-padding , wind_kõrgus-padding/2))
    pygame.draw.rect(window, (30, 36, 245), (padding,wind_kõrgus-padding-scoreboard_kõrgus, wind_laius-2*padding,scoreboard_kõrgus))
    
    hitpoints = font.render("HP: " + str(elud), True, BLACK)
    kc = font.render("KC: " + str(killcount), True, BLACK)
    kb = font.render("2up IN: " + str(10-kills_for_bonus), True, BLACK)
    
    window.blit(kb, dest = (330,520))
    window.blit(kc, dest = (200, 520))
    window.blit(hitpoints, dest = (30,520))

# Menüüelemendi valimine pausil ning in general pausil ollevate asjade visuaalne pool
menüü_valik = 0
def draw_pausil():
    global font_size
    x = [250,300,350,400,450,500]
    y = [0]
    global menüü_valik

    window.fill(background)
    jätka = font.render("Continue", True, (230,230,230))
    välju = font.render("Quit", True, (230,230,230))
    stats = font.render("Statistics", True, (230,230,230))

    y = (wind_laius - jätka.get_width())/2
    window.blit(jätka, dest = (y,x[0]))
    window.blit(stats, dest = (y,x[1]))
    window.blit(välju, dest = (y,x[2]))

    pygame.draw.rect(window, RED, (y-padding, x[menüü_valik]-padding, y, font_size+2*padding), 3)
    pygame.display.update()
    
# Statistikat vaadates visuaalne pool
def draw_stats():
    window.fill(background)
    d = shelve.open('score.txt')
    score = d['score']
    d.close()
    hs = font.render("Highscore: " + str(score), True, (230,230,230))
    y = (wind_laius - hs.get_width())/2
    window.blit(hs, dest = (y, 250))
    pygame.display.update()
    

def draw_endgame(kc):
    window.fill(nice_b)
    hs = font.render("Score: " + str(kc), True, (230,230,230))
    y = (wind_laius - hs.get_width())/2
    window.blit(hs, dest = (y, 250))
    pygame.display.update()
    

# Peamenüüga kõik visuaalne pool
def main_menu():
    window.fill((66, 126, 245))
    start = font.render("Press ENTER to START", True, BLACK)
    y = int(wind_laius - start.get_width())/2
    pygame.draw.rect(window, (230,0,0), (y-padding, 250-padding, y*4.4, font_size+2*padding))
    window.blit(start, dest = (y, 250))
    pygame.display.update()


# Kõik mängimise ajal inputiga seonduv
def nupud():
    global x
    global y
    global pause
    global run
    global laserX

    nupud = pygame.key.get_pressed()

    if nupud[pygame.K_LEFT] and x >= kiirus + padding:
        x -= kiirus
    if nupud[pygame.K_RIGHT] and x < wind_laius - laius - padding:
        x += kiirus
    if nupud[pygame.K_SPACE]:
        if laser_state is "ready":
            pygame.mixer.Sound.play(heli_laser)
            laserX = x
            laskmine(x,laserY)
    if nupud[pygame.K_ESCAPE]:
        delay()
        pause = not pause
        

# Literally tegin selle selleks, et hiljem oleks lihtsam helifaili vahetades muuta heli
def heli_menüü():
    pygame.mixer.Sound.play(heli_menüüs)


def nupud_stats():
    global stats
    global pause
    
    nupud = pygame.key.get_pressed()
    
    if nupud[pygame.K_ESCAPE]:
        delay()
        heli_menüü()
        stats = not stats
        pause = not pause
    if nupud[pygame.K_RETURN]:
        delay()
        heli_menüü()
        stats = not stats
     
# Kõik pausi ajal olles inputiga seonduv
def nupud_pausil():
    global pause
    global run
    global menüü_valik
    global stats

    nupud = pygame.key.get_pressed()

    if nupud[pygame.K_ESCAPE]:
        delay()
        pause = not pause
        
    if nupud[pygame.K_DOWN]:
        heli_menüü()
        delay()
        
        menüü_valik += 1
        if menüü_valik > 2:
            menüü_valik = 0
        
    if nupud[pygame.K_UP]:
        heli_menüü()
        delay()
        
        menüü_valik -= 1
        if menüü_valik < 0:
            menüü_valik = 2
        
    if nupud[pygame.K_RETURN]:
        heli_menüü()
        if menüü_valik == 0:
            delay()
            pause = not pause 
        if menüü_valik == 1:
            delay()
            stats = True 
        if menüü_valik == 2:
            delay()
            run = False
            


# Kõik inputiga seonduv mängu alguses / Start menüüs
def nupud_alguses():
    global pause
    global run_menu

    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_RETURN]:
        heli_menüü()
        delay()
        
        run_menu = False
        pause = False
        


# Main loop
run_menu = True
run = True
pause = True
stats = False

# INTROT EI EKSISTEERI, KUID KUI SEE UNCOMMENTIDA
# SIIS FLASHIB EKRAAN KAHTE VÄRVI JA LÄHEB MENÜÜSSE
play_intro = False

meteoriitide_genereerimine()
while run:
    # Kui ei ole paus, mäng käib!!!
    if not pause:
        aeg.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        print("FPS/RASKUSASTE: " +str(FPS))
        nupud()
        draw_elem()
        meteoriitide_liikumine()
        laseri_liikumine()
        
        elus()
        redraw()


    # Kui on pausil
    if pause:
        if not run_menu:
            if not stats:
                aeg.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                draw_pausil()
                nupud_pausil()

            # Stats menu
            if stats: # TODO Implement Stats
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                draw_stats()
                nupud_stats()
                

        # Algselt laetav peamenüü
        # run_menu = False
        # pause = True
        # Muutujad peavad olema nii, et peamenüü laeks ette ennast
        if run_menu: # TO DO
            aeg.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            if play_intro: # What a shitty ass intro
                intro()
            else:
                main_menu()
                nupud_alguses()

pygame.quit()
