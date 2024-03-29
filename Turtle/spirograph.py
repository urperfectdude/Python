import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
colors = ["Red","Blue","Green","Yellow"]

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    
    for _ in range (int (360/size_of_gap)): 
        tim.color(random.choice(colors))
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
    
draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()






