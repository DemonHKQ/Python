import threading
from scapy.all import *
import paramiko
import tkinter as tk
import optparse
import sys

class MyThread(threading.Thread):
    def __init__(self,func,*args):
        super().__init__()

        self.func = func
        self.args = args

        self.setDaemon(True)
        self.start()

    def run(self):
        self.func(*self.args)


def run_ssh(host,user,passwd):
    global ip_entry
    global user_entry
    global passwd_entry
    global box_list
    host = ip_entry.get()
    user = user_entry.get()
    passwd = passwd_entry.get()

    box_list.delete(tk.END)
    if len(host) > 0 and len(user) > 0 and len(passwd) > 0:
        try:
            box_list.insert(tk.END,"开始建立连接： " + host)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname = host , username = user , password = passwd)
            shell = ssh.invoke_shell()
            send_command(shell)
            shell.close()
            ssh.close()
        except Exception as e:
            print(str(e))
    else:
        box_list.delete(tk.END)
        box_list.insert(tk.END,"请输入正确参数")
def send_command(shell):
    global box_list
    box_list.insert(tk.END,"连接成功")
    t = threading.Thread(target = receive , args = (shell,))
    t.start()
    try:
        while True:
            cmd = sys.stdin.read(1)
            if cmd :
                shell.send(cmd)
            if not cmd:
                break
    except EOFError:
        pass
def receive(shell):
    try:
        while True:
            data = shell.recv(1024)
            if not data:
                sys.stdout.write("\r\n----------EOF-----------\r\n")
                sys.stdout.flush()
                break
            if data:
                sys.stdout.write(data.decode("utf-8"))
                sys.stdout.flush()
    except:
        pass 



root = tk.Tk()
root.geometry("500x200")
root.iconbitmap("D:\\0myico.ico")
root.title("ssh登录 By--Ryan_UX")

ip_label = tk.Label(root,text = "IP:").place(x = 5 , y = 0 , width = 10 , height = 30)
ip_entry = tk.Entry(root)
ip_entry.place(x = 20 , y = 0 , width = 190 , height = 30)

user_label = tk.Label(root,text = "username:").place(x = 215 , y = 0 , width = 60 , height = 30)
user_entry = tk.Entry(root)
user_entry.place(x = 280 , y = 0 , width = 50 , height = 30)

passwd_label = tk.Label(root,text = "passwd:").place(x = 330 , y = 0 , width = 50 , height = 30)
passwd_entry = tk.Entry(root,show = "*")
passwd_entry.place(x = 380 , y = 0 , width = 115 , height = 30)

ssh_button = tk.Button(root , text = "连接" , command = lambda :MyThread(run_ssh,ip_entry,user_entry,passwd_entry)).place(x = 10 , y = 40 , width = 480 , height = 30 )

box_list = tk.Listbox(root)
box_list.place(x = 10 , y = 80 , width = 480 , height = 110)

sb = tk.Scrollbar(box_list,command = box_list.yview()).pack(side = "right" , fill = "y")

tk.mainloop()
