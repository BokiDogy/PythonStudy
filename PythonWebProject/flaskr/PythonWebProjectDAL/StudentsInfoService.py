from flaskr.PythonWebProjectDAL import OracleHelper as oh
from flaskr.PythonWebProjectModels.StudentsInfo import Student
import pandas as pd

db = oh.OracleHelper()


class StudentsInfoService(object):

    def turndatalist(self,dbdata):
        oracledf = pd.DataFrame(dbdata)
        oracledf.columns = ['stuid', 'classid', 'stuname', 'birthday', 'stusex', 'address']
        result = []
        for index, row in oracledf.iterrows():
            s = Student()
            s.stuid = row["stuid"]
            s.classid = row["classid"]
            s.stuname = row["stuname"]
            s.birthday = row["birthday"]
            s.stusex = str(row["stusex"]).replace(' ', '')
            s.address = row["address"]
            result.append(s)
        return result

    def QueryAllStudentsInfo(self):
        sql = "select * from TEST_0323STRDENTS t"
        sqldata = db.ExecuteSelect(sql)
        result = self.turndatalist(sqldata)
        return result

    def querystu(self,words):
        sql = '''select *
                  from test_0323strdents t
                 where t.stuid in (select a.stuid
                                     from (select s.stuid,
                                                  replace(s.stuid || s.classid || s.stuname ||
                                                          s.birthday || s.stusex || s.address,
                                                          ' ',
                                                          '') allinfo
                                             from test_0323strdents s) a
                                    where instr(a.allinfo, :words) > 0)'''
        paras=[]
        paras.append(words)
        sqldata = db.ExecuteSelect(sql,paras)
        result = self.turndatalist(sqldata)
        return result

    def checkincolumns(self,newinfo):
        sql="SELECT column_name FROM all_tab_cols WHERE table_name = upper('test_0323strdents')"
        sqldata = db.ExecuteSelect(sql)
        for c in newinfo.keys():
            cname=c.upper()
            if not (cname,) in sqldata:
                return False
            else:
                sqldata.remove((cname,))
        return True

    def addnewstu(self,newinfo):
        isincolumns=self.checkincolumns(newinfo)
        if not isincolumns:
            return 0
        else:
            columns=""
            values=""
            paras=[]
            for k in newinfo.keys():
                columns=columns+k+","
                values=values+":"+k+","
                paras.append(newinfo[k])
            if len(columns)>0 and len(values)>0:
                columns=columns[:-1]
                values=values[:-1]
            sql=f"insert into test_0323strdents ({columns}) values ({values})"
            result=db.ExecuteNonSelect(sql,paras)
            return result

    def updatestu(self,sid,newinfo):
        isincolumns = self.checkincolumns(newinfo)
        if not isincolumns:
            return 0
        setsql=""
        paras=[]
        for k in newinfo.keys():
            setsql+=f" {k} = :{k},"
            paras.append(newinfo[k])
        if len(setsql)>0:
            setsql=setsql[:-1]
        sql=f"update test_0323strdents s set {setsql} where s.stuid=:stuid"
        paras.append(sid)
        result = db.ExecuteNonSelect(sql, paras)
        return result

    def delstu(self, sid):
        sql=f"delete test_0323strdents s where s.stuid=:stuid"
        result = db.ExecuteNonSelect(sql, [sid])
        return result