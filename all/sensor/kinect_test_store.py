import cv2
import time
import pykinect_azure as pykinect
import numpy as np
import pandas as pd
from PIL import Image

# -*- coding: utf-8 -*-


if __name__ == "__main__":

	# Initialize the library, if the library is not found, add the library path as argument
	pykinect.initialize_libraries()

	# Modify camera configuration
	device_config = pykinect.default_configuration
	# device_config.color_format = pykinect.K4A_IMAGE_FORMAT_COLOR_BGRA32
	device_config.color_resolution = pykinect.K4A_COLOR_RESOLUTION_1080P
	device_config.depth_mode = pykinect.K4A_DEPTH_MODE_NFOV_2X2BINNED

	print(device_config)

	# Start device
	RGB_start_time = time.time()
	RGB_start_time_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(RGB_start_time))

	video_filename = "./kinect_data/RGB_video/0/" + str(RGB_start_time) +".mkv"
	video_filename1 = "./kinect_data/RGB_video/1/" + str(RGB_start_time) +".mkv"
	video_filename2 = "./kinect_data/RGB_video/2/" + str(RGB_start_time) +".mkv"
	video_filename3 = "./kinect_data/RGB_video/3/" + str(RGB_start_time) +".mkv"
	video_filename4 = "./kinect_data/RGB_video/4/" + str(RGB_start_time) +".mkv"
	video_filename5 = "./kinect_data/RGB_video/5/" + str(RGB_start_time) +".mkv"
	video_filename6 = "./kinect_data/RGB_video/6/" + str(RGB_start_time) +".mkv"
	video_filename7 = "./kinect_data/RGB_video/7/" + str(RGB_start_time) +".mkv"
	video_filename8 = "./kinect_data/RGB_video/8/" + str(RGB_start_time) +".mkv"
	device = pykinect.start_device(device_index=0, config=device_config, record=True, record_filepath=video_filename)
	device1 = pykinect.start_device(device_index=1, config=device_config, record=True, record_filepath=video_filename1)
	device2 = pykinect.start_device(device_index=2, config=device_config, record=True, record_filepath=video_filename2)
	device3 = pykinect.start_device(device_index=3, config=device_config, record=True, record_filepath=video_filename3)
	device4 = pykinect.start_device(device_index=4, config=device_config, record=True, record_filepath=video_filename4)
	device5 = pykinect.start_device(device_index=5, config=device_config, record=True, record_filepath=video_filename5)
	'''device6 = pykinect.start_device(device_index=6, config=device_config, record=True, record_filepath=video_filename6)
	device7 = pykinect.start_device(device_index=7, config=device_config, record=True, record_filepath=video_filename7)
	device8 = pykinect.start_device(device_index=8, config=device_config, record=True, record_filepath=video_filename8)'''
	time_begin = time.time()
	time_begin_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_begin))
	print(time_begin)
	print(time_begin_string)

	depth_image_object_list = []
	depth_image_data_list = []
	image_data_list = []

	depth_image1_object_list = []
	depth_image1_data_list = []
	image1_data_list = []

	depth_image2_object_list = []
	depth_image2_data_list = []
	image2_data_list = []

	depth_image3_object_list = []
	depth_image3_data_list = []
	image3_data_list = []

	depth_image4_object_list = []
	depth_image4_data_list = []
	image4_data_list = []

	depth_image5_object_list = []
	depth_image5_data_list = []
	image5_data_list = []

	depth_image6_object_list = []
	depth_image6_data_list = []
	image6_data_list = []

	depth_image7_object_list = []
	depth_image7_data_list = []
	image7_data_list = []

	depth_image8_object_list = []
	depth_image8_data_list = []
	image8_data_list = []



	frame =0
	while True:

		# Get capture
		time_capture = time.time()
		capture = device.update()
		ret, depth_image = capture.get_colored_depth_image()
		ret_RGB, image = capture.get_color_image()
		depth_image_rgb_data = list(zip((time_capture, depth_image)))
		image_rgb_data = list(zip((time_capture, image)))
		depth_image_data_list.append(depth_image_rgb_data)
		image_data_list.append(image_rgb_data)
		depth_image_object_list.append(depth_image)


		time_capture1 = time.time()
		capture1 = device1.update()
		ret1, depth_image1 = capture1.get_colored_depth_image()
		ret1_RGB, image1 = capture1.get_color_image()
		depth_image1_rgb_data = list(zip((time_capture1, depth_image1)))
		image1_rgb_data = list(zip((time_capture1, image1)))
		depth_image1_data_list.append(depth_image1_rgb_data)
		image1_data_list.append(image1_rgb_data)
		depth_image1_object_list.append(depth_image1)

		time_capture2 = time.time()
		capture2 = device2.update()
		ret2, depth_image2 = capture2.get_colored_depth_image()
		ret2_RGB, image2 = capture2.get_color_image()
		depth_image2_rgb_data = list(zip((time_capture2, depth_image2)))
		image2_rgb_data = list(zip((time_capture2, image2)))
		depth_image2_data_list.append(depth_image2_rgb_data)
		image2_data_list.append(image2_rgb_data)
		depth_image2_object_list.append(depth_image2)

		time_capture3 = time.time()
		capture3 = device3.update()
		ret3, depth_image3 = capture3.get_colored_depth_image()
		ret3_RGB, image3 = capture3.get_color_image()
		depth_image3_rgb_data = list(zip((time_capture3, depth_image3)))
		image3_rgb_data = list(zip((time_capture3, image3)))
		depth_image3_data_list.append(depth_image3_rgb_data)
		image3_data_list.append(image3_rgb_data)
		depth_image3_object_list.append(depth_image3)

		time_capture4 = time.time()
		capture4 = device4.update()
		ret4, depth_image4 = capture4.get_colored_depth_image()
		ret4_RGB, image4 = capture4.get_color_image()
		depth_image4_rgb_data = list(zip((time_capture4, depth_image4)))
		image4_rgb_data = list(zip((time_capture4, image4)))
		depth_image4_data_list.append(depth_image4_rgb_data)
		image4_data_list.append(image4_rgb_data)
		depth_image4_object_list.append(depth_image4)

		time_capture5 = time.time()
		capture5 = device5.update()
		ret5, depth_image5 = capture5.get_colored_depth_image()
		ret5_RGB, image5 = capture5.get_color_image()
		depth_image5_rgb_data = list(zip((time_capture5, depth_image5)))
		image5_rgb_data = list(zip((time_capture5, image5)))
		depth_image5_data_list.append(depth_image5_rgb_data)
		image5_data_list.append(image5_rgb_data)
		depth_image5_object_list.append(depth_image5)

		'''time_capture6 = time.time()
		capture6 = device6.update()
		ret6, depth_image6 = capture6.get_colored_depth_image()
		ret6_RGB, image6 = capture6.get_color_image()
		depth_image6_rgb_data = list(zip((time_capture6, depth_image6)))
		image6_rgb_data = list(zip((time_capture6, image6)))
		depth_image6_data_list.append(depth_image6_rgb_data)
		image6_data_list.append(image6_rgb_data)
		depth_image6_object_list.append(depth_image6)

		time_capture7 = time.time()
		capture7 = device7.update()
		ret7, depth_image7 = capture7.get_colored_depth_image()
		ret7_RGB, image7 = capture7.get_color_image()
		depth_image7_rgb_data = list(zip((time_capture7, depth_image7)))
		image7_rgb_data = list(zip((time_capture7, image7)))
		depth_image7_data_list.append(depth_image7_rgb_data)
		image7_data_list.append(image7_rgb_data)
		depth_image7_object_list.append(depth_image7)

		time_capture8 = time.time()
		capture8 = device8.update()
		ret8, depth_image8 = capture8.get_colored_depth_image()
		ret8_RGB, image8 = capture8.get_color_image()
		depth_image8_rgb_data = list(zip((time_capture8, depth_image8)))
		image8_rgb_data = list(zip((time_capture8, image8)))
		depth_image8_data_list.append(depth_image8_rgb_data)
		image8_data_list.append(image8_rgb_data)
		depth_image8_object_list.append(depth_image8)'''


		#capture4 = device4.update()
		#capture5 = device5.update()
		#capture6 = device6.update()
		#capture7 = device7.update()
		#capture8 = device8.update()





		# Get the color depth image from the capture
		# ret, depth_image = capture.get_colored_depth_image()
		# ret1, depth_image1 = capture1.get_colored_depth_image()
		# ret2, depth_image2 = capture2.get_colored_depth_image()
		# ret2_1, image2 = capture2.get_color_image()
		# ret3, depth_image3 = capture3.get_colored_depth_image()
		# ret3_1, image3 = capture2.get_color_image()
		# ret4, depth_image4 = capture4.get_colored_depth_image()
		# ret5, depth_image5 = capture5.get_colored_depth_image()
		# ret6, depth_image6 = capture6.get_colored_depth_image()
		# ret7, depth_image7 = capture7.get_colored_depth_image()

		# print(time.time())



		# Plot the image
		'''if not ret2:
			continue
		if not ret2_1:
			continue'''
		'''if not (ret and ret1 and ret2 and ret3 and ret4 and ret5 and ret6 and ret7 and ret8
				and ret_RGB and ret1_RGB and ret2_RGB and ret3_RGB and ret4_RGB and ret5_RGB and ret6_RGB and ret7_RGB and ret8_RGB):
			continue'''
		if not (ret and ret1 and ret2 and ret3 and ret4 and ret5
				and ret_RGB and ret1_RGB and ret2_RGB and ret3_RGB and ret4_RGB and ret5_RGB):
			continue




		frame += 1
		if frame >= 120:#大概fps=6
			break


	time_image = time.time()
	time_image_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_image))

	time_gap = image_data_list[-1][0][0] - image_data_list[1][0][0]
	#fps = round(len(depth_image_object_list)/time_gap)
	fps = 5
	#fps = len(depth_image_object_list) / time_gap
	size = (320, 288)  # 需要转为视频的图片的尺寸

	fourcc_video = cv2.VideoWriter_fourcc('I', '4', '2', '0')
	file_end = '.avi'
	video = cv2.VideoWriter("./kinect_data/depth_video/0/" + time_image_string + file_end, fourcc_video, fps, size)
	video1 = cv2.VideoWriter("./kinect_data/depth_video/1/" + time_image_string + file_end, fourcc_video, fps, size)
	video2 = cv2.VideoWriter("./kinect_data/depth_video/2/" + time_image_string + file_end, fourcc_video, fps, size)
	video3 = cv2.VideoWriter("./kinect_data/depth_video/3/" + time_image_string + file_end, fourcc_video, fps, size)
	video4 = cv2.VideoWriter("./kinect_data/depth_video/4/" + time_image_string + file_end, fourcc_video, fps, size)
	video5 = cv2.VideoWriter("./kinect_data/depth_video/5/" + time_image_string + file_end, fourcc_video, fps, size)
	'''video6 = cv2.VideoWriter("./kinect_data/depth_video/6/" + time_image_string + file_end, fourcc_video, fps, size)
	video7 = cv2.VideoWriter("./kinect_data/depth_video/7/" + time_image_string + file_end, fourcc_video, fps, size)
	video8 = cv2.VideoWriter("./kinect_data/depth_video/8/" + time_image_string + file_end, fourcc_video, fps, size)'''
	# 视频保存在当前目录下
	for i in range(len(depth_image_object_list)):
		video.write(depth_image_object_list[i])
		video1.write(depth_image1_object_list[i])
		video2.write(depth_image2_object_list[i])
		video3.write(depth_image3_object_list[i])
		video4.write(depth_image4_object_list[i])
		video5.write(depth_image5_object_list[i])
		'''video6.write(depth_image6_object_list[i])
		video7.write(depth_image7_object_list[i])
		video8.write(depth_image8_object_list[i])'''
	video.release()
	video1.release()
	video2.release()
	video3.release()
	video4.release()
	video5.release()
	'''video6.release()
	video7.release()
	video8.release()'''
	cv2.destroyAllWindows()

	'''depth_image_data = pd.DataFrame(depth_image_data_list, columns=None)
	depth_image_data.to_csv('./kinect_data/depth/0/' + time_image_string + '.csv', index=None)
	image_data = pd.DataFrame(image_data_list, columns=None)
	image_data.to_csv('./kinect_data/RGB_img/0/' + time_image_string + '.csv', index=None)

	depth_image1_data = pd.DataFrame(depth_image1_data_list, columns=None)
	depth_image1_data.to_csv('./kinect_data/depth/1/' + time_image_string + '.csv', index=None)
	image1_data = pd.DataFrame(image1_data_list, columns=None)
	image1_data.to_csv('./kinect_data/RGB_img/1/' + time_image_string + '.csv', index=None)

	depth_image2_data = pd.DataFrame(depth_image2_data_list, columns=None)
	depth_image2_data.to_csv('./kinect_data/depth/2/' + time_image_string + '.csv', index=None)
	image2_data = pd.DataFrame(image2_data_list, columns=None)
	image2_data.to_csv('./kinect_data/RGB_img/2/' + time_image_string + '.csv', index=None)

	depth_image3_data = pd.DataFrame(depth_image3_data_list, columns=None)
	depth_image3_data.to_csv('./kinect_data/depth/3/' + time_image_string + '.csv', index=None)
	image3_data = pd.DataFrame(image3_data_list, columns=None)
	image3_data.to_csv('./kinect_data/RGB_img/3/' + time_image_string + '.csv', index=None)'''

	'''time_image = time.time()
	time_image_string = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time_image))
	depth_image2_data = pd.DataFrame(depth_image2_data_list, columns=None)
	depth_image2_data.to_csv('./kinect_data/depth/depth_RGB' + time_image_string + '.csv', index=None)

	image2_data = pd.DataFrame(image2_data_list, columns=None)
	image2_data.to_csv('./kinect_data/RGB_img/image_RGB' + time_image_string + '.csv', index=None)'''



	'''time_end = time.time()
		if time_end-time_begin>=60:
			time_end_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_end))
			print(time_end)
			print(time_end_string)
			break'''