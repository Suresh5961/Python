# append: a

file=open("W-binariFile.txt","a")

# hai=['Razak',89,45,9.1]

# file.write(str(hai))

# say={
#     "front end":"jinja",
#     "back end":['django','flask'],
#     "data base":"mongodb"
# }

# file.write(str(say))

wind=('Zealous',9.2,45,1200,False)

file.write("\n"+str(wind))

file.close()

print("Content appended")