from datetime import datetime
from pickle import dump, load
from Event import Event

class Organise:
    def __init__(self):
        self.__events=[]
    def pickling(self):
        file=open("suresh.doc","wb")
        # e1=Event("PPT",datetime.fromisoformat("2022-10-20"),"CSE")
        # self.__events.append(e1)
        dump(self.__events,file)
        file.close()
    def unpickling(self):
        file=open("suresh.doc","rb")
        self.__events=load(file)
        file.close()
    
    def plan(self,obj):
        self.unpickling()
        self.__events.append(obj)
        self.pickling()
        print(obj.getName(),"by",obj.getDepartment(),"has scheduled on",obj.getDate())
        
    def viewAll(self):
        self.unpickling()
        for x in self.__events:
            print(x)
    
    def enroll(self,person="",wish=""):
        self.unpickling()
        for x in self.__events:
            if x.getName() == wish:
                x.getParticipants().append(person)
                print(person,"has enrolled in",x.getName(),"on",x.getDate())
                self.pickling()
                return
        else:
            print(wish,"event doesn't found")
    
    def announce(self,person="",eve=""):
        self.unpickling()
        for x in self.__events:
            if x.getName()==eve:
                if person in x.getParticipants():
                    x.setWinner(person)
                    self.pickling()
                    print(person,"announced as winner",x.getName(),"held on",x.getDate())
                    return
        else:
            print(eve,"not found anywhere/",person,"is not part of event")
    
e1=Event("RoboExpo",datetime.fromisoformat("2022-12-01"),"Mech")
org=Organise()
# org.pickling()
# org.plan(e1)
# org.enroll("Annamalai","PPT")
# org.enroll("Manoj","CodeVita")
# org.enroll("Suresh","PPT")
# org.enroll("Hari","PPT")
# org.enroll("Vignesh","PPT")
# org.enroll("Victor","PPT")
# org.enroll("Manoj","PPT")
# org.enroll("Razak Mohamed","CodeVita")
# org.enroll("Sabari","CodeVita")

org.announce("Suresh","RoboExpo")
org.announce("Suresh kumar","PPT")
org.announce("Suresh","Paper")

org.announce("Hari","PPT")
org.announce("Manoj","CodeVita")

org.viewAll()