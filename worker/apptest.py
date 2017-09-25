#!/usr/bin/python
# coding=utf-8  
# Author: toryzen  
#  
# Create: 2016/06/22
#
#   app worker 示例 [文件名需要与类名一致]
import traceback

class apptest():
    def helloword(self,param):
        flag = "false"
        try:
            result = param["my"]
            flag = "true"
        except Exception,e:
            result = traceback.format_exc()
        return flag,result

if __name__ == '__main__':
    pass
