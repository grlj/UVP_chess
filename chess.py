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

    def castle(self, K_square, K_end_square, kind):
        if kind == 'long':
            R_square = 'a'
            R_end_square = 'd'
            move = 'O-O-O'
        else:
            R_square = 'h'
            R_end_square = 'f'
            move = 'O-O'
        if self.board[K_square].colour == 'b':
            temp_number = '8'
        else:
            temp_number = '1'
        R_square += temp_number
        R_end_square += temp_number
        self.board[K_end_square] = self.board[K_square]
        self.board[K_square] = False
        self.board[R_end_square] = self.board[R_square]
        self.board[R_square] = False
        self.game_log.append(move)
        self.board[K_end_square].move_log.append(move)
        self.board[R_end_square].move_log.append(move)
        self.switch_player()
        return kind.capitalize() + ' Castling'

    def en_passant(self, P_square, P_end_square, direction):
        if self.board[P_square].colour == 'b':
            row = '4'
        else:
            row = '5'
        temp_figure = self.board[P_square]
        taken_figure = self.board[chr(ord(P_square[0]) + int(direction)) + row]
        self.board[P_end_square] = temp_figure
        self.board[P_square] = False
        self.board[chr(ord(P_square[0]) + int(direction)) + row] = False
        if self.check_if_check((self.find_pieces('K', temp_figure.colour)[0])):
            self.board[P_square] = temp_figure
            self.board[P_end_square] = False
            self.board[chr(ord(P_square[0]) + int(direction)) + row] = taken_figure
            return False
        else:
            temp_figure.move_log.append(P_end_square)
            self.game_log.append(temp_figure.kind + P_end_square)
            self.switch_player()
            return 'En Passant'

    def move(self, start_square, end_square):  # preforms the move + castling + promotion + en passant
        temp_figure = self.board[start_square]
        if not temp_figure:
            return False
        elif self.player_to_move != temp_figure.colour:
            return False
# castling
        elif temp_figure.kind == 'K' and start_square == 'e1' and end_square == 'c1':
            if self.check_for_move('e1', 'd1') and self.check_for_move('e1', 'c1') and not self.check_if_check('e1'):
                return self.castle(start_square, end_square, 'long')
        elif temp_figure.kind == 'K' and start_square == 'e1' and end_square == 'g1':
            if self.check_for_move('e1', 'f1') and self.check_for_move('e1', 'g1') and not self.check_if_check('e1'):
                return self.castle(start_square, end_square, 'short')
        elif temp_figure.kind == 'K' and start_square == 'e8' and end_square == 'c8':
            if self.check_for_move('e8', 'd8') and self.check_for_move('e8', 'c8') and not self.check_if_check('e8'):
                return self.castle(start_square, end_square, 'long')
        elif temp_figure.kind == 'K' and start_square == 'e8' and end_square == 'g8':
            if self.check_for_move('e8', 'f8') and self.check_for_move('e8', 'g8') and not self.check_if_check('e8'):
                return self.castle(start_square, end_square, 'short')
# promotion
        elif temp_figure.kind == 'P' and end_square[1] == '8' and temp_figure.colour == 'w' and self.check_for_move(start_square, end_square):
            return 'Black Promotion'
        elif temp_figure.kind == 'P' and end_square[1] == '1' and temp_figure.colour == 'b' and self.check_for_move(start_square, end_square):
            return 'White Promotion'
