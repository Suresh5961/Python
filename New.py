#to find str palindrome or not

a="malayalam"
b=""
for i in a:
    b=i+b
if (a==b):
    print(a,"is palindrome")

else:
    print(a,"it's not palindrome")