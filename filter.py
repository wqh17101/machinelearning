# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 11:16:56 2017
只根据clf开头的字段检索
@author: wqh17
"""

import pandas as pd 
import os
import time

dir='E:\\di\\17310\\'
files=os.listdir(dir)
for i,filename in enumerate(files):
    filename=dir+filename
    break 
result=[]    

  
def ft(filename=filename,clf_event_time='',clf_device_name='',clf_user='',clf_pid='',clf_processname='',clf_subtype='',clf_file='',clf_url='',
       clf_ip='',clf_netprotocol='',clf_eventtype='',clf_all_pid='',clf_all_process=''):
    clf_event_time='clf_event_time='+clf_event_time
    clf_device_name='clf_device_name='+clf_device_name
    clf_user='clf_user='+clf_user
    clf_pid='clf_pid='+clf_pid
    clf_processname='clf_processname='+clf_processname
    clf_subtype='clf_subtype='+clf_subtype
    clf_file='clf_file='+clf_file
    clf_url='clf_url='+clf_url
    clf_ip='clf_ip='+clf_ip
    clf_netprotocol='clf_netprotocol='+clf_netprotocol
    clf_eventtype='clf_eventtype='+clf_eventtype
    clf_all_pid='clf_all_pid='+clf_all_pid
    clf_all_process='clf_all_process='+clf_all_process
    time0=time.time()
    with open(filename,'r',encoding='UTF-8') as f:
        print('this is {0}'.format(filename))
        n=0
        for line in f:
            if ((line.find(clf_event_time) >-1 )and (line.find(clf_device_name) >-1 )and (line.find(clf_user) >-1 )and (line.find(clf_pid) >-1) 
                and (line.find(clf_processname) >-1 )and (line.find(clf_subtype) >-1 )and (line.find(clf_file) >-1 )and (line.find(clf_url) >-1) 
                and (line.find(clf_ip) >-1 )and (line.find(clf_netprotocol) >-1 ) and (line.find(clf_eventtype) >-1 )and (line.find(clf_all_pid) >-1) 
                and (line.find(clf_all_process) >-1) ):
                #print(line)
                result.append(line)
            #split_line=line.split('\t')
            #if len(split_line)!=25:
                #print(len(split_line))
            n=n+1
        time1=time.time()
        print('{0} events in this file,using {1}s to match'.format(n,time1-time0))
    f.close()  
    return result
    
    
result=ft(filename=filename,clf_event_time='',clf_device_name='',clf_user='',clf_pid='',clf_processname='',clf_subtype='',clf_file='',clf_url='',
       clf_ip='',clf_netprotocol='',clf_eventtype='',clf_all_pid='',clf_all_process='')























