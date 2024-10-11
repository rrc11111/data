import cv2
import time
import pykinect_azure as pykinect
import socket
import re
import json
import requests
import datetime
import keyboard

DES_IP = "100.78.236.13"
#DES_IP = "192.168.0.122"
PORT = 7060
# xml_str = b'<?xml version="1.0" encoding="utf-8"?><Probe><Uuid>B2D5D4D2-808C-40F6-87CD-694C05C2B274</Uuid><Types>inquiry</Types></Probe> '
'''xml_str = b'<?xml version="1.0" encoding="utf-8" standalone="no"?><CaptureStart><Name VALUE="Remotetake01"/><SessionName VALUE="SessionName" /><Notes VALUE="Take notes if any"/>' \
          b'< Delay VALUE="Reserved" /><Description VALUE="" /><DatabasePath VALUE="F:/shared/"/><TimeCode VALUE="00:00:00:00"/<PacketID VALUE="0"/>>'

xml_end = b'<?xml version="1.0" encoding="utf-8"?><CaptureStop><Name VALUE="Remotetake01" /><Notes VALUE="Take notes go here if any." /><Assets VALUE="skel1, skel2, sword" />' \
		  b'<TimeCode VALUE="00:00:00:00" /><HostName VALUE="optional host name" /><ProcessID VALUE="optional process id" /></CaptureStop>'''

xml_str = b'<?xml version="1.0" encoding="UTF-8" standalone="no" ?><CaptureStart><Name VALUE="Remotetake01"/><SessionName VALUE="SessionName" /><Notes VALUE="Take notes if any"/>' \
          b'< Delay VALUE="Reserved" /><Description VALUE="" /><DatabasePath VALUE="F:/shared/"/><TimeCode VALUE="00:00:00:00"/><PacketID VALUE="0"/></CaptureStart>'


xml_end = b'<?xml version="1.0" encoding="utf-8"?><CaptureStop><Name VALUE="Remotetake01" /><Notes VALUE="Take notes go here if any." /><Assets VALUE="skel1, skel2, sword" />' \
          b'<TimeCode VALUE="00:00:00:00" /><HostName VALUE="optional host name" /><ProcessID VALUE="optional process id" /></CaptureStop>'
# 创建UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定监听多播数据包的端口
#s.bind(("", 7080))

s.sendto(xml_str, (DES_IP, PORT))
time_act_begin = time.time()
time_act_begin_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_act_begin))
print('动捕开始时间：', time_act_begin_string)
# print('动捕开始时间：', time_act_begin)
while True:
    time_act_end = time.time()
    '''if keyboard.is_pressed('q'):
        time_act_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_act_end))
        s.sendto(xml_end, (DES_IP, PORT))
        print('动捕结束时间：', time_act_end_string)
        break'''
    if time_act_end - time_act_begin >= 30:
        s.sendto(xml_end, (DES_IP, PORT))
        time_act_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_act_end))
        print('动捕结束时间：', time_act_end_string)
        break