# en passant
        elif temp_figure.kind == 'P' and start_square[1] == '5' and temp_figure.colour == 'w' and not self.board[end_square] and (end_square[0] == chr(ord(start_square[0]) + 1) or end_square[0] == chr(ord(start_square[0]) - 1)):
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) + 1) + '5' and len(self.board[chr(ord(start_square[0]) + 1) + '5'].move_log) == 1:
                return self.en_passant(start_square, end_square, '1')
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) - 1) + '5' and len(self.board[chr(ord(start_square[0]) - 1) + '5'].move_log) == 1:
                return self.en_passant(start_square, end_square, '-1')
        elif temp_figure.kind == 'P' and start_square[1] == '4' and temp_figure.colour == 'b' and not self.board[end_square] and (end_square[0] == chr(ord(start_square[0]) + 1) or end_square[0] == chr(ord(start_square[0]) - 1)):
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) + 1) + '4' and len(self.board[chr(ord(start_square[0]) + 1) + '4'].move_log) == 1:
                return self.en_passant(start_square, end_square, '1')
            if self.game_log[-1] == 'P' + chr(ord(start_square[0]) - 1) + '4' and len(self.board[chr(ord(start_square[0]) - 1) + '4'].move_log) == 1:
                return self.en_passant(start_square, end_square, '-1')
# else
        elif self.check_for_move(start_square, end_square):
            self.board[start_square] = False
            self.board[end_square] = temp_figure
            temp_figure.move_log.append(end_square)
            self.game_log.append(temp_figure.kind + end_square)
            self.switch_player()
            return 'Move'
        else:
            return False

    def start_game(self):
        for i in self.board:
            self.board[i] = False
        self.board['e8'] = Piece('K', 'b', [])
        self.board['d8'] = Piece('Q', 'b', [])
        self.board['f8'] = Piece('B', 'b', [])
        self.board['c8'] = Piece('B', 'b', [])
        self.board['g8'] = Piece('N', 'b', [])
        self.board['b8'] = Piece('N', 'b', [])
        self.board['h8'] = Piece('R', 'b', [])
        self.board['a8'] = Piece('R', 'b', [])
        self.board['a7'] = Piece('P', 'b', [])
        self.board['b7'] = Piece('P', 'b', [])
        self.board['c7'] = Piece('P', 'b', [])
        self.board['d7'] = Piece('P', 'b', [])
        self.board['e7'] = Piece('P', 'b', [])
        self.board['f7'] = Piece('P', 'b', [])
        self.board['g7'] = Piece('P', 'b', [])
        self.board['h7'] = Piece('P', 'b', [])

        self.board['e1'] = Piece('K', 'w', [])
        self.board['d1'] = Piece('Q', 'w', [])
        self.board['f1'] = Piece('B', 'w', [])
        self.board['c1'] = Piece('B', 'w', [])
        self.board['g1'] = Piece('N', 'w', [])
        self.board['b1'] = Piece('N', 'w', [])
        self.board['h1'] = Piece('R', 'w', [])
        self.board['a1'] = Piece('R', 'w', [])
        self.board['a2'] = Piece('P', 'w', [])
        self.board['b2'] = Piece('P', 'w', [])
        self.board['c2'] = Piece('P', 'w', [])
        self.board['d2'] = Piece('P', 'w', [])
        self.board['e2'] = Piece('P', 'w', [])
        self.board['f2'] = Piece('P', 'w', [])
        self.board['g2'] = Piece('P', 'w', [])
        self.board['h2'] = Piece('P', 'w', [])
        self.game_log = []
        self.player_to_move = 'w'


