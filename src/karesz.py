from src.game import *
from src.labirinth import Labirinth
class Karesz:
    def __init__(self,screen:Screen,labirinth:Labirinth):
        posX=0
        self.posX=0
        self.posY=1
        self.screen=screen
        self.screen.setKaresz(self)
        self.labirinth=labirinth
        self.screen.setTable(self.labirinth)
    def draw(self):
        self.screen.draw()
    def setPicture(self,path):
        self.picture = pygame.image.load(path)
    def getPicture(self):
        return self.picture
    def getPos(self):
        return [self.posX*40,self.posY*40]
    def move(self,x:int, y:int):
        self.posX+=x
        self.posY+=y
    


    
