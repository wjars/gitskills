#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd
import os
import time

class SystemTest:
    """
        Uniform system operation lib for Sector methods

        @Copyright: 2023, longsys
        Author: changwangm.cai
        @History:
            2023/08/25 initial version for uniform lib (changwang.cai@longsys.com)
    """
    def __init__(self, testInstance):
        self.testInstance = testInstance
        self.product = self.testInstance.args.product
        self.dev_path = self.PreParamMetercheck()

    def GetDeviesParam(self):
        """
        @brief: Get attribute with disk
        @return: memParam
        """
        dev_path = self.PreParamMetercheck()

        self.testInstance.logger.info("Test object presence ")
        DiskList = os.popen('fdisk ' + dev_path + ' ' + '-l').read()
        DisKParmList = DiskList.split()

        Byteindex, GBindex = DisKParmList.index('bytes'), DisKParmList.index('GB,')
        memCapacity_Byte, memCapacity_GB = DisKParmList[Byteindex - 1], DisKParmList[GBindex - 1]
        self.testInstance.logger.info("Test Storage memory {} byte".format(memCapacity_Byte))
        self.testInstance.logger.info("Test Storage memory {} GB".format(memCapacity_GB))

        deviceName = os.popen('ls ' + self.dev_path + '*').read()
        DevList = deviceName.split()
        Prartiton = DevList[0]


        memParam = {
            "GBCapacity": memCapacity_GB,
            "ByteCapacity": memCapacity_Byte,
            "DeviceDisk": Prartiton,
            "dev_path": dev_path
        }

        return memParam

    def configureBigOnePartition(self):
        """
        @brief:Get attribute with disk
        @return:None
        """
        test_dir_path = '/testFile'
        # 创建分区和挂载目录

        if not os.path.exists(test_dir_path):
            os.makedirs(test_dir_path)

        # 创建分区并使用全部空间
        os.system('echo -e "n\np\n1\n\n\nw\n" | fdisk ' + self.dev_path)
        os.system('partprobe ' + self.dev_path)
        time.sleep(1)

    def fileSystemConfigure(self, Prartiton):
        """
        @brief: Configure disk File system
        @param: Prartiton(device name)
        @return: None
        """

        test_dir_path = '/testFile'
        Prartiton = '/dev/' + Prartiton + ' '

        # 格式化为ext4格式
        os.system('mkfs.ext4 ' + '-F ' + Prartiton)

        # 挂载硬盘
        os.system('mount ' + Prartiton + test_dir_path)

        self.testInstance.logger.info('The Hard disk has mounted to {} ' .format(test_dir_path))

    def PreParamMetercheck(self):
        """
        @brief:
        @return:
        """
        dev_path = None
        if self.product == "SDCARD":
            dev_path = '/dev/mmcblk1'
        elif self.product == "USB":
            dev_path = '/dev/sda'
        else:
            self.testInstance.fail("The pre-condition set exception ")
        return dev_path



