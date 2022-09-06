#single inheritence

class A:
    def name(self):
        print("parent class")

class B(A):
    def name1(self):
        print("child class")
c=B()
c.name()
c.name1()

