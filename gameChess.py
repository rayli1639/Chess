'''
Created on Apr 27, 2020

@author: RayL
'''
import pygame
from board import Board

class GameChess():
    
    def __init__ (self,window):
        self.window = window
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.board = Board(self.window)
        self.board.drawBoard()
        self.board.drawPieces()
        self.possibleSpaces = []
        self.isSelected = False
        self.pieceSelected = 0
        self.turn = 1
        self.turnCol = 'white'
        self.oppoCol = 'black'
        self.whiteChecked = False
        self.blackChecked = False
    
    def checkIfRelieve(self,move):
        if move:
            return True
    
    def resetBoard(self):
        self.pieceSelected = 0
        self.possibleSpaces = []
        self.isSelected = False
        self.board.drawBoard()
        self.board.drawPieces()
    
    def pieceAction(self):
        self.possibleSpaces = self.pieceSelected.getSpaces(self.board.board)
        self.possibleSpaces = self.pieceSelected.checkPossibleSpaces(self.possibleSpaces,
                                                                     self.board,
                                                                     self.turnCol)
        self.pieceSelected.drawPossibleSpaces(self.possibleSpaces,self.board,self.window)
    
    def isMated(self):
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.color == self.turnCol:
                        possibleSpaces = piece.getSpaces(self.board.board)
                        possibleSpaces = piece.checkPossibleSpaces(possibleSpaces,
                                                                   self.board,
                                                                   self.turnCol)
                        if possibleSpaces != []:
                            return False
        return True
        
        
    def play(self):
        self.clock.tick(self.fps) #Update the clock by the fps every frame
        for event in pygame.event.get(): #Loop to check for user exit
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                coords = [x // self.board.spaceSize for x in pygame.mouse.get_pos()]
                coords.reverse()
                clickedSpace = self.board.board[coords[0]][coords[1]]
                if not self.isSelected:
                    if clickedSpace != 0 and clickedSpace.color == self.turnCol:
                        self.pieceSelected = clickedSpace
                        if self.pieceSelected != 0:
                            self.pieceAction()
                        self.isSelected = True
                elif self.isSelected:
                    if (clickedSpace == 0 or clickedSpace == self.pieceSelected or 
                        clickedSpace.color == self.oppoCol):
                        if coords in self.possibleSpaces:
                            self.board.move(self.pieceSelected,coords)
                            self.turn += 1
                        self.resetBoard()
                    else:
                        self.board.drawBoard()
                        self.board.drawPieces()
                        if clickedSpace.color == self.turnCol:
                            self.pieceSelected = self.board.board[coords[0]][coords[1]]
                            self.pieceAction()
                            self.isSelected = True 
        if self.turn % 2 == 1:
            if self.board.isKingChecked(self.board.whiteKing):
                self.whiteChecked = True
            else:
                self.whiteChecked = False
            self.turnCol = 'white'
            self.oppoCol = 'black'
        else:
            if self.board.isKingChecked(self.board.blackKing):
                self.blackChecked = True
            else:
                self.blackChecked = False
            self.turnCol = 'black'
            self.oppoCol = 'white'
        if self.isMated():
            print(f'{self.oppoCol} has won. {self.turnCol} was checkmated.')
            break
        pygame.display.update()