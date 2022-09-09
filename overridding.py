#over ridding

class a:
    def name(self):
        print("ip")
class b(a):                 #inharitence to a  in b  
    def name(self):
        super().name()
        print("nithya")
class c(b):
    def name(self):
        super().name()    #reffer to parents class
        print("aarthi")

x=c()
x.name()