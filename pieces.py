'''
Created on Apr 24, 2020

@author: RayL
'''
import pygame


def isKingChecked(king,board,dumBoard,s): 
        if dumBoard is not None:
            board = dumBoard
            
            if s is None:
                s = [king.row,king.col]
                
            if king.color == 'white':
                
                for row in board:
                    for piece in row:
                        if piece != 0:
                            if piece.color == 'black':
                                for space in piece.getSpaces(board,True):
                                    if space[0] == s[0] and space[1] == s[1]:
                                        print("Check was checked for")
                                        
                                        return True
            else:
                
                for row in board:
                    for piece in row:
                        if piece != 0:
                            if piece.color == 'white':
                                for space in piece.getSpaces(board,True):
                                    if space[0] == s[0] and space[1] == s[1]:
                                        print("Check was checked for")
                                        
                                        return True
                                    
            return False
            
        else:
            
            if s is None:
                s = [king.row,king.col]
                
            if king.color == 'white':
                
                for row in board.board:
                    for piece in row:
                        if piece != 0:
                            if piece.color == 'black':
                                for space in piece.getSpaces(board):
                                    if space[0] == s[0] and space[1] == s[1]:
                                        return True
                                        print("king in check")
            else:
                
                for row in board.board:
                    for piece in row:
                        if piece != 0:
                            if piece.color == 'white':
                                for space in piece.getSpaces(board):
                                    if space[0] == s[0] and space[1] == s[1]:
                                        return True
                                        print("king in Check")
                                        
            return False

def checkDiags(row,col,board,color,limit = None):
    
    possibleSpaces = []
    urStopped = False
    ulStopped = False
    drStopped = False
    dlStopped = False
    x = 1
    
    while True:
        
        if not urStopped:
            if row - x >= 0 and col + x <= 7:
                ur = board[row - x][col + x]
                if ur == 0:
                    possibleSpaces.append([row - x,col + x])
                else:
                    if ur.color != color:
                        possibleSpaces.append([row - x, col + x])
                    urStopped = True
            else:
                urStopped = True
                
        if not ulStopped:
            if row - x >= 0 and col - x >= 0:
                ul = board[row - x][col - x]
                if ul == 0:
                    possibleSpaces.append([row - x,col - x])
                else:
                    if ul.color != color:
                        possibleSpaces.append([row - x, col - x])
                    ulStopped = True
            else:
                ulStopped = True
                
        if not drStopped:
            if row + x <= 7 and col + x <= 7:
                dr = board[row + x][col + x]
                if dr == 0:
                    possibleSpaces.append([row + x,col + x])
                else:
                    if dr.color != color:
                        possibleSpaces.append([row + x, col + x])
                    drStopped = True
            else:
                drStopped = True
                
        if not dlStopped:
            if row + x <= 7 and col - x >= 0:
                dl = board[row + x][col - x]
                if dl == 0:
                    possibleSpaces.append([row + x,col - x])
                else:
                    if dl.color != color:
                        possibleSpaces.append([row + x, col - x])
                    dlStopped = True
            else:
                dlStopped = True
        x += 1
        
        if limit is not None:
            break
        if urStopped and ulStopped and drStopped and dlStopped:
            break
        
    return possibleSpaces

def checkFiles(row,col,board,color,limit = None):
    
    possibleSpaces = []
    uStopped = False
    dStopped = False
    rStopped = False
    lStopped = False
    x = 1
    
    while True:
        
        if not uStopped :
            if row - x >= 0:
                u = board[row - x][col]
                if u == 0:
                    possibleSpaces.append([row - x,col])
                else:
                    if u.color != color:
                        possibleSpaces.append([row - x, col])
                    uStopped = True
            else:
                uStopped = True
                
        if not lStopped:
            if col - x >= 0:
                l = board[row][col - x]
                if l == 0:
                    possibleSpaces.append([row,col - x])
                else:
                    if l.color != color:
                        possibleSpaces.append([row, col - x])
                    lStopped = True
            else:
                lStopped = True
                
        if not rStopped:
            if col + x <= 7:
                r = board[row][col + x]
                if r == 0:
                    possibleSpaces.append([row,col + x])
                else:
                    if r.color != color:
                        possibleSpaces.append([row, col + x])
                    rStopped = True
            else:
                rStopped = True
                
        if not dStopped:
            if row + x <= 7:
                d = board[row + x][col]
                if d == 0:
                    possibleSpaces.append([row + x,col])
                else:
                    if d.color != color:
                        possibleSpaces.append([row + x,col])
                    dStopped = True
            else:
                dStopped = True
        x += 1
        
        if limit is not None:
            break
        if uStopped and lStopped and dStopped and rStopped:
            break
        
    return possibleSpaces

