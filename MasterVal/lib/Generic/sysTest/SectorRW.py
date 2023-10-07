#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd
import os
import time

class SectorRW:
    """
        Uniform write/read lib for Sector methods

        @Copyright: 2023, longsys
        Author: changwangm.cai
        @History:
            2023/08/25 initial version for uniform lib (changwang.cai@longsys.com)
    """
    def __init__(self, testInstance):
        self.testInstance = testInstance

    def getMaxSectorAddress(self):
        """
        @brief:get end Sector number
        @return:Scriptor
        """

        return int(self.testInstance.lib.SystemTest.GetDeviesParam()["ByteCapacity"]) // 512

    def SectorWriteSingle(self, devFile, writeBuffer, length, startSector, doAddressOverlay=False):
        """
        @brief: send single sector write file
        @param devFile: mmcblkx/sdax
        @param writeBuffer: data to be writeb
        @param length: int
        @param startSector: int
        @param doAddressOverlay: Bool, whether FillAddressOverlay method for writeBuffer
        @return: None
        """
        MaxSectorNode = self.getMaxSectorAddress()

        if startSector > MaxSectorNode:
            self.testInstance.fail('Start Sector out of Device Memory Capacity')

        newWriteBuffer = self.testInstance.lidt.Buffer(length, writeBuffer.SectorSize)
        newWriteBuffer.CopyBuffer(writeBuffer)

        if doAddressOverlay:
            newWriteBuffer.FillAddressOverlay(startSector, 0, newWriteBuffer.SectorNum)

        WriteStr = newWriteBuffer.GetByteList(0, length * 512)
        WriteStr = bytes(WriteStr)

        with open(devFile, 'wb') as disk:
            disk.seek(startSector * 512)
            disk.write(WriteStr)

    def SectorReadSingle(self, devFile, writeBuffer, length, startSector, doAddressOverlay=False, doCompare=False):
        """
        @brief: send single sector Read file
        @param devFile: mmcblkx/sdax
        @param writeBuffer: data to be writeb
        @param length: int
        @param startSector: int
        @param doAddressOverlay: Bool, whether FillAddressOverlay method for writeBuffer
        @return: None
        """
        MaxSectorNode = self.getMaxSectorAddress()

        if startSector > MaxSectorNode:
            self.testInstance.fail('Start Sector out of Device Memory Capacity')
        with open(devFile, 'rb') as disk:
            disk.seek(startSector * 512)
            strRead = disk.read(length * 512)
        if doCompare:
            readBufferExp = self.testInstance.lidt.Buffer(length, writeBuffer.SectorSize)
            readBufferExp.CopyBuffer(writeBuffer)
            if doAddressOverlay:
                readBufferExp.FillAddressOverlay(startSector, 0, readBufferExp.SectorNum)

            WriteStr = readBufferExp.GetByteList(0, length * 512)
            WriteStr = bytes(WriteStr)
            if strRead != WriteStr:
                self.testInstance.logger.info(
                    "Data mismatch, sector index : {}, TL : {}" .format(startSector, length))
                self.testInstance.logger.info(strRead)
                self.testInstance.logger.info(WriteStr)
                self.testInstance.fail("DMC")

