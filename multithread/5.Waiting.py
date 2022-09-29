from threading import *
from time import sleep

class React(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
        self.click=[45,90,11,34,2.34,6.7,6.5,66,4,54,4,54.5,6.76,6,5]
    def run(self):
        print("welcome",self.name)
        for x in self.click:
            print(x)
            sleep(2)

r1=React("Annamalai")
r2=React("Sabari")
r3=React("Manoj")

r1.start()
r1.join()
r2.start()
r2.join()
r3.start()