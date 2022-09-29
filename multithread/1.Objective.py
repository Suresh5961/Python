'''
Multithread:

concurrent process

Thread

class Derived(Thread):
    def run():
        thread execution point

name>> name of the thread

functions:
    start
    sleep
    aquire
    release
    join

single task multithread
multi task multithread

'''

from threading import *


class Fiesta(Thread):
    def __init__(self,nm=""):
        super().__init__()
        self.name=nm
    def run(self):
        print("Welcome ",self.name)

f1=Fiesta("Suresh")
f2=Fiesta("Haripriya")
f3=Fiesta("poluma")

f1.start()
f2.start()
f3.start()