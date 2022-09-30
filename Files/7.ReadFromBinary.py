from pickle import *

obj=open("W-binariFile.txt","rb")

while True:
    try:
        hai=load(obj)
        print(hai)
    except EOFError as e:
        break

obj.close()