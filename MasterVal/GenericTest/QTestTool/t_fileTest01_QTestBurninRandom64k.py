#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import sys
import dtb
import random
import math
import time


class QTestBurninRandom64k(dtb.TestStart):
    """
        @Descriptor:
        QTest Tool Test Flow

        @Step::
            Step 1: Get device Disk Attribute
            Step 2: Get device Disk Max sector number
            Step 3: create and init test Map
            Step 4: Entry RW test Main flow

        @CurrentOwner: changwang.cai@longsys.com
        @OriginalAuthor: changwang.cai@longsys.com
        @testType: system test
    """

    def __init__(self):
        super().__init__()
        self.Sectorsize = 512
        self.bufMap = None
        self.BufferType = '64k'
        self.start = 0
        self.end = 0
        self.PrartitonName = None

    def initMap(self, start, end, value=0):
        """
        @brief: This is the creat test Buffer Map
        @return None.
        """
        zonSize = end - start + 1
        sectorNum = math.ceil(zonSize / self.Sectorsize)
        self.bufMap = self.lidt.Buffer(sectorNum, self.Sectorsize)
        self.bufMap.FillAll(value)
        self.start = start
        self.end = end

    def updateMap(self, start, length, value=0):
        """
        @brief: This is the main test function for this script.
        @return None.
        """
        offset = start - self.start

        for byte in range(offset, offset + length):
            self.bufMap.SetByte(byte, value)

    def checkData(self, start, chunkSize):
        """
        @brief: This is the main test function for this script.
        @return None.
        """
        bufActual = self.lidt.Buffer(chunkSize, self.Sectorsize)
        

    def RandomTest(self, maxBufferSize, maxSectornode):
        """
        @brief: This is the main test function for this script.
        @return None.
        """

        FileData = random.randint(0x00, 0xff)
        length = random.randint(0x01, maxBufferSize//512)
        Sectornode, BufferSize = random.randint(0, maxSectornode), random.randint(0x00, length)

        if maxSectornode - Sectornode < length:
            length = maxSectornode - Sectornode

        WriteBuffer = self.lidt.Buffer(length, self.Sectorsize)
        WriteBuffer.FillAll(FileData)

        self.logger.info("Fill data {} File startlba {}" .format(FileData, Sectornode))
        self.lib.SectorRW.SectorWriteSingle(self.PrartitonName, WriteBuffer, length, Sectornode, doAddressOverlay=True)
        self.lib.SectorRW.SectorReadSingle(self.PrartitonName, WriteBuffer, length, Sectornode, doAddressOverlay=True,
                                           doCompare=True)

        self.updateMap(Sectornode, length, value=FileData)

    def test(self):
        """
        @brief: This is the main test function for this script.
        @return None.
        """

        self.logger.info("Step 1: Get device Disk Attribute")
        deviceCheck = self.lib.SystemTest.GetDeviesParam()
        self.PrartitonName = deviceCheck["dev_path"]

        self.logger.info("Test device name {} " .format(self.PrartitonName))

        if self.BufferType == '64k':
            maxBufferSize = 1024 * 64
        elif self.BufferType == '128k':
            maxBufferSize = 1024 * 128
        elif self.BufferType == '256k':
            maxBufferSize = 1024 * 256
        elif self.BufferType == '512k':
            maxBufferSize = 1024 * 512
        elif self.BufferType == '1024k':
            maxBufferSize = 1024 * 1024

        self.logger.info("Step 2: Get device Disk Max sector number")
        maxSectornode = self.lib.SectorRW.getMaxSectorAddress()

        self.logger.info("Step 3: create and init test Map")
        self.initMap(0x00, maxSectornode)

        self.logger.info("Step 4: Entry RW test Main flow")
        StartTime = time.time()
        Cycle = 0
        while True:
            if (self.args.runTimes <= time.time() - StartTime) or (self.args.runCycles >= 100):
                break
            self.RandomTest(maxBufferSize, maxSectornode)
            Cycle += 1


if __name__ == "__main__":
    test = QTestBurninRandom64k()
    sys.exit(test.RUN())
