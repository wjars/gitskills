#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import os
import re
import sys
import random
import time
import dtb

class RWfileTest(dtb.TestStart):

    def __init__(self):
        super().__init__()

    def fileStatueInit(self):
        """
        @brief:
        @return:
        """
        pass

    def test(self):
        """
        @brief: This is the main test function for this script.
        @return None.
        """
        self.logger.info("test Running")


if __name__ == "__main__":
    test = RWfileTest()
    sys.exit(test.RUN())
