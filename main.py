'''
Created on Apr 24, 2020

@author: RayL
'''
from board import Board
import pygame
pygame.init()
window_x = 600
window_y = 600
window = pygame.display.set_mode((window_x,window_y)) #Create window
running = True
clock = pygame.time.Clock()
fps = 30
board = Board()
while running:
    clock.tick(fps) #Update the clock by the fps every frame
    for event in pygame.event.get(): #Loop to check for user exit
        if event.type == pygame.QUIT:
            running = False
