#!/usr/bin/env python
# coding=utf-8  
from subprocess import Popen,PIPE
import urllib,urllib2
import shlex,re
def getIfconfig():
        p = Popen(['ifconfig'],stdout=PIPE)
        return p.stdout.read().split('\n\n')
def parseIfconfig(data):
        macaddr = data.split('\n')[0].split()[-1]
        ipaddr = data.split('\n')[1].split()[1].split(':')[1]
        return macaddr,ipaddr
for i in [i.strip() for i in getIfconfig() if i and not i.startswith('lo')]:	
	s = {}
	s['macaddr'] = parseIfconfig(i)[0]
	s['ipaddr'] = parseIfconfig(i)[1]
data = s
def get_uuid():
	data = {}
	p = Popen(['dmidecode'],stdout=PIPE)
	s = p.stdout.readlines()
	a = []
	line_in = False
	for i in s:
	        if i.startswith('System Information'):
	                line_in = True
	                continue
	        if line_in:
	                a.append(i.strip())
	                if i.startswith('\n'):
	                        line_in = False
	                        break
	vendor = [i for i in a if i.startswith('Product')]
	sn = [i for i in a if i.startswith('UUID:')]
	data['vendor'] = vendor[0].split(': ')[1]
	data['sn'] = sn[0].split(': ')[1]
	return data
def get_version():
	data = {}
	number = re.compile(r'\d.\d',re.M)
	cmd = 'cat /etc/issue'
        p = Popen(shlex.split(cmd), stdout=PIPE)
        s = p.stdout.readlines()[0:]
	#osver = number.findall(s[0])
	data['osver'] = s[0].strip('\n')
	return data
def get_hostname():
	data = {}
	cmd = 'hostname -f'
        p = Popen(shlex.split(cmd), stdout=PIPE)
        s = p.stdout.readline().strip('\n')
	data['hostname'] = s
	return data
def get_uname():
	data = {}
	number = re.compile(r'x\d+\_+\d\d')
        cmd = 'uname -a'
        p = Popen(shlex.split(cmd), stdout=PIPE)
        s = p.stdout.readlines()
	os = s[0].split()[0]
	system = number.findall(s[0])
	data['system'] = system[0]
	data['os'] = os
	return data