'''
Created on Apr 27, 2020

@author: RayL
'''
import pygame
from board import Board
from pieces import isKingChecked
from network import Network


class GameChess():
    
    def __init__ (self,window):
        
        self.window = window
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.board = Board()
        self.board.drawBoard(self.window)
        self.board.drawPieces(self.window)
        self.possibleSpaces = []
        self.isSelected = False
        self.pieceSelected = 0
        self.turn = 1
        self.turnCol = 'white'
        self.oppoCol = 'black'
        self.whiteChecked = False
        self.blackChecked = False
        self.possibleStalemate = False
        self.drawCoords = None
        self.n = Network()
        self.n.connect()
    
    def resetBoard(self):
        
        self.pieceSelected = 0
        self.possibleSpaces = []
        self.isSelected = False
        self.board.drawBoard(self.window)
        if self.drawCoords != None:
            pygame.draw.rect(self.window,(100,235,25),
                             (self.drawCoords[0][0]*self.board.spaceSize,self.drawCoords[0][1]*self.board.spaceSize,
                              self.board.spaceSize,self.board.spaceSize))
            pygame.draw.rect(self.window,(100,235,25),
                             (self.drawCoords[1][0]*self.board.spaceSize,self.drawCoords[1][1]*self.board.spaceSize,
                              self.board.spaceSize,self.board.spaceSize))
        
        self.board.drawPieces(self.window)
    
    def pieceAction(self):
        
        self.possibleSpaces = self.pieceSelected.getSpaces(self.board)
        self.possibleSpaces = self.pieceSelected.checkPossibleSpaces(self.possibleSpaces,
                                                                     self.board,
                                                                     self.turnCol)
        self.pieceSelected.drawPossibleSpaces(self.possibleSpaces,self.board,self.window)
    
    def isMated(self):
        
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.color == self.turnCol:
                        possibleSpaces = piece.getSpaces(self.board.board,True)
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
                ##When the player chooses a piece when another piece is not selected
                    
                    if clickedSpace != 0 and clickedSpace.color == self.turnCol:
                        self.pieceSelected = clickedSpace
                        if self.pieceSelected != 0:
                            self.pieceAction()
                            
                        self.isSelected = True
                        
                elif self.isSelected:
                    
                    if (clickedSpace == 0 or clickedSpace == self.pieceSelected or 
                        clickedSpace.color == self.oppoCol):
                        
                        for space in self.possibleSpaces:
                            if coords[0] == space[0] and coords[1] == space[1]:
                                self.drawCoords = self.board.move(self.pieceSelected,space,self.window)
                                self.possibleStalemate = self.board.stalemate
                                self.turn += 1
                                self.n.send(self.board.board)
                        self.resetBoard()

                        
                    else:
                        
                        self.board.drawBoard(self.window)
                        self.board.drawPieces(self.window)
                        
                        if clickedSpace.color == self.turnCol:
                            self.pieceSelected = self.board.board[coords[0]][coords[1]]
                            self.pieceAction()
                            self.isSelected = True 
                            
            if self.turn % 2 == 1:
                
                if isKingChecked(self.board.whiteKing,self.board,None,None):
                    self.whiteChecked = True
                else:
                    self.whiteChecked = False
                    
                self.turnCol = 'white'
                self.oppoCol = 'black'
                
                for row in self.board.board:
                    for piece in row:
                        if piece != 0:
                            if piece.isPawn and piece.color != self.turnCol:
                                piece.canEnPassant = [False,[0,0]]
                                
            else:
        
                if isKingChecked(self.board.blackKing,self.board,None,None):
                    self.blackChecked = True
                else:
                    self.blackChecked = False
                    
                self.turnCol = 'black'
                self.oppoCol = 'white'
                
                for row in self.board.board:
                    for piece in row:
                        if piece != 0:
                            if piece.isPawn and piece.color != self.turnCol:
                                piece.canEnPassant = [False,[0,0]]
                                
            if self.isMated():

                if self.blackChecked:  
                    print('white has won. black was checkmated.')
                elif self.whiteChecked:
                    print('black has won. white was checkmated')
                else:
                    print('The match ended in a stalemate')
                self.running = False
                break
            
            if self.possibleStalemate:
                print('The match ended in a stalemate')
                self.running = False
                break
            
        pygame.display.update()