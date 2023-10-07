#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Private_Cmd_Migration 
@File    ：2724Define.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2023/9/25 16:18 
'''


MAX_ADJ_CAP = 3
CodeBlkCnt = 4
DiskParamBlkCnt = 2
MAX_CHIP_NUM = 4


class PRIVATE_DATA_TAG:
    def __init__(self):
        self.dwIsPageSpare0 = 0
        self.dwIsPageSpare1 = 0


class FLASH_PARAM:
    def __init__(self):
        self.dwTag = 0
        self.dwStructVer = 0
        self.bResserved0 = 0*[8]
        self.bRFreq = 0
        self.bWFreq = 0
        self.bSampleDot = 0
        self.bDQSDelay = 0
        self.bDelayBeforeWaitRB = 0
        self.bDelay_tWHR = 0
        self.bDelay_tADL = 0
        self.bReserved1 = 0
        self.bReserved2 = 0*[32]
        self.bCETotal = 0
        self.bLunPerCE = 0
        self.bInterleaveWay = 0
        self.bPlaneTotal = 0
        self.wByteOfPage = 0
        self.bSectOfPage = 0
        self.bEccSectPerPage = 0
        self.wPagePerBlk = 0
        self.wStrongPagePerBlk = 0
        self.wBlkPageSize = 0
        self.wBlockPerLUN = 0
        self.wLUNBlockSize = 0
        self.wPlaneRowSize = 0
        self.wBlockPerCE = 0
        self.wReserved3 = 0
        self.bBlockTotal = 0
        self.bFlashFeature = 0*[16]
        self.dwEccMode = 0
        self.bMaxEccErrorBit = 0
        self.bEccSectTotal = 0
        self.bBadInfoPosition = 0
        self.bPlaneCMDType = 0
        self.bReserved4 = 0*[36]
        self.bReservedK = 0*[128]


class IIR_UTBL:
    def __init__(self):
        self.dwTag = 0
        self.dwStructVersion = 0
        self.dwHWVersion = 0
        self.PLL_Config = 0
        self.bReserved0 = [0]*3
        self.CPU_Clock_Div = 0
        self.MCLK_Clock_Div = 0
        self.SCLK_Clock_Div = 0
        self.FCLK_Clock_Div = 0
        self.bFlashFeature = [0]*16
        self.bCETotal = 0
        self.bFcOpReadCycle = 0
        self.bFcOpWriteCycle = 0
        self.bFcRdSim = 0
        self.bBadBlkInfoType = 0
        self.bMaxReMappingBitSize = 0
        self.bReserved1 = [0]*2
        self.bCodeOfChip = [0]*CodeBlkCnt
        self.wCodePhyBlk = [0]*CodeBlkCnt
        self.wDiskParamBlk = [0]*DiskParamBlkCnt
        self.bDiskParamBlkChip = [0]*DiskParamBlkCnt
        self.bCodeEccMode = 0
        self.bMaxBITsubsection = 0
        self.wPMZoneSize = 0
        self.wRealRedundancyCoeff = 0
        self.bPageMapBlkCoeff = 0
        self.bRedundancyCoeff = [0]*3
        self.wReserveUserBlkNum = 0
        self.wReserveSectPerBlk = 0
        self.bIDA_EN = 0
        self.bInterLeaveRWDisable = 0
        self.wOrigBITBlkTotalPerPage = 0
        self.wCodeBlkValidPageTotal = 0
        self.bBuildBIT = 0
        self.bReserved2 = 0
        self.dwEmptyA5 = 0


class tySMART:
    def __init__(self):
        self.dwSMARTTag = 0
        self.dwSMARTVersions = 0
        self.bFWVersions = 0*[64]
        self.bFlashID = 0*[16]
        self.dwOriginalBabBlock = 0
        self.dwIncreaseBadBlock = 0
        self.dwSLCFreeBlockNumber = 0
        self.dwFreeBlockNumber = 0
        self.dwPowerUpNumber = 0
        self.dwLogicDataDisperse = 0
        self.dwDegreOfWearForCache = 0
        self.dwDegreOfWear = 0
        self.dwWearLevelingVarianceForCache = 0
        self.dwWearLevelingVariance = 0
        self.dwMaxWearNumberForCache = 0
        self.dwMaxWearNumber = 0
        self.dwReplaceNumber = 0
        self.dwCacheBlockDiviedPoint = 0
        self.lwWriteAllSectNum = 0
        self.dwIllegalPowerLossCount = 0
        self.dwUncorrectableCount = 0
        self.dwBackupFWUsedCount = 0
        self.dwBackupBootUsedCount = 0
        self.dwCRCErrCnt = 0
        self.wBITBlk = 0*[6]
        self.bBITBlkChip = 0*[6]
        self.wCodeBlk = 0*[2]
        self.bCodeBlkChip = 0*[2]
        self.dwBootIndexRow = 0*[2]
        self.wBootIndexCol = 0*[2]
        self.bBootIndexBlkChip = 0*[2]
        self.wDiskParamBlk = 0*[2]
        self.bDiskParamBlkChip = 0*[2]
        self.bUID = 0*[16]
        self.dwCollectNum = 0
        self.bRebuildReason = 0
        self.bSMTProtected = 0
        self.dwFreeTimeCollectFailCnt = 0
        self.dwVDTNum = 0
        self.bCollectCopyFail = 0
        self.bReserved0 = 0
        self.wLogWrCopyPageErrCnt = 0
        self.wEraseFailIgnoreBlkTotal = 0
        self.wDiscardCnt = 0
        self.wTrimCnt = 0
        self.wPackCmdCnt = 0
        self.wRPMBWRCnt = 0
        self.wRPMBImpCnt = 0
        self.wSecureWPCnt = 0
        self.wCmdQueCnt = 0
        self.wWPCnt = 0
        self.wBootWPCnt = 0
        self.wLockUnLockCnt = 0
        self.wRelWRCnt = 0
        self.wPowerNotificationCnt = 0
        self.wReserved3 = 0
        self.dwLDO1Value = 0
        self.bReserved = [0]*16
        self.MPInfo = MPInfo()
        self.bExtCsd = [0]*512


class MPInfo:
    def __init__(self):
        self.bMPToolVersions = 0
        self.wYear = 0
        self.bMonth = 0
        self.bDay = 0
        self.bHour = 0
        self.bMinute = 0
        self.bSecond = 0
        self.bScanType = 0
        self.bScanData = 0
        self.bScanConfig = 0
        self.bScanECCLevel = 0
        self.bFixedID = [0]*4
        self.bPrefixID = [0]*4
        self.bRandomID = [0]*8
        self.wStandbyCurrent = 0
        self.bInitialMaxErrorBit = 0
        self.bInitialAverageErrorBit = 0
        self.bInitialMinErrorBit = 0
        self.bReserved1 = [0]*80
        self.bOCR = [0]*4
        self.bCID = [0]*16
        self.bCSD = [0]*4


class tyUserSMART:
    def __init__(self):
        self.dwSMARTTag = 0
        self.dwSMARTVersions = 0
        self.wSMARTByteCount = 0
        self.bSMARTCheckSum = 0
        self.bFWVersions = [0]*64
        self.wYear = 0
        self.bMonth = 0
        self.bDay = 0
        self.bHour = 0
        self.bMinute = 0
        self.bSecond = 0
        self.bFlashID = [0]*16
        self.bFixedID = [0]*4
        self.bPrefixID = [0]*4
        self.bRandomID = [0]*8
        self.bInitialMaxErrorBit = 0
        self.dwOriginalBadBlock = 0
        self.dwIncreaseBadBlock = 0
        self.dwFreeBlockNumber = 0
        self.dwPowerUpNumber = 0
        self.lwWriteAllSectNum = 0
        self.dwIllegalPowerLossCount = 0
        self.BUID = [0]*16
        self.dwIDAStatus = 0
        self.bSMTProtected = 0


SMARTTag = (0x96325874)
SMARTVersions = (2)
class tySMART2705:
    def __init__(self):
        self.dwSMARTTag = 0
        self.dwSMARTVersions = 0
        self.bFWVersions = [0]*64
        self.bFlashID = [0]*16
        self.dwOriginalBabBlock = 0
        self.dwIncreaseBadBlock = 0
        self.dwSLCFreeBlockNumber = 0
        self.dwFreeBlockNumber = 0
        self.dwPowerUpNumber = 0
        self.dwLogicDataDisperse = 0
        self.dwDegreOfWearForCache = 0
        self.dwDegreOfWear = 0
        self.dwWearLevelingVarianceForCache = 0
        self.dwWearLevelingVariance = 0
        self.dwMaxWearNumberForCache = 0
        self.dwMaxWearNumber = 0
        self.dwReplaceNumber = 0
        self.dwCacheBlockDiviedPoint = 0
        self.lwWriteAllSectNum = 0
        self.dwIllegalPowerLossCount = 0
        self.dwUncorrectableCount = 0
        self.dwBackupFWUsedCount = 0
        self.dwBackupBootUsedCount = 0
        self.dwCRCErrCnt = 0
        self.wBITBlk = [0]*6
        self.bBITBlkChip = [0]*6
        self.wCodeBlk = [0]*2
        self.bCodeBlkChip = [0]*2
        self.dwBootIndexRow = [0]*2
        self.wBootIndexCol = [0]*2
        self.bBootIndexBlkChip = [0]*2
        self.wDiskParamBlk = [0]*2
        self.bDiskParamBlkChip = [0]*2
        self.bUID = [0]*16
        self.dwCollectNum = 0
        self.bRebuildReason = 0
        self.bSMTProtected = 0
        self.dwFreeTimeCollectFailCnt = 0
        self.dwVDTNum = 0
        self.bCollectCopyFail = 0
        self.bReserved = 0
        self.wLogWrCopyPageErrCnt = 0
        self.dwAllGarbGCCnt = 0
        self.dwReadRetryCnt = 0
        self.dwLevel3Cnt = 0
        self.dwBalanceCnt = 0
        self.dwBalanceHandleCnt = 0
        self.bReserved2 = [0]*28
        self.MPInfo = MPInfo()
        self.bExtCsd = [0]*512


# class MPInfo1:
#     def __init__(self, bMPToolVersions, wYear, bMonth, bDay, bHour, bMinute, bSecond, bScanType, bScanData, bScanConfig,
#                  bScanECCLevel, bFixedID, bPrefixID, bRandomID, wStandbyCurrent, bInitialMaxErrorBit, bInitialAverageErrorBit,
#                  bInitialMinErrorBit, bReserved1, bOCR, bCID, bCSD):
#         self.bMPToolVersions = bMPToolVersions
#         self.wYear = wYear
#         self.bMonth = bMonth
#         self.bDay = bDay
#         self.bHour = bHour
#         self.bMinute = bMinute
#         self.bSecond = bSecond
#         self.bScanType = bScanType
#         self.bScanData = bScanData
#         self.bScanConfig = bScanConfig
#         self.bScanECCLevel = bScanECCLevel
#         self.bFixedID = bFixedID
#         self.bPrefixID = bPrefixID
#         self.bRandomID = bRandomID
#         self.wStandbyCurrent = wStandbyCurrent
#         self.bInitialMaxErrorBit = bInitialMaxErrorBit
#         self.bInitialAverageErrorBit = bInitialAverageErrorBit
#         self.bInitialMinErrorBit = bInitialMinErrorBit
#         self.bReserved1 = bReserved1
#         self.bOCR = bOCR
#         self.bCID = bCID
#         self.bCSD = bCSD


class tyISP_TAG:
    def __init__(self):
        self.bScanBin = 0
        self.bPageID = 0
        self.wPageIndex = 0
        self.dwBankAddr = 0
        self.dwReserved0 = 0
        self.dwReserved1 = 0


class tyScanISPDef:
    def __init__(self):
        self.bIndex = 0
        self.bUsage = 0
        self.bReserved0 = 0
        self.bReserved1 = 0
        self.dwHeadLen = 0
        self.dwISPsize = 0
        self.bReserved2 = 0
        self.bReserved3 = 0
        self.dwBankAddr = 0
        self.bReserved4 = 0
        self.bReserved5 = 0


class _CMD_HEADER:
    def __init__(self):
        self.bCmd = 0
        self.bChipNum = 0


class _CMD_INIT:
    def __init__(self):
        self.Hdr = _CMD_HEADER()


class _CMD_READ_ID:
    def __init__(self):
        self.Hdr = _CMD_HEADER()


class _CMD_ERASE:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.bSLCMode = 0
        self.bEraseMode = 0
        self.dwBlockAddr = 0
        self.wBlockTotal = 0
        self.wReserved = 0
        self.wCodeCheckFlag = 0
        self.bCodeBlkIndex = 0


class tyLGErase:
    def __init__(self):
        self.bCmd = 0
        self.reserve = [0]*3
        self.dwStartAddr = 0
        self.dwEndAddr = 0


class tyeMMCWP:
    def __init__(self):
        self.bCmd = 0
        self.bReserve = [0]*3
        self.dwStartAddr = 0


class _CMD_GET_LBA_PHY:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.dwTagLBA = 0


class _CMD_READ:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wSectCnt = 0
        self.dwRowAddr = 0
        self.dwSeed = 0
        self.inner_tMode = tMode()
        self.wColAddr = 0
    # def __str__(self):
    #     return f"wSectCnt: {self.wSectCnt}, dwRowAddr: {self.dwRowAddr}, dwSeed: {self.dwSeed}, tMode: {self.tMode}"


class tMode:
    def __init__(self):
        self.PlaneCmd = 0   # 2-bit field
        self.CacheCmd = 0   # 1-bit field
        self.SLC = 0        # 2-bit field
        self.SeedType = 0   # 2-bit field
        self.Retry = 0      # 1-bit field
        self.EccEn = 0      # 1-bit field
        self.SpareType = 0  # 2-bit field
        self.DataType = 0   # 2-bit field
        self.IntlvOP = 0    # 1-bit field
        self.EccType = 0    # 2-bit field

    def Set_PlaneCmd(self, value):
        if value >= 0 and value <= 3:
            self.PlaneCmd = value
        else:
            raise ValueError("PlaneCmd must be a 2-bit value (0-3)")

    def Set_CacheCmd(self, value):
        if value == 0 or value == 1:
            self.CacheCmd = value
        else:
            raise ValueError("CacheCmd must be a 1-bit value (0 or 1)")

    def Set_SLC(self, value):
        if value >= 0 and value <= 3:
            self.SLC = value
        else:
            raise ValueError("SLC must be a 2-bit value (0-3)")

    def Set_SeedType(self, value):
        if value >= 0 and value <= 3:
            self.SeedType = value
        else:
            raise ValueError("SeedType must be a 2-bit value (0-3)")

    def Set_Retry(self, value):
        if value == 0 or value == 1:
            self.Retry = value
        else:
            raise ValueError("Retry must be a 1-bit value (0 or 1)")

    def Set_EccEn(self, value):
        if value == 0 or value == 1:
            self.EccEn = value
        else:
            raise ValueError("EccEn must be a 1-bit value (0 or 1)")

    def Set_SpareType(self, value):
        if value >= 0 and value <= 3:
            self.SpareType = value
        else:
            raise ValueError("SpareType must be a 2-bit value (0-3)")

    def Set_DataType(self, value):
        if value >= 0 and value <= 3:
            self.DataType = value
        else:
            raise ValueError("DataType must be a 2-bit value (0-3)")

    def Set_IntlvOP(self, value):
        if value == 0 or value == 1:
            self.IntlvOP = value
        else:
            raise ValueError("IntlvOP must be a 1-bit value (0 or 1)")

    def Set_EccType(self, value):
        if value >= 0 and value <= 3:
            self.EccType = value
        else:
            raise ValueError("EccType must be a 2-bit value (0-3)")

    def __str__(self):
        return f"PlaneCmd: {self.PlaneCmd}, CacheCmd: {self.CacheCmd}, SLC: {self.SLC}" \
               f"SeedType: {self.SeedType}, Retry: {self.Retry}, EccEn: {self.EccEn}" \
               f"SpareType: {self.SpareType}, DataType: {self.DataType}, IntlvOP: {self.IntlvOP}" \
               f"EccType: {self.EccType}"


class _CMD_WRITE:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wSectCnt = 0
        self.dwRowAddr = 0
        self.dwSeed = 0
        self.inner_tMode = tMode()
        self.wColAddr = 0


class _CMD_SCAN:
    def __init__(self):
        self.bCmd = 0
        self.bChipNum = 0
        self.wStartBlkNum = 0
        self.wScanBlockCnt = 0
        self.bScanCase = 0
        self.bDataErrBits = 0
        self.bSpareErrBits = 0
        self.Reserved = 0
        self.inner_tParam = tParam()


class tParam:
    def __init__(self):
        self.SLC = 0                # 1-bit field
        self.EccEn = 0              # 1-bit field
        self.Retry = 0              # 1-bit field
        self.MPlane = 0             # 1-bit field
        self.CacheProg = 0          # 1-bit field
        self.Copyback = 0           # 1-bit field
        self.ProgWay = 0            # 1-bit field
        self.ResultDensity = 0      # 2-bit field
        self.SyncWrChipTotal = 0    # 3-bit field
        self.Reserved = 0           # 20-bit field

    def Set_SLC(self, value):
        if value == 0 or value == 1:
            self.SLC = value
        else:
            raise ValueError("SLC must be a 1-bit value (0 or 1)")

    def Set_EccEn(self, value):
        if value == 0 or value == 1:
            self.EccEn = value
        else:
            raise ValueError("EccEn must be a 1-bit value (0 or 1)")

    def Set_Retry(self, value):
        if value == 0 or value == 1:
            self.Retry = value
        else:
            raise ValueError("Retry must be a 1-bit value (0 or 1)")

    def Set_MPlane(self, value):
        if value == 0 or value == 1:
            self.MPlane = value
        else:
            raise ValueError("MPlane must be a 1-bit value (0 or 1)")

    def Set_CacheProg(self, value):
        if value == 0 or value == 1:
            self.CacheProg = value
        else:
            raise ValueError("CacheProg must be a 1-bit value (0 or 1)")

    def Set_Copyback(self, value):
        if value == 0 or value == 1:
            self.Copyback = value
        else:
            raise ValueError("Copyback must be a 1-bit value (0 or 1)")

    def Set_ProgWay(self, value):
        if value == 0 or value == 1:
            self.ProgWay = value
        else:
            raise ValueError("ProgWay must be a 1-bit value (0 or 1)")

    def Set_ResultDensity(self, value):
        if value >= 0 and value <= 3:
            self.ResultDensity = value
        else:
            raise ValueError("ResultDensity must be a 2-bit value (0-3)")

    def Set_SyncWrChipTotal(self, value):
        if value >= 0 and value <= 7:
            self.SyncWrChipTotal = value
        else:
            raise ValueError("SyncWrChipTotal must be a 3-bit value (0-7)")

    def Set_Reserved(self, value):
        if value >= 0 and value <= 1048575:
            self.Reserved = value
        else:
            raise ValueError("Reserved must be a 20-bit value (0-1048575)")

    def __str__(self):
        return f"SLC: {self.SLC}, EccEn: {self.EccEn}, Retry: {self.Retry}" \
               f"MPlane: {self.MPlane}, CacheProg: {self.CacheProg}, Copyback: {self.Copyback}" \
               f"ProgWay: {self.ProgWay}, ResultDensity: {self.ResultDensity}, SyncWrChipTotal: {self.SyncWrChipTotal}" \
               f"Reserved: {self.Reserved}"


class _CMD_ReadScanPos:
    def __init__(self):
        self.bCmd = 0
        self.bReadState = 0


class _CMD_PHY_BURNIN:
    def __init__(self, Hdr, wStarBlkNum, wEndBlkNum, wLoopNum, bSLC, bDataMode):
        self.Hdr = _CMD_HEADER()
        self.wStarBlkNum = 0
        self.wEndBlkNum = 0
        self.wLoopNum = 0
        self.bSLC = 0
        self.bDataMode = 0


class _CMD_PHY_CHECK_BLOCKSET:
    def __init__(self, Hdr, wStartBlkNum, wEndBlkNum, bRetry, bSLC, bDataMode):
        self.Hdr = _CMD_HEADER()
        self.wStartBlkNum = 0
        self.wEndBlkNum = 0
        self.bRetry = 0
        self.bSLC = 0
        self.bDataMode = 0


class _CMD_BLINK:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.bMode = 0


class _CMD_STATUS:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.bLUN = 0
        self.bOption = 0


class _CMD_WRITE_BLK:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wPageTotal = 0
        self.dwBlockAddr = 0
        self.dwSeed = 0
        self.inner_tMode1 = tMode1()
        self.bRetryEccNum = 0


class _CMD_CHECK_BLK:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wPageTotal = 0
        self.dwBlockAddr = 0
        self.dwSeed = 0
        self.inner_tMode1 = tMode1()
        self.bRetryEccNum = 0


class tMode1:
    def __init__(self):
        self.PlaneCmd = 0   # 2-bit field
        self.CacheCmd = 0   # 1-bit field
        self.SLC = 0        # 2-bit field
        self.SeedType = 0   # 2-bit field
        self.Retry = 0      # 1-bit field
        self.EccEn = 0      # 1-bit field
        self.SpareType = 0  # 2-bit field
        self.DataType = 0   # 2-bit field
        self.IntlvOP = 0    # 1-bit field
        self.BootCode = 0   # 1-bit field
        self.Reserved = 0   # 1-bit field

    def Set_PlaneCmd(self, value):
        if value >= 0 and value <= 3:
            self.PlaneCmd = value
        else:
            raise ValueError("PlaneCmd must be a 2-bit value (0-3)")

    def Set_CacheCmd(self, value):
        if value == 0 or value == 1:
            self.CacheCmd = value
        else:
            raise ValueError("CacheCmd must be a 1-bit value (0 or 1)")

    def Set_SLC(self, value):
        if value >= 0 and value <= 3:
            self.SLC = value
        else:
            raise ValueError("SLC must be a 2-bit value (0-3)")

    def Set_SeedType(self, value):
        if value >= 0 and value <= 3:
            self.SeedType = value
        else:
            raise ValueError("SeedType must be a 2-bit value (0-3)")

    def Set_Retry(self, value):
        if value == 0 or value == 1:
            self.Retry = value
        else:
            raise ValueError("Retry must be a 1-bit value (0 or 1)")

    def Set_EccEn(self, value):
        if value == 0 or value == 1:
            self.EccEn = value
        else:
            raise ValueError("EccEn must be a 1-bit value (0 or 1)")

    def Set_SpareType(self, value):
        if value >= 0 and value <= 3:
            self.SpareType = value
        else:
            raise ValueError("SpareType must be a 2-bit value (0-3)")

    def Set_DataType(self, value):
        if value >= 0 and value <= 3:
            self.DataType = value
        else:
            raise ValueError("DataType must be a 2-bit value (0-3)")

    def Set_IntlvOP(self, value):
        if value == 0 or value == 1:
            self.IntlvOP = value
        else:
            raise ValueError("IntlvOP must be a 1-bit value (0 or 1)")

    def Set_BootCode(self, value):
        if value == 0 or value == 1:
            self.BootCode = value
        else:
            raise ValueError("BootCode must be a 1-bit value (0 or 1)")

    def Set_Reserved(self, value):
        if value == 0 or value == 1:
            self.Reserved = value
        else:
            raise ValueError("Reserved must be a 1-bit value (0 or 1)")

    def __str__(self):
        return f"PlaneCmd: {self.PlaneCmd}, CacheCmd: {self.CacheCmd}, SLC: {self.SLC}" \
               f"SeedType: {self.SeedType}, Retry: {self.Retry}, EccEn: {self.EccEn}" \
               f"SpareType: {self.SpareType}, DataType: {self.DataType}, IntlvOP: {self.IntlvOP}" \
               f"BootCode: {self.BootCode}, Reserved: {self.Reserved}"

class _CMD_RESET:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.bLUN = 0
        self.bOption = 0


class _CMD_RB:
    def __init__(self):
        self.Hdr = _CMD_HEADER()


class _CMD_ACTIVE:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.bCnt = 0


class _CMD_SET_OTP:
    def __init__(self):
        self.bCmd = 0
        self.bOTPBuf = [0]*16


class _CMD_GET_OTP:
    def __init__(self):
        self.bCmd = 0


class _CMD_SET_STP:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wStrongPageTotal = 0


class _CMD_GET_STP:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wStrongPageTotal = 0


class _CMD_SET_CodeUpdata:
    def __init__(self):
        self.bCmd = 0
        self.wSectorNum = 0
        self.dwRewrFlg = 0
        self.bDataFinish = 0
        self.bEraseAll = 0
        self.dwXORCheck = 0
        self.wValidPageTotal = 0


class _CMD_SET_SetDiskParam:
    def __init__(self):
        self.bCmd = 0
        self.bIndex = 0
        self.wReceive = 0
        self.dwArg0 = 0
        self.dwArg1 = 0
        self.dwArg2 = 0


class _CMD_SET_CMD6:
    def __init__(self):
        self.bCmd = 0
        self.reserve = [0]*3
        self.dwArg = 0


class MSC:
    def __init__(self):
        self.KeyID = 0
        self.Direction = 0
        self.OpCode = 0
        self.SubOpCode = 0
        self.Chip = 0
        self.Length = 0
        self.Address = 0
        self.Residue = 0
        self.TrxLen = 0
        self.KeyAdd = 0
        self.CmdLogAdd = 0
        self.Reserved = [0]*4


class Union:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.Init = _CMD_INIT()
        self.ReadID = _CMD_READ_ID()
        self.Erase = _CMD_ERASE()
        self.Read = _CMD_READ()
        self.Write = _CMD_WRITE()
        self.Scan = _CMD_SCAN()
        self.PhyBurnin = _CMD_PHY_BURNIN()
        self.CheckBlkSet = _CMD_PHY_CHECK_BLOCKSET()
        self.Blink = _CMD_BLINK()
        self.Status = _CMD_STATUS()
        self.WriBlk = _CMD_WRITE_BLK()
        self.ChkBlk = _CMD_CHECK_BLK()
        self.Reset = _CMD_RESET()
        self.Active = _CMD_ACTIVE()
        self.GetLBAPhy = _CMD_GET_LBA_PHY()
        self.SetOTP = _CMD_SET_OTP()
        self.GetOTP = _CMD_GET_OTP()
        self.GetSTP = _CMD_GET_STP()
        self.SetSTP = _CMD_SET_STP()
        self.CodeUpdate = _CMD_SET_CodeUpdata()
        self.SetDParam = _CMD_SET_SetDiskParam()
        self.CMD6 = _CMD_SET_CMD6()
        self.LGErase = tyLGErase()
        self.eMMCWP = tyeMMCWP()
        self.Reserved = [0]*440


class _CMD:
    def __init__(self):
        self.dwHead = [0]*8
        self.MSC = MSC()
        self.Union = Union()
        self.dwXOR = 0
        self.dwFlag = 0

    def __str__(self):
        return f"dwHead: {self.dwHead}, MSC: {self.MSC.__dict__}, " \
               f"Union: {self.Union.__dict__}, dwXOR: {self.dwXOR}, dwFlag: {self.dwFlag}"


UNION = Union()
UNION.Hdr.bCmd = 1
print(UNION)











