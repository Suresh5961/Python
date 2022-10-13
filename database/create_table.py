from pymysql import*

conObj=connect(host='localhost',user='root',password='',db='suresh')

qry="create table apartment(id int(4) not null, name varchar(255) not null,profession varchar(255) not null,family int(2) not null,contact int(10)not null,salary double not null)"

curObj=conObj.cursor()

curObj.execute(qry)

print("table has created")