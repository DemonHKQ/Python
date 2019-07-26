import socket
import time
import xlwt
import tkinter as tk
from threading import *
screenlock = Semaphore(value = 10)

ip = ""
rport = []
class MyThread(Thread):
	def __init__(self,func,*args):
		Thread.__init__(self)
		self.func = func
		self.args = args

		self.setDaemon(True)
		self.start()

	def run(self):
		self.func(*self.args)

def socket_scan(list_ports):
	global get_ports
	global get_ip
	global rport
	global ip
	rport = []
	ip = str(get_ip.get())
	ports = str(get_ports.get())
	list_ports.delete(0,tk.END)

	if len(ip) > 0:
		if len(str(ports)) > 0:
			if "," in ports:
				ports = ports.split(",")
				ports.sort()
				list_ports.insert(tk.END,"Start : " + time.ctime())
				list_ports.insert(tk.END,"Scanning: " + ip)
				for port in ports:
					try:
						socket.setdefaulttimeout(1)
						s = socket.socket()
						s.connect((ip,int(port)))
						rport.append(port)
						list_ports.insert(tk.END,str(port) + "             : " + "Open")
					except:
						pass
				list_ports.insert(tk.END,"Stop : " + time.ctime())

			elif "-" in ports:
				ports = ports.split("-")
				ports.sort()
				list_ports.insert(tk.END,"Start : " + time.ctime())
				list_ports.insert(tk.END,"Scanning: " + ip)
				for port in range(int(ports[0]),int(ports[1])+1):
					try:
						socket.setdefaulttimeout(0.5)
						s = socket.socket()
						s.connect((ip,int(port)))
						rport.append(port)
						list_ports.insert(tk.END,str(port) + "             : " + "Open")
					except:
						pass
				list_ports.insert(tk.END,"Stop : " + time.ctime())
			else:
				list_ports.insert(tk.END,"Start : " + time.ctime())
				list_ports.insert(tk.END,"Scanning: " + ip)
				try:
					socket.setdefaulttimeout(1)
					s = socket.socket()
					s.connect((ip,int(ports)))
					rport.append(ports)
					list_ports.insert(tk.END,str(ports) + "             : " + "Open")
				except:
					pass
				list_ports.insert(tk.END,"Stop : " + time.ctime())

		else:
			list_ports.insert(tk.END,"请输入端口!")
	else:
		list_ports.insert(tk.END,"请输入IP! ")


def xml(list_ports):
	global ip
	global rport

	list_ports.delete(0,tk.END)
	# book = xlwt.Workbook()
	# sheet1 = book.add_sheet("rport")
	if len(str(ip)) > 0 and len(str(rport)) > 0:
		try:
			book = xlwt.Workbook()
			sheet1 = book.add_sheet("rport")
			sheet1.write(0,0,"IP")
			sheet1.write(0,4,"Port")
			sheet1.write(1,0,ip)
			sheet1.write(1,4,",".join(rport))
			filename = "E:\\LX\\" + str(ip) + ".xls"
			book.save(filename)
			list_ports.insert(tk.END,"文件存放于: " + filename)
		except:
			list_ports.insert(tk.END,"Error! ")
	else:
		list_ports.insert(tk.END,"请开始后导出! ")
root = tk.Tk()
root.geometry("500x500")
root.iconbitmap("D:\\0myico.ico")
root.title("端口扫描 By -----Ryan_UX")

ports_label = tk.Label(root,text = "Ports:" , bg = "white")
ports_label.place(x = 10 , y = 0 , width = 40 , height = 30)
get_ports = tk.Entry(root)
get_ports.place(x = 50 , y = 0 , width = 440 , height = 30)

ip_label = tk.Label(root , text = "IP:" , bg = "white")
ip_label.place(x = 10 , y = 40 , width = 40 , height = 30)
get_ip = tk.Entry(root)
get_ip.place(x = 50 , y = 40 , width = 200 , height = 30)

button_ports = tk.Button(root,command = lambda :MyThread(socket_scan,list_ports) , text = "Start")
button_ports.place(x = 260 , y = 40 , width = 110 , height = 30)

button_xml = tk.Button(root , command = lambda :xml(list_ports) , text = "导出").place(x = 380 , y = 40 , width = 110 , height = 30)

list_ports = tk.Listbox(root,selectmode = "MULTIPLE")
list_ports.place(x = 10 , y = 80  , width = 480 , height = 460)
sb_list = tk.Scrollbar(list_ports,command = list_ports.yview)
sb_list.pack(side = "right" , fill = "y")

tk.mainloop()
