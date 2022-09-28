eric=(45,98,4.5,0,12.4,89,53,7,467,67,56,576)

try:
    pos1=int(input("Enter the position to extract data from tuple "))
    pos2=int(input("Enter the position to select the divident from tuple "))
    print(eric[pos1]/eric[pos2])

except IndexError as i:
    print(i,"\nindex should ne less than",len(eric))
    try:
        pos1=int(input("Enter the position to extract data from tuple "))
        pos2=int(input("Enter the position to select the divident from tuple "))
        print(eric[pos1]/eric[pos2])
    except ZeroDivisionError as e:
        print(e,"\nSelect index/pos except 3")
        pos2=int(input("Enter the position to select the divident from tuple "))
        print(eric[pos1]/eric[pos2])