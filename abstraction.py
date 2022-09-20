#abstraction :hinding the logic/body of the function

from abc import *              #To create abstraction function --abc

class wind(ABC):
    def hello(self):
        print("non abstraction method")


def there(self):
    pass                       #to use pass overriden the function other class

class Derive(wind):
    def own (self):
        print("Derive's own function")

    def there(self):              
        print("there derived/overriden fromwind")


d=Derive()
d.hello()
d.there()
d.own()





