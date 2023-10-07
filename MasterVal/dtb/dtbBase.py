#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import argparse
import inspect
import logging
import os
import random
import sys
import time
import dtb
import lidt

class dtbBase():
    """
    Top level base class for all dtb framework python cases
    Main function of this part
        1. command line argument parsing
        2. logging system
        3. Failure handling method

    """
    def __init__(self):

        print("entry dtbBase")
        self.parser = argparse.ArgumentParser()
        self.lidt = lidt

        self.addArguments()
        self.args, _ = self.parser.parse_known_args()
        self.exceptionMessage = ""

        for attr in dir(self.args):
            if not attr.startswith('_'):
                value = getattr(self.args, attr)
                if isinstance(value, bool):
                    for inputArg in sys.argv:
                        if attr in inputArg and 'False' in inputArg:
                            setattr(self.args, attr, False)
                            break
        if not os.path.exists(self.args.logFilePath):
            os.system('mkdir {}' .format(self.args.logFilePath))

        self.logFile = os.path.join(self.args.logFilePath, self.args.logFileName)
        self.logger = logging.getLogger(__name__)
        self.loggerHandling()

    def getHWInfo(self):
        """
        @brief: get the information of hardware
        """
        if not sys.platform.startswith("win"):
            cpuInfoFd = open("/proc/cpuinfo")
            for lineStr in cpuInfoFd:
                if lineStr.startswith("Hardware"):
                    cpuModel = lineStr.split(":")[1]
                    print(f"CPU Info:{cpuModel}")

        return None

    def loggerHandling(self):
        """
        @brief: log info handling
        """
        if not self.logger.handlers:
            self.logger.setLevel(self.args.logLevel)
            formatter = logging.Formatter("%(asctime)s = %(levelname)-8s %(module)s - %(message)s")
            if self.args.logFileEnable:
                fileHandler = logging.FileHandler(self.logFile)
                fileHandler.setFormatter(formatter)
                self.logger.addHandler(fileHandler)

            consoleHandler = logging.StreamHandler(sys.stdout)
            if self.args.product:
                consoleHandler.setLevel(logging.WARNING)
            consoleHandler.setFormatter(formatter)
            self.logger.addHandler(consoleHandler)

    def addArguments(self):
        """
        dtb framework configurable parameters
        """
        self.parser.add_argument('--randomSeed', type=int, default=0, help='Random seed value used in test')
        self.parser.add_argument('--logLevel', type=int, default=logging.DEBUG, help='log output level')
        self.parser.add_argument('--productTest', type=bool, default=False, help='production test enable')

        self.parser.add_argument('--logFileName', type=str,
                                 default=os.path.split(sys.argv[0].split('.py')[0])[1] + "_" + str(
                                     time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + ".log",
                                 help='The output file name')
        self.parser.add_argument('--uartLogFileName', type=str,
                                 default=os.path.split(sys.argv[0].split('.py')[0])[1] + "_" + "Uart" + "_" + str(
                                    time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + ".log",
                                 help='The output file name')
        self.parser.add_argument('--driverLogFileName', type=str,
                                 default=os.path.split(sys.argv[0].split('.py')[0])[1] + "_" + "Driver" + "_" + str(
                                     time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + '.log',
                                 help='The output file name')
        self.parser.add_argument('--logFilePath', type=str, default='/userdata/testLog',
                                 help='The folder path for log files')
        # Uart driver 待确认
        self.parser.add_argument('--uartport', type=str, default="    ", help='Serial port flag')

        self.parser.add_argument('--logFileEnable', type=bool, default=True, help='Flag to enable/disable output file')

        self.parser.add_argument('--uartLogfileEnable', type=bool, default=True, help='Flag to enable/disable output file')

        self.parser.add_argument('--doPdb', type=bool, default=False, help='Debug function if test fails')
        self.parser.add_argument('--runCycles', type=int, default=10, help='targe test cycles')
        self.parser.add_argument('--runTimes', type=int, default=10, help='targe test cycles')

    def Run(self):
        """
        @brief: test flow control, this function must be overwrite in subclass
        """
        return None

    def fail(self, message=""):
        """
        @brief: Fail, terminate the script and print fail information
        @param message:
        @return None:
        """
        self.__addFailDescriptor(message)

    def assertTrue(self, expression, message=""):
        """
        @brief: if not expression, then terminate the script and print fail information
        @param expression: bool the object that needs to judge
        @param message: string, the fail information
        """
        if not expression:
            self.__addFailDescriptor(message)

    def assertFalse(self, expression, message=""):
        """
        @brief: if not expression, then terminate the script and print fail information
        @param expression: bool the object that needs to judge
        @param message: string, the fail information
        """
        if expression:
            self.__addFailDescriptor(message)

    def __addFailDescriptor(self, message=""):
        """
        @brief: print abnormal log info
        """
        (fileName, lineNumber) = self.__getCallersLocation(stacksUp=2)

        self.logger.error("FAIL: file=%s, line=%s, %s", str(fileName), str(lineNumber), message)
        self.exceptionMessage = message
        raise dtb.TestFailError()

    def __getCallersLocation(self, stacksUp=2):
        """
        @brief: get specific error message
        @param stacksUp:
        @return :
               fileName: err code fill
               lineNumber: err code line
        """

        fileName = ""
        lineNumber = -1
        try:
            frame = inspect.stack()[stacksUp + 1]
            fileName = frame[1]
            lineNumber = frame[2]
        except Exception:
            pass

        return fileName, lineNumber




