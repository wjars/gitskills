#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：document_copy_1.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/12 9:43 
'''
import os
import random
import configparser
import shutil
import threading
import hashlib
import sys
import logging

total_file_cnt = 0
file_path_list = []
config_file_path = "folder_file_config.ini"


def setup_logger(log_filename="log.txt"):
    """
    @brief: Log message recording.
    @parameter: Defaults to 'log.txt'
    @return: logger.
    """
    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the logging level
    logger.setLevel(level=logging.DEBUG)

    # Create a file handler and set the logging level for the handler
    handler = logging.FileHandler(log_filename)
    handler.setLevel(logging.DEBUG)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)

    return logger


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


def copy_files(src_path, dst_path, lock, exception_list=None):
    """
    @brief: Copy the source folder to the destination path.
    @parameter: src_path: Path to the source file to be copied.
                dst_path: Destination path for copying.
                lock: lock variable.
                exception_list: List for storing caught exceptions
    @return: None
    """
    current_thread_name = threading.current_thread().name
    for src in src_path:
        try:
            src_prefix = os.path.dirname(src)
            root_index = src_prefix.find('root')
            suffix = src_prefix[root_index:]
            dst_path_tem = os.path.join(dst_path, suffix)
            # Check available disk space before copying
            if not os.path.exists(dst_path_tem):
                with lock:
                    # Use lock to ensure thread safety when creating the directory
                    os.makedirs(dst_path_tem, exist_ok=True)
            shutil.copy(src, dst_path_tem)
        except Exception as e:
            if exception_list is not None:
                with lock:
                    # Use lock to ensure thread safety when appending to the exception list
                    exception_list.append((current_thread_name, e))

                    sys.exit(1)
            else:
                raise e  # If exception_list is not provided, re-raise the exception


def copy_files_threaded(file_list, num_thread):
    """
    @brief: Multi-threaded copying of files and folders.
    @parameter: file_list: Files Path List.
                num_thread: Number of threads used.
    @return: None
    """
    length_of_list = len(file_list)
    if length_of_list >= num_thread:
        average_file_num = length_of_list // num_thread
        extra_file_num = length_of_list % num_thread
        # Divide the list of source files into m sublists, each consisting of n files
        divided_sources = [file_list[i:i + average_file_num] for i in
                           range(0, length_of_list - extra_file_num, average_file_num)]
        divided_sources[-1].extend(file_list[-extra_file_num:])
    else:
        average_file_num = 1
        divided_sources = [file_list[i:i + average_file_num] for i in
                           range(0, length_of_list)]
    # Multithreaded task implementation
    # Creating a Global Lock
    global_lock = threading.Lock()
    threads = []
    exceptions = []  # List to store exceptions raised in threads
    for files_to_copy in divided_sources:
        thread = threading.Thread(target=copy_files,
                                  args=(files_to_copy, destination_path, global_lock, exceptions),
                                  name=f"Thread-{len(threads) + 1}")
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    # Check if any exceptions occurred in threads
    if exceptions:
        # Call setup_logger() once outside the loop
        # logger = setup_logger()
        print("Exceptions occurred in threads:")
        for thread_name, e in exceptions:
            logger.error(f"Thread '{thread_name}' - An error occurred: {str(e)}")
            print(f"Thread '{thread_name}' - {e}")
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
    logger = setup_logger()
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
        logger.info("Files contents consistent")
    else:
        print("Files contents are inconsistent")
        logger.error("Files contents are inconsistent")
        sys.exit(1)
