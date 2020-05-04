import threading
import requests
import sys

real_domain = []
bad_domain = []
threads = []
port_list = [80,7001,8000,8080,9080,9081,9090,9200,9300,11211]
s = requests.session()
thread_max = threading.BoundedSemaphore(200)

class get_real_url(threading.Thread):
	def __init__(self,url,port):
		threading.Thread.__init__(self)
		self.url = url
		self.port = port
	def run(self):
		try:
			urls = str(self.url).strip()
			self.url = f"http://{str(self.url).strip()}:{self.port}/"
			codes = s.head(self.url,timeout = 3).status_code
			if(codes == 200 or codes == 301 or codes == 302 or codes == 403 or codes ==401):
				real_domain.append(self.url)
				print(f"{self.url.strip()}  is real")
			else:
				bad_domain.append(url)
		except:
			pass
		thread_max.release()


def real_url(file):
	with open(f"./{sys.argv[1]}","r") as files:
		with open(f"./{sys.argv[1].split('.')[0]}","w+") as filess:
			print("Start:..........")
			for url in files.readlines():
				for port in port_list:
					thread_max.acquire()
					starts = get_real_url(url,port)
					starts.start()
					threads.append(starts)
			for t in threads:
				t.join()
			print(f"real_url: 	{len(real_domain)}")
			filess.write(f"real_url : {len(real_domain)}" + "\n")
			for url in real_domain:
				filess.write(url + "\n")
			# filess.write("bad_url : " + "\n")
			# for bad in bad_domain:
			# 	filess.write(bad + "\n")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('''
usage:
	python3 get_real_domain.py files.txt
			''')	
		sys.exit()
	else:
		real_url(sys.argv[1])
