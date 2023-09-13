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

turtle.shape('turtle')
turtle.onkey(move(0),'d')
turtle.onkey(move(1),'s')
turtle.onkey(move(2),'a')
turtle.onkey(move(3),'w')
turtle.onkey(reset,'Escape')
turtle.listen()

