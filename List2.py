#Concatinated Two Lists

List1=[3,7,8,9]
List2=[9,6,5,3]
for i in List2:
    List1.append(i)
print("concatinated List \n",List1)

# Find negative number &positive num numbers in a list

lista=[23,-22,99-22,-21,-9,33,44,1,-1]
negative_number=[]
positive_number=[]
for i in lista:
    if i>=0:
        positive_number.append(i)
    elif i<=0:
        negative_number.append(i)
print("negative_number is printed",negative_number)
print("positive_number is printed",positive_number)

#Find even or odd 
even_num=[]
odd_num=[]
for i in range(1,10):
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
print("even_number is",even_num)
print(f"odd_number is {odd_num}")