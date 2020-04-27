'''
Created on Apr 24, 2020

@author: RayL
'''
import pygame

class Piece():
    
    def __init__(self,row,col,color):
        self.color = color
        self.row = row
        self.col = col
        self.isAlive = True
        self.isPawn = False
    
    def drawPossibleSpaces(self,possibleSpaces,board,window):
        currentPosCol = self.col*board.spaceSize
        currentPosRow = self.row*board.spaceSize
        pygame.draw.rect(window,(0,255,0),(currentPosCol,currentPosRow,
                            board.spaceSize,board.spaceSize))
        window.blit(self.image,(currentPosCol,currentPosRow))
        for space in possibleSpaces:
            pygame.draw.rect(window,(0,255,0),(space[1]*board.spaceSize,space[0]*board.spaceSize,
                                board.spaceSize,board.spaceSize))

class Pawn(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self,row,col,color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackPawn.png')
        else:
            self.image = pygame.image.load('sprites/whitePawn.png')
        self.canMoveTwo = True
        self.isPawn = True
        
    def getSpaces(self,board,window):
        ###When selected, highlight box, return possible spaces, and show possible spaces###
        possibleTakes = []
        possibleSpaces = []
        x = 1
        if self.canMoveTwo:
            r = 2
        else:
            r = 1
        while x <= r:
            if self.color == 'black':
                space = [self.row + x, self.col]
                if x == 1:
                    if self.col + 1 <= 7:
                        if (board.board[space[0]][self.col + 1] != 0 and
                            board.board[space[0]][self.col + 1].color == 'white'):
                            possibleTakes.append([space[0],self.col + 1])
                    if self.col - 1 >= 0 :
                        if (board.board[space[0]][self.col - 1] != 0 and
                            board.board[space[0]][self.col - 1].color =='white'):
                            possibleTakes.append([space[0],self.col - 1])
                if board.board[space[0]][space[1]] == 0:
                    possibleSpaces.append(space)
                else:
                    break
            else:
                space = [self.row - x, self.col]
                if x == 1:
                    if self.col + 1 <= 7:
                        if (board.board[space[0]][self.col + 1] != 0 and
                            board.board[space[0]][self.col + 1].color == 'black'):
                            possibleTakes.append([space[0],self.col + 1])
                    if self.col - 1 >= 0:
                        if (board.board[space[0]][self.col - 1] != 0 and
                            board.board[space[0]][self.col - 1].color =='black'):
                            possibleTakes.append([space[0],self.col - 1])
                if board.board[space[0]][space[1]] == 0:
                    possibleSpaces.append(space)
                else:
                    break               
            x += 1
        self.drawPossibleSpaces(possibleSpaces, board, window)
        for space in possibleTakes:
            pygame.draw.rect(window,(0,255,0),(space[1]*board.spaceSize,space[0]*board.spaceSize,
                                board.spaceSize,board.spaceSize))
            possibleSpaces.append(space)
        return possibleSpaces
            

class Knight(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackKnight.png')
        else:
            self.image = pygame.image.load('sprites/whiteKnight.png')
    
    def getSpaces(self,board,window):
        possibleSpaces = [
            [self.row + 2, self.col + 1],
            [self.row + 2, self.col - 1],
            [self.row - 2,self.col + 1],
            [self.row - 2, self.col - 1],
            [self.row + 1,self.col + 2],
            [self.row + 1,self.col - 2],
            [self.row -1, self.col + 2],
            [self.row -1, self.col -2]
            ]
        finalList = []
        for x in range(len(possibleSpaces) - 1):
            space = possibleSpaces[x]
            if ((space[0] <= 7 and space[1] <= 7) and 
                (space[0] >= 0 and space[1] >= 0)): 
                    if (board.board[space[0]][space[1]] == 0 or 
                        board.board[space[0]][space[1]].color != self.color):
                        finalList.append(space)
            x += 1
        self.drawPossibleSpaces(finalList,board,window)
        return finalList
            
class Bishop(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackBishop.png')
        else:
            self.image = pygame.image.load('sprites/whiteBishop.png')
        
class Rook(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackRook.png')
        else:
            self.image = pygame.image.load('sprites/whiteRook.png')

class Queen(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackQueen.png')
        else:
            self.image = pygame.image.load('sprites/whiteQueen.png')
            
class King(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackKing.png')
        else:
            self.image = pygame.image.load('sprites/whiteKing.png')
        


        
    
        
        
        