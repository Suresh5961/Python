#To get user input list
list=[]
a=int(input("Enter number of elements in list:"))
for i in range(0,a):
    ele=int(input("Enter elements:"))
    list.append(ele)
print("List are created :",list)

#Concatinated Two Lists
List1=[1,2,3,4,5]
List2=[6,7,8,9,10]
for i in List2:
    List1.append(i)
print("List are concatinated :\n",List1)


# Find negative number &positive num numbers in a list
n=int(input("Enter a range of numbers:"))
even_number=[]
odd_number=[]
for i in range(0,n+1):
    if i%2==0:
        even_number.append(i)
    else:
        odd_number.append(i)
print("even_numbers are printed:\n",even_number)
print("odd_numbers are printed:\n",odd_number)

#Find even or odd 
even_number=[]
odd_number=[]
for i in range(0,10):
    if i%2==0:
        even_number.append(i)
    else:
        odd_number.append(i)
print("even_numbers are printed:\n",even_number)
print("odd_numbers are printed:\n",odd_number)
'''
'''#remove negative numbers in the list
lista=[-6,7,-9,2,-5,3,4,9,-5,0]
for i in lista:
    if i<=0:
       lista.remove(i)
print("negative numbers are removed:\n",lista)