class Piece():
    
    def __init__(self,row,col,color):
        self.color = color
        self.row = row
        self.col = col
        self.isAlive = True
        self.isPawn = False
        self.isKing = False
        self.isRook = False
        self.spaceSize = 50
    
    def checkPossibleSpaces(self,possibleSpaces,board,col):
        
        finalList = []
        
        for space in possibleSpaces:
            dumBoard = [x[:] for x in board.board]
            board.move(Pawn(self.row,self.col,self.color),[space[0],space[1]],dumBoard)
            if col == 'white':
                if not isKingChecked(board.whiteKing,None,dumBoard,None):
                    finalList.append(space)
            else:
                if not isKingChecked(board.blackKing,None,dumBoard,None):
                    finalList.append(space)
                    
        return finalList
    
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
        self.canEnPassant = [False,[0,0]]
        
    def getSpaces(self,board,fake = False):
        ###When selected, highlight box, return possible spaces, and show possible spaces###
        possibleTakes = []
        possibleSpaces = []
        
        if fake:
            board = board
        else:
            board = board.board
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
                        if (board[space[0]][self.col + 1] != 0 and
                            board[space[0]][self.col + 1].color == 'white'):
                            possibleTakes.append([space[0],self.col + 1])
                    if self.col - 1 >= 0 :
                        if (board[space[0]][self.col - 1] != 0 and
                            board[space[0]][self.col - 1].color =='white'):
                            possibleTakes.append([space[0],self.col - 1])
                if board[space[0]][space[1]] == 0:
                    possibleSpaces.append(space)
                else:
                    break
            else:
                
                space = [self.row - x, self.col]
                
                if x == 1:
                    if self.col + 1 <= 7:
                        if (board[space[0]][self.col + 1] != 0 and
                            board[space[0]][self.col + 1].color == 'black'):
                            possibleTakes.append([space[0],self.col + 1])
                    if self.col - 1 >= 0:
                        if (board[space[0]][self.col - 1] != 0 and
                            board[space[0]][self.col - 1].color =='black'):
                            possibleTakes.append([space[0],self.col - 1])
                if board[space[0]][space[1]] == 0:
                    possibleSpaces.append(space)
                else:
                    break               
            x += 1
        for space in possibleTakes:
            possibleSpaces.append(space)
            
        if self.canEnPassant[0]:
            possibleSpaces.append(self.canEnPassant[1])
            
        return possibleSpaces
    
    def showMenu(self,window,color):
        if color == 'white':
            
            iQueen = pygame.image.load('sprites/whiteQueen.png')
            iRook = pygame.image.load('sprites/whiteRook.png')
            iBishop = pygame.image.load('sprites/whiteBishop.png')
            iKnight = pygame.image.load('sprites/whiteKnight.png')
            pygame.draw.rect(window,(255,255,255),(self.col*self.spaceSize,
                                             self.row*self.spaceSize,
                                             self.spaceSize,
                                             self.spaceSize*4))
            window.blit(iQueen,(self.col*self.spaceSize,self.row*self.spaceSize))
            window.blit(iRook,(self.col*self.spaceSize,(self.row + 1)*self.spaceSize))
            window.blit(iBishop,(self.col*self.spaceSize,(self.row + 2)*self.spaceSize))
            window.blit(iKnight,(self.col*self.spaceSize,(self.row + 3)*self.spaceSize))
            pygame.display.update()
            
            return {(self.row,self.col):Queen(self.row,self.col,color),
                    (self.row + 1,self.col):Rook(self.row,self.col,color),
                    (self.row + 2,self.col):Bishop(self.row,self.col,color),
                    (self.row + 3,self.col):Knight(self.row,self.col,color)
                    }
        else:
            
            iQueen = pygame.image.load('sprites/blackQueen.png')
            iRook = pygame.image.load('sprites/blackRook.png')
            iBishop = pygame.image.load('sprites/blackBishop.png')
            iKnight = pygame.image.load('sprites/blackKnight.png')
            pygame.draw.rect(window,(255,255,255),(self.col*self.spaceSize,
                                             self.row*self.spaceSize,
                                             self.spaceSize,
                                             self.spaceSize*4))
            window.blit(iQueen,(self.col*self.spaceSize,self.row*self.spaceSize))
            window.blit(iRook,(self.col*self.spaceSize,(self.row - 1)*self.spaceSize))
            window.blit(iBishop,(self.col*self.spaceSize,(self.row - 2)*self.spaceSize))
            window.blit(iKnight,(self.col*self.spaceSize,(self.row - 3)*self.spaceSize))
            pygame.display.update()
            
            return {(self.row,self.col):Queen(self.row,self.col,color),
                    (self.row - 1,self.col):Rook(self.row,self.col,color),
                    (self.row - 2,self.col):Bishop(self.row,self.col,color),
                    (self.row - 3,self.col):Knight(self.row,self.col,color)
                    }
            
    def promote(self,board,window):
        
        running = True
        while running:
            
            choices = self.showMenu(window,self.color)
            
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    coords = [x // self.spaceSize for x in pygame.mouse.get_pos()]
                    coords.reverse()
                    coords = tuple(coords)
                    if coords in choices:
                        board[self.row][self.col] = choices[coords]
                        running = False
                    
                    
                        
            

class Knight(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackKnight.png')
        else:
            self.image = pygame.image.load('sprites/whiteKnight.png')
    
    def getSpaces(self,board,fake = False):
        if fake:
            board = board
        else:
            board = board.board
            
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
        
        for x in range(len(possibleSpaces)):
            space = possibleSpaces[x]
            if ((space[0] <= 7 and space[1] <= 7) and 
                (space[0] >= 0 and space[1] >= 0)): 
                    if (board[space[0]][space[1]] == 0 or 
                        board[space[0]][space[1]].color != self.color):
                        finalList.append(space)
            x += 1
            
        return finalList
            
class Bishop(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackBishop.png')
        else:
            self.image = pygame.image.load('sprites/whiteBishop.png')
        
    def getSpaces(self,board,fake = False):
        if fake:
            board = board
        else:
            board = board.board
            
        possibleSpaces = checkDiags(self.row,self.col,board, self.color)
        
        return possibleSpaces
        
        
class Rook(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackRook.png')
        else:
            self.image = pygame.image.load('sprites/whiteRook.png')
        self.isRook = True
        self.canCastle = True

    def getSpaces(self,board,fake = False):
        if fake:
            board = board
        else:
            board = board.board
            
        possibleSpaces = checkFiles(self.row,self.col,board,self.color)
        
        return possibleSpaces

class Queen(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackQueen.png')
        else:
            self.image = pygame.image.load('sprites/whiteQueen.png')
            
    def getSpaces(self,board,fake = False):
        if fake: 
            board = board
        else:
            board = board.board
            
        p1 = checkDiags(self.row,self.col,board,self.color)
        p2 = checkFiles(self.row,self.col,board,self.color)
        possibleSpaces = p1 + p2
        
        return possibleSpaces
    
class King(Piece):
    
    def __init__(self,row,col,color):
        Piece.__init__(self, row, col, color)
        if self.color == 'black':
            self.image = pygame.image.load('sprites/blackKing.png')

        else:
            self.image = pygame.image.load('sprites/whiteKing.png')
            
        self.isKing = True
        self.canCastle = True
    
    def checkPossibleSpaces(self,possibleSpaces,board,col):
        finalList = []
        
        for space in possibleSpaces:
            
            dumBoard = [x[:] for x in board.board]
            dumKing = King(self.row,self.col,col)
            dumKing.canCastle = False
            dumBoard[self.row][self.col] = dumKing
            board.move(dumKing,[space[0],space[1]],dumBoard)
            
            if not isKingChecked(dumKing,None,dumBoard,[space[0],space[1]]):
                finalList.append(space)
                
        return finalList
    
    def attemptCastle(self,board):
        finalList = []
        if board.board[self.row][0] != 0:
            if board.board[self.row][0].isRook and board.board[self.row][0].canCastle:
                if board.board[self.row][self.col - 1] == 0 and board.board[self.row][self.col -2] == 0:
                    
                    p = self.checkPossibleSpaces([[self.row,self.col - 1],[self.row,self.col - 2]],
                                                  board,
                                                  self.color
                                                )
                    if len(p) == 2:
                        finalList.append([self.row,self.col - 2,'CLong'])
                        
        if board.board[self.row][7] != 0:            
                if board.board[self.row][7].isRook and board.board[self.row][7].canCastle:
                    if board.board[self.row][self.col + 1] == 0 and board.board[self.row][self.col + 2] == 0:
                        
                        p = self.checkPossibleSpaces([[self.row,self.col + 1],[self.row,self.col + 2]],
                                                      board,
                                                      self.color
                                                    )
                        
                        if len(p) == 2:
                            finalList.append([self.row,self.col + 2,'CShort'])
        return finalList
        

    def getSpaces(self,board,fake = False):
        possibleSpaces = []
        
        if fake:
            board = board
            
        else:
            b1 = board
            board = board.board
            
            if self.canCastle:
                possibleSpaces += self.attemptCastle(b1)
                
        p1 = checkDiags(self.row,self.col,board,self.color,limit = 'King')
        p2 = checkFiles(self.row,self.col,board,self.color,limit = 'King')
        possibleSpaces += p1 + p2
        return possibleSpaces

        
    
        
        
        