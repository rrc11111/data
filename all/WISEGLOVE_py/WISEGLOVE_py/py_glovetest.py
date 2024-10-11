from ctypes import *
import time
import ctypes
import sys, os
from pynput.keyboard import Controller,Key,Listener
from pynput import keyboard
import keyboard
import numpy as np
import msvcrt
lib = CDLL("./WISEGLOVEU3D.dll")

global disp
disp=ctypes.c_int
g_pGlove=ctypes.c_bool
num_sensor = ctypes.c_int #初始化传感器数量
num_pressure = ctypes.c_int #压力传感器数量
manu=(ctypes.c_int*32)()#厂家字串
sn=(ctypes.c_int*32)()#厂家字串
model=(ctypes.c_int*32)()#型号字串
angle=(c_float*14)()
sensor=(c_ushort*14)()
pdata=(ctypes.c_int*2)()
pdataraw=(ctypes.c_int*2)()

start_record = 0
end_record = 0

timestamp=ctypes.c_uint
feedback= np.array([64,64,64,64,64])

print ("Press q to exit this program!")
print ("Press s to show sensor value!")
print ("Press a to show angle!")
print ("Press r to zero angle!")


lib.wgInit.restype = ctypes.c_bool
g_pGlove=lib.wgInit()
lib.wgGetNumOfSensor.restype = ctypes.c_int
num_sensor=lib.wgGetNumOfSensor()
lib.wgGetNumOfPressure.restype = ctypes.c_int
num_pressure=lib.wgGetNumOfPressure()
if g_pGlove==False:
	print("请插上数据手套")
else:
	print("数据手套已成功连接！")
	print("该数据手套角度传感器的个数:%d"%num_sensor)
	print("该数据手套压力传感器的个数:%d"%num_pressure)

#lib.wgSetCalibMode(ctypes.c_int(0))#自动标定

#打印手指各关节标签：拇指MCP(01),IP(02),拇指食指(03),食指MCP-PIP(04,05),食指中指(06),中指MCP-DIP(07,08),
#                  中指环指(09),环指MCP-DIP(10,11),环指小指(12),小指MCP-DIP(13,14)
for i in range (num_sensor):
	print ("第%s个\t" %(i+1) ,end="")
print('\n')

while True:
	if msvcrt.kbhit():
		key=msvcrt.getch()
		#print(type(key))
		keystr=str(key, encoding="utf-8")
		if (keystr=='q'):
			break;
		if (keystr=='a'):
			disp=1
			print("disp==1")
		if (keystr=='s'):
			disp=0
			print("disp=0")
		if (keystr=='r'):
			lib.wgResetCalib()
	if disp==1:
		lib.wgGetAngle.restype = ctypes.c_uint
		timestamp=lib.wgGetAngle(angle)
		for i in range (num_sensor):
			print("%.2f\t" %angle[i],end="")
		print ('\r',end='')
	if disp==0:
		lib.wgGetData.restype = ctypes.c_uint
		timestamp=lib.wgGetData(sensor)
		for i in range (num_sensor):
			print("%.2f\t" %sensor[i],end="")
		print ('\r',end='')
	time.sleep(0.1)
lib.wgClose()
