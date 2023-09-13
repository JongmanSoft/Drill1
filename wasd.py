import turtle

def move(a):
    if a == 0:
        turtle.setheading(0)
    elif a == 1:
        turtle.setheading(90)
    elif a == 2:
        turtle.setheading(180)
    else :
        turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
def reset():
    turtle.reset()
