try:
    hello=int(input("enter the number"))
    print(hello*2)

except ValueError as v:
    print(v)
    hello=int(input("enter the value as numeric not character "))
    print(hello*2)


print("Rach the end")
