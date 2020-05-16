'''
Created on Apr 27, 2020

@author: RayL
'''
import pygame
from board import Board
from pieces import isKingChecked
from network import Network
from board import create_FEN

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
        self.whiteChecked = False
        self.blackChecked = False
        self.possibleStalemate = False
        self.drawCoords = None
        self.n = Network()
        info = self.n.getInfo()
        self.color = info[0]
        self.board.whiteKing = info[1]
        self.board.blackKing = info[2]
        boardInfo = self.n.send('Receiving Data')
        self.board.board = boardInfo[0]
        self.board.positions = boardInfo[2]
    
        if self.color == 'white':
            self.isTurn = True
            self.turnCol = 'white'
            self.oppoCol = 'black'
        else:
            self.isTurn = False
            self.turnCol = 'black'
            self.oppoCol = 'white'
        
    
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
        
        isSelfMated = True
        isOpponentMated = True
        
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.color == self.turnCol:
                        possibleSpaces = piece.getSpaces(self.board.board,True)
                        possibleSpaces = piece.checkPossibleSpaces(possibleSpaces,
                                                                   self.board,
                                                                   self.turnCol)
                        if possibleSpaces != []:
                            isSelfMated = False
                            break
        if isSelfMated:
            return isSelfMated
                        
        for row in self.board.board:
            for piece in row:
                if piece != 0:
                    if piece.color == self.oppoCol:
                        possibleSpaces = piece.getSpaces(self.board.board,True)
                        possibleSpaces = piece.checkPossibleSpaces(possibleSpaces,
                                                                   self.board,
                                                                   self.oppoCol)
                        if possibleSpaces != []:
                            isOpponentMated = False
                            break

        if isOpponentMated:
            return isOpponentMated
        else:
            return False
    
    def play(self):
        
        
        for row in self.board.board: #Update blackKing and whiteKing
            for piece in row:
                if piece != 0:
                    if piece.color == 'white' and piece.isKing:
                        self.board.whiteKing = piece
                    elif piece.color == 'black' and piece.isKing:
                        self.board.blackKing = piece
                   
        if isKingChecked(self.board.whiteKing,self.board,None,None):
            self.whiteChecked = True
        else:
            self.whiteChecked = False
    
        if isKingChecked(self.board.blackKing,self.board,None,None):
            self.blackChecked = True
        else:
            self.blackChecked = False          

        if self.isMated():
            if self.blackChecked:  
                print('white has won. black was checkmated.')
            elif self.whiteChecked:
                print('black has won. white was checkmated')
            else:
                print('The match ended in a stalemate')
                
            self.running = False
                
        if self.possibleStalemate:
            print('The match ended in a stalemate')
            self.running = False
        
        self.clock.tick(self.fps) #Update the clock by the fps every frame
        
        if self.isTurn is False:
            for event in pygame.event.get(): #Loop to check for user exit
                
                if event.type == pygame.QUIT:
                    self.running = False
                    
            dB = self.n.send('Receiving Data')
            if self.color == dB[1]:
                self.board.board = dB[0]
                self.resetBoard()
                self.isTurn = True
                self.board.positions = dB[2]
                self.drawCoords = dB[3]
                self.resetBoard()
                
                for pos in self.board.positions:
                    if pos[1] == 2:
                        print('The match ended in a stalemate')
                        self.running = False
        
        else:
            
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
                                    
                                    if self.board.board[space[0]][space[1]] != 0:
                                        takes = True
                                    else:
                                        takes = False
                                        
                                    self.drawCoords = self.board.move(self.pieceSelected,space,self.window)
                            
                                    pos = create_FEN(self.board.board)

                                    self.n.send([self.board.board,self.drawCoords])
                                
                                    add_to_pos = False
                                    index = None
                                    
                                    for p in self.board.positions:
                                        if pos == p[0]:
                                            add_to_pos = True
                                            index = self.board.positions.index(p)
                                        
                                    if add_to_pos:
                                        
                                        info = self.n.send([pos,2,index]) #2 Signifies adding to stalemate counter
                                        for pos in info[2]:
                                            if pos[1] == 2:
                                                self.possibleStalemate = True                           
                                                
                                    else:
                                        
                                        self.n.send([[pos,0],0]) #0 Signifies adding a board state
                                        
                                    if self.pieceSelected.isPawn or takes:
                                        
                                        self.n.send([[pos,0],1]) #1 Signifies resetting stalemate counter
                    
                                    self.isTurn = False
                                    
                            self.resetBoard()
                            
                        else:
                            
                            self.resetBoard()
                            
                            if clickedSpace.color == self.turnCol:
                                self.pieceSelected = self.board.board[coords[0]][coords[1]]
                                self.pieceAction()
                                self.isSelected = True 
                                
            for row in self.board.board:
                for piece in row:
                    if piece != 0:
                        if piece.isPawn and piece.color != self.turnCol:
                            piece.canEnPassant = [False,[0,0]]
            
        pygame.display.update()