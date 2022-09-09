'''#over loding concept not working in python

class a:
    def aa(self,a):
        print(a)
    def aa(self,a,b):
        print(a+b)
    def aa(self,a,b,c):
        print(a+b+c)
s=a()
#s.aa(10)
#s.aa(21.21)
s.aa(10,21,10) '''   #its automatically last fuc so error will acured




#using python in overloading

class sum:
    def a(self,a=None,b=None,c=None):
       if a!=None and b!=None and c!=None:
           return (a+b+c)
       elif a!=None and b!=None:
           return(a+b)
       else:
            return(a) #or print(a)
            

x=sum()
print("sum",x.a(10,10,10))
print("sum",x.a(10,10))
print("sum",x.a(20))