#-*- coding:utf-8 -*-
import os,sys
import uuid

def getSysInfo():
    print(os.getcwd())
    return 'null'

def getSum(i):
    s=0
    for a in range(1,i+1):
        s=s+a
    return s

def getUUID():
    return uuid.UUID()








