#value error handling


try: 
   hello=int(input("enter the number"))
   print(hello*2)

except ValueError as v:
       print(v)
       hello=int(input("enter the number values only "))
       print(hello*2)

print("Rach the end")
       