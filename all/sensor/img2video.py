import cv2
import numpy as np
import glob
import os
import argparse

# 其它格式的图片也可以
class pngfile:
    def __init__(self, input, output):
        self.input = input
        self.output = output
    def img2vedio(self, frame_rate):
        img_array = []
        for img_name in glob.glob(self.input):
            img = cv2.imread(img_name)
            height, width, layers = img.shape
            size = (width, height)
            img_array.append(img)

        # avi：视频类型，mp4也可以
        # cv2.VideoWriter_fourcc(*'DIVX')：编码格式
        # 5：视频帧率
        # size:视频中图片大小
        out = cv2.VideoWriter(self.output,
                              cv2.VideoWriter_fourcc(*'DIVX'),
                              frame_rate, size)

        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='img2video')
    parser.add_argument('--input',
                        type=str,
                        required=True,
                        help='input file of png')
    parser.add_argument('--output',
                        type=str,
                        help='output path to store video')
    args = parser.parse_args()
    depth_video = pngfile(args.input, args.output)
    depth_video.img2vedio(12.96)
    print("合成成功")
