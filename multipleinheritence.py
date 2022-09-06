# multiple inheritence
#two base class and one derived class
class travel:         #base class1
    def name(self):
        print("car travel")

class travel2:        #base class 2
    def name2(self):
        print("bike travel")
class travel3(travel,travel2):   #drived class
    def name3(self):
        print("train travel")
    
a=travel3()
a.name()
a.name2()
a.name3()