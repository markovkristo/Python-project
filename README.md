# project_Mibo
Programmeerimine (LTAT.03.001) aines grupitöö käigus loodud projekt. (Informaatika 1. semester)

#siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame
FPS = 60
wind_laius = 480
wind_kõrgus = 600
x = 50
y = 450
laius = 20
kõrgus = 0
kiirus = 20
#värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#pilt
laev = pygame.image.load("playerShip1_green.png")

#aken
pygame.init()
wind = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Rip off Space Invaders")
aeg = pygame.time.Clock()
#mängja 
def redraw():  
    wind.fill(BLACK)
    wind.blit(laev,(x,y))
    pygame.display.update()


#main loop
run = True
while run:
    aeg.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_LEFT] and x > kiirus:
        x -= kiirus
    if nupud[pygame.K_RIGHT] and x < wind_laius - laius - kiirus:
        x += kiirus
    if nupud[pygame.K_UP] and y > kiirus:
        y -= kiirus
    if nupud[pygame.K_DOWN] and y < wind_laius - kõrgus - kiirus:
        y += kiirus
    
    redraw()
    
    

pygame.quit()

