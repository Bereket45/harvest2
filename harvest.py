# AUTHOR: BEREKET WOLDE
# ID: UGR/25575/14

from cs1robots import *
load_world("worlds/harvest2.wld")
hubo=Robot()
hubo.set_pause(0.1)
hubo.set_trace('blue')
def turn_right():
    for i in range(3):
        hubo.turn_left()
def crossway_move():
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()
def pick_and_crossway_move():
    hubo.pick_beeper()
    crossway_move()
def crossway_left_turn():
    hubo.move()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
def crossway_right_turn():
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
def crossway_trip():
    for i in range(5):
        pick_and_crossway_move()
    hubo.pick_beeper()
    crossway_left_turn()
    for i in range(5):
        pick_and_crossway_move()
    hubo.pick_beeper()
    crossway_right_turn()
for i in range(5):
    hubo.move()
hubo.turn_left()
hubo.move()
for i in range(2):
    crossway_trip()
for i in range(5):
    pick_and_crossway_move()
hubo.pick_beeper()
crossway_left_turn()
for i in range(5):
    pick_and_crossway_move()
hubo.pick_beeper()
