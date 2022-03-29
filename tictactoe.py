import math


class Board:
    last_move = -1
    def __init__(self):
        self.board = [[0,0,0], [0,0,0] , [0,0,0]]

    def squareToPos(self, square):
        y = (square-1)%3
        x = math.floor((square-1)/3)
        return (x,y)
    
    def display(self):
        for row in self.board:
            for col in row:
                if col != 0:
                    print(col, end="\t")
                else:
                    print("", end="\t")
            print()
        return
    
    def play(self, square, player):
        self.last_move = square
        pos = self.squareToPos(square)
        self.board[pos[0]][pos[1]] = player
        return
    
    def undo(self):
        pos = self.squareToPos(self.last_move)
        self.board[pos[0]][pos[1]] = 0
        self.last_move = -1
        return

    def check_win(self):
        for row in self.board: #If any row
            if row[0] == row[1] == row[2] and row[0] != 0:
                return (True, row[0])
        
        for j in range(3): #If any column
            if self.board[0][j] == self.board[1][j] == self.board[2][j] and self.board[0][j] != 0:
                return (True, self.board[0][j])
        
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[1][1] != 0: #Dia 1
            return (True, self.board[0][0])

        elif self.board[0][2] == self.board[1][1] == self.board[2][0]  and self.board[1][1] != 0: #Dia 2
            return (True, self.board[0][2])

        if 0 not in self.board[0] and 0 not in self.board[1] and 0 not in self.board[2] :
            return (None, None)
        return (False, None)

