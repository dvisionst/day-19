# from turtle import Turtle, Screen
# import random


# def p_instance(papa, xpos, ypos, color):
#     papa.color(color)
#     papa.shape("turtle")
#     papa.shapesize(3, 3, 3)
#     papa.penup()
#     papa.setx(xpos)
#     papa.sety(ypos)
#     papa.pendown()


# def p_pace(p_turtle, distance):
#     p_turtle.forward(distance)




# horizontal = -810
# finish_line = 780
# clergy_screen = Screen()
# papa_nihil = Turtle()
# p_instance(papa_nihil, horizontal, 250, "black")
# print(papa_nihil.heading())

# # papa1 = Turtle()
# # p_instance(papa1, horizontal, 125, "steelblue3")
# # #
# # papa2 = Turtle()
# # p_instance(papa2, horizontal, 0, "goldenrod1")
# #
# # papa3 = Turtle()
# # p_instance(papa3, horizontal, -125, "peru")
# #
# # cardi_c = Turtle()
# # p_instance(cardi_c, horizontal, -250, "DarkRed")

# clergy_screen.exitonclick()

from turtle import Turtle, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
i = 0
xcor = -240
ycor = -75
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = []
for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    turtle_list.append(tim)
    tim.penup()
    tim.goto(xcor, ycor)
    i += 1
    ycor += 25

if user_bet:
    is_race_on = True

while is_race_on:
    some_turtle = random.choice(turtle_list)
    rand_distance = random.randint(0, 10)
    some_turtle.forward(rand_distance)
    race_pos = some_turtle.xcor()
    if race_pos >= 230:
        winner_color = some_turtle.color()
        is_race_on = False
if winner_color[0] == user_bet:
    print(f"Congrats, {winner_color[0]} turtle won the race. You win the bet!")
else:
    print(f"Sorry! The {winner_color[0]} turtle won the race, you lose your bet.")

my_screen.exitonclick()