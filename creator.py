#!/usr/bin/env python3
from core import ACUX
import sys, time, os

API_KEY = "api" # CHANGE_IT
SERVER = "ip:3443" # CHANGE_IT

if len(sys.argv) > 2:
	urls = open(sys.argv[1], 'r').read().splitlines()
	SITES = list((urls))
	descr = str(sys.argv[2])
else:
	print("urls.txt and description required\nFor example: " + sys.argv[0] + " urls.txt rogakopyta")
	exit()
	
acunetix = ACUX(host=SERVER,api=API_KEY,timeout=30)
target_ids = []
i = 0

for site in SITES:
	try:
		target_ids.append(acunetix.add_and_start(site,descr)['target_id'])
		print(str(i+1) + ". Created {}".format(site))
		# os.system('echo ' + '"' + target_ids[i] + '" >> t_ids.txt')
		i += 1
		time.sleep(5)
	except:
		print("Starting error")
		pass
