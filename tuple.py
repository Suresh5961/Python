'''S=(1,2,3,"ABCD",2.0,'a')
print(type(S))

H=("suresh")
H1=("suresh",)  # using , tuple
print(type(H))
print(type(H1))
print(len(H))

print(H[2])

print(H[-1])

print(H[0:3])  #n-1 

print(H[2:])
print(H[:2])'''

#tuple change to--> list Then do Change,(Add,remove..ex)


Z=("bala","deena","Krishna","Kabi")
print(type(Z),Z)

X=list(Z)
print(X)
X[2]="b"
Z=tuple(X)
print(Z)

X.append("ram")   
X.insert(1,"A1")
X.remove("bala")
print(X)

C=tuple(X)  #---> again change to tuple
print(C)


D=C*2     
print(D)

W=(1,2,3,4,1,2,1)
S=W.count(2)    #--show how many time repeted the given num
print(S)
T=W.index(2)  #--print given num position
print(T)