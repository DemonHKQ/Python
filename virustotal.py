import requests
import socket
import sys
import os
s = requests.session()
class domain():
	def __init__(self,url):
		self.url = url
		self.domain_scan()
	def domain_scan(self):
		url = "https://www.virustotal.com/vtapi/v2/domain/report"
		data = {'apikey':'4ad4e5eed7579fdd2261729ede4279cb8b09162765ef664d2b0bcb00becc5c8f','domain':self.url} 
		response = s.get(url , params = data)
		res = response.json()['subdomains']
		self.cs(res)
	def cs(self,res):
		if len(res) <= 0:
			print("Not Found Domain !")
			sys.exit(0)
		else:
			self.report(res)
	def report(self,res):
		lj = "E:\\LX"
		if os.path.exists(lj) == True:
			lj1 = lj + "\\" + self.url + "_" + "domain.txt"
			with open(lj1,'w+') as file:
				for x in res:
					addr = socket.getaddrinfo(x,'http')[0][4][0]
					print(f"{x}				{addr}")
					data = f"{x}			{addr}"
					file.write(data + "\n")
			os.system("start " + lj1)
		if os.path.exists(lj) == False:
			os.makedirs(lj)
			lj2 = lj + "\\" + self.url + "_" + "domain.txt"
			with open(lj2,'w+') as file:
				for x in res:
					addr = socket.getaddrinfo(x,'http')[0][4][0]
					print(f"{x}				{addr}")
					data = f"{x}			{addr}"
					file.write(data + "\n")
			os.system("start " + lj2)
def main():
	if len(sys.argv) < 2:
		print("usage: \n\t virustotal.py url")
		sys.exit(0)
	url = sys.argv[1]
	domains = domain(url)
if __name__ == "__main__":
	main()