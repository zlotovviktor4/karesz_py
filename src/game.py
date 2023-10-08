import pygame
from src.labirinth import Labirinth
#Inicializáljuk a pygame könyvtárat hogy tudjuk használni a későbbiekben
class Screen:
    def __init__(self,screen) -> None:
        self.screen=screen
        self.table=[[" "]]
        
    def setTable(self,lab:Labirinth):
        self.table=lab.getTable()
    def setKaresz(self,karesz):
        self.karesz=karesz
    def setPicture(self):
        self.picture=self.karesz.getPicture()

    def draw(self):
        pygame.init()
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if self.table[i][j]=="0":
                    pygame.draw.rect(self.screen, [0,0,0], pygame.Rect(j*40, i*40, 40, 40))
                elif self.table[i][j]=="1":
                    pygame.draw.rect(self.screen, [255,0,0], pygame.Rect(j*40, i*40, 40, 40))
                elif self.table[i][j]=="F":
                    pygame.draw.rect(self.screen, [0,0,255], pygame.Rect(j*40, i*40, 40, 40))
        self.screen.blit(self.picture,self.karesz.getPos())

    def game(self):
        pygame.init()
        fps=60
        clock = pygame.time.Clock()
        isRunning=True
        while isRunning:
            self.screen.fill([0,0,0])
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    isRunning=False
            
            #Frissítés
            
            #Rajzolás
            self.draw()
            pygame.display.flip()

            #Várakozás a következő frame elött
            clock.tick(fps)
            
        pygame.quit()
