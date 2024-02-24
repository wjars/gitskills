#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_log 
@File    ：log_management.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/29 15:50 
'''
import logging
from logging.handlers import TimedRotatingFileHandler
import os
import shutil
import time


class LogManagement:
    def __init__(self, log_filename, log_level=logging.DEBUG, retention_days=30, cleanup_threshold=0.2):
        self.log_filename = log_filename
        self.log_level = log_level
        self.retention_days = retention_days
        self.cleanup_threshold = cleanup_threshold
        self.logger = self.setup_logger()

    def setup_logger(self):
        log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        rotating_handler = TimedRotatingFileHandler(self.log_filename, when='midnight', interval=1, backupCount=7)
        rotating_handler.setFormatter(log_formatter)

        logger = logging.getLogger('log_management_logger')
        logger.setLevel(self.log_level)
        logger.addHandler(rotating_handler)

        return logger

    def cleanup_logs(self):
        # Delete logs older than retention_days
        current_time = time.time()
        retention_period = self.retention_days * 24 * 60 * 60
        for file_name in os.listdir(os.path.dirname(self.log_filename)):
            file_path = os.path.join(os.path.dirname(self.log_filename), file_name)
            if os.path.isfile(file_path) and current_time - os.path.getctime(file_path) > retention_period:
                os.remove(file_path)
                self.logger.info(f"Deleted log file: {file_path}")

        # Check disk space and trigger cleanup if below threshold
        disk_usage = shutil.disk_usage(os.path.dirname(self.log_filename))
        free_space_percentage = disk_usage.free / disk_usage.total
        if free_space_percentage < self.cleanup_threshold:
            self.logger.warning(f"Low disk space ({free_space_percentage:.2%}). Initiating log cleanup.")


def configure_logger(log_filename, log_level=logging.DEBUG, retention_days=30, cleanup_threshold=0.2):
    return LogManagement(log_filename, log_level, retention_days, cleanup_threshold).logger
