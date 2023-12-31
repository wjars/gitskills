#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

"""
This module contains all of the exception that are generated by dtb.
All of them will be used by the dtb framework, not open to script users.
"""

import dtb

class dtbError(Exception):
    """
    define the exceptions that are generated by dtb
    """
    def __init__(self, message=""):
        Exception.__init__(self, message)

class TestFailError(dtbError):
    """
    define the dtb errors
    """
    def __init__(self, message=""):
        dtb.dtbError.__init__(self, message)
