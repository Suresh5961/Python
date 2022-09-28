from array import *

hai=array('i',[12,67,9,35,89,5,1,3,19])

# fun definition
def show():
    for x in hai:print(x)
    
def update(pos):
    try:
        newone=int(input("tell us new value "))
        hai[pos]=newone
    except IndexError as i:
        print(i)
        # rethrow the error to the caller
        raise i
    

#fun calling
show()
try:
    update(20)
except IndexError as ind:
    print(ind,"Enter the index within",len(hai))
    point=int(input("enter the position "))
    update(point)
show()