#Fibonacci
fib=int(input("How many terms? :"))
count=0
n1,n2=0,1
if fib<=0:
    print("please enter positive num")
elif fib==1:
    print("sequency number up to :",fib)
    print(n1)
else:
    while count<fib:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1


