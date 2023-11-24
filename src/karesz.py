from src.game import *
from src.labirinth import Labirinth
class Karesz:
    Directions={0:"R",1:"D",2:"L",3:"U"}
    def __init__(self,screen:Screen,labirinth:Labirinth):
        posX=0
        self.posX=0
        self.posY=1
        self.screen=screen
        self.screen.setKaresz(self)
        self.labirinth=labirinth
        self.screen.setTable(self.labirinth)
        self.dir=0
    def draw(self):
        self.screen.draw()
    def setPicture(self,path):
        self.picture = pygame.image.load(path)
    def getPicture(self):
        return pygame.transform.rotate(self.picture,90*self.dir)
    def getPos(self,blockSize:int) -> list:
        return [self.posX*blockSize,self.posY*blockSize]
    def setPosition(self,x:int, y:int):
        self.posX=x
        self.posY=y
    def move(self):
        if self.isThereWallInFrontOfMe():
            return None
        pos=self.getPosInFrontOfMe()
        self.setPosition(pos[0],pos[1])
            
    def turn(self,turnDir:str)->None:
        if(turnDir=="L"):
            self.dir+=1
            self.dir%=4
        if(turnDir=="R"):
            self.dir+=3
            self.dir%=4
    def isThereWallInFrontOfMe(self)->bool:
        frontPos=self.getPosInFrontOfMe()
        table=self.labirinth.getTable()
        if(table[frontPos[1]][frontPos[0]]=='1'):
            return True
        return False
    def getPosInFrontOfMe(self)->list:
        frontPos=self.getPos(1)
        if(self.dir==0):
            frontPos[0]+=1
        elif(self.dir==1):
            frontPos[1]-=1
        elif(self.dir==2):
            frontPos[0]-=1
        elif(self.dir==3):
            frontPos[1]+=1
        return frontPos
    def isThatFinish(self) ->bool:
        pos=self.getPos(1)
        table=self.labirinth.getTable()
        if(table[pos[1]][pos[0]]=="F"):
            return True
        return False
kjshdfgkjhsdgkjjshfkjhsfl

sdjfhusdjf
    
    


    
