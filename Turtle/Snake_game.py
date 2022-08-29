from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600,height=400)
screen.bgcolor("black")
screen.title("My snake Game")

screen.exitonclick()

segment_1= Turtle("square")
segment_1.color("white")

segment_2= Turtle("square")
segment_2.color("white")
segment_2.goto(-20,0)

segment_3= Turtle("square")
segment_3.color("white")
segment_3.goto(-40,0)

starting_positions=[(0,0),(-20,0),(-40,0)]
segments = []

for position in starting_positions:
    new_segment= Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in segments :
        seg.forward(20)
        