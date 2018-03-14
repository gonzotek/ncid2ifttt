#!/usr/bin/python
#-*-coding: utf-8-*-

#
# simple ncid-client
#


import socket
import re
#import pynotify
import phonenumbers
import pyfttt
import os
import time

def incomingCall(call):
	nmbr = re.search(r"(NMBR\*)([\w]*)(\*)", call).group(2)
	nmbr = phonenumbers.format_number(phonenumbers.parse(nmbr, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
	return nmbr

def main():
	# NCID-Server (Vodafone EasyBox 602)
	host = "192.168.1.141"
	port = 3333
	
	s = socket.socket()
	try:
		s.connect((host, port))
		#n = pynotify.Notification("")
		#pynotify.init("liveNCID")
		while True:
			data = s.recv(1024)
			if data[:4] == "CID:":
				#n.update("Incoming Call", incomingCall(data[:-1]), os.path.abspath("./icons/phone_white.png"))
				nmbr = incomingCall(data[:-1])
				pyfttt.send_event("cfRb2o-zPtX7pcIUaDlaU5", "phone_call", nmbr)
				#n.show()
				#time.sleep(20)
				#n.close()
	except:
		pass
	finally:
		s.close()


if __name__ == "__main__":
	main()

