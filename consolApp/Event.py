
from datetime import datetime


class Event:
    def __init__(self,nm="",dt=datetime.utcnow,dp=""):
        self.__eveName=nm
        self.__eveDate=dt
        self.__eveDepartment=dp;
        self.__participants=[]
        self.__winner=""
    
    # setter
    def setName(self,nm=""):self.__eveName=nm
    def setDate(self,dt=datetime.utcnow):self.__eveDate=dt
    def setDepartment(self,dp=""):self.__eveDepartment=dp
    def setParticipants(self,part=[]):self.__participants=part
    def setWinner(self,win=""):self.__winner=win
    
    # getter
    def getName(self):return self.__eveName
    def getDate(self):return self.__eveDate
    def getDepartment(self):return self.__eveDepartment
    def getParticipants(self):return self.__participants
    def getWinner(self):return self.__winner
    
    def __str__(self):
        return self.__eveName+" "+str(self.__eveDate)+" "+self.__eveDepartment+" "+str(self.__participants)+" "+self.__winner+"\n"
        