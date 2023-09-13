import turtle

def d():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
def s():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def a():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
def w():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def reset():
    turtle.reset()

turtle.shape('turtle')
turtle.onkey(d,'d')
turtle.onkey(s,'s')
turtle.onkey(a,'a')
turtle.onkey(w,'w')
turtle.onkey(reset,'Escape')
turtle.listen()

