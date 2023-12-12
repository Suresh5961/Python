import turtle
screen = turtle.Screen()
screen.bgcolor("lightpink")
t=turtle.Turtle()
t.shape('turtle')
t.pensize(3)




def squar():
    for i in range(4):
        t.left(90)
        t.forward(100)

def triangal():
    t.pencolor("black")
    t.left(90)
    t.fd(100)
    t.left(30)
    t.fd(100)
    t.left(120)
    t.fd(100)
    
def regtangular():
    t.left(120)
    t.fd(250)
    t.right(90)
    t.fd(100)
    t.right(90)
    t.fd(150)
def reg():
    t.right(180)
    t.fd(150)
    t.left(90)
    t.fd(185)
    t.left(90)
    t.fd(199)
    t.left(90)
    t.penup()
    t.fd(185)
    t.pendown()
    
    






squar()
triangal()
regtangular()
reg()
