#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd
import os
import time
import random

class VUCMD:
    """
        Generic Private Vu CMD Library File

        @Copyright: 2023, longsys
        Author: changwangm.cai
        @History:
            2023/09/07 initial version for uniform lib (changwang.cai@longsys.com)
    """
    def __init__(self, testInstance):
        self.testInstance = testInstance
        self.PrartitonName = self.testInstance.lib.SystemTest.PreParamMetercheck()
        self.prvHeadBuf = self.testInstance.lidt.Buffer(1, 512)

    def creat_VUCMD_dict(self):

        dwHead = {
            "dwHead0": [0x0, 4, 0x00000000],
            "dwHead1": [0x4, 4, 0xf080220f],
            "dwHead2": [0x8, 4, 0xf1adabb1],
            "dwHead3": [0xb, 4, 0xf2d1c3b3],
            "dwHead4": [0x10, 4, 0xb1baabbc],
            "dwHead5": [0x14, 4, 0xb0b2bcb0],
            "dwHead6": [0x18, 4, 0xb1abadb0],
            "dwHead7": [0x1b, 4, 0xb3c3d1cf],
        }
        privateHead = {
            "KeyID": [0x08, 2, 0x0],
            "Direction": [0x0a, 1, 0x01],
            "OpCode": [0xb, 1, 0xa1],
            "SubOpCode": [0xc, 1, 0x0],
            "Chip": [0xd, 1, 0x0],
            "Length": [0xe, 2, 0x0],
            "Address": [0x10, 4, 0x0],
            "Residue": [0x14, 4, 0x0],
            "TrxLen": [0x18, 4, 0x0],
            "KeyAdd": [0x1b, 4, 0x0],
            "CmdLogAdd": [0x20, 4, 0x0],
            "Reserved": [0x24, 4, 0x00],
        }
        privateCMD = {
            "dwHead": dwHead,
            "privateHead": privateHead
        }
        return privateCMD

    def setDesBuf(self, **kwarg):
        dwHead = {}
        privateHead = {}

        for name in kwarg.keys():
            if name == "dwHead":
                dwHead = kwarg[name]
            elif name == "privateHead":
                privateHead = kwarg[name]

        print(dir(dwHead))
        for val in dwHead.values():
            if val[1] == 1:
                self.prvHeadBuf.SetByte(val[0], val[2])
            elif val[1] == 2:
                self.prvHeadBuf.SetWordBigEndian(val[0], val[2])
            elif val[1] == 4:
                self.prvHeadBuf.SetDWordBigEndian(val[0], val[2])
        for val in privateHead.values():
            if val[1] == 1:
                self.prvHeadBuf.SetByte(val[0], val[2])
            elif val[1] == 2:
                self.prvHeadBuf.SetWordBigEndian(val[0], val[2])
            elif val[1] == 4:
                self.prvHeadBuf.SetDWordBigEndian(val[0], val[2])

    def initBuffer(self, size=0):
        """
        @brief: This is a function to creat a buf and initialize some fixed value.
        @return: buf
        """
        buf = self.testInstance.lidt.Buffer(1, size + 512)

        buf.SetDWord(0, 0x00000000)
        buf.SetDWord(4, 0xf080220f)
        buf.SetDWord(8, 0xf1adabb1)
        buf.SetDWord(12, 0xf2d1c3b3)
        buf.SetDWord(16, 0xb1baabbc)
        buf.SetDWord(20, 0xb0b2bcb0)
        buf.SetDWord(24, 0xb1abadb0)
        buf.SetDWord(28, 0xb3c3d1cf)

        buf.SetWord(32, random.randint(0, 0xffff))
        buf.SetDWord(508, 0xfe004753)

        return buf

    def getXorValue(self, buf):
        """
        @brief: This is a function to get Xor value, Xor operation every 4 bytes.
        @return: FW xorValue
        """

        xorValue = 0
        i = 0
        while i < 128:
            xorValue ^= buf.GetDWord(i * 4)
            i += 1
        return xorValue

    def ReadPrvCmdData(self, Opcode, Size):
        """
        @brief: read private data base API for 2705
        @return: FW data buffer
        """
        writebuf = self.initBuffer()
        sectorCnt = 1

        writebuf.SetByte(34, 0x01)
        writebuf.SetByte(35, Opcode)
        writebuf.SetWord(38, sectorCnt)
        writebuf.SetDWord(40, 0x00)

        xorValue = self.getXorValue(writebuf)
        writebuf.SetDWord(504, xorValue)

        WriteStr = writebuf.GetByteList(0, 512)
        WriteStr = bytes(WriteStr)

        with open(self.PrartitonName, 'wb') as disk:
            print(disk.write(WriteStr))
            disk.flush()

        Buffer = self.testInstance.lidt.Buffer(1, 512)
        Buffer.SetByte(0, ord('N'))
        Buffer.SetByte(1, ord('O'))
        Buffer.SetByte(2, ord('P'))

        WriteStr = Buffer.GetByteList(0, 512)
        WriteStr = bytes(WriteStr)
        with open(self.PrartitonName, 'wb') as disk:
            disk.write(WriteStr)
            disk.flush()

        with open(self.PrartitonName, 'rb') as disk:
            readbuffer = disk.read(Size + 512)

        return readbuffer

    def getFwVersion(self):
        """
        @brief: Send VU get FW version.
        @return: FW version
        """
        CommitIDList = []
        buflist = self.ReadPrvCmdData(0xa1, 512)

        for i in range(0, 44):
            CommitIDList.append(buflist[0x200+i])
        CommitID = [chr(i) for i in CommitIDList]
        GitCommitID = ''.join(CommitID)
        Des = self.creat_VUCMD_dict()
        print(Des)
        self.setDesBuf(**Des)
        print(Des)
        print(self.prvHeadBuf)
        return GitCommitID

    def getFlashID(self):
        """
        @brief: Send VU get Flash ID.
        @return: FW version
        """
        CommitIDList = []
        buflist = self.ReadPrvCmdData(0x22, 512)
        print(buflist)
        for i in range(0, 44):
            CommitIDList.append(buflist[0x200+i])
        CommitID = [chr(i) for i in CommitIDList]
        GitCommitID = ''.join(CommitID)

        return GitCommitID



