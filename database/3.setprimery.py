from pymysql import*

conObj=connect(host='localhost',user='root',passwd='',db='suresh')

#qry="alter table apartment add primary key(id)"

qry="alter table apartment change id id int(4) auto_increment"

curObj=conObj.cursor()

curObj.execute(qry)

#print("table primary key has added")

print("table AI has add")