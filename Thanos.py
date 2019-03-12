#!/usr/bin/python3
# -------------------------------------------
# Thanos.py: Decimation for your files      |
# -------------------------------------------

import os
import random

import ctypes, sys

def execute_():
    mydir = os.getcwd()
    filelist = [f for f in os.listdir(mydir)]
    random.shuffle(filelist)
    length_ = round(len(filelist)/2)
    filelist = filelist[:length_]
    for f in filelist:
        if f.endswith("Thanos.py"):
            pass
        else:
            print(f)
            #os.remove(os.path.join(mydir, f))

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

    # Code of your program here
if is_admin():
    execute_()

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    execute_()