class Moves:

    def is_on_playboard(self, square):
        if 0 < ord(square[0]) - 96 < 9 and 0 < int(square[1:]) < 9:
            return True
        else:
            return False

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

    def check_if_ok(self, square, test_square, playboard):  # does not check if given square is inside playboard
        if not playboard[square]:
            return 1
        elif playboard[square].colour != playboard[test_square].colour:
            return 2
        elif playboard[square].colour == playboard[test_square].colour:
            return 3

    def straight_move(self, square, direction, sign, playboard):
        if direction == 'horizontal':
            letter_coef = sign
            number_coef = 0
        else:
            letter_coef = 0
            number_coef = sign
        i = 1
        possible_squares = []
        while self.is_on_playboard(chr(ord(square[0]) + i * letter_coef) + str(int(square[1]) + i * number_coef)):
            temp_square = chr(ord(square[0]) + i * letter_coef) + str(int(square[1]) + i * number_coef)
            if self.check_if_ok(temp_square, square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break
        return possible_squares

    def diagonal_move(self, square, vertical_sign, horizontal_sign, playboard):
        possible_squares = []
        i = 1
        while self.is_on_playboard(chr(ord(square[0]) + i * horizontal_sign) + str(int(square[1]) + i * vertical_sign)):
            temp_square = chr(ord(square[0]) + i * horizontal_sign) + str(int(square[1]) + i * vertical_sign)
            if self.check_if_ok(temp_square, square, playboard) == 1:
                possible_squares.append(temp_square)
                i += 1
            elif self.check_if_ok(temp_square, square, playboard) == 2:
                possible_squares.append(temp_square)
                break
            else:
                break
        return possible_squares

    def K(self, test_square, playboard):
        possible_squares = []

        for i in range(-1, 2):
            for j in range(-1, 2):
                temp_square = chr(ord(test_square[0]) + j) + str(int(test_square[1]) + i)
                if self.is_on_playboard(temp_square) and self.check_if_ok(temp_square, test_square, playboard) in [1, 2]:
                    possible_squares.append(temp_square)

        if playboard[test_square].move_log == []:  # for check_for_move to work - castling
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
        return self.R(test_square, playboard) + self.B(test_square, playboard)

    def R(self, test_square, playboard):
        possible_squares = self.straight_move(test_square, 'horizontal', 1, playboard)
        possible_squares += self.straight_move(test_square, 'horizontal', -1, playboard)
        possible_squares += self.straight_move(test_square, 'vertical', 1, playboard)
        possible_squares += self.straight_move(test_square, 'vertical', -1, playboard)
        return possible_squares

    def B(self, test_square, playboard):
        possible_squares = self.diagonal_move(test_square, 1, 1, playboard)
        possible_squares += self.diagonal_move(test_square, 1, -1, playboard)
        possible_squares += self.diagonal_move(test_square, -1, -1, playboard)
        possible_squares += self.diagonal_move(test_square, -1, 1, playboard)
        return possible_squares

    def N(self, test_square, playboard):
        possible_squares = []

        for i in [-2, 2]:
            for j in [-1, 1]:
                temp_square1 = chr(ord(test_square[0]) + i) + str(int(test_square[1]) + j)
                temp_square2 = chr(ord(test_square[0]) + j) + str(int(test_square[1]) + i)
                if self.is_on_playboard(temp_square1) and temp_square1 != test_square:
                    if self.check_if_ok(temp_square1, test_square, playboard) in [1, 2]:
                        possible_squares.append(temp_square1)
                if self.is_on_playboard(temp_square2) and temp_square2 != test_square:
                    if self.check_if_ok(temp_square2, test_square, playboard) in [1, 2]:
                        possible_squares.append(temp_square2)
        return possible_squares

    def P(self, test_square, playboard):  # en passant and promotion entairely carried out in move
        possible_squares = []
        if playboard[test_square].colour == 'w':
            coef = 1
            start_line = '2'
        else:
            coef = -1
            start_line = '7'
        temp_square1 = test_square[0] + str(int(test_square[1]) + 1 * coef)
        temp_square2 = test_square[0] + str(int(test_square[1]) + 2 * coef)
        if self.is_on_playboard(temp_square1) and not playboard[temp_square1]:
            possible_squares.append(temp_square1)
        if self.is_on_playboard(temp_square2) and test_square[1] == start_line and not playboard[temp_square2] and not playboard[temp_square1]:
            possible_squares.append(temp_square2)
        for i in [1, -1]:
            temp_square = chr(ord(test_square[0]) + i) + str(int(test_square[1]) + 1 * coef)
            if self.is_on_playboard(temp_square) and playboard[temp_square] and playboard[temp_square].colour != playboard[test_square].colour:
                possible_squares.append(temp_square)
        return possible_squares


class Piece:

    def __init__(self, kind, colour, possible_squares):
        self.kind = kind
        self.colour = colour
        self.possible_squares = possible_squares
        self.move_log = []

    def encode(self):  # utf-8 html for piece (missing &# needed)
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
