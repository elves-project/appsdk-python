#!/usr/bin/python
# coding=utf-8  
# Author: toryzen  
#  
# Create: 2016/06/22
#
# app processor 入口 

import ConfigParser
import logging
from util.log4py import log4py
from service.service import processorThread
from util.thriftutil import  AppService
from util.thriftutil import ttypes
from thrift import Thrift  
from thrift.transport import TSocket  
from thrift.transport import TTransport  
from thrift.protocol import TBinaryProtocol  
from thrift.protocol import TCompactProtocol  
from thrift.server import TServer
import traceback
import time

var = {}
log=log4py("app-processor.py")

def getConfig(configFile):
    try:
        cf = ConfigParser.ConfigParser()  
        cf.read(configFile)
    except Exception,e:
        log.error(e)  
        traceback.print_exc()
    for section in cf.sections():
        for key,values in cf.items(section):
            log.debug("Config:"+key+":"+values)
            var[key] = values

class AppThriftServer: 
    def __init__(self,var):
        self.var = var

    def runProcessor(self, reIns):
        log.info('runProcessor Start...')
        pThread = processorThread(reIns.ins,reIns.flag,reIns.costtime,reIns.result)
        pThread.setDaemon(True)
        flag = 0
        startTime = time.time()
        try:
            pThread.start()
            flag = 1
            message = "success"
        except Exception,e:
            message = e
        log.info('runProcessor Finish...')
        return message

if __name__ == "__main__":

    #加载配置文件
    getConfig('setting.ini')
    
    #开启Thrift Service
    handler = AppThriftServer(var)
    processor = AppService.Processor(handler)  
    transport = TSocket.TServerSocket(var['ip'],var['port'])
    tfactory = TTransport.TBufferedTransportFactory()  
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    log.info('Starting App('+var['appname']+') Processor Service Success...')
    server.serve()
