'''class A:
    def __init__(self):     #constractor to intialized the object
        print("happy to see")
    
    def b(self):                  #function
        print("feeling sad")
    
a=A()  #only called constractor object     # a is object

a.b()
'''

#constractor using parameter
'''
class com:
    def __init__(self,name,age,college):
        print("name",name)
        print("age",age)
        print("college",college)
    
B=com("aarthi",21,"mec")   #parameter passings'''

#accessing constractor object in normal finction using "self" keyword


class S:
    def __init__(self,place,company):
          self.A=place
          self.B=company
    def fun(self):
        print("place:",self.A) #using self keyword access costractor object
        print("company:",self.B)

F=S("Chennai","CTS")
F.fun()

#addition program

class H:
    def __init__(self,polu,dolu):
        self.a=polu
        self.b=dolu
    def Add(self):
        d=self.a+self.b
        print("Add",d)
A=H(40,20)
A.Add()


