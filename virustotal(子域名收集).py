import requests
import socket
import xlwt
import sys
import os
import nmap
s = requests.session()
ip = []
ports = "21,22,23,25,110,80,111,137,139,443,445,143,514,873,1433,1521,1500,1723,2080,2083,2181,2601,3128,3312,3311,3306,3389,3690,4848,5000,6379,7001,7002,7778,8000,8443,8069,8080,8089,9080,9081,9091,9200,9300,27017,27017,50070,50030"

class domain():
	def __init__(self,url):
		self.url = url
		self.domain_scan()

	def domain_scan(self):
		url = "https://www.virustotal.com/vtapi/v2/domain/report"
		data = {'apikey':'4ad4e5eed7579fdd2261729ede4279cb8b09162765ef664d2b0bcb00becc5c8f','domain':self.url} 
		response = s.get(url , params = data)
		res = response.json()['subdomains']   #获取所有子域
		print("********************收集子域中********************")
		self.cs(res)

	def cs(self,res):
		if len(res) <= 0:   #判断获取成功没
			print("Not Found Domain !")
			sys.exit(0)
		else:
			try:
				for x in res:
					ip.append(socket.getaddrinfo(x,"http")[0][4][0])
			except:
				pass
			key = dict(zip(res,ip))
			self.url_status(res,key)

	def url_status(self,res,key):
		lj = "E:\\LX"
		ress = []
		if os.path.exists(lj) == True:  #判断路劲是否存在
			for x in res:
				try:
					response = s.get("http://" + x,timeout = 2)  #判断域名是否可访问 
					if response.status_code == 200:
						print(x + "*********200 OK! " + "  IP:--------------: " + key[x])
						ress.append(x)
				except:
					pass
			self.xml(ress,lj,key)
		if os.path.exists(lj) == False:
			os.makedirs(lj)
			for x in res:
				try:
					response = s.get("http://" + x,timeout = 2) 
					if response.status_code == 200:
						print(x + "*********200 OK! " + "  IP:--------------: " + key[x])
						ress.append(x)
				except:
					pass
			self.xml(ress,lj,key)

	def xml(self,res,lj,key):
		book = xlwt.Workbook()#创建一个Excel
		sheet1 = book.add_sheet("domain")  #在里面创建一个名为domain的sheet
		print("**********子域端口信息收集中************")
		for x in range(len(res)):
			scan_port = []
			#ipaddr = socket.getaddrinfo(res[x],"http")[0][4][0]
			self.nmap_scan(key[res[x]],scan_port)
			sheet1.write(x,0,res[x])  #往sheet第x行第一列写入数据
			sheet1.write(x,4,key[res[x]])
			sheet1.write(x,8,str(scan_port))
		filename = lj + "\\" + self.url + ".xls"
		book.save(filename)

	def nmap_scan(self,ip,scan_port):
		try:
			print(f"[*] {ip}")
			nm = nmap.PortScanner()
			nm.scan(hosts = ip,arguments = f"-T4 -Pn -p {ports}")
			rports = list(nm[str(ip)]["tcp"].keys())
			rports.sort()
			for rport in rports:
				scan_port.append(rport)
		except:
			pass

def main():
	if len(sys.argv) < 2:
		print("usage: \n\t python virustotal.py url")
		sys.exit(0)

	domain_scan = domain(sys.argv[1])

if __name__ == "__main__":
	main()