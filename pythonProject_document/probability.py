#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：probability.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/11 11:30 
'''
import os
import random
import shutil


# def create_files_in_folders(root_path):
#     tatol_file = 0
#     # Create a root folder
#     root_folder = os.path.join(root_path, 'root')
#     os.makedirs(root_folder, exist_ok=True)
#
#     # Create sequentially named subfolders in the root folder
#     for i in range(1, random.randint(1, 10) + 1):
#         folder_name_1 = f"{i}"
#         folder_path_1 = os.path.join(root_folder, folder_name_1)
#         os.makedirs(folder_path_1, exist_ok=True)
#
#         for j in range(1, random.randint(1, 10) + 1):
#             folder_name_2 = f"{j}"
#             folder_path_2 = os.path.join(folder_path_1, folder_name_2)
#             os.makedirs(folder_path_2, exist_ok=True)
#
#             # Create a random number of files in each subfolder
#             for k in range(1, random.randint(1, 10) + 1):
#                 file_name = f"{k}"
#                 file_path = os.path.join(folder_path_2, file_name)
#                 tatol_file += 1
#     return tatol_file
#
#
def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
        print(f"Folder {folder_path} and its contents have been deleted.")
    except Exception as e:
        print(f"Error deleting folder: {e}")


def generate_random_file_content(size):
    # Generate random file contents, using a simple example here
    return os.urandom(size)


def create_files_in_folders(root_path):
    file_path_list = []
    folder_path_list = []
    tatol_file = 0
    # Create a root folder
    root_folder = os.path.join(root_path, 'root')
    os.makedirs(root_folder, exist_ok=True)

    for x in range(1, random.randint(1, 10) + 1):
        file_name_1 = f"{x * 11}"
        file_path_1 = os.path.join(root_folder, file_name_1)
        file_size = random.randint(1, 1024 * 1024)
        with open(file_path_1, 'wb') as file:
            file.write(generate_random_file_content(file_size))
        tatol_file += 1

    # Create sequentially named subfolders in the root folder
    for i in range(1, random.randint(1, 10) + 1):
        folder_name_1 = f"{i}"
        folder_path_1 = os.path.join(root_folder, folder_name_1)
        os.makedirs(folder_path_1, exist_ok=True)

        for y in range(1, random.randint(1, 10) + 1):
            file_name_2 = f"{y * 11}"
            file_path_2 = os.path.join(folder_path_1, file_name_2)
            file_size = random.randint(1, 1024 * 1024)
            with open(file_path_2, 'wb') as file:
                file.write(generate_random_file_content(file_size))
            tatol_file += 1

        for j in range(1, random.randint(1, 10) + 1):
            folder_name_2 = f"{j}"
            folder_path_2 = os.path.join(folder_path_1, folder_name_2)
            os.makedirs(folder_path_2, exist_ok=True)

            # Create a random number of files in each subfolder
            for k in range(1, random.randint(1, 10) + 1):
                file_name = f"{k}"
                file_path_3 = os.path.join(folder_path_2, file_name)
                # Randomly generate file sizes ranging from 1 byte to 1MB
                file_size = random.randint(1, 1024 * 1024)
                with open(file_path_3, 'wb') as file:
                    file.write(generate_random_file_content(file_size))
                tatol_file += 1

    # print("tatol_file:", tatol_file)
    # print("len(file_path_list):", len(file_path_list))
    # print("len(folder_path_list):", len(folder_path_list))
    # print(file_path_list)
    # print(folder_path_list)
    return tatol_file


if __name__ == '__main__':
    list = []
    source_path = r'D:\download\pycharm\pythonProject_document\source_folder'
    for i in range(10000):
        file_num = create_files_in_folders(source_path)
        print("生成的文件数为:", file_num)
        if file_num < 10:
            list.append(file_num)
        delete_folder(os.path.join(source_path, 'root'))
    print("生成文件小于10的次数为:", len(list))
