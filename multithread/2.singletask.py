from threading import *

class booking(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
        self.__total=50

    def run(self):
        print("welcom",self.name,"to inox multiflex")
        required=int(input("tell us required tickets"))
        if required<=self.__total:
            self.__total-=required
            print(required,"ticket has issued",self.name)
        else:
            print("Available is",self.__total)

a1=booking("suresh")
a2=booking("manoj")
a3=booking("sri")

a1.start()
a1.join()
a2.start()
a2.join()
a3.start()