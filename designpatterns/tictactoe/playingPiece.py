from enum import Enum

class Piece(Enum):
    type1 = 'X'
    type2 = 'O'

class playingPiece:
    def __init__(self,type:Piece):
        self.piece = type
