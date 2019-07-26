import tkinter as tk
import socket
import requests
import time
import xlwt
import threading

ress = []
key = []
s = requests.session()
class MyThread(threading.Thread):
	def __init__(self,func,*args):
		super().__init__()

		self.func = func
		self.args = args

		self.setDaemon(True)
		self.start()

	def run(self):
		self.func(*self.args)

def domain_scan(list_info):
	global url_input
	global ress
	global key
	urls = url_input.get()
	ip = []
	if len(urls) > 0:
		list_info.insert(tk.END,"Start Time :------" + str(time.ctime()))
		try:
			url = "https://www.virustotal.com/vtapi/v2/domain/report"
			data = {'apikey':'4ad4e5eed7579fdd2261729ede4279cb8b09162765ef664d2b0bcb00becc5c8f','domain':urls} 
			response = s.get(url , params = data)
			res = response.json()['subdomains']
			for x in res:
				try:
					status = s.get("http://" + x,timeout = 2).status_code
					if status == 200:
						ress.append(x)
				except:
					pass
		except:
			pass
		for x in ress:
			try:
				addr = socket.getaddrinfo(x,"http")[0][4][0]
				ip.append(addr)
			except:
				ip.append(" ")
		key = dict(zip(ress,ip))
		get_url(list_info,ress,key)
	else:
		list_info.insert(tk.END,"请输入域名 ：")

def get_url(list_info,ress,key):
	for x in range(len(ress)):
		list_info.insert(tk.END,str(ress[x]) + "---------" + str(key[ress[x]]))
	list_info.insert(tk.END,"Stop Time :------" + time.ctime())

def xml(url_input,list_info):
	global ress
	global key
	if len(url_input.get()) > 0:
		list_info.insert(tk.END,"开始导出： ")
		try:
			book = xlwt.Workbook()
			sheet1 = book.add_sheet("domain")
			for x in range(len(ress)):
				sheet1.write(x,0,ress[x])
				sheet1.write(x,4,key[ress[x]])
			filename = "E:\\LX\\" + str(url_input.get()) + ".xls"
			book.save(filename)
			list_info.insert(tk.END,"文件存放在 : " +  "E:\\LX\\" + str(url_input.get()) + ".xls")
		except:
			pass
	else:
		list_info.insert(tk.END,"请先查询后导出 ：")

root = tk.Tk()
root.geometry("500x500")
root.iconbitmap("D:\\0myico.ico")
root.title("子域名收集 By--Ryan_UX")

# sb = tk.Scrollbar(root)
# sb.pack(side = "right",fill = "y")

url_input = tk.Entry(root)
url_input.place(x = 10 , y = 0 , width = 490 , height = 30)

list_info = tk.Listbox(root)
list_info.place(x = 10 , y = 80  , width = 480 , height = 460)

button1 = tk.Button(root,command = lambda :MyThread(xml,url_input,list_info) , text = "导出")
button1.place(x = 10 , y = 40 , width = 240 , height = 30)

# button = tk.Button(root ,command = lambda :MyThread(get_url,list_info,ress,key) , text = "查询")
button2 = tk.Button(root ,command = lambda :MyThread(domain_scan,list_info) , text = "查询")
button2.place(x = 260 , y = 40 , width = 240 , height = 30)

sb = tk.Scrollbar(list_info)
sb.pack(side = "right",fill = "y")
sb.config(command = list_info.yview)


tk.mainloop()
