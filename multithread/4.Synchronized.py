from threading import *

class Find(Thread):
    def __init__(self, nm=""):
        super().__init__()
        self.name=nm
        self.__quick=[34,90,11,56,3,1,35,4,68,45,6,7,85,44,56,8,90]
    def run(self):
        print("welcome",self.name)
        lk.acquire()
        try:
            userData=int(input("Enter the data to search "))
            pos=self.__quick.index(userData)
            print(pos,"where",userData,"exists",self.name)
        except ValueError as v:
            print(v)
            userData=int(input("Enter the data to search "))
            pos=self.__quick.index(userData)
            print(pos,"where",userData,"exists",self.name)
        lk.release()
        print("Thanks you",self.name)
        
lk=Lock()
        
f1=Find("Vimal")
f2=Find("Roggers")
f3=Find("Victor")

f1.start()
f2.start()
f3.start()