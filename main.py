from karesz import *

#Ablak létrehozása
width= 640
height=480
screen = pygame.display.set_mode((width, height))
lab=Labirinth("file.txt")

window=Screen(screen)
karesz = Karesz(window,lab)
karesz.setPicture("img\\karesz.png")
window.setPicture()
karesz.draw()
window.game()
karesz.labirinth.print()