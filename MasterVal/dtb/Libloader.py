#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import importlib
import os
import sys
import inspect

PROJ_LIB_DIR = "lib"
PROJ_CONFIG_DIR = "config"
PROJ_GENERIC_DIR = "Generic"
PROJ_SYSTest_DIR = "sysTest"

class Libloader():
    """
    @brief: A module used by test scripts to load lib scripts or config files dynamically
    @Copyright: 2023, longsys
    @Author: changwang.cai@longsys.com
    """

    def __init__(self, testInstance, loadCfg=False):
        """
        @brief: initialization when create instance of this class
        @param: testInstance A /a instance test instance
        @return: this method raises no value
        @exception: this method raises no exception
        """
        self.testInstance = testInstance
        self._loadCfg = loadCfg
        self._libDirName = PROJ_LIB_DIR if not self._loadCfg else PROJ_CONFIG_DIR

        self._objCache = {}
        self._libPath = None
        if self._libPath is None:
            self._getLibPath()

    def _getLibPath(self):
        """
        @brief: get cfg path..
        @return a type of path(produce lib path , generic lib path)
        @exception This method raises exception when lib path can't be found
        """
        if self._libPath is None:
            pathList = os.path.abspath(__file__).split(os.sep)
            rootPath = os.path.join(os.sep.join(pathList[:pathList.index("dtb")]), self._libDirName)
            for root, dirs, dummy_files in os.walk(rootPath):
                if not root.startswith('_') and root not in sys.path:
                    sys.path.insert(0, root)

                if (PROJ_GENERIC_DIR in dirs) and (self.testInstance.args.product in dirs):
                    if self.testInstance.args.customer == "Generic":
                        self._libPath = (
                            root + os.sep + self.testInstance.args.product, root + os.sep + PROJ_GENERIC_DIR + os.sep + "sysTest")
                    else:
                        raise RuntimeError("Customer %s not exist in current product directory"
                                           % (self.testInstance.args.customer))

    def __getattr__(self, clsName):
        """
        @brief: get attributes of current class
        @param: cls_name A \\s str value indicates the lib class name to load
        @return: Instance of target lib class
        @exception This method raises exception when target lib can't be found or initialized failed
        """
        if clsName in self._objCache:
            return self._objCache[clsName]
        for libPath in self._libPath:

            if sys.path[0] != libPath[:libPath.index(self._libDirName)]:
                sys.path.insert(0, libPath[:libPath.index(self._libDirName)])
            for libFile in os.listdir(libPath):

                if not libFile.endswith(".py"):
                    continue

                if libFile.startswith("_"):
                    continue

                modName = libFile.split(".")[0]
                if modName not in sys.modules:
                    modPath = os.path.join(libPath, modName)[libPath.index(self._libDirName):].replace(os.sep, '.')
                    impMod = importlib.import_module(modPath)
                else:
                    impMod = sys.modules[modName]

                for name, cls in inspect.getmembers(impMod, inspect.isclass):
                    if name.lower() == clsName.lower():
                        clsType = type('Bridge_' + clsName, (cls,), dict())
                        self._objCache[clsName] = clsType(self.testInstance)
                        return self._objCache[clsName]

        raise RuntimeError("Fail to find class {0} under path {1}" .format(clsName, self._libPath))
