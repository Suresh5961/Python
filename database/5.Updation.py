from pymysql import *

conObj=connect(host='localhost',user='root',password='',db='suresh')

curObj=conObj.cursor()

#insertion/update/delete
conObj.autocommit(True)

# update by pk
# qry="""update apartment set profession='Team Lead',salary=salary+0.24 where id=2"""

# update by another field/ condition
qry="""update apartment set salary=salary+0.05 where family>=3"""

curObj.execute(qry)

print("Record has updated")