# ----------------------------------------------------------------------------
# -                        Open3D: www.open3d.org                            -
# ----------------------------------------------------------------------------
# Copyright (c) 2018-2023 www.open3d.org
# SPDX-License-Identifier: MIT
# ----------------------------------------------------------------------------

# examples/python/reconstruction_system/sensors/azure_kinect_mkv_reader.py

import argparse
import open3d as o3d
import os
import json
import sys
import cv2
import numpy as np

pwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(pwd, '..'))
from initialize_config import initialize_config


class ReaderWithCallback:

    def __init__(self, input, output):
        self.flag_exit = False
        self.flag_play = True
        self.input = input
        self.output = output

        self.reader = o3d.io.AzureKinectMKVReader()
        self.reader.open(self.input)
        if not self.reader.is_opened():
            raise RuntimeError("Unable to open file {}".format(self.input))

    def escape_callback(self, vis):
        self.flag_exit = True
        return False

    def space_callback(self, vis):
        if self.flag_play:
            print('Playback paused, press [SPACE] to continue.')
        else:
            print('Playback resumed, press [SPACE] to pause.')
        self.flag_play = not self.flag_play
        return False

    def run(self):
        glfw_key_escape = 256
        glfw_key_space = 32
        vis = o3d.visualization.VisualizerWithKeyCallback()
        vis.register_key_callback(glfw_key_escape, self.escape_callback)
        vis.register_key_callback(glfw_key_space, self.space_callback)

        vis_geometry_added = False
        vis.create_window('reader', 1920, 540)

        print(
            "MKV reader initialized. Press [SPACE] to pause/start, [ESC] to exit."
        )

        if self.output is not None:
            abspath = os.path.abspath(self.output)
            metadata = self.reader.get_metadata()
            o3d.io.write_azure_kinect_mkv_metadata(
                '{}\intrinsic.json'.format(abspath), metadata)

            config = {
                'path_dataset': abspath,
                'path_intrinsic': '{}\intrinsic.json'.format(abspath)
            }
            initialize_config(config)
            with open('{}\config.json'.format(abspath), 'w') as f:
                json.dump(config, f, indent=4)

        idx = 0

        while not self.reader.is_eof() and not self.flag_exit:
            if self.flag_play:
                # pcd = o3d.geometry.PointCloud()
                rgbd = self.reader.next_frame()
                if rgbd is None:
                    continue

                if not vis_geometry_added:
                    vis.add_geometry(rgbd)
                    vis_geometry_added = True

                if self.output is not None:
                    color_filename = '{0}\color\{1:05d}.jpg'.format(
                        self.output, idx)
                    # print('Writing to {}'.format(color_filename))
                    o3d.io.write_image(color_filename, rgbd.color)
                    # print(np.asarray(rgbd.color))
                    rgbd_image = o3d.geometry.RGBDImage.create_from_color_and_depth(
                        o3d.geometry.Image(np.asarray(rgbd.color)),
                        o3d.geometry.Image(np.asarray(rgbd.depth)),
                        convert_rgb_to_intensity=False)
                    cx = 958.4725341796875
                    cy = 553.2557983398438
                    fx = 912.1604614257812
                    fy = 912.01220703125
                    intrinsic = o3d.camera.PinholeCameraIntrinsic(1920, 1080, fx, fy, cx, cy)
                    pcd = o3d.geometry.PointCloud.create_from_rgbd_image(rgbd_image, intrinsic)
                    pcd.transform([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, 1]])
                    # pcd.points = o3d.utility.Vector3dVector(temp.points)
                    # pcd.colors = o3d.utility.Vector3dVector(temp.colors)
                    # print(pcd.points)

                    pcd_filename = '{0}\pcd\{1:05d}.pcd'.format(
                        self.output, idx)
                    o3d.io.write_point_cloud(pcd_filename, pcd)
                    print('Writing to {}'.format(pcd_filename))


                    # Flip it, otherwise the pointcloud will be upside down

                    depth_filename = '{0}\depth\{1:05d}.png'.format(
                        self.output, idx)
                    print('Writing to {}'.format(depth_filename))

                    depth_array = np.asarray(rgbd.depth)
                    normalized_depth = cv2.normalize(depth_array, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

                    # 将单通道灰度图像映射为热力图
                    colormap_depth_image = cv2.applyColorMap(normalized_depth, cv2.COLORMAP_JET)

                    # 将热力图转换为 open3d Image 对象
                    colormap_depth_o3d = o3d.geometry.Image(colormap_depth_image)

                    # o3d.io.write_image(depth_filename, rgbd.depth)
                    o3d.io.write_image(depth_filename, colormap_depth_o3d)

                    idx += 1

            try:
                vis.update_geometry(rgbd)
            except NameError:
                pass
            vis.poll_events()
            vis.update_renderer()
        self.reader.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Azure kinect mkv reader.')
    parser.add_argument('--input',
                        type=str,
                        required=True,
                        help='input mkv file')
    parser.add_argument('--output',
                        type=str,
                        help='output path to store color/ and depth/ images')
    args = parser.parse_args()

    if args.input is None:
        parser.print_help()
        exit()

    if args.output is None:
        print('No output path, only play mkv')
    # elif not os.path.exists(args.output):
    #     directory = os.path.dirname(args.output)  # 使用 os.makedirs 创建目录（如果不存在）
    #     print(directory)
    #     os.makedirs(directory, exist_ok=True)
    elif os.path.isdir(args.output):
        print('Output path {} already existing, only play mkv'.format(
            args.output))
        args.output = None
    else:
        try:
            # directory = os.path.dirname(args.output, exist_ok=True)
            os.makedirs(args.output, exist_ok=True)
            os.mkdir('{}\color'.format(args.output))
            os.mkdir('{}\depth'.format(args.output))
            os.mkdir('{}\pcd'.format(args.output))
        except (PermissionError, FileExistsError):
            print('Unable to mkdir {}, only play mkv'.format(args.output))
            args.output = None

    reader = ReaderWithCallback(args.input, args.output)
    reader.run()
