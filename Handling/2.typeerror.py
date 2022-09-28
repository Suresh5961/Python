hai=[23.5,8,89,54,87,96,8,0,'name']

try:
    pos=int(input("tell us position"))

    print(hai[pos]/2)

except TypeError as obj:
    print(obj,"\nenter the position not 8th one")
    pos=int(input("tell us position"))
    print(hai[pos]/2)