#coding: utf-8

import os

moduleDir = os.path.split(__file__)[0]
ignoreFiles = [ 'readme', '*~', '*.py', '*.pyc', '*.original' ]

def locate_data_directory():
    dataDirName = "data"
    e = os.getenv('LOCDIC_DATA_DIRECTORY', None)
    if e:
        return e
        
    homeDir = os.getenv('HOME', None)
    if homeDir:
        configDir = os.path.join(homeDir, ".locdic")
        if os.path.exists(configDir):
            return os.path.join(configDir, dataDirName)

    return os.path.join(moduleDir, dataDirName)

dataDir = locate_data_directory()