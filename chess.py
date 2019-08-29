class Board:

    def __init__(self):
        self.player_to_move = 'w'
        self.game_log = []
        self.board = {'a8': False, 'b8': False, 'c8': False, 'd8': False, 'e8': False, 'f8': False, 'g8': False, 'h8': False,
                      'a7': False, 'b7': False, 'c7': False, 'd7': False, 'e7': False, 'f7': False, 'g7': False, 'h7': False,
                      'a6': False, 'b6': False, 'c6': False, 'd6': False, 'e6': False, 'f6': False, 'g6': False, 'h6': False,
                      'a5': False, 'b5': False, 'c5': False, 'd5': False, 'e5': False, 'f5': False, 'g5': False, 'h5': False,
                      'a4': False, 'b4': False, 'c4': False, 'd4': False, 'e4': False, 'f4': False, 'g4': False, 'h4': False,
                      'a3': False, 'b3': False, 'c3': False, 'd3': False, 'e3': False, 'f3': False, 'g3': False, 'h3': False,
                      'a2': False, 'b2': False, 'c2': False, 'd2': False, 'e2': False, 'f2': False, 'g2': False, 'h2': False,
                      'a1': False, 'b1': False, 'c1': False, 'd1': False, 'e1': False, 'f1': False, 'g1': False, 'h1': False}

    def switch_player(self):
        if self.player_to_move == 'w':
            self.player_to_move = 'b'
        else:
            self.player_to_move = 'w'

    def check_if_check(self, K_square):
        for i in self.board:
            j = self.board[i]
            if j and j.kind != 'K':
                squares = Moves().arbitrary(i, self.board)
                if K_square in squares:
                    return True
            elif j and j.kind == 'K' and j.colour != self.board[K_square].colour:
                squares = Moves().arbitrary(i, self.board)
                if K_square in squares:
                    return True

    def find_pieces(self, desired_kind, desired_colour):
        squares_with_pieces = []
        for i in self.board:
            if self.board[i] and self.board[i].colour == desired_colour and self.board[i].kind == desired_kind:
                squares_with_pieces.append(i)
        return squares_with_pieces

    def check_for_move(self, start_square, end_square):  # simulates desired move and checks for checks returns board as it was given
        temp_figure = self.board[start_square]
        if not temp_figure:
            return False
        else:
            possible_end_squares = Moves().arbitrary(start_square, self.board)

        if end_square not in possible_end_squares:
            return False
        else:
            target = self.board[end_square]
            self.board[start_square] = False
            self.board[end_square] = temp_figure
            king_square = self.find_pieces('K', temp_figure.colour)[0]
            if self.check_if_check(king_square):
                self.board[start_square] = temp_figure
                self.board[end_square] = target
                return False
            self.board[start_square] = temp_figure
            self.board[end_square] = target
            return True

    def promotion(self, desired_promotion, start_square, end_square):
        temp_figure = self.board[start_square]
        temp_figure.kind = desired_promotion
        self.board[end_square] = temp_figure
        self.board[start_square] = False
        temp_figure.move_log.append(end_square + '=' + desired_promotion)
        self.game_log.append(end_square + '=' + desired_promotion)
        self.switch_player()

    def move(self, start_square, end_square):  # preforms the move + castling + promotion + en passant
        temp_figure = self.board[start_square]
        if not temp_figure:
            return False
        elif self.player_to_move != temp_figure.colour:
            return False
        elif temp_figure.kind == 'K' and start_square == 'e1' and end_square == 'c1':
            if self.check_for_move('e1', 'd1') and self.check_for_move('e1', 'c1') and not self.check_if_check('e1'):
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board['d1'] = self.board['a1']
                self.board['a1'] = False
                self.game_log.append('O-O-O')
                temp_figure.move_log.append('O-O-O')
                self.board['d1'].move_log.append('O-O-O')
                self.switch_player()
                return True
        elif temp_figure.kind == 'K' and start_square == 'e1' and end_square == 'g1':
            if self.check_for_move('e1', 'f1') and self.check_for_move('e1', 'g1') and not self.check_if_check('e1'):
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board['f1'] = self.board['h1']
                self.board['h1'] = False
                self.game_log.append('O-O')
                temp_figure.move_log.append('O-O')
                self.board['f1'].move_log.append('O-O')
                self.switch_player()
                return True
        elif temp_figure.kind == 'K' and start_square == 'e8' and end_square == 'c8':
            if self.check_for_move('e8', 'd8') and self.check_for_move('e8', 'c8') and not self.check_if_check('e8'):
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board['d8'] = self.board['a8']
                self.board['a8'] = False
                self.game_log.append('O-O-O')
                temp_figure.move_log.append('O-O-O')
                self.board['d8'].move_log.append('O-O-O')
                self.switch_player()
                return True
        elif temp_figure.kind == 'K' and start_square == 'e8' and end_square == 'g8':
            if self.check_for_move('e8', 'f8') and self.check_for_move('e8', 'g8') and not self.check_if_check('e8'):
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board['f8'] = self.board['h8']
                self.board['h8'] = False
                self.game_log.append('O-O')
                temp_figure.move_log.append('O-O')
                self.board['f8'].move_log.append('O-O')
                self.switch_player()
                return True
        elif temp_figure.kind == 'P' and end_square[1] == '8' and temp_figure.colour == 'w' and self.check_for_move(start_square, end_square):
            return 'Promotion'
        elif temp_figure.kind == 'P' and end_square[1] == '1' and temp_figure.colour == 'b' and self.check_for_move(start_square, end_square):
            return 'Promotion'
        elif temp_figure.kind == 'P' and start_square[1] == '5' and temp_figure.colour == 'w' and not self.board[end_square] and (end_square[0] == chr(ord(start_square[0]) + 1) or end_square[0] == chr(ord(start_square[0]) - 1)):
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) + 1) + '5' and len(self.board[chr(ord(start_square[0]) + 1) + '5'].move_log) == 1:
                t_fig = self.board[chr(ord(start_square[0]) + 1) + '5']
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board[chr(ord(start_square[0]) + 1) + '5'] = False
                if self.check_if_check((self.find_pieces('K', temp_figure.colour)[0])):
                    self.board[start_square] = temp_figure
                    self.board[end_square] = False
                    self.board[chr(ord(start_square[0]) + 1) + '5'] = t_fig
                    return False
                else:
                    temp_figure.move_log.append(end_square)
                    self.game_log.append(temp_figure.kind + end_square)
                    self.switch_player()
                    return True
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) - 1) + '5' and len(self.board[chr(ord(start_square[0]) - 1) + '5'].move_log) == 1:
                t_fig = self.board[chr(ord(start_square[0]) - 1) + '5']
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board[chr(ord(start_square[0]) - 1) + '5'] = False
                if self.check_if_check((self.find_pieces('K', temp_figure.colour)[0])):
                    self.board[start_square] = temp_figure
                    self.board[end_square] = False
                    self.board[chr(ord(start_square[0]) - 1) + '5'] = t_fig
                    return False
                else:
                    temp_figure.move_log.append(end_square)
                    self.game_log.append(temp_figure.kind + end_square)
                    self.switch_player()
                    return True
        elif temp_figure.kind == 'P' and start_square[1] == '4' and temp_figure.colour == 'b' and not self.board[end_square] and (end_square[0] == chr(ord(start_square[0]) + 1) or end_square[0] == chr(ord(start_square[0]) - 1)):
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) + 1) + '4' and len(self.board[chr(ord(start_square[0]) + 1) + '4'].move_log) == 1:
                t_fig = self.board[chr(ord(start_square[0]) + 1) + '4']
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board[chr(ord(start_square[0]) + 1) + '4'] = False
                if self.check_if_check((self.find_pieces('K', temp_figure.colour)[0])):
                    self.board[start_square] = temp_figure
                    self.board[end_square] = False
                    self.board[chr(ord(start_square[0]) + 1) + '4'] = t_fig
                    return False
                else:
                    temp_figure.move_log.append(end_square)
                    self.game_log.append(temp_figure.kind + end_square)
                    self.switch_player()
                    return True
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) - 1) + '4' and len(self.board[chr(ord(start_square[0]) - 1) + '4'].move_log) == 1:
                t_fig = self.board[chr(ord(start_square[0]) - 1) + '4']
                self.board[end_square] = temp_figure
                self.board[start_square] = False
                self.board[chr(ord(start_square[0]) - 1) + '4'] = False
                if self.check_if_check((self.find_pieces('K', temp_figure.colour)[0])):
                    self.board[start_square] = temp_figure
                    self.board[end_square] = False
                    self.board[chr(ord(start_square[0]) - 1) + '4'] = t_fig
                    return False
                else:
                    temp_figure.move_log.append(end_square)
                    self.game_log.append(temp_figure.kind + end_square)
                    self.switch_player()
                    return True
        elif self.check_for_move(start_square, end_square):
            self.board[start_square] = False
            self.board[end_square] = temp_figure
            temp_figure.move_log.append(end_square)
            self.game_log.append(temp_figure.kind + end_square)
            self.switch_player()
            return True
        else:
            return False


