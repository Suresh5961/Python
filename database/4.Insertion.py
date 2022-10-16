from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

curObj=conObj.cursor()

#insertion/update/delete
conObj.autocommit(True)

nm=input("Enter the name ")
pf=input("Tell us your profession ")
ct=int(input("Tell us family members count "))
mob=int(input("Tell us contact number "))
sl=float(input("Tell us your salary "))

'''
varchar >> str  >> %s
int >> %d
float >> %f

'''

qry="""insert into apartment(name,profession,family,contact,salary) values('%s','%s',%d,%d,%f)"""%(nm,pf,ct,mob,sl)

curObj.execute(qry)

print("Record has inserted")