# python3.12 32-bit
# pip install keyboard

from ctypes import *
import time
import ctypes
import sys, os
import keyboard
import numpy as np
import msvcrt
import threading
import math

# 加载右手开发库
lib = CDLL("./wisegloveu3d_R.dll")


# 加载左手开发库
# lib = CDLL("./wisegloveu3d_L.dll")

# 四元素转欧拉角quaternion(wxyz)
def euler_from_quaternion(quaternion):
    # x, y, z, w = quaternion[0], quaternion[1], quaternion[2], quaternion[3]
    w, x, y, z = quaternion[0], quaternion[1], quaternion[2], quaternion[3]
    r = math.atan2(2 * (w * x + y * z), 1 - 2 * (x * x + y * y))
    r = r / math.pi * 180
    p = math.asin(2 * (w * y - z * x))
    p = p / math.pi * 180
    y = math.atan2(2 * (w * z + x * y), 1 - 2 * (y * y + z * z))
    y = y / math.pi * 180
    return r, p, y


global disp
disp = ctypes.c_int
g_pGlove = ctypes.c_bool
num_sensor = ctypes.c_int  # 初始化传感器数量
num_pressure = ctypes.c_int  # 压力传感器数量
manu = (ctypes.c_int * 32)()  # 厂家字串
sn = (ctypes.c_int * 32)()  # 厂家字串
model = (ctypes.c_int * 32)()  # 型号字串
fingerangle = (c_float * 19)()

armquat = (c_float * 16)()
fingerraw = (c_ushort * 19)()
pressureraw = (c_ushort * 19)()

disp = 5
timestamp = ctypes.c_uint

print("q 退出程序")
print("r 标定手指&手臂")
print("z 握力清零")

print("0 显示手指原始值")
print("1 显示手指角度")
print("2 显示手臂角度")
print("3 显示握力值")

lib.wgInit.restype = ctypes.c_bool
g_pGlove = lib.wgInit(-1)  # 参数: -1 =随便连接左手或者右手, 0 =连接左手 ,1=连接右手

lib.wgGetNumOfSensor.restype = ctypes.c_int
num_sensor = lib.wgGetNumOfSensor()

lib.wgGetNumOfPressure.restype = ctypes.c_int
num_pressure = lib.wgGetNumOfPressure()

lib.wgGetNumOfArm.restype = ctypes.c_int
num_arm = lib.wgGetNumOfArm()

lib.wgGetData.restype = ctypes.c_uint
lib.wgGetAngle.restype = ctypes.c_uint
lib.wgGetQuat.restype = ctypes.c_uint
lib.wgGetQuatOrg.restype = ctypes.c_uint
lib.wgGetPressureRaw.restype = ctypes.c_uint

if g_pGlove == False:
    print("请插上数据手套")
else:
    print("数据手套已成功连接！")
    print("该数据手套角度传感器数:%d" % num_sensor)
    print("该数据手套握力传感器数:%d" % num_pressure)
    print("该数据手套手臂传感器数:%d" % num_arm)

# lib.wgSetCalibMode(ctypes.c_int(0))#自动标定

for i in range(num_sensor):
    print("第%s个\t" % (i + 1), end="")
print('\n')

while True:
    if keyboard.is_pressed("q"):
        print("Exiting...")
        break
    elif keyboard.is_pressed("0"):
        disp = 0
        print("显示手指原始值")
    elif keyboard.is_pressed("1"):
        disp = 1
        print("显示手指角度")
    elif keyboard.is_pressed("2"):
        disp = 2
        print("显示手臂角度")
    elif keyboard.is_pressed("3"):
        disp = 3
        print("显示握力值")

    elif keyboard.is_pressed("r"):
        lib.wgResetCalib()
        lib.wgResetQuat()
        print("标定")
    elif keyboard.is_pressed("z"):
        lib.wgZeroPressure()
        print("置零")

    if disp == 0:
        timestamp = lib.wgGetData(fingerraw)
        if timestamp > 0:
            print("finger raw:%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d"
                  % (fingerraw[0], fingerraw[1], fingerraw[2], fingerraw[3], fingerraw[4], fingerraw[5], fingerraw[6],
                     fingerraw[7], fingerraw[8], fingerraw[9], fingerraw[10],
                     fingerraw[11], fingerraw[12], fingerraw[13], fingerraw[14], fingerraw[15], fingerraw[16],
                     fingerraw[17], fingerraw[18]))

    elif disp == 1:
        timestamp = lib.wgGetAngle(fingerangle)
        if timestamp > 0:
            print(
                "finger angle:%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f,%.1f"
                % (fingerangle[0], fingerangle[1], fingerangle[2], fingerangle[3], fingerangle[4], fingerangle[5],
                   fingerangle[6], fingerangle[7], fingerangle[8], fingerangle[9],
                   fingerangle[10], fingerangle[11], fingerangle[12], fingerangle[13], fingerangle[14], fingerangle[15],
                   fingerangle[16], fingerangle[17], fingerangle[18]))

    elif disp == 2:

        # 读手臂传感器原始的四元素值
        # timestamp=lib.wgGetQuatOrg(armquat)

        # 读手臂传感器标定后的四元素值,如需要原始值的话调用本函数
        timestamp = lib.wgGetQuat(armquat)

        if timestamp > 0:
            quat0 = [armquat[0], armquat[1], armquat[2], armquat[3]]
            [x0, y0, z0] = euler_from_quaternion(quat0)

            quat1 = [armquat[4], armquat[5], armquat[6], armquat[7]]
            [x1, y1, z1] = euler_from_quaternion(quat1)

            quat2 = [armquat[8], armquat[9], armquat[10], armquat[11]]
            [x2, y2, z2] = euler_from_quaternion(quat2)

            print(
                "手掌:%.2f,%.2f,%.2f==前臂:%.2f,%.2f,%.2f==大臂:%.2f,%.2f,%.2f" % (x0, y0, z0, x1, y1, z1, x2, y2, z2))

    elif disp == 3:
        # 读握力感器值 单位克
        timestamp = lib.wgGetPressureRaw(pressureraw)
        if timestamp > 0:
            print("grasp:%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d"
                  % (pressureraw[0], pressureraw[1], pressureraw[2], pressureraw[3], pressureraw[4], pressureraw[5],
                     pressureraw[6], pressureraw[7], pressureraw[8], pressureraw[9], pressureraw[10],
                     pressureraw[11], pressureraw[12], pressureraw[13], pressureraw[14], pressureraw[15],
                     pressureraw[16], pressureraw[17], pressureraw[18]))

    time.sleep(0.01)

lib.wgClose()