class Moves:

    playboard_squares = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                         'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                         'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                         'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                         'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                         'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                         'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                         'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']

    def arbitrary(self, test_square, playboard):
        temp_figure = playboard[test_square]
        if temp_figure:
            if temp_figure.kind == 'K':
                return Moves().K(test_square, playboard)
            elif temp_figure.kind == 'Q':
                return Moves().Q(test_square, playboard)
            elif temp_figure.kind == 'R':
                return Moves().R(test_square, playboard)
            elif temp_figure.kind == 'B':
                return Moves().B(test_square, playboard)
            elif temp_figure.kind == 'N':
                return Moves().N(test_square, playboard)
            elif temp_figure.kind == 'P':
                return Moves().P(test_square, playboard)

    def check_if_ok(self, square, test_square, playboard):
        if not playboard[square]:
            return 1
        elif playboard[square].colour != playboard[test_square].colour:
            return 2
        elif playboard[square].colour == playboard[test_square].colour:
            return 3

    def K(self, test_square, playboard):
        possible_squares = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                temp_square = chr(ord(test_square[0]) + j) + str(int(test_square[1]) + i)
                if temp_square in self.playboard_squares and self.check_if_ok(temp_square, test_square, playboard):
                    possible_squares.append(temp_square)

        if playboard[test_square].move_log == []:
            if playboard[test_square].colour == 'w':
                if playboard['a1'] and playboard['a1'].kind == 'R' and playboard['a1'].move_log == [] and not playboard['b1'] and not playboard['c1'] and not playboard['d1']:
                    possible_squares.append('c1')
                if playboard['h1'] and playboard['h1'].kind == 'R' and playboard['h1'].move_log == [] and not playboard['f1'] and not playboard['g1']:
                    possible_squares.append('g1')
            if playboard[test_square].colour == 'b':
                if playboard['a8'] and playboard['a8'].kind == 'R' and playboard['a8'].move_log == [] and not playboard['b8'] and not playboard['c8'] and not playboard['d8']:
                    possible_squares.append('c8')
                if playboard['h8'] and playboard['h8'].kind == 'R' and playboard['h8'].move_log == [] and not playboard['f8'] and not playboard['g8']:
                    possible_squares.append('g8')

        return possible_squares

    def Q(self, test_square, playboard):
        possible_squares = []

        possible_squares += self.R(test_square, playboard)
        possible_squares += self.B(test_square, playboard)

        return possible_squares

    def R(self, test_square, playboard):
        possible_squares = []

        i = 1
        while i + int(test_square[1]) < 9:
            temp_square = test_square[0] + str(int(test_square[1]) + i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = -1
        while i + int(test_square[1]) > 0:
            temp_square = test_square[0] + str(int(test_square[1]) + i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i -= 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = 1
        while i + ord(test_square[0]) - 97 < 8:
            temp_square = chr(ord(test_square[0]) + i) + test_square[1]
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = -1
        while i + ord(test_square[0]) - 97 > -1:
            temp_square = chr(ord(test_square[0]) + i) + test_square[1]
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i -= 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        return possible_squares

    def B(self, test_square, playboard):
        possible_squares = []

        i = 1
        while i + int(test_square[1]) < 9 and i + ord(test_square[0]) - 97 < 8:
            temp_square = chr(ord(test_square[0]) + i) + str(int(test_square[1]) + i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = -1
        while i + int(test_square[1]) > 0 and i + ord(test_square[0]) - 97 > -1:
            temp_square = chr(ord(test_square[0]) + i) + str(int(test_square[1]) + i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i -= 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = 1
        while i + int(test_square[1]) < 9 and - i + ord(test_square[0]) - 97 > -1:
            temp_square = chr(ord(test_square[0]) - i) + str(int(test_square[1]) + i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        i = 1
        while - i + int(test_square[1]) > 0 and i + ord(test_square[0]) - 97 < 8:
            temp_square = chr(ord(test_square[0]) + i) + str(int(test_square[1]) - i)
            if self.check_if_ok(temp_square, test_square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, test_square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break

        return possible_squares

    def N(self, test_square, playboard):
        possible_squares = []

        for i in [-2, 2]:
            for j in [-1, 1]:
                temp_square1 = chr(ord(test_square[0]) + i) + str(int(test_square[1]) + j)
                temp_square2 = chr(ord(test_square[0]) + j) + str(int(test_square[1]) + i)
                if temp_square1 in self.playboard_squares and temp_square1 != test_square:
                    if not playboard[temp_square1]:
                        possible_squares.append(temp_square1)
                    elif playboard[test_square].colour != playboard[temp_square1].colour:
                        possible_squares.append(temp_square1)
                if temp_square2 in self.playboard_squares and temp_square2 != test_square:
                    if not playboard[temp_square2]:
                        possible_squares.append(temp_square2)
                    elif playboard[test_square].colour != playboard[temp_square2].colour:
                        possible_squares.append(temp_square2)

        return possible_squares

    def P(self, test_square, playboard):
        possible_squares = []
        if playboard[test_square].colour == 'w':
            temp_square1 = test_square[0] + str(int(test_square[1]) + 1)
            temp_square2 = test_square[0] + str(int(test_square[1]) + 2)
            if temp_square1 in self.playboard_squares and not playboard[temp_square1]:
                possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and test_square[1] == '2' and not playboard[temp_square2]:
                possible_squares.append(temp_square2)
            temp_square1 = chr(ord(test_square[0]) - 1) + str(int(test_square[1]) + 1)
            temp_square2 = chr(ord(test_square[0]) + 1) + str(int(test_square[1]) + 1)
            if temp_square1 in self.playboard_squares and playboard[temp_square1] and playboard[temp_square1].colour == 'b':
                possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and playboard[temp_square2] and playboard[temp_square2].colour == 'b':
                possible_squares.append(temp_square2)
        else:
            temp_square1 = test_square[0] + str(int(test_square[1]) - 1)
            temp_square2 = test_square[0] + str(int(test_square[1]) - 2)
            if temp_square1 in self.playboard_squares and not playboard[temp_square1]:
                possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and test_square[1] == '7' and not playboard[temp_square2]:
                possible_squares.append(temp_square2)
            temp_square1 = chr(ord(test_square[0]) - 1) + str(int(test_square[1]) - 1)
            temp_square2 = chr(ord(test_square[0]) + 1) + str(int(test_square[1]) - 1)
            if temp_square1 in self.playboard_squares and playboard[temp_square1] and playboard[temp_square1].colour == 'w':
                possible_squares.append(temp_square1)
            if temp_square2 in self.playboard_squares and playboard[temp_square2] and playboard[temp_square2].colour == 'w':
                possible_squares.append(temp_square2)

        return possible_squares


class Piece:

    def __init__(self, kind, colour, possible_squares):
        self.kind = kind
        self.colour = colour
        self.possible_squares = possible_squares
        self.move_log = []

    def encode(self):
        i = 0
        if self.kind == 'K':
            i += 12
        elif self.kind == 'Q':
            i += 13
        elif self.kind == 'R':
            i += 14
        elif self.kind == 'B':
            i += 15
        elif self.kind == 'N':
            i += 16
        elif self.kind == 'P':
            i += 17
        if self.colour == 'b':
            i += 6

        return int('98' + str(i))

gameboard = Board()
wN = Piece('K', 'b', [])
gameboard.board['e8'] = wN
print(Moves().K('e8', gameboard.board))
bN = Piece('R', 'b', [])
gameboard.board['h8'] = bN
gameboard.move('e8', 'g8')
print(Moves().arbitrary('e8', gameboard.board))
