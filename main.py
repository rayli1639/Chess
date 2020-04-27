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
turn = 1
turnCol = 'white'
oppoCol = 'black'
while running:
    clock.tick(fps) #Update the clock by the fps every frame
    for event in pygame.event.get(): #Loop to check for user exit
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            coords = [x // board.spaceSize for x in pygame.mouse.get_pos()]
            coords.reverse()
            clickedSpace = board.board[coords[0]][coords[1]]
            if not isSelected:
                if clickedSpace.color == turnCol:
                    pieceSelected = clickedSpace
                    if pieceSelected != 0:
                        possibleSpaces = pieceSelected.getSpaces(board,window)
                    isSelected = True
            elif isSelected:
                if clickedSpace == 0 or clickedSpace == pieceSelected or clickedSpace.color == oppoCol:
                    if coords in possibleSpaces:
                        board.move(pieceSelected,coords)
                        turn += 1
                    pieceSelected = 0
                    possibleSpaces = []
                    isSelected = False
                    board.drawBoard()
                    board.drawPieces()
                else:
                    board.drawBoard()
                    board.drawPieces()
                    if clickedSpace.color == turnCol:
                        pieceSelected = board.board[coords[0]][coords[1]]
                        possibleSpaces = pieceSelected.getSpaces(board,window)
                        isSelected = True
        if turn % 2 == 1:
            turnCol = 'white'
            oppoCol = 'black'
        else:
            turnCol = 'black'
            oppoCol = 'white'
    pygame.display.update()
    
            

            
            

            
