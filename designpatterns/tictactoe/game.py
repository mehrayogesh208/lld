from collections import deque
import board
import player
import playingPiece
class TicTacToe:
    def __init__(self):
        self.Board = list()
        self.Players = deque()
    def initializeGame(self):
        self.Board = board.Board(3,3)
        Player1 = player.Player("123",playingPiece.playingPiece(playingPiece.Piece.type1))
        Player2 = player.Player("987",playingPiece.playingPiece(playingPiece.Piece.type2))
        self.Players.append(Player1)
        self.Players.append(Player2)
    def startGame(self):
        isWinner = False
        while not isWinner:
            currentPlayer = self.Players.popleft()
            print("Current Player is {}".format(currentPlayer.id))
            emptyCells = self.Board.getNonEmptyCells()
            print(emptyCells)
            x,y = list(map(int,input().split()))
            if not self.Board.addPiece(x,y,currentPlayer.piece):
                print("Non empty cell !! Try Again")
                self.Players.appendleft(currentPlayer)
            else:
                if self.Board.isWinner():
                    print("Winner current player {}".format(currentPlayer.id))
                    break
                self.Players.append(currentPlayer)
