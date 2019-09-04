# -*- coding: utf-8 -*-

import os
import bottle
from chess import Board, Moves, Piece

gameboard = Board()
gameboard.start_game()

path = os.path.abspath("views")

@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root=path)

@bottle.get('/')
def print_board():
    return bottle.template('test_web.tpl', playboard=gameboard)


@bottle.get('/move_end')
def print_board1():
    return bottle.template('test_web_end.tpl', playboard=gameboard)


@bottle.get('/promote')
def print_promotion():
    return bottle.template('test_web_promotion.tpl')


@bottle.get('/game_log')
def print_game_log():
    return bottle.template('game_log.tpl', game_log=gameboard.game_log)



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
    if move == 'White Promotion' or move == 'Black Promotion':  # needs extra player input
        bottle.redirect('/promote')
    else:
        bottle.redirect('/')


@bottle.post('/promote')
def promote():
    kind = str(bottle.request.forms["i"])
    print(kind)
    gameboard.promotion(kind, start_sq, end_sq)
    bottle.redirect('/')


@bottle.post('/game_log')
def game_log():
    bottle.redirect('/game_log')


@bottle.post('/new_game')
def new_game():
    gameboard.start_game()
    bottle.redirect('/')


bottle.run(debug=True, reloader=True)
