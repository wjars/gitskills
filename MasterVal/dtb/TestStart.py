#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import os
import sys
import random
import traceback
import time
import pdb
import lidt

from dtb.dtbBase import dtbBase
from dtb.Libloader import Libloader

PASS = 0
FAIL = 1

class TestStart(dtbBase):
    """

    """
    def __init__(self):
        super().__init__()

        self.testPass = False
        self.mainTestPass = False
        self.testStaus = False
        self.SDCardSYSTestEnable = False
        self.USBSYSTestEnable = False
        try:
            self.lib = Libloader(self)
        except Exception as e:
            print(e)
            print("create Dut fail, cannot execute any command, will exit!")

    def addArguments(self):
        """
        dtb framework configurable parameters
        """
        super().addArguments()
        self.parser.add_argument('--product', type=str, default="SDCARD", help='Product name')
        self.parser.add_argument('--customer', type=str, default='Generic',
                                 help='specify the target customer name under test ')

    def RUN(self):
        """
        @brief: all steps will follow the step to run.
        @return: None
        """
        strTime = self.testStarted()

        try:
            self.logger.info("module version: {}".format(self.lidt.version))
            self.logger.info("module commit id: {}".format(self.lidt.commit_id))

            self.test()
            self.mainTestPass = True
            self.testPass = True

        except Exception as e:
            stackTrace = traceback.format_exc()
            self.logger.error(stackTrace)

        finally:
            self.testCompleted(strTime)

        if self.testPass:
            self.logger.info('=========================================TEST PASS====================================')
        else:
            self.logger.info('=========================================TEST FAIL====================================')
        return self.testStaus

    def test(self):
        """
        @brief: Do test work.
        @return: None.
        """
        pass

    def testStarted(self):
        """
        @brief: Print same useful info when script prepare to run.
        @return: None.
        """
        startTime = time.time()
        self.logger.info("the start time for this script: %f", startTime)
        return startTime

    def testCompleted(self, strTime):
        """
        @brief: Print some useful info when script done.
        @param: A float value which represents the time.
        @return: None.
        """
        tolSenconds = round((time.time() - float(strTime)), 3)
        self.logger.info("Script test has been running for {0} second." .format(tolSenconds))
        return tolSenconds

    def cleanupTest(self):
        """
        @breaf: Do clean up test.
        @return: None
        """
        self.logger.info("==========================cleanupTest========================")
        self.logger.info('CMD Line: {}' .format(sys.argv))
