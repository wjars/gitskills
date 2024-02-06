#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonProject_document
@File    ：document_copy.py
@IDE     ：PyCharm
@Author  ：厄运马马卡
@Date    ：2024/1/9 18:06
"""
import os
import random
import shutil
import time
import threading
import hashlib


def generate_random_file_content(size):
    """
    @brief: Generating Random Data.
    @parameter: Size of random data generated (unit: bytes).
    @return: Random encrypted string.
    """
    return os.urandom(size)


def create_files_in_folders(root_path, destination_path):
    """
    @brief: Recursive creation of folders and files.
    @parameter: root_path: source path.
                destination_path: target path.
    @return: file_path_list: File path list.
             folder_path_list: Folder path list.
    """
    file_path_list = []
    folder_path_list = []
    tatol_file = 0
    # Create a root folder
    root_folder = os.path.join(root_path, 'root')
    os.makedirs(root_folder, exist_ok=True)

    for x in range(1, random.randint(1, 10) + 1):
        file_name_1 = f"{x*11}"
        file_path_1 = os.path.join(root_folder, file_name_1)
        file_size = random.randint(1, 1024 * 1024)
        with open(file_path_1, 'wb') as file:
            file.write(generate_random_file_content(file_size))
        tatol_file += 1
        file_path_list.append(file_path_1)
        folder_path_list.append(destination_path)

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
            file_path_list.append(file_path_2)
            folder_path_list.append(os.path.join(destination_path, folder_name_1))

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
                file_path_list.append(file_path_3)
                folder_path_list.append(os.path.join(destination_path, folder_name_1, folder_name_2))
    # print("tatol_file:", tatol_file)
    # print("len(file_path_list):", len(file_path_list))
    # print("len(folder_path_list):", len(folder_path_list))
    # print(file_path_list)
    # print(folder_path_list)
    return file_path_list, folder_path_list


def copy_files(source, destination, lock):
    """
    @brief: Copy the source folder to the destination path.
    @parameter: source: Path to the source file to be copied.
                destination: Destination path for copying.
                lock: lock variable.
    @return: None
    """
    try:
        for index, src in enumerate(source):
            if not os.path.exists(destination[index]):
                with lock:
                    # Use lock to ensure thread safety when creating the directory
                    os.makedirs(destination[index], exist_ok=True)
            shutil.copy(src, destination[index])
    except Exception as e:
        print(f"Error copying files: {e}")


def copy_files_threaded(file_list, folder_list):
    """
    @brief: Multi-threaded copying of files and folders.
    @parameter: file_list: Files Path List.
                folder_list: Folders Path List.
    @return: None
    """
    length_of_list = len(file_list)
    if length_of_list >= 10:
        average_file_num = length_of_list // 10
        extra_file_num = length_of_list % 10

        divided_sources = [file_list[i:i + average_file_num] for i in
                           range(0, length_of_list - extra_file_num, average_file_num)]
        divided_sources[-1].extend(file_list[-extra_file_num:])
        divided_destination = [folder_list[i:i + average_file_num] for i in
                               range(0, len(folder_list) - extra_file_num, average_file_num)]
        divided_destination[-1].extend(folder_list[-extra_file_num:])
    else:
        average_file_num = 1
        divided_sources = [file_list[i:i + average_file_num] for i in
                           range(0, length_of_list)]
        divided_destination = [folder_list[i:i + average_file_num] for i in
                               range(0, len(folder_list))]
        print(divided_sources)
    # Multithreaded task implementation
    # 创建一个全局锁对象
    global_lock = threading.Lock()
    threads = []
    for index, files_to_copy in enumerate(divided_sources):
        thread = threading.Thread(target=copy_files, args=(files_to_copy, divided_destination[index], global_lock))
        threads.append(thread)
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def hash_file(file_path):
    """
    @brief: Calculate the hash value (md5).
    @parameter: file_path: Path to the file whose hash is to be calculated.
    @return: The result of calculating the file hash (using the MD5 algorithm), in hexadecimal.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read(1024)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(1024)
    return hasher.hexdigest()


def compare_folders(src, dest):
    """
    @brief: Compare hashes of files before and after copying.
    @parameter: src: Source file path.
                    dest: Target File Path
    @return: True or False.
    """
    src_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(src) for f in filenames]
    dest_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dest) for f in filenames]
    # print("len(src_files):", len(src_files))
    # print("len(dest_files):", len(dest_files))

    src_hashes = {f: hash_file(f) for f in src_files}
    dest_hashes = {f: hash_file(f) for f in dest_files}

    return set(src_hashes.values()) == set(dest_hashes.values())


if __name__ == "__main__":
    # start_time = time.time()
    source_path = r'D:\download\pycharm\pythonProject_document\source_folder'
    destination_path = r'D:\download\pycharm\pythonProject_document\destination_folder'
    destination_path = os.path.join(destination_path, "root")
    file_list, folder_list = create_files_in_folders(source_path, destination_path)
    copy_files_threaded(file_list, folder_list)
    print(f"Successfully created root folder 'root' in {source_path} ")
    result = compare_folders(source_path, destination_path)
    if result:
        print("Files content consistency")
    else:
        print("Files contents are inconsistent")
    # end_time = time.time()
    # execution_time_ms = (end_time - start_time) * 1000
    # print(f"程序运行时间: {execution_time_ms:.2f} 毫秒")
    # random.randint(1, 10)