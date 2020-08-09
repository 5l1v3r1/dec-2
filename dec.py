#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#Author D4RK5H4D0W5
C1 = '\033[1;36m'
G0 = '\033[0;32m'
W0 = '\033[0;37m'
R0 = '\033[0;31m'
import requests, sys, os
from bs4 import BeautifulSoup
try:
	os.system('cls' if os.name == 'nt' else 'clear')
	print '''%s
    ____  __________________  ______  ______
   / __ \/ ____/ ____/ __ \ \/ / __ \/_  __/  %sCoded by D4RKSH4D0WS%s
  / / / / __/ / /   / /_/ /\  / /_/ / / /     %sIG @anonroz_team%s
 / /_/ / /___/ /___/ _, _/ / / ____/ / /      %sFB gg.gg/AnonRoz-Team%s
/_____/_____/\____/_/ |_| /_/_/     /_/       MD5, SHA1, SHA256, SHA384, and SHA512%s
	'''%(C1,W0,C1,W0,C1,W0,C1,W0)
	for dec in open(sys.argv[1]).read().splitlines():
		print 
		print 'Decrypt   :',dec
		api=requests.post('https://shadowcrypt.net/tools/tools',data={'data_type':'decrypt','data_input':dec,'data_submit':''})
		print BeautifulSoup(api.text,'html.parser').findAll('pre')[0].text.replace('\n\n','')
except requests.exceptions.ConnectionError:
	exit('%s[%s!%s] Check internet'%(W0,R0,W0))
except IOError:
	exit('%s[%s!%s] File does not exist'%(W0,R0,W0))
except IndexError:
	exit('%s[%s!%s] Use : python2 %s list.txt'%(W0,R0,W0,sys.argv[0]))
except KeyboardInterrupt:
	exit('\n%s[%s!%s] Exit'%(W0,R0,W0))
