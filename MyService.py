from dbUtil import Mydb
import pygame


class MyService :
    def __init__(self) :
        self.user = None

    def login(self , uname , password) :
        sql = "select * from t_user where uname=%s and password=%s"
        user = Mydb().execQueryOne(sql , uname , password)
        if user :
            self.user = user
            return True
        else :
            return False

    def add_music(self , files) :
        for f in files :
            start = f.rfind("/") + 1
            end = f.rfind(".mp3")
            music_name = f[start :end]
            # 根据歌名查询数据是否有该首歌
            sql = "select * from t_music where music_name=%s"
            music = Mydb().execQueryOne(sql , music_name)
            if music :
                # 查询关联表t_list 该用户是否添加了这首歌
                sql = "select * from t_list where mid=%s and uid=%s"
                t_list = Mydb().execQueryOne(sql , music[0] , self.user[0])
                if not t_list :
                    sql = "insert into t_list(mid,uid) values(%s,%s)"
                    Mydb().execDML(sql , music[0] , self.user[0])
            else :
                # 将音乐保存到t_music
                sql = "insert into t_music(music_name,path) values(%s,%s)"
                mid = Mydb().execDML(sql , music_name , f)

                # 用户选择的音乐保存到t_list
                sql = "insert into t_list(mid,uid) values(%s,%s)"
                Mydb().execDML(sql , mid , self.user[0])

    # 查询用户的音乐列表
    def findListByUser(self) :
        sql = "select m.music_name from t_music m,t_list t where m.id=t.mid and t.uid=%s"
        return Mydb().execQueryAll(sql , self.user[0])

    # 删除音乐
    def delete_music(self , music_name) :
        # 根据音乐名称查询音乐id
        sql = "select id from t_music where music_name = %s"
        mid = Mydb().execQueryOne(sql , music_name)
        # 删除关联表中的数据及t_list
        sql = "delete from t_list where uid=%s and mid=%s"
        Mydb().execDML(sql , self.user[0] , mid[0])

    # 播放音乐
    def playMuisc(self , music_name) :
        # 根据名称查询音乐的path
        sql = "select path from t_music where music_name=%s"
        path = Mydb().execQueryOne(sql , music_name)
        pygame.mixer.init()
        pygame.mixer.music.load(path[0])
        pygame.mixer.music.play()