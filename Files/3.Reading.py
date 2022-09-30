# reading: r mode

#obj=open("mybasic.doc","r")

#obj=open("D:\PythonClass//types of error.txt","r")

obj=open("D:\PythonClass//types of error.txt","r")

# data=obj.read()
# print(data)

data=obj.read(100)
print(data)

obj.close()