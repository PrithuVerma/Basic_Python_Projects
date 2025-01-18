from turtle import *
import random

screen = Screen()
screen.setup(width=500,height=500)
bet = screen.textinput(title="Make your bet", prompt='Choose a color tp bet on a turtle : ')
colors = ['red','orange','blue','green','purple','yellow']
y_positions = [-100 , -50, 0 , 50, 100, 150 ]

for i in range(0,6):
    Jikki = Turtle(shape='turtle')
    Jikki.penup()
    Jikki.goto(x= -200, y= y_positions[i])
    Jikki.color(random.sample(colors, 1))

screen.exitonclick()


