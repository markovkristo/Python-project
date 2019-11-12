# Siin on suht head disainid jne. https://opengameart.org/content/space-shooter-redux
import pygame

FPS = 120
wind_laius = 800
wind_kõrgus = 600
x = 50
y = 450
padding = 10

laius = 20
kõrgus = 20
kiirus = 5

# Värvid
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
background = (31, 31, 31)

# Pilt
# Ajutiselt debugi jaoks välja kommenteeritud
# See tuleb ka alati kaasa panna githubi vms!
#laev = pygame.image.load("playerShip1_green.png")

# Aken
pygame.init()
window = pygame.display.set_mode((wind_laius,wind_kõrgus))
pygame.display.set_caption("Rip off Space Invaders")
aeg = pygame.time.Clock()

# Mängja 
def redraw():  
    window.fill(background)
    #window.blit(laev,(x,y)) # Ajutine
    pygame.draw.rect(window, RED, (x, y, laius,kõrgus)) # Ajutine
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
    if nupud[pygame.K_UP] and y >= kiirus + padding: # Fixed
        y -= kiirus
    if nupud[pygame.K_DOWN] and y < wind_kõrgus - kõrgus - padding: # Fixed
        y += kiirus
    
    redraw()
    
    

pygame.quit()
