#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：hash_compare.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/9 18:06 
'''
import os
import shutil
import random
import string
import hashlib
import threading




def hash_file(file_path):
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read(1024)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(1024)
    return hasher.hexdigest()


def compare_folders(src, dest):
    src_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(src) for f in filenames]
    dest_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dest) for f in filenames]
    print(src_files)
    print(dest_files)

    src_hashes = {f: hash_file(f) for f in src_files}
    dest_hashes = {f: hash_file(f) for f in dest_files}
    print(src_hashes)
    print(dest_hashes)

    return set(src_hashes.values()) == set(dest_hashes.values())




if __name__ == "__main__":
    # 设置源文件夹和目标文件夹
    source_folder = "D:\download\pycharm\pythonProject_document\source_folder"
    destination_folder = "D:\download\pycharm\pythonProject_document\destination_folder"
    # 比较源文件夹和目标文件夹
    result = compare_folders(source_folder, destination_folder)

    if result:
        print("文件夹内容一致")
    else:
        print("文件夹内容不一致")


