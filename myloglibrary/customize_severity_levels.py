#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：pythonProject_log
@File    ：customize_severity_levels.py
@IDE     ：PyCharm
@Author  ：厄运马马卡
@Date    ：2024/1/30 14:07
"""

import configparser
import logging
import os
import time
import psutil
import sys
from logging.handlers import RotatingFileHandler
import shutil
import gzip

# define custom severity level
DEBUG = 10
INFO = 20
NOTICE = 25
WARNING = 30
ERROR = 40


# Creating a Custom Logger Class
class CustomLogger(logging.Logger):
    LEVELS = {
        'DEBUG': DEBUG,
        'INFO': INFO,
        'NOTICE': NOTICE,
        'WARNING': WARNING,
        'ERROR': ERROR
    }

    def __init__(self, name):
        try:
            super(CustomLogger, self).__init__(name)
            self.handler_way = int(_get_param('LoggingConfig', 'OutputConsole'))
            self.disk_space_threshold = int(_get_param('LoggingConfig', 'DiskSpaceThreshold'))
            self.custom_filter_level = int(_get_param('LoggingConfig', 'CustomFilterLevel'))
            self.log_file_path = _get_param('Paths', 'DstLog')

            if _check_disk_space(self.log_file_path, self.disk_space_threshold):
                _delete_old_logs(self.log_file_path, 0)

            # self.compress_logs(self.log_file_path)
            self._setup_logging()
        except Exception as e:
            print(f"Error during logger initialization: {str(e)}")

    def _setup_logging(self):
        # Add custom severity levels to logging module
        for level_name, level_value in self.LEVELS.items():
            logging.addLevelName(level_value, level_name)

        if self.handler_way:
            console_handler = logging.StreamHandler()
        else:
            log_file_name = (os.path.split(sys.argv[0].split('.py')[0])[-1]) + '_' \
                            + time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time())) + '.log'
            console_handler = RotatingFileHandler(filename=os.path.join(self.log_file_path, log_file_name)
                                                  , maxBytes=242, backupCount=1, delay=True)
        console_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        custom_filter = CustomFilter(self.custom_filter_level)
        console_handler.addFilter(custom_filter)
        self.addHandler(console_handler)

    def notice(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'NOTICE'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        logger.notice("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        if self.isEnabledFor(NOTICE):
            self._log(NOTICE, msg, args, **kwargs)

    # def compress_logs(self, logs_directory):
    #     for root, dirs, files in os.walk(logs_directory):
    #         for file in files:
    #             if not file.endswith(".gz"):
    #                 file_path = os.path.join(root, file)
    #                 with open(file_path, "rb") as f_in, gzip.open(file_path + ".gz", "wb") as f_out:
    #                     shutil.copyfileobj(f_in, f_out)
    #                 os.remove(file_path)
    #                 print(f"Compressed log file: {file_path}")


# Creating a Custom Filter Class
class CustomFilter(logging.Filter):
    def __init__(self, level):
        super().__init__()
        self.level = level

    def filter(self, record):
        return record.levelno >= self.level


def _get_param(section, option):
    # Read parameters from a configuration file
    config = configparser.ConfigParser()
    config.read('D:\download\pycharm\pythonProject_log\myloglibrary\logging_config.ini')
    return config.get(section, option)


def _check_disk_space(path, threshold):
    try:
        disk_usage = psutil.disk_usage(path)
        free_percentage = disk_usage.free / disk_usage.total * 100
        return free_percentage < threshold
    except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
        print(f"Error accessing disk space information: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error during disk space check: {str(e)}")
        return False


def _delete_old_logs(logs_directory, num_to_keep):
    try:
        log_files = sorted(os.listdir(logs_directory), key=lambda x: os.path.getmtime(os.path.join(logs_directory, x)))

        # Ensure we keep at least num_to_keep log files

        if 0 == num_to_keep:
            files_to_delete = log_files
        else:
            files_to_delete = log_files[:-num_to_keep] if len(log_files) > num_to_keep else []

        for file_to_delete in files_to_delete:
            file_path = os.path.join(logs_directory, file_to_delete)
            os.remove(file_path)
            print(f"Deleted old log file: {file_path}")
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error deleting old logs: {str(e)}")
    except Exception as e:
        print(f"Unexpected error during old logs deletion: {str(e)}")


def delete_logs(log_path, days_to_keep):
    try:
        if days_to_keep == 0:
            for file_name in os.listdir(log_path):
                file_path = os.path.join(log_path, file_name)
                os.remove(file_path)
                print(f"Deleted log file: {file_path}")
        else:
            current_time = time.time()

            # Converting days to seconds
            seconds_to_keep = days_to_keep * 24 * 3600

            for file_name in os.listdir(log_path):
                file_path = os.path.join(log_path, file_name)

                # Get the last modification time of a document
                last_modified_time = os.path.getmtime(file_path)

                # Calculate the number of seconds the file is away from the current time
                seconds_difference = current_time - last_modified_time

                # If the specified number of days is exceeded, the deletion operation is performed
                if seconds_difference > seconds_to_keep:
                    os.remove(file_path)
                    print(f"Deleted log file: {file_path}")

        return 0
    except Exception as e:
        print(f"Error deleting old log files: {str(e)}")
        return 1
