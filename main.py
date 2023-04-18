import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import getpass
import shutil
class CampusNet:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.driver = None
        self.root = tk.Tk()
        self.root.title("一键校园网 1.0.0")
        self.root.geometry("300x400")
        self.create_gui()

    def create_gui(self):
        # 创建输入框
        username_label = tk.Label(self.root, text="请输入用户名：")
        username_label.pack(pady=10)
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=10)

        password_label = tk.Label(self.root, text="请输入密码：")
        password_label.pack(pady=10)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=10)

        # 创建按钮
        self.save_button = tk.Button(self.root, text="保存", command=self.save_user_info)
        self.save_button.pack(pady=10)

        
    def boot_selfstart(self):
        a=os.path.basename(sys.argv[0])#获取自身文件名
        d=getpass.getuser()#获取用户名
        b=r'C:\\Users'
        b+='\\'+d+'\\'+r'AppData\\Roaming\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
        c=b#启动目录
        b+='\\'+a
        if os.path.exists(b):#判断文件是否已复制
            print("我已经有啦"+b)
        else:
            shutil.copy(a,c)#复制文件到启动目录 
            print("复制完成")

    def connect_wifi(self):
        # 连接WiFi
        os.system('netsh wlan connect name="NHWiFi"')

    def open_webpage(self):
        # 打开网页
        self.driver = webdriver.Chrome()
        self.driver.get("http://172.16.255.253/a70.htm")
        self.driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[2]')\
            .send_keys(self.username_entry.get())
        self.driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[3]')\
            .send_keys(self.password_entry.get())
         
        # 点击选项栏
        self.driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/select')\
            .click()
    
        # 选择中国移动
        self.driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/select/option[3]')\
            .click()
    
        # 点击确定
        self.driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[1]')\
            .click()
        os.system('taskkill /F /IM chrome.exe')
    def close_window(self):
        # 关闭窗口
        self.root.destroy()

    def save_user_info(self):
        # 保存用户信息
        with open("user_info.txt", "w") as f:
            f.write(self.username_entry.get() + "\n")
            f.write(self.password_entry.get() + "\n")
        self.connect_wifi()
        self.open_webpage()
        self.root.after(5, self.close_window)

    def load_user_info(self):
        # 加载用户信息
        if os.path.exists("user_info.txt"):
            with open("user_info.txt", "r") as f:
                self.username = f.readline().strip()
                self.password = f.readline().strip()
                self.username_entry.insert(0, self.username)
                self.password_entry.insert(0, self.password)
                self.connect_wifi()
                self.open_webpage()
                self.root.after(1, self.close_window)

if __name__ == "__main__":
    campus_net = CampusNet()
    campus_net.load_user_info()
    campus_net.boot_selfstart()
    campus_net.root.mainloop()









