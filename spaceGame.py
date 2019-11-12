# Siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame

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


# Aken
pygame.init()
window = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Rip off Space Invaders")
aeg = pygame.time.Clock()

# Pilt
# Ajutiselt debugi jaoks välja kommenteeritud
# See tuleb ka alati kaasa panna githubi vms!
laev = pygame.image.load("playerShip1_green.png").convert()

laius = laev.get_width()
kõrgus = laev.get_height()

x = padding
y = wind_kõrgus-2*padding-scoreboard_kõrgus - kõrgus

# Mängja 
def redraw():  
    window.fill(RED)
    pygame.draw.rect(window, background, (padding/2, padding/2, wind_laius-padding , wind_kõrgus-padding))
    pygame.draw.rect(window, BLUE, (padding,wind_kõrgus-padding-scoreboard_kõrgus, wind_laius-2*padding,scoreboard_kõrgus))
    window.blit(laev,(x,y)) # Ajutine
    pygame.display.update()
    

# Main loop
run = True
while run:
    aeg.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    nupud = pygame.key.get_pressed()
    if nupud[pygame.K_LEFT] and x >= kiirus + padding: # Fixed 
        x -= kiirus
    if nupud[pygame.K_RIGHT] and x < wind_laius - laius - padding: # Fixed
        x += kiirus

    redraw()
    

pygame.quit()