import socket
import time
from tqdm import tqdm


def host_name(val):
    try:
        return socket.gethostbyname(val)
    except socket.gaierror:
        print("Invalid Hostname")
        return 

def port_scan(ip,st,end):
    re=[]
    start=time.time()
    for port in tqdm(range(st,end+1),desc="Scanning in progress "):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        st=time.perf_counter()
        c=s.connect_ex((ip,port))
        et=time.perf_counter()
        en=et-st
        try:
            serv=socket.getservbyport(port)
        except:
            serv="Unknown"
        if c==0:
            re.append((port,"Open",serv,en))
        else:
            re.append((port,f"{c}(closed/filtered)",serv,en))
        
    end=time.time()
    s.close()
    t=end-start
    return t,re

