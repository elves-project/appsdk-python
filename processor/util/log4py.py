#!/usr/bin/env python
# coding=utf-8  
#  
#   Author: ablozhou  
#   E-mail: ablozhou@gmail.com  
#  
#   Copyright 2010 ablozhou  
#  
#   Distributed under the terms of the GPL (GNU Public License)  
#  
#   hzdq is free software; you can redistribute it and/or modify  
#   it under the terms of the GNU General Public License as published by  
#   the Free Software Foundation; either version 2 of the License, or  
#   (at your option) any later version.  
#  
#   This program is distributed in the hope that it will be useful,  
#   but WITHOUT ANY WARRANTY; without even the implied warranty of  
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the  
#   GNU General Public License for more details.  
#  
#   You should have received a copy of the GNU General Public License  
#   along with this program; if not, write to the Free Software  
#   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA  
#  
# 2010.3.14 写文件，log级别常数定义  
import datetime  
import sys  
import traceback  
import codecs  
import types  
import logging
import os
import time 
#log编码全部按utf8处理  
loglevels = {'stdout':['info','debug','warn','error','fatal'],  
    'file':['info','debug','warn','error','fatal']  
    }  
#print os.getcwd()+'/logs/logs.txt' 
logfile = os.getcwd()+'/logs/logs.'+time.strftime('%Y-%m-%d',time.localtime(time.time()))+'.txt'  
class log4py():  
    def __init__(self,modulename="gloabal"):  
        self.filename = logfile  
        #self.flag = set(loglevel['stdout']+loglevel['file'])  
        self.loglevel = loglevels  
        self.modulename = modulename  
        self.fcname = None  
    class function():  
        def __init__(self,fcname,parent):  
            parent.debug('enter ',fcname)  
            self.fcname = fcname  
            self.parent = parent  
        def __del__(self):  
            self.parent.debug('exit ',self.fcname)  
    def dbgfc(self,fcname):  
        '''''set debug function name'''  
        f = None  
        if 'debug' in self.flag:  
            f = self.function(fcname,self)  
        return f  
    def _gettime(self):  
        return datetime.datetime.now().isoformat()  
    def outstd(self,*fmt):  
        s = self.fmtstr(*fmt)  
        print s  
    def outfile(self,*fmt):  
        s = self.fmtstr(*fmt)  
        #print 'before outfile '+s  
        if s:  
            #print 'outfile '+s  
            encoding = 'utf8'  
            out = open(logfile, 'a+')#, encoding  
            out.write(s)  
            out.write('\n')  
            out.close()  
    def fmtstr(self, *fmt):  
        str = ''  
        encoding = 'utf8'#缺省utf8编码  
        for i in fmt:  
            if not type(i) in [types.UnicodeType, types.StringTypes, types.StringType]:  
                s= repr(i)  
            else:  
                s = i  
            if type(s) == type(u''):  
                str += s.encode(encoding)  
            else:  
                str += s  
            str += '.'  
        #str += '/n'  
        #print 'fmtstr:'+str  
        return str  
    def debug(self,*fmt):  
        if 'debug' in self.loglevel['stdout']:  
            self.outstd(self._gettime(),'[DEBUG]',self.modulename,*fmt)  
        if 'debug' in self.loglevel['file']:  
            #print 'debug file ...'  
            self.outfile(self._gettime(),'[DEBUG]',self.modulename,*fmt)  
    def warn(self,*fmt):  
        if 'warn' in self.loglevel['stdout']:  
            self.outstd(self._gettime(),'[WARN]',self.modulename,*fmt)  
        if 'warn' in self.loglevel['file']:  
            self.outfile(self._gettime(),'[WARN]',self.modulename,*fmt)  
    def info(self,*fmt):  
        if 'info' in self.loglevel['stdout']:  
            self.outstd(self._gettime(),'[INFO]',self.modulename,*fmt)  
        if 'info' in self.loglevel['file']:  
            self.outfile(self._gettime(),'[INFO]',self.modulename,*fmt)  
    def error(self,*fmt):  
        #print '/033[0;30;41m',  
        if 'error' in self.loglevel['stdout']:  
            self.outstd(self._gettime(),'[ERROR]',self.modulename,*fmt)  
        if 'error' in self.loglevel['file']:  
            self.outfile(self._gettime(),'[ERROR]',self.modulename,*fmt)  
        #print '/033[0m'  
    def fatal(self,*fmt):  
        if 'fatal' in self.loglevel['stdout']:  
            self.outstd(self._gettime(),'[FATAL',self.modulename,*fmt)  
        if 'fatal' in self.loglevel['file']:  
            self.outfile(self._gettime(),'[FATAL',self.modulename,*fmt)  
#unit test  
if __name__ == '__main__':  
    log=log4py()  
    log.outstd('INFO','stdout','test')  
    log.outfile('INFO','stdout','test')  
    log.debug('debug information 调试')  
    log.error('errorrrrrrrrrrrrrrr')  
    log.debug('hello')  