#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_H2testw 
@File    ：H2test.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2023/10/18 9:40 
'''
import itertools
import psutil
import os
import glob
import struct
import time
import errno


class H2test:
    def __init__(self):
        self.delete_file_percent = 100
        self.cycles = 1
        self.wait_per_cycle = 1
        self.endless_verify = False
        self.option_type = 0
        self.test_size_mb = 2560
        self.written_files = []
        self.read_speed_mean = 0
        self.read_speed_min = 0
        self.read_speed_max = 0
        self.write_speed_mean = 0
        self.write_speed_min = 0
        self.write_speed_max = 0
        self.last_write = False
        self.speed_time = 0
        self.speed_bytes = 0
        self.read_time = 0
        self.write_time = 0
        self.root_directory = 0

    def to_do_work(self):
        self.select_disk()
        for i in range(self.cycles) if not self.endless_verify else itertools.count():
            self.read_speed_max = 0
            self.read_speed_min = 0
            self.read_speed_mean = 0
            self.write_speed_max = 0
            self.write_speed_min = 0
            self.write_speed_mean = 0

            if (0 == self.option_type and not self.endless_verify) or \
                    (0 == i and 0 == self.option_type and self.endless_verify):
                ret = self.write_process()
                if not ret and self.endless_verify:
                    break
                if not ret:
                    continue
            if 1 == self.option_type:
                # 构建文件路径匹配模式
                file_pattern = os.path.join(self.root_directory, "*.h2w")
                # 获取匹配的文件列表并按文件名排序
                file_list = sorted(glob.glob(file_pattern))
                self.written_files = file_list
            self.verify_process()
            self.write_summary_speed()
            if i != self.cycles - 1:
                if 0 != self.wait_per_cycle:
                    time.sleep(self.wait_per_cycle * 60)
                if 0 == self.option_type and not self.endless_verify:
                    if not self.delete_h2w_files(self.delete_file_percent):
                        return 0
        return 1

    def end_work(self):
        self.delete_h2w_files(self.delete_file_percent)

    def select_disk(self):
        # 获取所有可用的磁盘
        available_disks = []
        for partition in psutil.disk_partitions():
            if partition.device and os.path.isdir(partition.mountpoint):
                available_disks.append(partition.device)

        print("Available disks:")
        for i, DISK in enumerate(available_disks):
            print(f"{i + 1}. {DISK}")

        while True:
            try:
                choice = int(input("Select a disk (1, 2, etc.): "))
                if 1 <= choice <= len(available_disks):
                    selected_disk = available_disks[choice - 1]
                    self.root_directory = selected_disk
                    return selected_disk
                else:
                    print("Invalid choice. Please select a valid option.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def build_h2_data(self, n_sec_pos):
        data = bytearray()
        for _ in range(2048):
            ull = n_sec_pos
            data.extend(struct.pack('Q', ull))
            for _ in range(63):
                ull = ull * 0x01 + 17
                data.extend(struct.pack('Q', ull))
            n_sec_pos += 512
        return data

    def write_process(self):
        print("Writing data... ... ... ... ... ...")
        self.written_files.clear()
        test_size_bytes = self.test_size_mb * 1024 ** 2  # Convert MB to bytes
        file_number = 1
        total = 0
        self.write_time = 0
        if not self.last_write:
            self.speed_time = 0
            self.speed_bytes = 0
        disk_full = False
        self.last_write = True

        numbers_bytes_written = 0  # Variables related to timing variables

        while total < test_size_bytes and not disk_full:
            file_name = f"{file_number}.h2w"
            file_path = os.path.join(self.root_directory, file_name)
            try:
                with open(file_path, "wb") as file:
                    need = 0x100000
                    file_size = need * 1024
                    free_temp = 0
                    total_temp = 0
                    free_temp = free_temp // 1024 // 1024 * 1024 * 1024
                    if file_size > free_temp:
                        file_size = free_temp
                    file_written = 0
                    self.written_files.append(file_path)
                    for i in range(1024):
                        if not disk_full:
                            data_buffer = self.build_h2_data(0x40000000 * (file_number - 1) + 0x100000 * i)
                            need = 0x100000
                            if test_size_bytes < need:
                                need = test_size_bytes
                            if test_size_bytes - total < need:
                                need = test_size_bytes - total
                            write = 0

                            while write < need:
                                start_time = time.perf_counter()
                                bytes_written = file.write(data_buffer)
                                if bytes_written < 0:
                                    error_code = os.errno
                                    if error_code == errno.ENOSPC:
                                        disk_full = True
                                        break
                                # file.flush()
                                if 0 == bytes_written:
                                    break
                                end_time = time.perf_counter()
                                execution_time_ms = (end_time - start_time) * 1000000
                                self.speed_time += execution_time_ms
                                self.write_time += execution_time_ms
                                # print("speed_time:", self.speed_time)

                                self.speed_bytes += bytes_written
                                # print("speed_bytes:", self.speed_bytes)
                                if self.speed_time >= 1000000:
                                    diff_time = 1.0 * self.speed_time / 1000000.0
                                    speed = self.speed_bytes / diff_time / 1024 / 1024.0  # 单位MB/s
                                    self.speed_time = 0
                                    self.speed_bytes = 0
                                    if 0 == self.write_speed_mean:
                                        self.write_speed_mean = speed
                                    if 0 == self.write_speed_min:
                                        self.write_speed_min = speed
                                    if self.write_speed_max < speed:
                                        self.write_speed_max = speed
                                    if self.write_speed_min > speed:
                                        self.write_speed_min = speed
                                    self.write_speed_mean = (speed + self.write_speed_mean) / 2
                                write += bytes_written
                            if 0 == write:
                                break

                            total += write
                            file_written += write
                            numbers_bytes_written += write
                            total_temp += write
                            if total >= test_size_bytes:
                                break
                    file.close()
                print(f"Created {file_name} with size: {total_temp / (1024 ** 2):.2f} MB")
                file_number += 1
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except PermissionError:
                print("No permission to manipulate the file")
            except OSError as e:
                if e.errno == 28:
                    disk_full = True
                    print("Insufficient disk space, please free up disk space and try again.")
                else:
                    print(f"Other file system errors have occurred: {e}")
        # print("speed_time:", self.speed_time)
        # print("speed_bytes", self.speed_bytes)
        if 1000000 > self.speed_time > 0:
            # print("speed_time:", self.speed_time)
            diff_time = 1.0 * self.speed_time / 1000000.0
            # print("diff_time:", diff_time)
            # print("speed_bytes:", self.speed_bytes)
            speed = self.speed_bytes / diff_time / 1024 / 1024.0  # 单位MB/s
            # print("speed:", speed)
            self.speed_time = 0
            self.speed_bytes = 0
            if 0 == self.write_speed_mean:
                self.write_speed_mean = speed
            if 0 == self.write_speed_min:
                self.write_speed_min = speed
            if self.write_speed_max < speed:
                self.write_speed_max = speed
            if self.write_speed_min > speed:
                self.write_speed_min = speed
            self.write_speed_mean = (speed + self.write_speed_mean) / 2
            return True

    def write_summary_speed(self):
        print("speed summary:")
        print(f"write min = {self.write_speed_min:.2f}MB/s, write max = {self.write_speed_max:.2f}MB/s, "
              f"write average = {self.write_speed_mean:.2f}MB/s")
        print(f"read min = {self.read_speed_min:.2f}MB/s, read max = {self.read_speed_max:.2f}MB/s, "
              f"read average = {self.read_speed_mean:.2f}MB/s")

    def delete_h2w_files(self, percent):
        if 0 == percent:
            return True
        # 构建文件路径匹配模式
        file_pattern = os.path.join(self.root_directory, "*.h2w")

        # 获取匹配的文件列表并按文件名排序
        file_list = sorted(glob.glob(file_pattern))

        # 计算要删除的文件数量
        num_files_to_delete = int(percent / 100 * len(file_list))

        # 删除文件，从后往前删除
        for i in range(num_files_to_delete):
            file_to_delete = file_list.pop()
            os.remove(file_to_delete)
            # print(f"Deleted: {file_to_delete}")
        return True

    def verify_process(self):
        print("Validating data... ... ... ... ... ...")
        size = len(self.written_files)
        # print(size)
        total = 0
        if self.last_write:
            self.speed_time = 0
            self.speed_bytes = 0
        self.last_write = False
        numbers_bytes_written = 0
        for index in range(size):
            numbers_bytes_written += 1
            try:
                with open(self.written_files[index], 'rb') as file:
                    total_temp = 0
                    # print(self.written_files[index])
                    for i in range(1024):
                        # print("进入第二层循环")
                        data_buffer = self.build_h2_data(0x40000000 * index + 0x100000 * i)
                        need = 0x100000
                        if self.test_size_mb * 1024 * 1024 < need:
                            need = self.test_size_mb * 1024 * 1024
                        if self.test_size_mb * 1024 * 1024 - total < need:
                            need = self.test_size_mb * 1024 * 1024 - total
                        read = 0
                        while read < need:
                            # print("进入第三层循环")
                            start_time = time.perf_counter()
                            bytes_read = file.read(need)
                            if not bytes_read:
                                break
                            # print("读到的长度：", len(bytes_read))
                            end_time = time.perf_counter()
                            execution_time_us = (end_time - start_time) * 1000000

                            # print("execution_time_us", execution_time_us)
                            self.speed_time += execution_time_us
                            self.read_time += execution_time_us
                            self.speed_bytes += len(bytes_read)
                            # print("speed_bytes", self.speed_bytes)
                            # print("speed_time", self.speed_time)
                            if self.speed_time >= 1000000:
                                diff_time = 1.0 * self.speed_time / 1000000.0
                                speed = self.speed_bytes / diff_time / 1024 / 1024.0  # 单位MB/s
                                self.speed_time = 0
                                self.speed_bytes = 0
                                if 0 == self.read_speed_mean:
                                    self.read_speed_mean = speed
                                if 0 == self.read_speed_min:
                                    self.read_speed_min = speed
                                if self.read_speed_max < speed:
                                    self.read_speed_max = speed
                                if self.read_speed_min > speed:
                                    self.read_speed_min = speed
                                self.read_speed_mean = (speed + self.read_speed_mean) / 2
                            read += len(bytes_read)
                            # print("read:", read)
                        total += read
                        total_temp += read
                        if 0 == read:
                            break
                        expected_offset = 0
                        bytes_read = bytearray(bytes_read)
                        if bytes_read != data_buffer:
                            print(f"LOG NOTE: MismatchFileName: {self.written_files[index]}, "
                                  f"Mismatch Pos: {i * 0x100000}")
                    file.close()
                print(f"Verified {self.written_files[index]} with size: {total_temp / (1024 ** 2):.2f} MB")
            except FileNotFoundError:
                print(f"File not found: {self.written_files[index]}")
            except Exception as e:
                print(f"An error occurred while processing {self.written_files[index]}: {str(e)}")
        # print("speed_time:", self.speed_time)
        # print("speed_bytes", self.speed_bytes)
        if 1000000 > self.speed_time > 0:
            diff_time = 1.0 * self.speed_time / 1000000.0
            speed = self.speed_bytes / diff_time / 1024 / 1024.0  # 单位MB/s
            self.speed_time = 0
            self.speed_bytes = 0
            if 0 == self.read_speed_mean:
                self.read_speed_mean = speed
            if 0 == self.read_speed_min:
                self.read_speed_min = speed
            if self.read_speed_max < speed:
                self.read_speed_max = speed
            if self.read_speed_min > speed:
                self.read_speed_min = speed
            self.read_speed_mean = (speed + self.read_speed_mean) / 2


if __name__ == "__main__":
    test = H2test()
    # disk = test.select_disk()
    # # test_size_mb = float(input("Enter the test space size (in MB): "))
    # test.write_process()
    # test.verify_process()
    # test.write_summary_speed()
    test.to_do_work()
    # test.delete_h2w_files(100)
