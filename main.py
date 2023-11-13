from src.karesz import *

#Ablak létrehozása
width= 640
height=480
screen = pygame.display.set_mode((width, height))
lab=Labirinth("file.txt")


window=Screen(screen)
karesz = Karesz(window,lab)
karesz.setPicture("img\\karesz.png")


def move():
    karesz.move()
    window.display()
def turn(dir:str):
    karesz.turn(dir)
    window.display()
while not karesz.isThatFinish():
    turn("R")
    while karesz.isThereWallInFrontOfMe():
        turn("L")
    move()
    
karesz.labirinth.print()
