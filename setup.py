import sys
import os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
os.environ['TCL_LIBRARY'] = r'C:\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Python36\tcl\tk8.6'

build_exe_options = {"packages": [], "include_files" : [r"C:\Python36\DLLs\tcl86t.dll", r"C:\Python36\DLLs\tk86t.dll"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = "Win32GUI"

setup(  name = "聖槍刺擊傷害模擬器",
        version = "0.1.0",
        description = "模擬聖槍刺擊的最大傷害",
        options = {"build_exe": build_exe_options},
        executables = [Executable("VaretyrSpearSimulation.py", targetName = "聖槍刺擊傷害模擬器.exe", base=base)])