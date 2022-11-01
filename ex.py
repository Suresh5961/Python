from pymysql import*

conObj=connect(host='localhost',user='root',password='')
qry="creat database myfile"
curObj=conObj.cursor()
curObj.execute(qry)

print("create sssucess")

def insert(name,age,place):
    pass

def update(name,age,place):
    pass

def delete(id):
    pass

def select():
    pass

while True:
    print("1.insertdata")
    print("2.update")
    print("3.delete")
    print("4,select data")
    print("5.exit")
    Choice=int(input("enter ur choice"))

if choice==1:
    name=input("enter name")
    age=input("enter age")
    place=input("enter place")

    insert(name,age,place)

elif choice==2:
    name=input("enter name")
    age=input("enter age")
    place=input("enter place")

    update(name,age,place)



elif choice==4:
    name=input("enter name")
    age=input("enter age")
    place=input("enter place")

    select(name,age,place)

elif choice==3:
    id=input("enter the id to delete")
    delete(id)
elif choice==5:
    quit()

else:
    print("invalid select")