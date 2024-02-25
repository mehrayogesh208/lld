import playingPiece
from typing import List
class Board:
    def __init__(self,rows,columns):
        self.rows = rows
        self.columns = columns
        self.grid = [[None for j in range(0,self.columns)] for i in range(self.rows)]

    def addPiece(self,row,col,piece:playingPiece.playingPiece)->bool:
        if self.grid[row][col] is  None:
            self.grid[row][col] = piece
            return True
        return False
    
    def getNonEmptyCells(self):
        emptyCells = []
        for row in range(0,self.rows):
            for col in range(0,self.columns):
                if self.grid[row][col] is None:
                    emptyCells.append((row,col))
        return emptyCells
    
    def isWinner(self):
        #Add logic to find the 
        return False


    
