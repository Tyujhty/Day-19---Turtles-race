from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "orange", "yellow", "blue", "purple", "green"]
'''Initialize the user bet'''
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle is going to win? Enter a color: ")

y_position = -125

for turtle_index in range(0, 6):
    tony = Turtle(shape="turtle")
    tony.color(colors[turtle_index])
    tony.penup()
    tony.goto(x=-240, y=y_position)
    y_position += 50



screen.exitonclick()