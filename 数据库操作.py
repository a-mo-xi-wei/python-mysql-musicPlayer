import pymysql

if __name__ == '__main__' :

    connection = None
    cursor = None
    try :
        connection = pymysql.connect(host = 'localhost' , user = 'root' , password = '123456' ,
                                     db = "student" , charset = 'utf8')
        print(connection)

        cursor = connection.cursor()

        # sql = ("insert into students(name,age,grade) values('kali',33,2)")
        #
        # count = cursor.execute(sql)
        #
        # print("count: ",count)
        #
        # sql = ("update students set grade = 3 where name = 'kali'")
        #
        # count = cursor.execute(sql)
        #
        # print("count: ",count)

        sql = ("delete from students where name = 'kali'")

        count = cursor.execute(sql)

        print("count: " , count)

        # 执行DML时会开启一个事务，需要自行提交
        connection.commit()

        sql = "select * from students"

        cursor.execute(sql)

        ans = cursor.fetchall()

        for a in ans :
            print(a , end = '\n')
    except Exception as e :
        print("Error: " , e)
        if connection :
            connection.rollback()
    finally :
        if cursor :
            cursor.close()
        if connection :
            connection.close()
