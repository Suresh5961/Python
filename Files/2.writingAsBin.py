# writing file as binary which helps to write data as same format
# also prevent to open file in general mode

from pickle import *

obj=open("W-binariFile.txt","wb")

hai=['Razak',89,45,9.1]

say={
    "front end":"jinja",
    "back end":['django','flask'],
    "data base":"mongodb"
}

wind=('Zealous',9.2,45,1200,False)

# # binary format
# quick=dumps(say)
# print(quick)

dump(hai,obj)
dump(say,obj)
dump(wind,obj)

obj.close()