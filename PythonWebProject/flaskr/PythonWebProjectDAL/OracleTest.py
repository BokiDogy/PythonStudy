from flaskr.PythonWebProjectDAL import OracleHelper as oh
from flaskr.PythonWebProjectModels.StudentsInfo import Student
import pandas as pd
db=oh.OracleHelper()

# sql="select * from person where name like :sname and  depart_id = :did"
# paras=[]
# paras.append("%王%")
# paras.append(21)
# queryresult=db.ExecuteSelect(sql,paras)
# for p in queryresult:
#     print(f"{p[1]}")

# sql="update TEST_0320CLASSES t set t.classname='五年一班' where t.classid=6"
# paras=[]
# paras.append(7)
# paras.append("信息化小组")
# dmlcount=db.ExecuteNonSelect(sql)
# print(f"删除行数： {dmlcount}")
# queryresult=db.ExecuteSelect("select * from TEST_0320CLASSES t ")
# for p in queryresult:
#     for s in p:
#         print(s)
def QueryAllStudentsInfo():
    sql="select * from TEST_0323STRDENTS t"
    sqldata=db.ExecuteSelect(sql)
    oracledf = pd.DataFrame(sqldata)
    oracledf.columns = ['stuid','classid','stuname','birthday','stusex','address']
    result=[]
    for index,row in oracledf.iterrows():
        s=Student()
        s.stuid=row["stuid"]
        s.classid=row["classid"]
        s.stuname=row["stuname"]
        s.birthday=row["birthday"]
        s.stusex=row["stusex"]
        s.address=row["address"]
        result.append(s)
    return result

allstu=QueryAllStudentsInfo()
for s in allstu:
    print(f"{s.stuid},{s.stuname},{s.stusex},{s.address},{s.classid},{s.birthday}")