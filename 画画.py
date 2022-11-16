import turtle

import numpy as np

my_turtle = turtle.Turtle()
my_win1 = turtle.Screen()
my_win=my_win1.setup(0,0,1080,1080)

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.color('red')
        my_turtle.forward(line_len)  # turtle前进
        my_turtle.right(90)   # turtle向右转
        draw_spiral(my_turtle, line_len - 5) #turtle继续前进向右转
draw_spiral(my_turtle, 200)
my_win.exitonclick()


