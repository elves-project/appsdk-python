#!/usr/bin/python
# coding=utf-8  
# Author: toryzen  
#  
# Create: 2016/06/22
#
#   app processor 主逻辑
import traceback

import sys,time
sys.path.append('../')
import threading
from util.log4py import log4py

log=log4py("service.py")

class processorThread(threading.Thread):
    def __init__(self, ins, flag, costtime, message):
        threading.Thread.__init__(self)
        self.ins = ins
        self.flag = flag
        self.costtime = costtime
        self.message = message
    
    def run(self):
    	log.info("processor start !")
        print "---------GET RESULT----------"
        print "Ins=",self.ins
        print "Flag=",self.flag
        print "Costtime=",self.costtime
        print "Message=",self.message
        log.info("processor end !")


if __name__ == "__main__":
    pThread = processorThread("false",10,"1q2w3e4r")
    pThread.setDaemon(True)
    pThread.start()

