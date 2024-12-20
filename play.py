from MyService import MyService
import tkinter
from tkinter.filedialog import askopenfilenames


class PlayWindow :
    def __init__(self , myService) :
        self.myService = myService
        self.listbox = None

    # 导入音乐
    def impMusic(self , even) :
        print('点击了导入音乐按钮')
        # 打开磁盘选择音乐
        files = askopenfilenames(filetypes = [("mp3","*.mp3")])
        # 导入音乐，将选择的音乐保存到数据库
        self.myService.add_music(files)
        self.flush_list()

    # 查询当前用户的音乐列表
    def flush_list(self) :
        # 清空列表
        self.listbox.delete(0 , tkinter.END)
        # 查询该用户的所有音乐列表
        music_list = self.myService.findListByUser()
        if music_list :
            for m in music_list :
                self.listbox.insert(tkinter.END , m)

    # 播放音乐
    def playMusic(self , even) :
        print('点击了播放音乐按钮')
        # 获取播放的音乐
        index = self.listbox.curselection()
        music_name = self.listbox.get(index)
        # 调用方法播放音乐
        self.myService.playMuisc(music_name)

    # 删除音乐
    def deleteMusic(self , even) :
        print('点击了删除音乐按钮')
        # 获取删除音乐的名称
        index = self.listbox.curselection()
        music_name = self.listbox.get(index)
        print(music_name)
        # 调用删除方法删除音乐
        self.myService.delete_music(music_name)
        # 刷新列表
        self.flush_list()

    def showWindow(self) :
        # 显示窗口
        top = tkinter.Tk()

        # 添加按钮
        play_button = tkinter.Button(top , text = "播放")
        imp_button = tkinter.Button(top , text = "导入音乐")
        delete_button = tkinter.Button(top , text = "删除")
        play_button.grid(row = 0 , column = 0 , padx = 5 , pady = 5)
        imp_button.grid(row = 0 , column = 2 , padx = 5 , pady = 5)
        delete_button.grid(row = 0 , column = 4 , padx = 5 , pady = 5)

        # 添加列表
        self.listbox = tkinter.Listbox(top)
        self.listbox.grid(row = 1 , column = 0 , padx = 5 , pady = 5 , columnspan = 9)

        # 给按钮添加点击事件
        imp_button.bind("<ButtonRelease-1>" , self.impMusic)
        play_button.bind("<ButtonRelease-1>" , self.playMusic)
        delete_button.bind("<ButtonRelease-1>" , self.deleteMusic)

        # 添加音乐列表
        self.flush_list()

        top.mainloop()


if __name__ == "__main__" :
    uname = input("请输入用户名:")
    password = input("请输入密码:")
    myservice = MyService()
    if myservice.login(uname , password) :
        print('登录成功')
        playWindow = PlayWindow(myservice)
        playWindow.showWindow()

    else :
        print('登录失败')