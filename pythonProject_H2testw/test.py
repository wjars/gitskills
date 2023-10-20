#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_H2testw 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2023/10/18 11:36 
'''

import struct
import time

# with open("E:\\2.h2w", 'rb') as file:
#     start_time = time.perf_counter()
#     bytes_read = file.read()
#     # print(bytes_read)
#     end_time = time.perf_counter()
#     execution_time_us = (end_time - start_time) * 1000000
#     # file.flush()
#     file.close()
# print("时间间隔：", execution_time_us)
# with open("E:\\2.h2w", 'rb') as file:
#     start_time = time.perf_counter()
#     bytes_read = file.read()
#     # print(bytes_read)
#     end_time = time.perf_counter()
#     execution_time_us = (end_time - start_time) * 1000000
#     file.flush()
# file.close()
# print("时间间隔：", execution_time_us)

import os

# # 打开文件以供写入，使用O_DIRECT标志
# with open("E:\\1.h2w", "wb", buffering=0) as file:
#     # 生成1GB的数据（这里使用0来填充）
#     one_gb_data = bytes([1] * 1024 * 1024 * 1024)
#
#     # 写入数据
#     file.write(one_gb_data)
#
# # 从磁盘读取数据，同样使用O_DIRECT标志
with open("E:\\1.h2w", "rb", buffering=0) as file:
    start_time = time.perf_counter()
    read_data = file.read()
    end_time = time.perf_counter()
    execution_time_us = (end_time - start_time) * 1000000

#
# # 检查读取的数据的大小
# print("时间间隔：", execution_time_us)
# # print("读取的数据大小：", len(read_data), "bytes")
def build_h2_data(n_sec_pos):
    data = bytearray()
    for _ in range(2048):
        ull = n_sec_pos
        data.extend(struct.pack('Q', ull))
        for _ in range(63):
            ull = ull * 0x01 + 17
            data.extend(struct.pack('Q', ull))
        n_sec_pos += 512
    return data
a = build_h2_data(0)
print(type(a))
print(type(read_data))


def read_ull(data, offset):
    return struct.unpack_from('Q', data, offset)[0]
# for j in range(len(bytes_read) // 8):
                        #     file_data_ull = read_ull(bytes_read, j * 8)
                        #     expected_data_ull = read_ull(data_buffer, expected_offset)
                        #
                        #     if file_data_ull != expected_data_ull:
                        #         print(f"Data mismatch at file {self.written_files[index]}, "
                        #               f"Data mismatch at index {expected_offset}")
                        #         # Do something if data doesn't match, e.g., raise an exception
                        #     expected_offset += 8