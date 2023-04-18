import os
import tkinter as tk
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By


# Create GUI
root = tk.Tk()
root.title("一键校园网 1.0.0")
root.geometry("300x400")

#destory windows
def close_window():
    root.destroy()

# Create entry boxes
username_label = tk.Label(root, text="请输入用户名：")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

password_label = tk.Label(root, text="请输入密码：")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=10)

# Save username and password
def save_username_and_password():
    with open("user_info.txt", "w") as f:
        f.write(username_entry.get() + "\n")
        f.write(password_entry.get() + "\n")
    print("用户名和密码已保存")
    # Open main window after saving username and password
    one_click()

save_button = tk.Button(root, text="保存", command=save_username_and_password)
save_button.pack(pady=10)

# Load username and password
if os.path.exists("user_info.txt"):
    with open("user_info.txt", "r") as f:
        username = f.readline().strip()
        password = f.readline().strip()
else:
    username = ""
    password = ""

# Set default values for entry boxes
username_entry.insert(0, username)
password_entry.insert(0, password)

# Create buttons
def connect_wifi_and_open_webpage():
    os.system('netsh wlan connect name="NHWiFi"')
    try:
        driver=webdriver.Chrome()
        driver.get("http://172.16.255.253/a70.htm")
        driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[2]').send_keys(
            username_entry.get())
        driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[3]').send_keys(
            password_entry.get())
         
        #点击选项栏
        driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/select').click()
    
        #选择中国移动
        driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/select/option[3]').click()
    
        #点击确定
        driver.find_element(By.XPATH,'//*[@id="edit_body"]/div[3]/div[3]/form/input[1]').click()
    
        messagebox.showinfo('三秒后自动关闭','连接wifi成功啦！')
        os.system('taskkill /F /IM chrome.exe')
    except:
        messagebox.showinfo('提示','连接wifi失败？')
        
    
def one_click():
    if username_entry.get() and password_entry.get():
        connect_wifi_and_open_webpage()
        root.after(3000, close_window)     
    else:
        print("请输入用户名和密码")



root.mainloop()

