from flaskr.PythonWebProjectDAL.StudentsInfoService import StudentsInfoService


class StudentsInfoManager(object):
    def __init__(self):
        self.ss = StudentsInfoService()

    def QueryAll(self):
        return self.ss.QueryAllStudentsInfo()

    def querystu(self,words):
        return self.ss.querystu(words)

    def addnewstu(self,newinfo):
        return self.ss.addnewstu(newinfo)