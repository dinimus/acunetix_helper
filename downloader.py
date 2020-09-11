#!/usr/bin/env python3
from core import ACUX
import sys, time
import traceback

API_KEY = "api_key" # CHANGE_IT
SERVER = "ip:3443" # CHANGE_IT

if len(sys.argv) > 2:
	targ = open(sys.argv[1], 'r').read().splitlines()
	urls = list((targ))
	date = sys.argv[2]
else:
	print("urls.txt and first report's date (year-month-day) required\nFor example: " + sys.argv[0] + " urls.txt 2020-01-31")
	exit()
	
acunetix = ACUX(host=SERVER,api=API_KEY,timeout=30)
downloads = []
allreports = acunetix.reports()

for i in range(0,len(allreports['reports'])):
	for j in range(0,len(urls)):
		if allreports['reports'][i]['source']['description'].split(';')[0] == urls[j] and allreports['reports'][i]['generation_date'].split('T')[0] >= date:
			downloads.append(allreports['reports'][i]['download'][0]) # you can change 0 to 1 if you want to download pdf format
n = 1
for link in downloads:
	try:
		filename, filecontent = acunetix.downloader(endpoint=link)
		print(str(n) + ". Report created: " + filename)
		n += 1
		# print(filecontent)
		with open(filename, "wb") as file:
			file.write(filecontent)
		time.sleep(1)
	except:
		print("Downloading error")
		print(traceback.format_exc())
		exit()
