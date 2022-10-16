from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

# qry="alter table apartment add primary key(id)"

# qry="alter table apartment change id id int(4) auto_increment"
qry="alter table apartment change contact contact bigint(10)"

curObj=conObj.cursor()

curObj.execute(qry)

# print("Table Primary key has added")

print("Table AI has added")