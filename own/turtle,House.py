import turtle as t
import time
class A:
    def squar1():
        t.shape('turtle')
        t.pencolor('red')
        t.bgcolor("black")
        t.pensize(3)
        t.begin_fill()
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        t.left(90)
        t.forward(100)
        '''for i in range(4):
            t.left(90)
            t.forward(100)'''
class B(A):
    def triangle():
        t.backward(100)
        t.left(155)
        t.forward(102)
        t.right(123)
        t.forward(108)
       
  
B()
B.squar1()
B.triangle()

time.sleep(5)