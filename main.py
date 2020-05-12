'''
Created on Apr 24, 2020

@author: RayL
'''
from gameChess import GameChess
import pygame
pygame.init()
window_x = 400
window_y = 400
window = pygame.display.set_mode((window_x,window_y)) #Create window
game = GameChess(window)
while game.running:
    game.play()