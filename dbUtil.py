import pymysql

class Mydb:
    config = {
        'host' : 'localhost',
        'user' : 'root',
        'password' : '123456',
        'db' : "music",
        'charset' : 'utf8'  # 字符集，utf8保证中文正常显示
    }
    def __init__(self):
        self.connection = pymysql.connect(**Mydb.config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    def execDML(self,sql,*args):
        try:
            count = self.cursor.execute(sql,args)
            self.connection.commit()
            return count
        except Exception as e:
            print(e)
            if self.connection:
                self.connection.rollback()

    def execQueryOne(self,sql,*args):
        try:
            self.cursor.execute(sql,args)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
    def execQueryAll(self,sql,*args):
            try:
                self.cursor.execute(sql,args)
                return self.cursor.fetchall()
            except Exception as e:
                print(e)

if __name__ == "__main__":
    dbUtil = Mydb()
    sql = "delete from students where name = %s"
    count = dbUtil.execDML(sql,"jack")
    print(dbUtil.execQuery("select * from students"),end = '\n')

    #sql = "select * from students where name = 'jack'"
    #print(dbUtil.execQueryOne(sql))
