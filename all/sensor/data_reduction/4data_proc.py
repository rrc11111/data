import shutil
import os


def move_and_rename(source_path, destination_folder, new_filename):
    try:
        # 确保目标文件夹存在，如果不存在则创建
        os.makedirs(destination_folder, exist_ok=True)

        # 构建目标路径，将文件移动到指定文件夹并重命名
        destination_path = os.path.join(destination_folder, new_filename)
        shutil.move(source_path, destination_path)

        print(f"移动成功：{source_path} 到 {destination_path}")

    except Exception as e:
        print(f"移动失败：{e}")


def list_files_with_extension(folder_path, extension):
    """
    列出文件夹中特定扩展名的所有文件名

    参数：
    - folder_path: 文件夹路径
    - extension: 扩展名（例如：'.txt'）
    """
    file_names = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return file_names


if __name__ == '__main__':
    sub_path = 'D:/All_kichen_data/sub17_source_data_weiyi'

    # path_emg = sub_path + '/delsys_data/emg'
    # files_names_emg = list_files_with_extension(
    #     path_emg,
    #     '.csv')
    # for i in range(len(files_names_emg)):
    #     move_and_rename(path_emg + '/' + files_names_emg[i],
    #                     path_emg + f'/C{(i + 2) // 2}-source_data/T{i % 2 + 1}', files_names_emg[i])
    #
    # path_acc = sub_path + '/delsys_data/acc'
    # files_names_acc = list_files_with_extension(
    #     path_acc,
    #     '.csv')
    # for i in range(len(files_names_acc)):
    #     move_and_rename(path_acc + '/' + files_names_acc[i],
    #                     path_acc + f'/C{(i + 2) // 2}-source_data/T{i % 2 + 1}', files_names_acc[i])
    #
    path_glove = sub_path + '/gloves_data'
    files_names_glove_right = list_files_with_extension(
        path_glove + '/right',
        '.csv')
    for i in range(len(files_names_glove_right)):
        move_and_rename(path_glove + '/right/' + files_names_glove_right[i],
                        path_glove + f'/C{(i + 2) // 2}-source_data/T{i % 2 + 1}', files_names_glove_right[i])

    files_names_glove_left = list_files_with_extension(
        path_glove + '/left',
        '.csv')
    for i in range(len(files_names_glove_left)):
        move_and_rename(path_glove + '/left/' + files_names_glove_left[i],
                        path_glove + f'/C{(i + 2) // 2}-source_data/T{i % 2 + 1}', files_names_glove_left[i])

    # path_kinect = sub_path + '/kinect_data/RGB_video'
    #
    # for j in range(2, 3):
    #     files_names_mkv = list_files_with_extension(path_kinect + f'/{j}',
    #                                                 '.mkv')
    #     files_names_txt = list_files_with_extension(path_kinect + f'/{j}',
    #                                                 '.txt')
    #     for i in range(len(files_names_mkv)):
    #         move_and_rename(path_kinect + f'/{j}/' + files_names_mkv[i],
    #                         path_kinect + f'/{j}/C{(i + 2) // 2}-source_data/T{i % 2 + 1}',
    #                         f'kinect_{j}_' + files_names_mkv[i])
    #
    #     for i in range(len(files_names_txt)):
    #         move_and_rename(path_kinect + f'/{j}/' + files_names_txt[i],
    #                         path_kinect + f'/{j}/C{(i + 2) // 2}-source_data/T{i % 2 + 1}',
    #                         f'kinect_{j}_' + files_names_txt[i])

    # path_micro = sub_path + '/voice_data'
    # for j in range(0, 4):
    #     files_names_wav = list_files_with_extension(path_micro + f'/{j}',
    #                                                 '.wav')
    #     files_names_micro_txt = list_files_with_extension(path_micro + f'/{j}',
    #                                                       '.txt')
    #     for i in range(len(files_names_wav)):
    #         move_and_rename(path_micro + f'/{j}/' + files_names_wav[i],
    #                         path_micro + f'/{j}/C{(i + 2) // 2}-source_data/T{i % 2 + 1}',
    #                         f'micro_{j}_' + files_names_wav[i])
    #
    #     for i in range(len(files_names_micro_txt)):
    #         move_and_rename(path_micro + f'/{j}/' + files_names_micro_txt[i],
    #                         path_micro + f'/{j}/C{(i + 2) // 2}-source_data/T{i % 2 + 1}',
    #                         f'micro_{j}_' + files_names_micro_txt[i])
