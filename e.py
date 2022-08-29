#Posword Program
posword1=int(input("enter pos"))
posword2=int(input("enter pos2 again"))
if (posword1<=8):
    if(posword1==posword2):
        print("currect")
    else:
        print("pos did't match")
else:
    print("need more character") 