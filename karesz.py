import pygame

#Inicializáljuk a pygame könyvtárat hogy tudjuk használni a későbbiekben
pygame.init()







def game(screen):
    fps=60
    clock = pygame.time.Clock()
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
        clock.tick(fps)
        
    pygame.quit()
