from turtle import *
import turtle
import time

t=turtle.Turtle()
t.speed(2)


t.shape("turtle")
t.pensize(10)
t.pencolor("blue")
t.penup()
t.bk(300)
t.pendown()
class A:
    def Pp():
        t.right(90)
        t.fd(130)
        t.bk(100)
        t.fd(50)
        t.left(90)
        t.circle(40,180)
        t.right(180)
    def Oo():
        t.penup()
        t.forward(100)
        t.pendown()
        t.left(180)
        t.circle(50)
    def Ll():
        t.penup()
        t.left(180)
        t.forward(70)
        t.pendown()
        t.right(90)
        t.forward(100)
        t.left(90)
        t.forward(50)
    def Uu():
        t.penup()
        t.forward(25)
        t.pendown()
        t.left(90)
        t.forward(100)
        t.bk(100)
        t.right(90)
        t.forward(50)
        t.left(90)
        t.forward(100)
        t.right(90)
        t.penup()
        t.forward(100)
        t.pendown()
A()
A.Pp()
A.Oo()
A.Ll()
A.Uu()
time.sleep(5)
class B:
    T= turtle.Turtle()
    T.shape("turtle")
    def heart():
        for i in range(200):
            pen.right(10)
            pen.forward(19)
B()
B.heart()