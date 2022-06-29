

from colorsys import yiq_to_rgb
import pygame
from pygame.locals import *
import sys
import SavingSystem

pygame.init()
Screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
dr = False

global xS
global yS
global xpS
global ypS

xS = SavingSystem.GetInfo(1, "0")
yS = SavingSystem.GetInfo(2, "0")
xpS = SavingSystem.GetInfo(3, "0")
ypS = SavingSystem.GetInfo(4, "0")



def drawButton(X, Y, posX, posY ,draw):
    if draw == True:
        pygame.draw.rect(screen, 'red', (posX, posY, X - posX, Y - posY))    

while True:
    
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            
            posx, posy = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP:
            xS = str(x)
            SavingSystem.SaveInfo(1, xS)

            yS = str(y)
            SavingSystem.SaveInfo(2, yS)

            xpS = str(posx)
            SavingSystem.SaveInfo(3, xS)

            ypS = str(posy)
            SavingSystem.SaveInfo(4, xS)
            dr = True
            
        
            
    

    screen.fill('black')


    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]:
        pygame.draw.rect(screen, 'white', (posx, posy, x - posx, y - posy), 3)
        dr == False
        
        
    drawButton(int(xS), int(yS), int(xpS), int(ypS), True)
    
    

    pygame.display.update()
    
