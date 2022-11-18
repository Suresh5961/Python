'''for i in range(4):
        t.left(90)
        t.forward(100)'''

import turtle
t=turtle.Turtle()
t.shape('turtle')
t.pensize(3)
t.pencolor("green")

def squar():
    for i in range(4):
        t.left(90)
        t.forward(100)

def triangal():
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

def door():
    t.left(90)
    t.fd(20)
    for i in range(4):
        t.left(90)
        t.forward(40)
    
    

squar()
triangal()
regtangular()
reg()
door()
