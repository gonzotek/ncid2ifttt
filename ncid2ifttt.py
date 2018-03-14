#!/usr/bin/python
#-*-coding: utf-8-*-

#
# python ncid-client to pass caller id data to an ifttt webhook trigger
#

import socket
import re
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
	host = "127.0.0.1"
	port = 3333
	maker_key = "SECRET_KEY_HERE"
	maker_event = "phone_call"
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
				pyfttt.send_event(maker_key, maker_event, nmbr)
				#n.show()
				#time.sleep(20)
				#n.close()
	except:
		pass
	finally:
		s.close()


if __name__ == "__main__":
	main()

