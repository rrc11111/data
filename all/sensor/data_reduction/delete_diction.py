import os
import shutil

def delete_files_in_folder(folder_path):
    # 遍历指定文件夹下的所有文件和子文件夹
    for root, dirs, files in os.walk(folder_path):
        # 删除当前路径下的文件夹
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
            except OSError:
                # 文件夹不为空，无法直接删除
                pass
            # 创建空文件夹
            os.makedirs(dir_path, exist_ok=True)

        # 删除所有文件
        for file in files:
            file_path = os.path.join(root, file)
            os.remove(file_path)

if __name__ == "__main__":
    folder_to_clear = r'C:\Users\Dell\Desktop\sub1_xionson'
    delete_files_in_folder(folder_to_clear)