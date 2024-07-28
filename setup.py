import sys
import os
from cx_Freeze import setup, Executable

files = ['bikerdomz.ico']

target = Executable(
    script = "main.py",
    base ="Win32GUI",
    icon = "bikerdomz.ico"
)

setup(
    name = "BikerDomzApp",
    version = "1.0",
    description ="Inventory Management System",
    author = "CCS",
    options = {'build.exe' : {'include_files' : files}},
    executables = [target]
)
