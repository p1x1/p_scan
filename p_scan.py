#!/usr/bin/python2.7

import sys, socket
from datetime import datetime as dt
from colorama import init,Fore

init(autoreset=True)

def help_panel():
	print "-"*50
	print Fore.RED + "[!] HELP PANEL "
	print "-"*50
	print Fore.GREEN + "\n\t [*] python p_scan.py" + Fore.YELLOW + " <IP>"

def banner():
	print "-"* 50
	print Fore.YELLOW+"[*]Scanning target --> " + target
	print Fore.YELLOW+"[#]Time started --> " +str(dt.now())
	print "-"* 50


if __name__ == "__main__":

	if len(sys.argv) == 2:
		target = socket.gethostbyname(sys.argv[1])
	else:
		help_panel()
		sys.exit(1)

	banner()
	try:
		for port in range(0,65535):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result == 0:
				print Fore.RED+"[!] Port {p} is open".format(p=port)
			s.close()

	except KeyboardInterrupt:
		print Fore.YELLOW+"[!] Exiting ..."
		sys.exit(1)
	except socket.gaierror:
		print Fore.YELLOW+"[!] Hostname could not be resolved"
		sys.exit(1)
	except socket.error:
		print Fore.YELOW+"[!] Cant connect to the server" + target
		sys.exit(1)
