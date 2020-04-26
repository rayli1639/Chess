'''
Created on Apr 24, 2020

@author: RayL
'''
from board import Board
import pygame
pygame.init()
window_x = 400
window_y = 400
window = pygame.display.set_mode((window_x,window_y)) #Create window
running = True
clock = pygame.time.Clock()
fps = 30
board = Board(window)
board.show()
while running:
    clock.tick(fps) #Update the clock by the fps every frame
    board.drawPieces()
    for event in pygame.event.get(): #Loop to check for user exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = [x / board.spaceSize for x in pygame.mouse.get_pos()]
            print (coords)
            
