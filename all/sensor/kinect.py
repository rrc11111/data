import cv2
import time
import pykinect_azure as pykinect
import numpy as np
import pandas as pd
import keyboard

# -*- coding: utf-8 -*-


if __name__ == "__main__":
    # Initialize the library, if the library is not found, add the library path as argumqent
    pykinect.initialize_libraries()

    # Modify camera configuration
    device_config = pykinect.default_configuration
    # device_config.color_format = pykinect.K4A_IMAGE_FORMAT_COLOR_BGRA32
    device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_1080P
    device_config.depth_mode = pykinect.K4A_DEPTH_MODE_NFOV_2X2BINNED

    print(device_config)

    # Start device
    RGB_start_time = time.time()
    RGB_start_time_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(RGB_start_time))
    video_filename = "D:/database/kinect_data/RGB_video/0/camera1" + RGB_start_time_string + ".mkv"
    video_filename1 = "D:/database/kinect_data/RGB_video/1/camera2" + RGB_start_time_string + ".mkv"
    video_filename2 = "D:/database/kinect_data/RGB_video/2/camera3" + RGB_start_time_string + ".mkv"
    video_filename3 = "D:/database/kinect_data/RGB_video/3/" + RGB_start_time_string + ".mkv"
    video_filename4 = "D:/database/kinect_data/RGB_video/4/" + RGB_start_time_string + ".mkv"
    video_filename5 = "D:/database/kinect_data/RGB_video/5/" + RGB_start_time_string + ".mkv"
    video_filename6 = "D:/database/kinect_data/RGB_video/6/" + RGB_start_time_string + ".mkv"
    video_filename7 = "D:/database/kinect_data/RGB_video/7/" + RGB_start_time_string + ".mkv"
    video_filename8 = "D:/database/kinect_data/RGB_video/8/" + RGB_start_time_string + ".mkv"

    device = pykinect.start_device(device_index=0, config=device_config, record=True, record_filepath=video_filename)
    device1 = pykinect.start_device(device_index=1, config=device_config, record=True, record_filepath=video_filename1)
    device2 = pykinect.start_device(device_index=2, config=device_config, record=True, record_filepath=video_filename2)
    # device3 = pykinect.start_device(device_index=3, config=device_config, record=True, record_filepath=video_filename3)
    # device4 = pykinect.start_device(device_index=4, config=device_config, record=True, record_filepath=video_filename4)
    # device5 = pykinect.start_device(device_index=5, config=device_config, record=True, record_filepath=video_filename5)
    # device6 = pykinect.start_device(device_index=6, config=device_config, record=True, record_filepath=video_filename6)
    # device7 = pykinect.start_device(device_index=7, config=device_config, record=True, record_filepath=video_filename7)
    # device8 = pykinect.start_device(device_index=8, config=device_config, record=True, record_filepath=video_filename8)
    time_begin = time.time()
    time_begin_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_begin))
    # print(time_begin)
    print("kinect开始时间：", time_begin_string)
    # print("kinect开始时间：", time_begin)
    # calibration_0 = device.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_0)
    # calibration_1 = device1.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_1)
    # calibration_2 = device2.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_2)
    # calibration_3 = device3.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_3)
    # calibration_4 = device4.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_4)
    # calibration_5 = device5.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_5)
    # calibration_6 = device6.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_6)
    # calibration_7 = device7.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_7)
    # calibration_8 = device8.get_calibration(device_config.depth_mode, device_config.color_resolution)
    # print(calibration_8)


timestamp = []
timestamp1 = []
timestamp2 = []
timestamp3 = []
timestamp4 = []
timestamp5 = []
timestamp6 = []
timestamp7 = []
timestamp8 = []

while True:

    # Get capture

    capture = device.update()
    time0 = time.time()
    timestamp.append(time0)

    capture1 = device1.update()
    time1 = time.time()
    timestamp1.append(time1)

    capture2 = device2.update()
    time2 = time.time()
    timestamp2.append(time2)

    # capture3 = device3.update()
    # time3 = time.time()
    # timestamp3.append(time3)

    # capture4 = device4.update()
    # time4 = time.time()
    # timestamp4.append(time4)
    #
    # capture5 = device5.update()
    # time5 = time.time()
    # timestamp5.append(time5)
    #
    # capture6 = device6.update()
    # time6 = time.time()
    # timestamp6.append(time6)
    #
    # capture7 = device7.update()
    # time7 = time.time()
    # timestamp7.append(time7)

    # capture8 = device8.update()
    # time8 = time.time()
    # timestamp8.append(time8)
    # Press q key to stop
    time_end = time.time()

    '''if keyboard.is_pressed('q'):
        time_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end))
        print('kinect结束时间：',time_end_string)
        break'''
    if time_end - time_begin >= 30:
        time_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end))
        print('kinect结束时间：', time_end_string)
        break


    '''if cv2.waitKey(1) == ord('q'):
        break'''

gap = '\n'
f = open("D:/database/kinect_data/RGB_video/0/camera1" + RGB_start_time_string + ".txt", "w")
f1 = open("D:/database/kinect_data/RGB_video/1/camera2" + RGB_start_time_string + ".txt", "w")
f2 = open("D:/database/kinect_data/RGB_video/2/camera3" + RGB_start_time_string + ".txt", "w")
# f3 = open("./database/kinect_data/RGB_video/3/" + RGB_start_time_string + ".txt", "w")
# f4 = open("./database/kinect_data/RGB_video/4/" + RGB_start_time_string + ".txt", "w")
# f5 = open("./database/kinect_data/RGB_video/5/" + RGB_start_time_string + ".txt", "w")
# f6 = open("./database/kinect_data/RGB_video/6/" + RGB_start_time_string + ".txt", "w")
# f7 = open("./database/kinect_data/RGB_video/7/" + RGB_start_time_string + ".txt", "w")
# f8 = open("./database/kinect_data/RGB_video/8/" + RGB_start_time_string + ".txt", "w")

f.write(gap.join(str(i) for i in timestamp))
f1.write(gap.join(str(i) for i in timestamp1))
f2.write(gap.join(str(i) for i in timestamp2))
# f3.write(gap.join(str(i) for i in timestamp3))
# f4.write(gap.join(str(i) for i in timestamp4))
# f5.write(gap.join(str(i) for i in timestamp5))
# f6.write(gap.join(str(i) for i in timestamp6))
# f7.write(gap.join(str(i) for i in timestamp7))
# f8.write(gap.join(str(i) for i in timestamp8))

f.close()
f1.close()
f2.close()
# f3.close()
# f4.close()
# f5.close()
# f6.close()
# f7.close()
# f8.close()
