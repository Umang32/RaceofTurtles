import turtle
import random

is_race = False

screen = turtle.Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
all_turtle = []


for turtle_index in range(0, 6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race = True

while is_race:
    for turtle in all_turtle:
        if turtle.xcor() > 220:
            is_race = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won {winning_color}")
            else:
                print(f"You have lost and color {winning_color} won")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()
