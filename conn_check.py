#!/usr/bin/python
import os, time
from time import sleep
from subprocess import Popen, PIPE

response = 1

while True:
# If the response from ping is 0, internet is up
   while response != 0:
     # Ping 8.8.8.8 once to check connection. This is a public DNS server of Google
     response = os.system("ping -c 1 " + “8.8.8.8”)
     if response != 0: # Restart the wireless interface
	print("Internet not available")
	cmd = "sudo ifdown --force wlan0 && sudo ifup wlan0" 
	# eth0 to restart ethernet although this is not essential since the connection is automatically detected over ethernet
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	time.sleep(60) # Wait for 60 seconds before trying again
     

