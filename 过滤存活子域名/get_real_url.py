# Get multiple domain name resolutions as files
import requests
import dns.resolver
import tldextract
import threading
import sys
import argparse
import time
import re


info = []
ip_list = []
thread_max = threading.BoundedSemaphore(200)
threads_list = []

class threads_get(threading.Thread):
    def __init__(self,domain):
        threading.Thread.__init__(self)
        self.domain = domain
    def run(self):
        self.domain = domian_extract(self.domain)
        getcname = get_record_cname(self.domain)
        getdns = get_record_a(self.domain)
        getns = get_record_ns(self.domain)

        if getdns is not None:
            getdns_str = ",".join(f"{x}" for x in getdns)
        else:
            getdns = ""

        if getcname is not None:
            getcname = getcname
        else:
            getcname = ""

        if getns is not None:
            getns = getns
        else:
            getns = ""

        try:
            print('{:<35s}{:<35s}{:<35s}{:<35s}'.format(self.domain, getcname, getns, getdns_str))
            str1 = '{:<35s}{:<35s}{:<35s}{:<35s}'.format(self.domain, getcname, getns, getdns_str)
            info.append(str1)
        except:
            pass

        if getdns is not None:
            ip_list.append(getdns)
        thread_max.release()


def domian_extract(domain):

    source_domain = tldextract.extract(domain)
    if source_domain.subdomain == '':
        domain = "{}.{}".format(source_domain.domain, source_domain.suffix)
    else:
        domain = "{}.{}.{}".format(source_domain.subdomain, source_domain.domain, source_domain.suffix)
    return domain


# Get CNAME record
def get_record_cname(domain):

    domian_extract(domain)
    try:
        domain = dns.resolver.query(domain, "CNAME")
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 5:
                    return ip.to_text()
    except:

        return None


# Get A record

def get_record_a(domain):

    try:
        domain = dns.resolver.query(domain, "A")
        iplist = []
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 1:
                    iplist.append(ip.address)
        return iplist

    except:

        return None


# Get NS record

def get_record_ns(domain):

    domian_extract(domain)

    try:

        domain = dns.resolver.query(domain, "NS")
        for domain in domain.response.answer:
            for ip in domain.items:
                if ip.rdtype == 2:
                    return ip.to_text()
    except:

        return None




def get_record_file(file_path):

    if file_path is  None:
        sys.exit(1)
    with open(file_path) as f:
        print("{:<35s}{:<35s}{:<35s}{:35s}".format("Domain", "CNAME", "NS", "A"))
        for line in f:
            domain = line.strip("\n")
            thread_max.acquire()
            t = threads_get(domain)
            t.start()
            threads_list.append(t)
        for tt in threads_list:
            tt.join()


        # Formatting to remove duplicate IP
        formatList = []
        for id in ip_list:
            if id not in formatList:
                formatList.append(id)
        myList = [x for j in formatList for x in j]
        print("=" * 12, "remove duplicates info", "=" * 14)
        print("{}".format(myList))
        with open(f"./{sys.argv[1].split('.')[0]}_ips.txt","a+") as file:
            for x in myList:
                file.write(x + "\n")
        with open(f"./{sys.argv[1].split('.')[0]}_info.txt","a+") as f:
            f.write("{:<35s}{:<35s}{:<35s}{:35s}".format("Domain", "CNAME", "NS", "A") + "\n")
            for x in info:
                f.write((x + "\n"))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('''
usage:
    python3 get_domain_info.py domain.txt
            ''')    
        sys.exit()
    else:
        get_record_file(sys.argv[1])
