

from colorsys import yiq_to_rgb
import pygame
from pygame.locals import *
import sys


pygame.init()
Screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()


while True:
    
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            
        
            
    

    screen.fill('black')


    mouse_presses = pygame.mouse.get_pressed()
    if mouse_presses[0]:
        
        
        
        pygame.draw.rect(screen, 'white', (posx, posy, x - posx, y - posy), 7)
    
    

    pygame.display.update()
    
