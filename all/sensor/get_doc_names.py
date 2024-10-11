import os


def list_files_with_extension(folder_path, extension):
    """
    列出文件夹中特定扩展名的所有文件名

    参数：
    - folder_path: 文件夹路径
    - extension: 扩展名（例如：'.txt'）
    """
    file_names = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return file_names


# 示例用法
folder_path = r'C:\Users\Dell\Desktop\all\kinect\database\kinect_data\RGB_video\1'
extension = '.mkv'
files = list_files_with_extension(folder_path, extension)
m = 0
with open('1.txt', 'w') as file:
    for i in range(1,18):
        for j in range(1,3):
            # 打开文件以写入模式
            # 逐行写入内容
            file.write(
                'python kinect/azure_kinect_mkv_reader.py --input kinect/database/kinect_data/RGB_video/1/' + files[
                    m] + f' --output kinect/database/kinect_data/C{i}_source_data/T{j}\n')
            m += 1
