#coding: utf-8

import os
import subprocess

try:
    subprocess.check_output(["tre-agrep", "--help"])
except OSError:
    raise ImportError("tre-agrep not found. locdic depends on tre-agrep")

version = "0.3.0"
moduleDir = os.path.split(__file__)[0]
ignoreFiles = [ 'readme', '*~', '*.py', '*.pyc', '*.original' ]

homeDir = os.getenv('HOME', None)
if not homeDir:
    raise SystemError("can't getenv: $HOME")

def locate_data_directory():
    dataDirName = "data"
    e = os.getenv('LOCDIC_DATA_DIRECTORY', None)
    if e:
        return e
        
    configDir = os.path.join(homeDir, ".locdic")
    if os.path.exists(configDir):
        return os.path.join(configDir, dataDirName)

    return os.path.join(moduleDir, dataDirName)

dataDir = locate_data_directory()

historyDir = os.path.join(homeDir, ".locdic", "history")
