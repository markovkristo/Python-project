# Siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame
import time

FPS = 120
wind_laius = 600
wind_kõrgus = 600
padding = 10
scoreboard_kõrgus = 100
font_size = 36

kiirus = 5
x = padding
y = wind_kõrgus-padding-scoreboard_kõrgus

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = (31, 31, 31)


# SETUP
pygame.init()
pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), font_size)

window = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Rip off Space Invaders")
aeg = pygame.time.Clock()


# Pilt
laev = pygame.image.load("playerShip1_green.png").convert()
laius = laev.get_width()
kõrgus = laev.get_height()

x = padding
y = wind_kõrgus-2*padding-scoreboard_kõrgus - kõrgus

def delay(n = 0.2):
    time.sleep(n)

# Mängja 
def redraw():  
    window.blit(laev,(x,y)) # Ajutine
    pygame.display.update()
    
    
def draw_elem():
    window.fill(RED)
    pygame.draw.rect(window, background, (padding/2, padding/2, wind_laius-padding , wind_kõrgus-padding))
    pygame.draw.rect(window, BLUE, (padding,wind_kõrgus-padding-scoreboard_kõrgus, wind_laius-2*padding,scoreboard_kõrgus))

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

# Kõik inputiga seonduv
def nupud():
    global x
    global y
    global pause
    global run
    
    nupud = pygame.key.get_pressed()

    if nupud[pygame.K_LEFT] and x >= kiirus + padding: # Fixed 
        x -= kiirus
    if nupud[pygame.K_RIGHT] and x < wind_laius - laius - padding: # Fixed
        x += kiirus
    if nupud[pygame.K_ESCAPE]:
        pause = not pause
        delay()        

def nupud_pausil():
    global pause
    global run
    global menüü_valik
    
    nupud = pygame.key.get_pressed()
    
    if nupud[pygame.K_ESCAPE]:
        pause = not pause
        delay()
    if nupud[pygame.K_DOWN]:
        menüü_valik += 1
        if menüü_valik > 2:
            menüü_valik = 0
        delay()
    if nupud[pygame.K_UP]:
        menüü_valik -= 1
        if menüü_valik < 0:
            menüü_valik = 2
        delay()     
    if nupud[pygame.K_RETURN]:
        if menüü_valik == 0:
            pause = not pause
            delay()
        if menüü_valik == 2:
            run = False


    
# Main loop
run_menu = False
run = True
pause = True
stats = False

while run:
    if pause == False:
        aeg.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        nupud()
        draw_elem()
        redraw()
        
    if pause == True:
        if not run_menu:
            if not stats:
                aeg.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False        
                draw_pausil()
                nupud_pausil()
            if stats: # TODO Implement Stats
                run = False
        if run_menu: # TO DO
            print('')
            
pygame.quit()