#!/usr/bin/python
#-*-coding: utf-8-*-
# ncid2ifttt is a python ncid-client to pass caller id data to an ifttt webhook trigger

import os
import re
import socket
import time
import json
import phonenumbers
import pyfttt

def incomingCall(call):
	nmbr = re.search(r"(NMBR\*)([\w]*)(\*)", call).group(2)
	nmbr = phonenumbers.format_number(phonenumbers.parse(nmbr, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
	return nmbr

def main():
	ncid_config = None
	for loc in os.curdir, os.path.expanduser("~"), "/etc/ncid2ifttt":
		try:
			with open(os.path.join(loc,"ncid2ifttt-config.json")) as source:
				ncid_config = json.load(source)
		except IOError:
			pass
	ncid_host = ncid_config["ncid_host"]
	ncid_port = ncid_config["ncid_port"]
	ifttt_key = ncid_config["ifttt_key"]
	ifttt_event = ncid_config["ifttt_event"]
	s = socket.socket()
	try:
		s.connect((ncid_host, ncid_port))
		while True:
			data = s.recv(1024)
			if data[:4] == "CID:":
				nmbr = incomingCall(data[:-1])
				pyfttt.send_event(ifttt_key, ifttt_event, nmbr)
			time.sleep(0.1)
	except:
		pass
	finally:
		s.close()

if __name__ == "__main__":
	main()
