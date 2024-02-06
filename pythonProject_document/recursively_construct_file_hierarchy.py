#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：recursively_construct_file_hierarchy.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/15 16:54 
'''
import os
import random


def generate_random_data(size):
    """生成随机数据"""
    return os.urandom(size)


def create_folders_and_files(path, depth):
    """递归创建文件夹和文件"""
    if depth <= 0:
        return
    # 生成随机数量的文件夹和文件
    num_folders = random.randint(1, 10)
    num_files = random.randint(1, 10)
    if not os.path.exists(root_folder):
        os.mkdir(root_folder)

    for i in range(1, num_folders + 1):
        folder_name = f"{i}"
        folder_path = os.path.join(path, folder_name)
        os.mkdir(folder_path)
        if depth == 1:  # 最后一级目录，只创建文件
            num_files_last = random.randint(1, 10)
            for j in range(1, num_files_last + 1):
                file_name = f"{j * 11}"
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'wb') as file:
                    file.write(generate_random_data(random.randint(1, 1024 * 1024)))
        else:
            create_folders_and_files(folder_path, depth - 1)

    for i in range(1, num_files + 1):
        file_name = f"{i * 11}"
        file_path = os.path.join(path, file_name)
        with open(file_path, 'wb') as file:
            file.write(generate_random_data(random.randint(1, 1024 * 1024)))


if __name__ == "__main__":
    target_location = "D:\download\pycharm\pythonProject_document\source_folder"  # 请替换成你想要的目标位置
    root_folder = os.path.join(target_location, "root")
    # if not os.path.exists(root_folder):
    #     os.mkdir(root_folder)
    create_folders_and_files(root_folder, 0)  # 2 表示根目录下有两层子目录，总共三级目录
    print("文件夹和文件生成完成。")
