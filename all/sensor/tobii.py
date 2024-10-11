# -*- coding: utf-8 -*-
import socket
import re
import json
import requests
import datetime
import time
import keyboard


#创建tbbioo
url= 'http://192.168.75.51/rest/recorder!start'
headers = {"content-type":"application/json"}
res_start = requests.post(url, json=[], headers=headers)
time_tobii_begin = time.time()
time_tobii_begin_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_tobii_begin))
#print(time_begin)
print("tobii开始时间：",time_tobii_begin_string)
# print("tobii开始时间：",time_tobii_begin)
url_end = 'http://192.168.75.51/rest/recorder!stop'
headers = {"content-type": "application/json"}
while True:
    time_tobii_end = time.time()
    '''if keyboard.is_pressed('q'):
        time_tobii_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_tobii_end))
        print('tobii结束时间：', time_tobii_end_string)
        res_end = requests.post(url_end, json=[], headers=headers)
        break'''
    if time_tobii_end - time_tobii_begin >= 30:
        time_tobii_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_tobii_end))
        print('tobii结束时间：', time_tobii_end_string)
        res_end = requests.post(url_end, json=[], headers=headers)
        break
