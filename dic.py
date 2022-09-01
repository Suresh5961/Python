'''# two position 1.key 2.value
a={"name":"SS","age":21,"name2":"HH"}
print(type(a),a)
print(a["age"])
print(len(a))


#method 1.get  2.keys 3.value 4.add
b={"name":"pp","age":21,"frds":["sam","ip","nithya"]}
print(b)
print(b["age"])

c=b.get("name")
print(c)
c=b.keys()
print(c)

b["bike"]="Ns"   #-->add key and value
print(b)

c=b.values()  #--->only print  value
print(c)

b["age"]=26   #---->change values
print(b)

b.update({"name":"SH"})   #----> also change values
print(b)
'''
#remove method 1.pop ,2.popitem 3.del 4.clear
x={"name":"oo","age":"21","frds":["sam","ip","nithya"],"food":"biriyani"}
print(x)

print(x.pop("name"))
#print(x)

x.popitem()   # remove  last item 
print(x)

del x["age"]
print(x)

x.clear()
print(x)

#for loop using
y={"name":"pp","age":21,"game":"crikt","frds":["sam","ram","ip"]}
print(y)

for i in y:
    print(y[i])
for i in y.values():
    print(i)
for i in y.keys():
    print(i)
for i,j in y.items():
    print(i,j)







