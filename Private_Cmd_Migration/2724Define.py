#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：Private_Cmd_Migration 
@File    ：2724Define.py
@IDE     ：PyCharm 
@Author  ：厄运马马卡
@Date    ：2023/9/25 16:18 
'''


class PRIVATE_DATA_TAG:
    def __init__(self, dwIsPageSpare0, dwIsPageSpare1):
        self.dwIsPageSpare0 = dwIsPageSpare0
        self.dwIsPageSpare1 = dwIsPageSpare1


class FLASH_PARAM:
    def __init__(self, dwTag, dwStructVer, bResserved0, bRFreq, bWFreq, bSampleDot, bDQSDelay, bDelayBeforeWaitRB,
                 bDelay_tWHR, bDelay_tADL, bReserved1, bReserved2, bCETotal, bLunPerCE, bInterleaveWay, bPlaneTotal,
                 wByteOfPage, bSectOfPage, bEccSectPerPage, wPagePerBlk, wStrongPagePerBlk, wBlkPageSize,
                 wBlockPerLUN, wLUNBlockSize, wPlaneRowSize, wBlockPerCE, wReserved3, bBlockTotal, bFlashFeature,
                 dwEccMode, bMaxEccErrorBit, bEccSectTotal, bBadInfoPosition, bPlaneCMDType, bReserved4, bReservedK):
        self.dwTag = dwTag
        self.dwStructVer = dwStructVer
        self.bResserved0 = bResserved0
        self.bRFreq = bRFreq
        self.bWFreq = bWFreq
        self.bSampleDot = bSampleDot
        self.bDQSDelay = bDQSDelay
        self.bDelayBeforeWaitRB = bDelayBeforeWaitRB
        self.bDelay_tWHR = bDelay_tWHR
        self.bDelay_tADL = bDelay_tADL
        self.bReserved1 = bReserved1
        self.bReserved2 = bReserved2
        self.bCETotal = bCETotal
        self.bLunPerCE = bLunPerCE
        self.bInterleaveWay = bInterleaveWay
        self.bPlaneTotal = bPlaneTotal
        self.wByteOfPage = wByteOfPage
        self.bSectOfPage = bSectOfPage
        self.bEccSectPerPage = bEccSectPerPage
        self.wPagePerBlk = wPagePerBlk
        self.wStrongPagePerBlk = wStrongPagePerBlk
        self.wBlkPageSize = wBlkPageSize
        self.wBlockPerLUN = wBlockPerLUN
        self.wLUNBlockSize = wLUNBlockSize
        self.wPlaneRowSize = wPlaneRowSize
        self.wBlockPerCE = wBlockPerCE
        self.wReserved3 = wReserved3
        self.bBlockTotal = bBlockTotal
        self.bFlashFeature = bFlashFeature
        self.dwEccMode = dwEccMode
        self.bMaxEccErrorBit = bMaxEccErrorBit
        self.bEccSectTotal = bEccSectTotal
        self.bBadInfoPosition = bBadInfoPosition
        self.bPlaneCMDType = bPlaneCMDType
        self.bReserved4 = bReserved4
        self.bReservedK = bReservedK


class IIR_UTBL:
    MAX_ADJ_CAP = 3
    CodeBlkCnt = 4
    DiskParamBlkCnt = 2
    MAX_CHIP_NUM = 4
    def __init__(self, dwTag, dwStructVersion, dwHWVersion, PLL_Config, bReserved0, CPU_Clock_Div, MCLK_Clock_Div,
                 SCLK_Clock_Div, FCLK_Clock_Div, bFlashFeature, bCETotal, bFcOpReadCycle, bFcOpWriteCycle, bFcRdSim,
                 bBadBlkInfoType, bMaxReMappingBitSize, bReserved1, bCodeOfChip, wCodePhyBlk, wDiskParamBlk,
                 bDiskParamBlkChip, bCodeEccMode, bMaxBITsubsection, wPMZoneSize, wRealRedundancyCoeff, wReserveUserBlkNum,
                 wReserveSectPerBlk, bIDA_EN, bInterLeaveRWDisable, wOrigBITBlkTotalPerPage, wCodeBlkValidPageTotal,
                 bBuildBIT, bReserved2, dwEmptyA5):
        self.dwTag = dwTag
        self.dwStructVersion = dwStructVersion
        self.dwHWVersion = dwHWVersion
        self.PLL_Config = PLL_Config
        self.bReserved0 = bReserved0
        self.CPU_Clock_Div = CPU_Clock_Div
        self.MCLK_Clock_Div = MCLK_Clock_Div
        self.SCLK_Clock_Div = SCLK_Clock_Div
        self.FCLK_Clock_Div = FCLK_Clock_Div
        self.bFlashFeature = bFlashFeature
        self.bCETotal = bCETotal
        self.bFcOpReadCycle = bFcOpReadCycle
        self.bFcOpWriteCycle = bFcOpWriteCycle
        self.bFcRdSim = bFcRdSim
        self.bBadBlkInfoType = bBadBlkInfoType
        self.bMaxReMappingBitSize = bMaxReMappingBitSize
        self.bReserved1 = bReserved1
        self.bCodeOfChip = bCodeOfChip
        self.wCodePhyBlk = wCodePhyBlk
        self.wDiskParamBlk = wDiskParamBlk
        self.bDiskParamBlkChip = bDiskParamBlkChip
        self.bCodeEccMode = bCodeEccMode
        self.bMaxBITsubsection = bMaxBITsubsection
        self.wPMZoneSize = wPMZoneSize
        self.wRealRedundancyCoeff = wRealRedundancyCoeff
        self.wReserveUserBlkNum = wReserveUserBlkNum
        self.wReserveSectPerBlk = wReserveSectPerBlk
        self.bIDA_EN = bIDA_EN
        self.bInterLeaveRWDisable = bInterLeaveRWDisable
        self.wOrigBITBlkTotalPerPage = wOrigBITBlkTotalPerPage
        self.wCodeBlkValidPageTotal = wCodeBlkValidPageTotal
        self.bBuildBIT = bBuildBIT
        self.bReserved2 = bReserved2
        self.dwEmptyA5 = dwEmptyA5


class tySMART:
    def __init__(self, dwSMARTTag, dwSMARTVersions, bFWVersions, bFlashID, dwOriginalBabBlock, dwIncreaseBadBlock,
                 dwSLCFreeBlockNumber, dwFreeBlockNumber, dwPowerUpNumber, dwLogicDataDisperse, dwDegreOfWearForCache,
                 dwDegreOfWear, dwWearLevelingVarianceForCache, dwWearLevelingVariance, dwMaxWearNumberForCache,
                 dwMaxWearNumber, dwReplaceNumber, dwCacheBlockDiviedPoint, lwWriteAllSectNum, dwIllegalPowerLossCount,
                 dwUncorrectableCount, dwBackupFWUsedCount, dwBackupBootUsedCount, dwCRCErrCnt, wBITBlk, bBITBlkChip,
                 wCodeBlk, bCodeBlkChip, dwBootIndexRow, wBootIndexCol, bBootIndexBlkChip, wDiskParamBlk, bDiskParamBlkChip,
                 bUID, dwCollectNum, bRebuildReason, bSMTProtected, dwFreeTimeCollectFailCnt, dwVDTNum, bCollectCopyFail,
                 bReserved0, wLogWrCopyPageErrCnt, wEraseFailIgnoreBlkTotal, wDiscardCnt, wTrimCnt, wPackCmdCnt, wRPMBWRCnt,
                 wRPMBImpCnt, wSecureWPCnt, wCmdQueCnt, wWPCnt, wBootWPCnt, wLockUnLockCnt, wRelWRCnt, wPowerNotificationCnt,
                 wReserved3, dwLDO1Value, bReserved, inner_MPInfo, bExtCsd):
        self.dwSMARTTag = dwSMARTTag
        self.dwSMARTVersions = dwSMARTVersions
        self.bFWVersions = bFWVersions
        self.bFlashID = bFlashID
        self.dwOriginalBabBlock = dwOriginalBabBlock
        self.dwIncreaseBadBlock = dwIncreaseBadBlock
        self.dwSLCFreeBlockNumber = dwSLCFreeBlockNumber
        self.dwFreeBlockNumber = dwFreeBlockNumber
        self.dwPowerUpNumber = dwPowerUpNumber
        self.dwLogicDataDisperse = dwLogicDataDisperse
        self.dwDegreOfWearForCache = dwDegreOfWearForCache
        self.dwDegreOfWear = dwDegreOfWear
        self.dwWearLevelingVarianceForCache = dwWearLevelingVarianceForCache
        self.dwWearLevelingVariance = dwWearLevelingVariance
        self.dwMaxWearNumberForCache = dwMaxWearNumberForCache
        self.dwMaxWearNumber = dwMaxWearNumber
        self.dwReplaceNumber = dwReplaceNumber
        self.dwCacheBlockDiviedPoint = dwCacheBlockDiviedPoint
        self.lwWriteAllSectNum = lwWriteAllSectNum
        self.dwIllegalPowerLossCount = dwIllegalPowerLossCount
        self.dwUncorrectableCount = dwUncorrectableCount
        self.dwBackupFWUsedCount = dwBackupFWUsedCount
        self.dwBackupBootUsedCount = dwBackupBootUsedCount
        self.dwCRCErrCnt = dwCRCErrCnt
        self.wBITBlk = wBITBlk
        self.bBITBlkChip = bBITBlkChip
        self.wCodeBlk = wCodeBlk
        self.bCodeBlkChip = bCodeBlkChip
        self.dwBootIndexRow = dwBootIndexRow
        self.wBootIndexCol = wBootIndexCol
        self.bBootIndexBlkChip = bBootIndexBlkChip
        self.wDiskParamBlk = wDiskParamBlk
        self.bDiskParamBlkChip = bDiskParamBlkChip
        self.bUID = bUID
        self.dwCollectNum = dwCollectNum
        self.bRebuildReason = bRebuildReason
        self.bSMTProtected = bSMTProtected
        self.dwFreeTimeCollectFailCnt = dwFreeTimeCollectFailCnt
        self.dwVDTNum = dwVDTNum
        self.bCollectCopyFail = bCollectCopyFail
        self.bReserved0 = bReserved0
        self.wLogWrCopyPageErrCnt = wLogWrCopyPageErrCnt
        self.wEraseFailIgnoreBlkTotal = wEraseFailIgnoreBlkTotal
        self.wDiscardCnt = wDiscardCnt
        self.wTrimCnt = wTrimCnt
        self.wPackCmdCnt = wPackCmdCnt
        self.wRPMBWRCnt = wRPMBWRCnt
        self.wRPMBImpCnt = wRPMBImpCnt
        self.wSecureWPCnt = wSecureWPCnt
        self.wCmdQueCnt = wCmdQueCnt
        self.wWPCnt = wWPCnt
        self.wBootWPCnt = wBootWPCnt
        self.wLockUnLockCnt = wLockUnLockCnt
        self.wRelWRCnt = wRelWRCnt
        self.wPowerNotificationCnt = wPowerNotificationCnt
        self.wReserved3 = wReserved3
        self.dwLDO1Value = dwLDO1Value
        self.bReserved = bReserved
        self.inner_MPInfo = MPInfo()
        self.bExtCsd = bExtCsd


class MPInfo:
    def __init__(self, bMPToolVersions, wYear, bMonth, bDay, bHour, bMinute, bSecond, bScanType, bScanData, bScanConfig,
                 bScanECCLevel, bFixedID, bPrefixID, bRandomID, wStandbyCurrent, bInitialMaxErrorBit, bInitialAverageErrorBit,
                 bInitialMinErrorBit, bReserved1, bOCR, bCID, bCSD):
        self.bMPToolVersions = bMPToolVersions
        self.wYear = wYear
        self.bMonth = bMonth
        self.bDay = bDay
        self.bHour = bHour
        self.bMinute = bMinute
        self.bSecond = bSecond
        self.bScanType = bScanType
        self.bScanData = bScanData
        self.bScanConfig = bScanConfig
        self.bScanECCLevel = bScanECCLevel
        self.bFixedID = bFixedID
        self.bPrefixID = bPrefixID
        self.bRandomID = bRandomID
        self.wStandbyCurrent = wStandbyCurrent
        self.bInitialMaxErrorBit = bInitialMaxErrorBit
        self.bInitialAverageErrorBit = bInitialAverageErrorBit
        self.bInitialMinErrorBit = bInitialMinErrorBit
        self.bReserved1 = bReserved1
        self.bOCR = bOCR
        self.bCID = bCID
        self.bCSD = bCSD


class tyUserSMART:
    def __init__(self, dwSMARTTag, dwSMARTVersions, wSMARTByteCount, bSMARTCheckSum, bFWVersions, wYear, bMonth, bDay,
                 bHour, bMinute, bSecond, bFlashID, bPrefixID, bRandomID, bInitialMaxErrorBit, dwOriginalBadBlock,
                 dwIncreaseBadBlock, dwFreeBlockNumber, dwPowerUpNumber, lwWriteAllSectNum, dwIllegalPowerLossCount,
                 BUID, dwIDAStatus, bSMTProtected):
        self.dwSMARTTag = dwSMARTTag
        self.dwSMARTVersions = dwSMARTVersions
        self.wSMARTByteCount = wSMARTByteCount
        self.bSMARTCheckSum = bSMARTCheckSum
        self.bFWVersions = bFWVersions
        self.wYear = wYear
        self.bMonth = bMonth
        self.bDay = bDay
        self.bHour = bHour
        self.bMinute = bMinute
        self.bSecond = bSecond
        self.bFlashID = bFlashID
        self.bPrefixID = bPrefixID
        self.bRandomID = bRandomID
        self.bInitialMaxErrorBit = bInitialMaxErrorBit
        self.dwOriginalBadBlock = dwOriginalBadBlock
        self.dwIncreaseBadBlock = dwIncreaseBadBlock
        self.dwFreeBlockNumber = dwFreeBlockNumber
        self.dwPowerUpNumber = dwPowerUpNumber
        self.lwWriteAllSectNum = lwWriteAllSectNum
        self.dwIllegalPowerLossCount = dwIllegalPowerLossCount
        self.BUID = BUID
        self.dwIDAStatus = dwIDAStatus
        self.bSMTProtected = bSMTProtected


SMARTTag = (0x96325874)
SMARTVersions = (2)
class tySMART2705:
    def __init__(self, dwSMARTTag, dwSMARTVersions, bFWVersions, bFlashID, dwOriginalBabBlock, dwIncreaseBadBlock,
                 dwSLCFreeBlockNumber, dwFreeBlockNumber, dwPowerUpNumber, dwLogicDataDisperse, dwDegreOfWearForCache,
                 dwDegreOfWear, dwWearLevelingVarianceForCache, dwWearLevelingVariance, dwMaxWearNumberForCache,
                 dwMaxWearNumber, dwReplaceNumber, dwCacheBlockDiviedPoint, lwWriteAllSectNum, dwIllegalPowerLossCount,
                 dwUncorrectableCount, dwBackupFWUsedCount, dwBackupBootUsedCount, dwCRCErrCnt, wBITBlk, bBITBlkChip,
                 wCodeBlk, bCodeBlkChip, dwBootIndexRow, wBootIndexCol, bBootIndexBlkChip, wDiskParamBlk, bDiskParamBlkChip,
                 bUID, dwCollectNum, bRebuildReason, bSMTProtected, dwFreeTimeCollectFailCnt, dwVDTNum, bCollectCopyFail,
                 bReserved, wLogWrCopyPageErrCnt, dwAllGarbGCCnt, dwReadRetryCnt, dwLevel3Cnt, dwBalanceCnt, dwBalanceHandleCnt,
                 bReserved2, inner_MPInfo, bExtCsd):
        self.dwSMARTTag = dwSMARTTag
        self.dwSMARTVersions = dwSMARTVersions
        self.bFWVersions = bFWVersions
        self.bFlashID = bFlashID
        self.dwOriginalBabBlock = dwOriginalBabBlock
        self.dwIncreaseBadBlock = dwIncreaseBadBlock
        self.dwSLCFreeBlockNumber = dwSLCFreeBlockNumber
        self.dwFreeBlockNumber = dwFreeBlockNumber
        self.dwPowerUpNumber = dwPowerUpNumber
        self.dwLogicDataDisperse = dwLogicDataDisperse
        self.dwDegreOfWearForCache = dwDegreOfWearForCache
        self.dwDegreOfWear = dwDegreOfWear
        self.dwWearLevelingVarianceForCache = dwWearLevelingVarianceForCache
        self.dwWearLevelingVariance = dwWearLevelingVariance
        self.dwMaxWearNumberForCache = dwMaxWearNumberForCache
        self.dwMaxWearNumber = dwMaxWearNumber
        self.dwReplaceNumber = dwReplaceNumber
        self.dwCacheBlockDiviedPoint = dwCacheBlockDiviedPoint
        self.lwWriteAllSectNum = lwWriteAllSectNum
        self.dwIllegalPowerLossCount = dwIllegalPowerLossCount
        self.dwUncorrectableCount = dwUncorrectableCount
        self.dwBackupFWUsedCount = dwBackupFWUsedCount
        self.dwBackupBootUsedCount = dwBackupBootUsedCount
        self.dwCRCErrCnt = dwCRCErrCnt
        self.wBITBlk = wBITBlk
        self.bBITBlkChip = bBITBlkChip
        self.wCodeBlk = wCodeBlk
        self.bCodeBlkChip = bCodeBlkChip
        self.dwBootIndexRow = dwBootIndexRow
        self.wBootIndexCol = wBootIndexCol
        self.bBootIndexBlkChip = bBootIndexBlkChip
        self.wDiskParamBlk = wDiskParamBlk
        self.bDiskParamBlkChip = bDiskParamBlkChip
        self.bUID = bUID
        self.dwCollectNum = dwCollectNum
        self.bRebuildReason = bRebuildReason
        self.bSMTProtected = bSMTProtected
        self.dwFreeTimeCollectFailCnt = dwFreeTimeCollectFailCnt
        self.dwVDTNum = dwVDTNum
        self.bCollectCopyFail = bCollectCopyFail
        self.bReserved = bReserved
        self.wLogWrCopyPageErrCnt = wLogWrCopyPageErrCnt
        self.dwAllGarbGCCnt = dwAllGarbGCCnt
        self.dwReadRetryCnt = dwReadRetryCnt
        self.dwLevel3Cnt = dwLevel3Cnt
        self.dwBalanceCnt = dwBalanceCnt
        self.dwBalanceHandleCnt = dwBalanceHandleCnt
        self.bReserved2 = bReserved2
        self.inner_MPInfo = MPInfo1()
        self.bExtCsd = bExtCsd


class MPInfo1:
    def __init__(self, bMPToolVersions, wYear, bMonth, bDay, bHour, bMinute, bSecond, bScanType, bScanData, bScanConfig,
                 bScanECCLevel, bFixedID, bPrefixID, bRandomID, wStandbyCurrent, bInitialMaxErrorBit, bInitialAverageErrorBit,
                 bInitialMinErrorBit, bReserved1, bOCR, bCID, bCSD):
        self.bMPToolVersions = bMPToolVersions
        self.wYear = wYear
        self.bMonth = bMonth
        self.bDay = bDay
        self.bHour = bHour
        self.bMinute = bMinute
        self.bSecond = bSecond
        self.bScanType = bScanType
        self.bScanData = bScanData
        self.bScanConfig = bScanConfig
        self.bScanECCLevel = bScanECCLevel
        self.bFixedID = bFixedID
        self.bPrefixID = bPrefixID
        self.bRandomID = bRandomID
        self.wStandbyCurrent = wStandbyCurrent
        self.bInitialMaxErrorBit = bInitialMaxErrorBit
        self.bInitialAverageErrorBit = bInitialAverageErrorBit
        self.bInitialMinErrorBit = bInitialMinErrorBit
        self.bReserved1 = bReserved1
        self.bOCR = bOCR
        self.bCID = bCID
        self.bCSD = bCSD


class tyISP_TAG:
    def __init__(self, bScanBin, bPageID, wPageIndex, dwBankAddr, dwReserved0, dwReserved1):
        self.bScanBin = bScanBin
        self.bPageID = bPageID
        self.wPageIndex = wPageIndex
        self.wPageIndex = wPageIndex
        self.dwBankAddr = dwBankAddr
        self.dwReserved0 = dwReserved0
        self.dwReserved1 = dwReserved1


class tyScanISPDef:
    def __init__(self, bIndex, bUsage, bReserved0, bReserved1, dwHeadLen, dwISPsize, bReserved2, bReserved3,
                 dwBankAddr, bReserved4, bReserved5):
        self.bIndex = bIndex
        self.bUsage = bUsage
        self.bReserved0 = bReserved0
        self.bReserved1 = bReserved1
        self.dwHeadLen = dwHeadLen
        self.dwISPsize = dwISPsize
        self.bReserved2 = bReserved2
        self.bReserved3 = bReserved3
        self.dwBankAddr = dwBankAddr
        self.bReserved4 = bReserved4
        self.bReserved5 = bReserved5


class _CMD_HEADER:
    def __init__(self):
        self.bCmd = 0
        self.bChipNum = 0


class _CMD_INIT:
    def __init__(self):
        self.Hdr = 0


class _CMD_READ_ID:
    def __init__(self, Hdr):
        self.Hdr = Hdr


class _CMD_ERASE:
    def __init__(self, Hdr, bSLCMode, bEraseMode, dwBlockAddr, wBlockTotal, wReserved, wCodeCheckFlag, bCodeBlkIndex):
        self.Hdr = Hdr
        self.bSLCMode = bSLCMode
        self.bEraseMode = bEraseMode
        self.dwBlockAddr = dwBlockAddr
        self.wBlockTotal = wBlockTotal
        self.wReserved = wReserved
        self.wCodeCheckFlag = wCodeCheckFlag
        self.bCodeBlkIndex = bCodeBlkIndex


class tyLGErase:
    def __init__(self, bCmd, reserve, dwStartAddr, dwEndAddr):
        self.bCmd = bCmd
        self.reserve = reserve
        self.dwStartAddr = dwStartAddr
        self.dwEndAddr = dwEndAddr


class tyeMMCWP:
    def __init__(self, bCmd, bReserve, dwStartAddr):
        self.bCmd = bCmd
        self.bReserve = bReserve
        self.dwStartAddr = dwStartAddr


class _CMD_GET_LBA_PHY:
    def __init__(self, Hdr, dwTagLBA):
        self.Hdr = Hdr
        self.dwTagLBA = dwTagLBA


class _CMD_READ:
    def __init__(self, Hdr, wSectCnt, dwRowAddr, dwSeed, inner_tMode, wColAddr):
        self.Hdr = Hdr
        self.wSectCnt = wSectCnt
        self.dwRowAddr = dwRowAddr
        self.dwSeed = dwSeed
        self.inner_tMode = tMode()
        self.wColAddr = wColAddr
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
    def __init__(self, Hdr, wSectCnt, dwRowAddr, dwSeed, inner_tMode, wColAddr):
        self.Hdr = Hdr
        self.wSectCnt = wSectCnt
        self.dwRowAddr = dwRowAddr
        self.dwSeed = dwSeed
        self.inner_tMode = tMode()
        self.wColAddr = wColAddr


class _CMD_SCAN:
    def __init__(self, bCmd, bChipNum, wStartBlkNum, wScanBlockCnt, bScanCase, bDataErrBits, bSpareErrBits, Reserved):
        self.bCmd = bCmd
        self.bChipNum = bChipNum
        self.wStartBlkNum = wStartBlkNum
        self.wScanBlockCnt = wScanBlockCnt
        self.bScanCase = bScanCase
        self.bDataErrBits = bDataErrBits
        self.bSpareErrBits = bSpareErrBits
        self.Reserved = Reserved


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
    def __init__(self, bCmd, bReadState):
        self.bCmd = bCmd
        self.bReadState = bReadState


class _CMD_PHY_BURNIN:
    def __init__(self, Hdr, wStarBlkNum, wEndBlkNum, wLoopNum, bSLC, bDataMode):
        self.Hdr = Hdr
        self.wStarBlkNum = wStarBlkNum
        self.wEndBlkNum = wEndBlkNum
        self.wLoopNum = wLoopNum
        self.bSLC = bSLC
        self.bDataMode = bDataMode


class _CMD_PHY_CHECK_BLOCKSET:
    def __init__(self, Hdr, wStartBlkNum, wEndBlkNum, bRetry, bSLC, bDataMode):
        self.Hdr = Hdr
        self.wStartBlkNum = wStartBlkNum
        self.wEndBlkNum = wEndBlkNum
        self.bRetry = bRetry
        self.bSLC = bSLC
        self.bDataMode = bDataMode


class _CMD_BLINK:
    def __init__(self, Hdr, bMode):
        self.Hdr = Hdr
        self.bMode = bMode


class _CMD_STATUS:
    def __init__(self, Hdr, bLUN, bOption):
        self.Hdr = Hdr
        self.bLUN = bLUN
        self.bOption = bOption


class _CMD_WRITE_BLK:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wPageTotal = 0
        self.dwBlockAddr = 0
        self.dwSeed = 0
        self.bRetryEccNum = 0


class _CMD_CHECK_BLK:
    def __init__(self):
        self.Hdr = _CMD_HEADER()
        self.wPageTotal = 0
        self.dwBlockAddr = 0
        self.dwSeed = 0
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
    def __init__(self, Hdr, bLUN, bOption):
        self.Hdr = Hdr
        self.bLUN = bLUN
        self.bOption = bOption


class _CMD_RB:
    def __init__(self, Hdr):
        self.Hdr = Hdr


class _CMD_ACTIVE:
    def __init__(self, Hdr, bCnt):
        self.Hdr = Hdr
        self.bCnt = bCnt


class _CMD_SET_OTP:
    def __init__(self, bCmd, bOTPBuf):
        self.bCmd = bCmd
        self.bOTPBuf = bOTPBuf


class _CMD_GET_OTP:
    def __init__(self, bCmd):
        self.bCmd = bCmd


class _CMD_SET_STP:
    def __init__(self, bCmd, wStrongPageTotal):
        self.bCmd = bCmd
        self.bOTPBuf = wStrongPageTotal


class _CMD_GET_STP:
    def __init__(self, bCmd, wStrongPageTotal):
        self.bCmd = bCmd
        self.bOTPBuf = wStrongPageTotal


class _CMD_SET_CodeUpdata:
    def __init__(self, bCmd, wSectorNum, dwRewrFlg, bDataFinish, bEraseAll, dwXORCheck, wValidPageTotal):
        self.bCmd = bCmd
        self.wSectorNum = wSectorNum
        self.dwRewrFlg = dwRewrFlg
        self.bDataFinish = bDataFinish
        self.bEraseAll = bEraseAll
        self.dwXORCheck = dwXORCheck
        self.wValidPageTotal = wValidPageTotal


class _CMD_SET_SetDiskParam:
    def __init__(self, bCmd, bIndex, wReceive, dwArg0, dwArg1, dwArg2):
        self.bCmd = bCmd
        self.bIndex = bIndex
        self.wReceive = wReceive
        self.dwArg0 = dwArg0
        self.dwArg1 = dwArg1
        self.dwArg2 = dwArg2


class _CMD_SET_CMD6:
    def __init__(self, bCmd, reserve, dwArg):
        self.bCmd = bCmd
        self.reserve = reserve
        self.dwArg = dwArg


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











