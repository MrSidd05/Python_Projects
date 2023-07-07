def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
                

#even this question i was unable to solve
#this question says that the robotll sart from any postion and any direction and the hint is check for the right side if the right is clear then move right if not then move straight else move left