'''
Created on Apr 24, 2020

@author: RayL
'''
from board import Board
import pygame
test = 2
test = 2
pygame.init()
window_x = 400
window_y = 400
window = pygame.display.set_mode((window_x,window_y)) #Create window
running = True
clock = pygame.time.Clock()
fps = 30
board = Board(window)
board.show()
board.drawBoard()
board.drawPieces()
possibleSpaces = []
isSelected = False
pieceSelected = 0
clickBuffer = 0
while running:
    clock.tick(fps) #Update the clock by the fps every frame
    for event in pygame.event.get(): #Loop to check for user exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.key.get_pressed():
            print(board.board)
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = [x // board.spaceSize for x in pygame.mouse.get_pos()]
            coords.reverse()
            if not isSelected:
                pieceSelected = board.board[coords[0]][coords[1]]
                if pieceSelected != 0:
                    possibleSpaces = pieceSelected.getSpaces(board,window)
                print(pieceSelected)
                print(coords)
                print(possibleSpaces)
                isSelected = True
            elif isSelected:
                if board.board[coords[0]][coords[1]] != 0:
                    board.drawBoard()
                    board.drawPieces()
                    pieceSelected = board.board[coords[0]][coords[1]]
                    possibleSpaces = pieceSelected.getSpaces(board,window)
                    isSelected = True
                else:
                    if coords in possibleSpaces:
                        board.move(pieceSelected,coords)
                    pieceSelected = 0
                    possibleSpaces = []
                    isSelected = False
                    board.drawBoard()
                    board.drawPieces()
    pygame.display.update()
    
            

            
            

            
