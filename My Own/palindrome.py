#to find str palindrome or not

a="malayalam"
b=""
for i in a:
    b=i+b
if (a==b):
    print(a,"is palindrome")

else:
    print(a,"it's not palindrome")

#find number is palindrome or not

N=int(input("Enter num to check palindrome or not :"))
temp=N
reversed_num=0
while (N>0):
    reminder=N%10
    reversed_num=(reversed_num*10)+reminder
    N=N//10
if (temp==reversed_num):
    print(temp,"is paindrome")
else:
    print(temp,"is not palindrome")