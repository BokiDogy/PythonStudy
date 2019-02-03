import os
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'  # 解决中文乱码问题
import cx_Oracle as co


class OracleHelper():
    def __init__(self, constr = "scott/orcl@localhost:1521/orcl"):
        self.constr = constr  # 连接字符串

    def GetOracleConnection(self):
        return co.connect(self.constr)


    def ExecuteNonSelect(self, sql, paras=[]):
        con = self.GetOracleConnection()
        cur = con.cursor()
        cur.execute(sql, paras)
        result = cur.rowcount
        cur.close()
        con.commit()
        con.close()
        return result

    def ExecuteSelect(self, sql, paras=[]):
        con = self.GetOracleConnection()
        cur = con.cursor()
        cur.execute(sql, paras)
        result = cur.fetchall()
        cur.close()
        con.close()
        return result

    def GetFirstRowCol(self, sql, paras=[]):
        con = self.GetOracleConnection()
        cur = con.cursor()
        cur.execute(sql, paras)
        result = None
        if cur.rowcount > 0:
            result = cur.fetchall()[0][0]
        cur.close()
        con.close()
        return result

    def GetPRDResult(self, procname, paras=[]):
        con = self.GetOracleConnection()
        cur = con.cursor()
        result = None
        paras.append(result)
        cur.callproc(procname, paras)
        cur.close()
        con.close()
        return result
