import pygame

#Inicializáljuk a pygame könyvtárat hogy tudjuk használni a későbbiekben
pygame.init()

fps=60
fpsClock = pygame.time.Clock()

#Ablak létrehozása
width= 640
height=480
screen = pygame.display.set_mode((width, height))

isRunning=True

while isRunning:
    screen.fill([0,0,0])
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            isRunning=False
    
    #Frissítés

    #Rajzolás
    pygame.display.flip()

    #Várakozás a következő frame elött
    fpsClock.tick(fps)
    
pygame.quit()
