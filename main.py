import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
colors = ["red", "orange", "yellow", "blue", "purple", "green"]
'''Initialize the user bet'''
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win? Enter a color: ")

y_position = -125
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_position)
    y_position += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ! The  {winning_color} is the winner")
            else:
                print(f"You've lost ! The  {winning_color} is the winner")
        random_forward = random.randint(0, 15)
        turtle.forward(random_forward)

screen.exitonclick()