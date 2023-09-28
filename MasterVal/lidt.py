#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Copyright (C), 2023, Longsys Electronics Co .Ltd

import sys
import os
import inspect


print("case Running")

import os

stm_folder = "/STM/3720"

my_dir_path = os.path.dirname(__file__)
stm_folder = os.path.abspath(my_dir_path + stm_folder)

sys.path.append(stm_folder)
print(stm_folder)

import py_ls_device

for m in inspect.getmembers(py_ls_device):
    globals()[m[0]] = m[1]
