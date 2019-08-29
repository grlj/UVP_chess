# -*- coding: utf-8 -*-

import bottle
from chess import Board, Moves, Piece

bottle.TEMPLATE_PATH.insert(0, 'views')

gameboard = Board()
bK = Piece('K', 'b', [])
bQ = Piece('Q', 'b', [])
bR1 = Piece('R', 'b', [])
bR2 = Piece('R', 'b', [])
bB1 = Piece('B', 'b', [])
bB2 = Piece('B', 'b', [])
bN1 = Piece('N', 'b', [])
bN2 = Piece('N', 'b', [])
bP1 = Piece('P', 'b', [])
bP2 = Piece('P', 'b', [])
bP3 = Piece('P', 'b', [])
bP4 = Piece('P', 'b', [])
bP5 = Piece('P', 'b', [])
bP6 = Piece('P', 'b', [])
bP7 = Piece('P', 'b', [])
bP8 = Piece('P', 'b', [])

wK = Piece('K', 'w', [])
wQ = Piece('Q', 'w', [])
wR1 = Piece('R', 'w', [])
wR2 = Piece('R', 'w', [])
wB1 = Piece('B', 'w', [])
wB2 = Piece('B', 'w', [])
wN1 = Piece('N', 'w', [])
wN2 = Piece('N', 'w', [])
wP1 = Piece('P', 'w', [])
wP2 = Piece('P', 'w', [])
wP3 = Piece('P', 'w', [])
wP4 = Piece('P', 'w', [])
wP5 = Piece('P', 'w', [])
wP6 = Piece('P', 'w', [])
wP7 = Piece('P', 'w', [])
wP8 = Piece('P', 'w', [])
gameboard.board['e8'] = bK
gameboard.board['d8'] = bQ
gameboard.board['f8'] = bB1
gameboard.board['c8'] = bB2
gameboard.board['g8'] = bN1
gameboard.board['b8'] = bN2
gameboard.board['h8'] = bR1
gameboard.board['a8'] = bR2
gameboard.board['a7'] = bP1
gameboard.board['b7'] = bP2
gameboard.board['c7'] = bP3
gameboard.board['d7'] = bP4
gameboard.board['e7'] = bP5
gameboard.board['f7'] = bP6
gameboard.board['g7'] = bP7
gameboard.board['h7'] = bP8

gameboard.board['e1'] = wK
gameboard.board['d1'] = wQ
gameboard.board['f1'] = wB1
gameboard.board['c1'] = wB2
gameboard.board['g1'] = wN1
gameboard.board['b1'] = wN2
gameboard.board['h1'] = wR1
gameboard.board['a1'] = wR2
gameboard.board['a2'] = wP1
gameboard.board['b2'] = wP2
gameboard.board['c2'] = wP3
gameboard.board['d2'] = wP4
gameboard.board['e2'] = wP5
gameboard.board['f2'] = wP6
gameboard.board['g2'] = wP7
gameboard.board['h2'] = wP8

@bottle.get('/')
def print_board():
    return bottle.template('test_web.tpl', playboard = gameboard)

@bottle.get('/move_end')
def print_board1():
    return bottle.template('test_web_end.tpl', playboard = gameboard)

@bottle.get('/promote')
def print_board2():
    return bottle.template('test_web_promotion.tpl')


start_sq = ''
end_sq = ''

@bottle.post('/move_start')
def move_start():
    global start_sq
    start_sq = bottle.request.forms["i"]
    bottle.redirect('/move_end')

@bottle.post('/move')
def move_end():
    global end_sq
    end_sq = bottle.request.forms["i"]
    move = gameboard.move(start_sq, end_sq)
    if move == 'Promotion':
        print('jaaaj')
        bottle.redirect('/promote')
    else:
        bottle.redirect('/')

@bottle.post('/promote')
def promote():
    kind = str(bottle.request.forms["i"])
    print(kind)
    gameboard.promotion(kind, start_sq, end_sq)
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)
