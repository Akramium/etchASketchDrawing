from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

heading = 0


def move_forward():
    timmy.forward(50)


def back_forward():
    timmy.back(50)


def turn_left():
    global heading
    heading += 10
    timmy.setheading(heading)


def turn_right():
    global heading
    heading -= 10
    timmy.setheading(heading)


def clear():
    timmy.home()
    timmy.clear()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=back_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
