from  pymysql import*


conObj=connect(host='localhost',user='root',password='')

qry="create database suresh"

curObj=conObj.cursor()

curObj.execute(qry)

print("database has created")