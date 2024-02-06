#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：document_threadpool_copy.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/16 14:03 
'''
import os
import random
import configparser
import shutil
from concurrent.futures import ThreadPoolExecutor
import hashlib
import sys

total_file_cnt = 0
file_path_list = []
config_file_path = "folder_file_config.ini"


def get_param(section, option):
    """
    @brief: Getting Parameters in the Configuration File.
    @parameter: section: A section or region of a configuration file.
                option: A specific configuration item (parameter) in a given section.
    @return: The value of the parameter.
    """
    config = configparser.ConfigParser()
    config.read(config_file_path)
    return config.get(section, option)


def generate_random_file_content(size):
    """
    @brief: Generating Random Data.
    @parameter: Size of random data generated (unit: bytes).
    @return: Random encrypted string.
    """
    return os.urandom(size)


def __create_folders_and_files(src_path, depth):
    """
    @brief: Recursive creation of folders and files.
    @parameter: src_path: source path.
                depth: Level of documentation.
    @return: None
    """
    global total_file_cnt
    if depth <= 0:
        print("Folder depth should be greater than 0")
        sys.exit(1)
    if depth == 1:  # Last level of directory, file creation only
        if not os.path.exists(src_path):
            os.mkdir(src_path)
        num_files_last = random.randint(min_file_cnt, max_file_cnt)
        for j in range(1, num_files_last + 1):
            file_name = f"{j}.txt"
            file_path = os.path.join(src_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(generate_random_file_content(random.randint(min_fill_data_size, max_fill_data_size)))
            total_file_cnt += 1
            file_path_list.append(file_path)
    else:
        # Generate a random number of folders and files
        num_folders = random.randint(min_folder_cnt, max_folder_cnt)
        num_files = random.randint(min_file_cnt, max_file_cnt)
        if not os.path.exists(src_path):
            os.mkdir(src_path)
        for i in range(1, num_folders + 1):
            folder_name = f"{i}"
            folder_path = os.path.join(src_path, folder_name)
            os.mkdir(folder_path)
            __create_folders_and_files(folder_path, depth - 1)

        for i in range(1, num_files + 1):
            file_name = f"{i}.txt"
            file_path = os.path.join(src_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(generate_random_file_content(random.randint(min_fill_data_size, max_fill_data_size)))
            total_file_cnt += 1
            file_path_list.append(file_path)


def copy_files(src_path, dst_path, exception_list=None):
    """
    @brief: Copy the source folder to the destination path.
    @parameter: src_path: Path to the source file to be copied.
                dst_path: Destination path for copying.
                exception_list: List for storing caught exceptions
    @return: None
    """

    try:
        src_prefix = os.path.dirname(src_path)
        root_index = src_prefix.find('root')
        suffix = src_prefix[root_index:]
        dst_path_tem = os.path.join(dst_path, suffix)
        # Check available disk space before copying
        if not os.path.exists(dst_path_tem):
            os.makedirs(dst_path_tem, exist_ok=True)
        shutil.copy(src_path, dst_path_tem)
    except Exception as e:
        if exception_list is not None:
            exception_list.append(e)
            sys.exit(1)
        else:
            raise e  # If exception_list is not provided, re-raise the exception


def copy_files_threaded(file_list, num_thread):
    """
    @brief: Threadpool copying of files and folders.
    @parameter: file_list: Files Path List.
                num_thread: Number of threads used.
    @return: None
    """
    exceptions = []  # List to store exceptions raised in threads
    with ThreadPoolExecutor(max_workers=num_thread) as executor:
        for files_to_copy in file_list:
            executor.submit(copy_files, files_to_copy, destination_path, exceptions)

    # Check if any exceptions occurred in threads
    if exceptions:
        print("Exceptions occurred in threads:")
        for e in exceptions:
            print(f"- {e}")
        # Raise an exception
        raise RuntimeError("Error(s) occurred during file copy in one or more threads")


def cal_hash_value(file_path):
    """
    @brief: Calculate the hash value (md5).
    @parameter: Path to the file whose hash is to be calculated.
    @return: The result of calculating the file hash (using the MD5 algorithm), in hexadecimal.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as file:
        buf = file.read(1024)
        while len(buf) > 0:
            hasher.update(buf)
            buf = file.read(1024)
    return hasher.hexdigest()


def compare_folders(src_path, dst_path):
    """
    @brief: Compare hashes of files before and after copying.
    @parameter: src_path: Source path.
                dst_path: Destination path.
    @return: True or False.
    """
    src_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(src_path) for f in filenames]
    dst_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dst_path) for f in filenames]
    # print("len(src_files):", len(src_files))
    # print("len(dst_files):", len(dst_files))

    src_hashes = {f: cal_hash_value(f) for f in src_files}
    dst_hashes = {f: cal_hash_value(f) for f in dst_files}

    return set(src_hashes.values()) == set(dst_hashes.values())


if __name__ == "__main__":
    source_path = get_param('Paths', 'source_path')
    destination_path = get_param('Paths', 'destination_path')
    min_folder_cnt = int(get_param('Settings', 'min_folder_cnt'))
    max_folder_cnt = int(get_param('Settings', 'max_folder_cnt'))
    min_file_cnt = int(get_param('Settings', 'min_file_cnt'))
    max_file_cnt = int(get_param('Settings', 'max_file_cnt'))
    min_fill_data_size = int(get_param('Settings', 'min_fill_data_size'))
    max_fill_data_size = int(get_param('Settings', 'max_fill_data_size'))
    folder_depth = int(get_param('Settings', 'depth'))
    number_threads = int(get_param('Settings', 'num_thread'))
    # emmc = int(get_param('Settings', 'emmc'))
    folder_path = os.path.join(source_path, "root")
    dst_path = os.path.join(destination_path, 'root')
    __create_folders_and_files(folder_path, folder_depth)
    # print("Folder and file generation complete.")
    # print("total_file_cnts = ", total_file_cnt)
    # print("len(file_path_list):", len(file_path_list))
    # print("len(folder_path_list):", len(folder_path_list))
    # print("file_path_list:", file_path_list)
    # print("folder_path_list:", folder_path_list)
    print(total_file_cnt)
    try:
        copy_files_threaded(file_path_list, number_threads)
    except RuntimeError as e:
        print(f"Error: {e}")
        sys.exit(1)
    result = compare_folders(source_path, destination_path)
    if result:
        print("Files content consistency")
    else:
        print("Files contents are inconsistent")
        sys.exit(1)

