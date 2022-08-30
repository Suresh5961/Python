a={1,3,4,5,'a',"SS","CC"}
print(type(a))
print(a)
print(len(a))

a.add("S1")
print(a)

b={1,2,3,4,5,6,7,"CC",'b'}

a.update(b)
print(a)
 
a.remove("SS")   #discard,remove,pop--- delete 
print(a)

a.discard('a')
print(a)

print(a.pop())
print(a)