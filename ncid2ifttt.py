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
		while True:
			data = s.recv(1024)
			if data[:4] == "CID:":
				nmbr = incomingCall(data[:-1])
				pyfttt.send_event(maker_key, maker_event, nmbr)
				time.sleep(0.05)
	except:
		pass
	finally:
		s.close()

if __name__ == "__main__":
	main()

