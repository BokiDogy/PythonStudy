import OracleHelper as oh

db=oh.OracleHelper()

# sql="select * from person where name like :sname and  depart_id = :did"
# paras=[]
# paras.append("%王%")
# paras.append(21)
# queryresult=db.ExecuteSelect(sql,paras)
# for p in queryresult:
#     print(f"{p[1]}")

sql="update TEST_0320CLASSES t set t.classname='五年一班' where t.classid=6"
paras=[]
paras.append(7)
paras.append("信息化小组")
dmlcount=db.ExecuteNonSelect(sql)
print(f"删除行数： {dmlcount}")
queryresult=db.ExecuteSelect("select * from TEST_0320CLASSES t ")
for p in queryresult:
    for s in p:
        print(s)
