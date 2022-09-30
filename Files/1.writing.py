# open("file location","mode")
# modes : w,r,a,wb,rb

# using open can create new file in 'w' mode
obj=open("mybasic.doc","w")
print(obj.name)
obj.write("This is sure kumar's first file")
print(obj.closed)
obj.close()
print(obj.closed)