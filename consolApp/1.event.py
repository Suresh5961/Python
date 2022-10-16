

from datetime import datetime


class Event:
    def __init__(self,nm="",dt=datetime.fromisoformat("YYYY-MM-DD"),dp=""):
        self.__eveName=nm
        self.__eveDate=dt
        self.__eveDepartment=dp;
        self.__participants=[]
        self.__winner=""


    #setter

    def setName(self,nm=""):self.__eveName=nm
    def setDate(self,dt=datetime.fromisoformat("YYY-MM-DD")):self.__eveDate=dt
    def setDepartment(self,dp=""):self.__eveDepartment=dp
    def setparticipants(self,part=[]):self.__participants=part
    def setWinner(self,win=""):self.__winner=win


#getter

    def getName(self):return self.__eveName
    def getDate(self):return self.__eveDate
    def getDepartment(self):return self.__eveDepartment
    def getWinner(self):return self.__winner


def __str__(self):
    return self.__eveName+""+str(self.__eveDate)+""+self.__eveDepartment+""+str(self.__participant)+""+self.__winner+"\n"
