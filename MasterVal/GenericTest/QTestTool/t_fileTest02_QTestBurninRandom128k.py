#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd
import sys

from t_fileTest02_QTestBurninRandom64k import QTestBurninRandom64k


class QTestBurninRandom128k(QTestBurninRandom64k):
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
        self.BufferType = '128k'


if __name__ == "__main__":
    test = QTestBurninRandom128k()
    sys.exit(test.RUN())
