#encapulation 
# data hidding >> even object creat to the class directly, can't access the data/var/objcet
#but can access the function

from tokenize import ContStr
from xml.sax.handler import feature_external_ges


class laptop:

    def __init__(self,mob="",bnd="",cost=0,feat=""):
        self.__model=mob
        self.__brand=bnd
        self.__price=cost
        self.__fetures=feat


    def setmodel(self,mod=""):
        self.__model=model=mod
    def setbrand(self,bnd=""):self.__brand=bnd
    def setfeture(self,feat=0):self.__feture=feat
    def setprice(self,cost=0):self.__price=cost


    def getmodel(self):return self.__model
    def getbrand(self):return self.__brand
    def getprice(self):
        return self.__price

    def __str__(self):
        return self.__model+" "+self.__brand+" "+self.__features+" "+str(self.__price)
    

#initialize via constructor
mob1=Mobile("5S","Realme",8999,"128GB Internal")
print(mob1.getBrand(),mob1.getFeatures(),mob1.getModel(),mob1.getPrice())

mob2=Mobile()
print(hasattr(mob2,"__brands"))
mob2.setBrand("Nokia")
mob2.setFeatures("64 Internal")
mob2.setModel("6.1Plus")
mob2.setPrice(9888)
print(mob2)

#print(hasattr(mob2,"brands"))
