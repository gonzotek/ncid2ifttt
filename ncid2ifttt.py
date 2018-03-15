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
import json

def incomingCall(call):
	nmbr = re.search(r"(NMBR\*)([\w]*)(\*)", call).group(2)
	nmbr = phonenumbers.format_number(phonenumbers.parse(nmbr, 'US'), phonenumbers.PhoneNumberFormat.NATIONAL)
	return nmbr

def main():
	ncid_config= None
	for loc in os.curdir, os.path.expanduser("~"), "/etc/ncid2ifttt", os.environ.get("NCID2IFTTT_CONF"):
		try:
			with open(os.path.join(loc,"ncid-config.json")) as source:
				ncid_config = json.load(source)
		except IOError:
			pass
	#ncid_config = json.load(open('ncid-config.json'))
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
				time.sleep(0.05)
	except:
		pass
	finally:
		s.close()

if __name__ == "__main__":
	main()

