# Siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame
import time

FPS = 120
wind_laius = 600
wind_kõrgus = 800
padding = 10
scoreboard_kõrgus = 100

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
font = pygame.font.Font(pygame.font.get_default_font(), 36)

window = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Rip off Space Invaders")
aeg = pygame.time.Clock()


# Pilt
laev = pygame.image.load("playerShip1_green.png").convert()
laius = laev.get_width()
kõrgus = laev.get_height()

x = padding
y = wind_kõrgus-2*padding-scoreboard_kõrgus - kõrgus


# Mängja 
def redraw():  
    window.blit(laev,(x,y)) # Ajutine
    pygame.display.update()
    
    
def draw_elem():
    window.fill(RED)
    pygame.draw.rect(window, background, (padding/2, padding/2, wind_laius-padding , wind_kõrgus-padding))
    pygame.draw.rect(window, BLUE, (padding,wind_kõrgus-padding-scoreboard_kõrgus, wind_laius-2*padding,scoreboard_kõrgus))


def draw_pausil():
    x = [250,300,350,400,450,500]
    y = [0]
    
    window.fill(background)
    jätka = font.render("Continue", False, (230,230,230))
    välju = font.render("Quit", False, (230,230,230))
    
    y = (wind_laius - jätka.get_width())/2
    window.blit(jätka, dest = (y,x[0]))
    window.blit(välju, dest = (y,x[1]))
    
    pygame.draw.rect(window, RED, (y-padding, x[1]-padding, y, 50), 3)
    
    pygame.display.update()

# Kõik inputiga seonduv
def nupud():
    global x
    global y
    global pause
    global run
    
    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_ESCAPE]:
        run = False
    if nupud[pygame.K_LEFT] and x >= kiirus + padding: # Fixed 
        x -= kiirus
    if nupud[pygame.K_RIGHT] and x < wind_laius - laius - padding: # Fixed
        x += kiirus
    if nupud[pygame.K_RETURN]:
        pause = not pause
        time.sleep(0.5)
        

def nupud_pausil():
    global pause
    global run
    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_ESCAPE]:
        run = False    
    if nupud[pygame.K_RETURN]:
        pause = not pause
        time.sleep(0.5)    


# Main loop
run = True
pause = True

while run:
    if pause == True:
        aeg.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        nupud()
        draw_elem()
        redraw()
        
    if pause == False:
        aeg.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        draw_pausil()
        nupud_pausil()

pygame.quit()