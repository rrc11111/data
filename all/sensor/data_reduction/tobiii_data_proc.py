import shutil
import os


def move_folder(source_folder, destination_folder):
    try:
        os.makedirs(destination_folder, exist_ok=True)
        # 执行移动操作
        shutil.move(source_folder, destination_folder)

        print(f"移动成功：{source_folder} 到 {destination_folder}")

    except Exception as e:
        print(f"移动失败：{e}")


def get_subdirectories(folder_path):
    try:
        # 获取文件夹下的所有文件和文件夹
        entries = os.listdir(folder_path)

        # 筛选出文件夹的名字
        subdirectories = [entry for entry in entries if os.path.isdir(os.path.join(folder_path, entry))]

        return subdirectories

    except Exception as e:
        print(f"获取文件夹名字失败：{e}")
        return []


if __name__ == '__main__':
    path_tobii = 'D:/All_kichen_data/sub15_source_data_chenyuhang/tobii_data'
    files_names_tobii = get_subdirectories(path_tobii)
    for i in range(len(files_names_tobii)):
        move_folder(path_tobii + '/' +files_names_tobii[i],
                    path_tobii + f'/C{(i + 2) // 2}-source_data/T{i % 2 + 1}')
