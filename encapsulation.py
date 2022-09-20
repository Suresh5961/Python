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
        return self.__model+""+seelf.__brand+""sel
