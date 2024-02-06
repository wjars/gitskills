#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pythonProject_document 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2024/1/11 14:31 
'''

import logging
import os
import time

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 项目的根路径
log_path = os.path.join(project_path, "logs")  # log的存放路径
if not os.path.exists(log_path): os.mkdir(log_path)  # 不存在log文件夹，则自动创建


class Logger(object):
    default_formats = {
        # 终端输出格式
        'console_fmt': '%(log_color)s%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s',
        # 日志输出格式
        'file_fmt': '%(asctime)s-%(filename)s-[line:%(lineno)d]-%(levelname)s-[日志信息]: %(message)s'
    }

    def __init__(self, name=None, log_level=logging.DEBUG):
        self.name = name
        # ①创建一个记录器
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel("INFO")  # 设置日志级别为 'level'，即只有日志级别大于等于'level'的日志才会输出
        self.log_formatter = logging.Formatter(self.default_formats["file_fmt"])  # 创建formatter
        self.console_formatter = logging.Formatter(self.default_formats["file_fmt"])  # 创建formatter
        # ②创建屏幕-输出到控制台，设置输出等级
        self.streamHandler = logging.StreamHandler()
        self.streamHandler.setLevel("DEBUG")
        # ③创建log文件，设置输出等级
        time_now = time.strftime('%Y_%m%d_%H', time.localtime()) + '.log'  # log文件命名：2022_0402_21.log
        self.fileHandler = logging.FileHandler(os.path.join(log_path, time_now), 'a', encoding='utf-8')
        self.fileHandler.setLevel("DEBUG")
        # ④用formatter渲染这两个Handler
        self.streamHandler.setFormatter(self.console_formatter)
        self.fileHandler.setFormatter(self.log_formatter)
        # ⑤将这两个Handler加入logger内
        if not self.logger.handlers:  # 在新增handler时判断是否为空,解决log重复打印的问题
            self.logger.addHandler(self.streamHandler)
            self.logger.addHandler(self.fileHandler)

    def getLogger(self):
        return self.logger


logger = Logger().getLogger()

if __name__ == '__main__':
    logger = Logger().getLogger()
    logger.warning("warning")
    logger.error("error")
    logger.info("info")
    logger.debug("debug")
    logger.critical("critical")





import logging.handlers
from config.config import LOG_PATH
import time
import os

class GetLogger:
    logger = None

    # 获取 logger
    @classmethod
    def get_logger(cls):
        # 如果 logger为空
        if cls.logger is None:
            # 获取日志器
            cls.logger = logging.getLogger()
            # 设置日志器默认级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器 控制台
            sh = logging.StreamHandler()
            # 获取处理 文件（时间）
            current_time = time.strftime("%Y-%d-%m-%H_%M_%S", time.localtime(time.time()))
            file_name = current_time + ".log"
            file_path = os.path.join(LOG_PATH, file_name)
            th = logging.handlers.TimedRotatingFileHandler(filename=file_path,
                                                           when="M",
                                                           interval=1,
                                                           backupCount=2,
                                                           encoding="utf-8")
            # 获取格式器
            fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
            fmt = logging.Formatter(fm)
            # 将格式器 设置 处理器中
            sh.setFormatter(fmt)
            th.setFormatter(fmt)
            # 将处理器 添加到 日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
        # 返回 日志器
        return cls.logger


if __name__ == '__main__':
    # 返回日志实例用来调用
    log = GetLogger().get_logger()
    log.debug("Debug INFO")
    log.info("info INFO")
    log.error("error INFO")
    log.warning("warning INFO")



log_manager = LogManagement(log_filename='example.log',
                            log_level=logging.DEBUG,
                            retention_days=30,
                            cleanup_threshold=0.2)
log_manager.logger.info("This is an example log message.")
log_manager.cleanup_logs()


