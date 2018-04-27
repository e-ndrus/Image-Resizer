# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 12:09:05 2018

@author: User
"""

import sys
from cx_Freeze import setup, Executable

import os
os.environ['TCL_LIBRARY'] = "C:\\Users\\User\\Anaconda3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\User\\Anaconda3\\tcl\\tk8.6"

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Image Resizer",
        version = "0.1",
        description = "A small tool for resizing and renaming jpg files.",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Image Resizer.py", base=base)])