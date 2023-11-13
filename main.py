from src.karesz import *

#Ablak létrehozása
width= 640
height=480
screen = pygame.display.set_mode((width, height))
lab=Labirinth("file.txt")

window=Screen(screen)
karesz = Karesz(window,lab)
karesz.setPicture("img\\karesz.png")
karesz.draw()
karesz.move()
for i in range(4):
    karesz.turn("R")
print(karesz.isThereWallInFrontOfMe())
print(karesz.getPosInFrontOfMe())
window.display()
window.game()
karesz.labirinth.print()
