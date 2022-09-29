from threading import*

class house:
    list=[23,78,9,89,10,70,36,67,54,44,55,66,2,3,11,2]

class one(Thread,house):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("welcom",self.name)
        self.list.sort()
        for y in self.list:
            print(y)
class two(Thread,house):
     def __init__(self,nm=""):
        super().__init__()
        self.name=nm
     def run(self):
        lk.acquire()
        print("welcom",self.name)
        pos=int(input("Tell us position to delete"))
        self.list.pop(pos)
        for x in self.list:print(x)
        lk.release()
        
lk=Lock()
        
a1=one("Vinayak")
a2=one("Anand")
b1=two("Tarun")
b2=two("Bajaj")

a1.start()
a2.start()
b1.start()
b2.start()
