def turn_right():
    turn_left()
    turn_left()
    turn_left()


while front_is_clear():
    move()
turn_left()

while not at_goal():
    if not right_is_clear() and front_is_clear():
        move()
    elif right_is_clear():
        turn_right()
        move()
    elif not front_is_clear():
        turn_left()