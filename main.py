# import colorgram          # colorgram package is installed here
#
# colors = colorgram.extract("spotpainting.jpg", 30)
## extract() returns color objects with artibutes rgb , hsl

# rgb_list = []
# for color in colors:
#     red = color.rgb[0]
#     green = color.rgb[1]
#     blue = color.rgb[2]
#     # each color objects has artibutes rgb which is a tuple with (red_value, green_value, blue_value)
#     rgb_tuple = (red, green, blue)
#     rgb_list.append(rgb_tuple)
#
# print(rgb_list)
## after printing list of rgb tuples we copy it and use it in turtle graphics to create spot painting
## after copying we select only those rgb values that do not indicate background color

colors_list_rgb = [(176, 49, 81), (19, 110, 163), (49, 169, 112), (53, 126, 60), (231, 201, 76), (229, 130, 96), (212, 87, 115), (16, 61, 135), (118, 169, 209), (27, 55, 81), (232, 70, 28), (152, 64, 38), (139, 196, 169), (159, 206, 203), (82, 49, 60), (180, 168, 61), (33, 89, 50), (200, 133, 151), (255, 207, 0), (222, 178, 185), (231, 175, 163), (59, 158, 170)]

import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()      # hides the path of turtle and turtle shape too



tim.setheading(225)
tim.forward(300)
tim.setheading(0)
for _ in range(10):
    for moves in range(10):
        tim.dot(20, random.choice(colors_list_rgb))
        tim.forward(50)
        if (moves+1)%10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)







screen = Screen()
screen.exitonclick()

