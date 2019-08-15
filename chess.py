class Board:

    def __init__(self):
        self.board = {'a1': False, 'a2': False, 'a3': False, 'a4': False, 'a5': False, 'a6': False, 'a7': False, 'a8': False, 
        'b1': False, 'b2': False, 'b3': False, 'b4': False, 'b5': False, 'b6': False, 'b7': False, 'b8': False, 
        'c1': False, 'c2': False, 'c3': False, 'c4': False, 'c5': False, 'c6': False, 'c7': False, 'c8': False, 
        'd1': False, 'd2': False, 'd3': False, 'd4': False, 'd5': False, 'd6': False, 'd7': False, 'd8': False, 
        'e1': False, 'e2': False, 'e3': False, 'e4': False, 'e5': False, 'e6': False, 'e7': False, 'e8': False, 
        'f1': False, 'f2': False, 'f3': False, 'f4': False, 'f5': False, 'f6': False, 'f7': False, 'f8': False, 
        'g1': False, 'g2': False, 'g3': False, 'g4': False, 'g5': False, 'g6': False, 'g7': False, 'g8': False, 
        'h1': False, 'h2': False, 'h3': False, 'h4': False, 'h5': False, 'h6': False, 'h7': False, 'h8': False}
   
    def move(self, start_square, end_square):
        temp_figure = self.board[start_square]
        if not temp_figure:
            return #TODO error message
        possible_end_squares = temp_figure #TODO
        if end_square not in possible_end_squares:
            return 
        else:
            self.board[start_square] = False
            self.board[end_square] = temp_figure


class Figures:
    playboard_squares = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 
        'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 
        'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 
        'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 
        'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 
        'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 
        'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
    def K(self, square):
        possible_squares = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                temp_square = chr(odr(square[0]) + j) + str(int(square[1]) + i)
                if temp_square in self.playboard_squares and temp_square != square:
                    possible_squares.append(temp_square)
        return possible_squares
    
    def Q(self, square):
        possible_squares = []

        possible_squares += self.R(square)
        possible_squares += self.B(square) 
        
        return possible_squares
    
    def R(self, square):
        possible_squares = []

        for i in range(-7, 8): #ORTHOGONAL
            temp_square1 = square[0] + str(int(square[1]) + i)
            temp_square2 = chr(odr(square[0]) + i) + square[1]
            if temp_square1 in self.playboard_squares and temp_square1 != square:
                    possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and temp_square2 != square:
                    possible_squares.append(temp_square2)

        return possible_squares
    
    def B(self, square):
        possible_squares = []

        for i in range(-7, 8): #DIAGONAL
            temp_square1 = chr(odr(square[0]) + i) + str(int(square[1]) + i)
            temp_square2 = chr(odr(square[0]) + i) + str(int(square[1]) - i)
            if temp_square1 in self.playboard_squares and temp_square1 != square:
                    possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and temp_square2 != square:
                    possible_squares.append(temp_square2)
        
        return possible_squares

    def N(self, square):
        possible_squares = []

        for i in [-2, 2]:
            for j in [-1, 1]:
                temp_square1 = chr(odr(square[0]) + i) + str(int(square[1]) + j)
                temp_square2 = chr(odr(square[0]) + j) + str(int(square[1]) + i)
                if temp_square1 in self.playboard_squares and temp_square1 != square:
                    possible_squares.append(temp_square1)
                if temp_square2 in self.playboard_squares and temp_square2 != square:
                    possible_squares.append(temp_square2)
            
        return possible_squares

    def P(self, square)