#Author: WOODNET (https://woodnet.000webhostapp.com/)
#Github: https://github.com/Woodnet
#21.03.2020
#Python 3.7
from scapy.all import *
from scapy.all import Ether
from colorama import *
from datetime import datetime
import time,os

init()
now = datetime.now()

def sniffing(pkt):
    blacklist = open("blacklist.txt", "r")
    data = blacklist.read()
    blacklist.close()
    if (IP in pkt):
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        f = True
    else:
        f = False
    if (TCP in pkt):
        tcp_sport = pkt[TCP].sport
        tcp_dport = pkt[TCP].dport
    else:
        f = False
    if (f == True):
        m = True
        if (str(ip_dst) not in data and str(ip_src) not in data):
            print(Fore.WHITE + " [" + Fore.RED + " %s"%(now) + Fore.WHITE + " ] " + Fore.GREEN + " [+] %s:%s"%(str(ip_src),(tcp_sport)) + Fore.YELLOW + " --> " + Fore.GREEN + " %s:%s"%(str(ip_dst),(tcp_dport)))
            print(" ")
            m = False
        if (str(ip_dst) in data and str(ip_src) in data):
            print(Fore.WHITE + " [" + Fore.RED + " %s"%(now) + Fore.WHITE + " ] " + Fore.CYAN + " [+] %s:%s"%(str(ip_src),(tcp_sport)) + Fore.YELLOW + " --> " + Fore.CYAN + " %s:%s"%(str(ip_dst),(tcp_dport)))
            print(" ")
            m = False
        if (m == True):
            if (str(ip_src) in data):
                print(Fore.WHITE + " [" + Fore.RED + " %s"%(now) + Fore.WHITE + " ] " + Fore.CYAN + " [+] %s:%s"%(str(ip_src),(tcp_sport)) + Fore.YELLOW + " --> " + Fore.GREEN + " %s:%s"%(str(ip_dst),(tcp_dport)))
                print(" ")
                m = False
            if (m == True):
                if (str(ip_dst) in data):
                    print(Fore.WHITE + " [" + Fore.RED + " %s"%(now) + Fore.WHITE + " ] " + Fore.GREEN + " [+] %s:%s"%(str(ip_src),(tcp_sport)) + Fore.YELLOW + " --> " + Fore.CYAN + " %s:%s"%(str(ip_dst),(tcp_dport)))
                    print(" ")
                    m = False
    time.sleep(1.5)
try:
    os.system("cls")
except:
    os.system("clear")
print(" ")
print(" ")
c = input(Fore.YELLOW + "Counter" + Fore.CYAN + ">>>" + Fore.YELLOW + " ")
n_ip = input(Fore.YELLOW + "Own IP-Address" + Fore.CYAN + ">>>" + Fore.YELLOW + " ")
x = 0
m = 0
while (x < int(c)):
    if (m == 0):
        m += 1
        print(Fore.WHITE + " [" + Fore.RED + " %s"%(now) + Fore.WHITE + " ] " + Fore.YELLOW + " [*] Sniffing..")
        print(" ")
    sniff(filter="ip",count=24,prn=sniffing)
    sniff(filter="ip and host %s"%(n_ip),count=24,prn=sniffing)
    sniff(filter="tcp",count=24,prn=sniffing)
    x += 1
