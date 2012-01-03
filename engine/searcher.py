#coding: utf-8

import os
import subprocess

class Searcher:
    def __init__(self, dataDir=None):
        self.dataDir = None
        self.dataFiles = None
        if dataDir:
            self.set_data_dir(dataDir)
    
    def set_data_dir(self, dataDir):
        assert os.path.isdir(dataDir)
        self.dataDir = dataDir
        self.dataFiles = [f for f in os.listdir(dataDir) \
                if os.path.isfile(os.path.join(dataDir, f))]

    def search(self, query, options=None):
        assert self.dataDir is not None
        cmdLine = ["agrep", query]
        if options:
            cmdLine[1:1] = options
        d = {}
        for f in self.dataFiles:
            p = os.path.join(self.dataDir, f)
            try:
                r = subprocess.check_output(cmdLine + [p],
                        stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                d[f] = e
            d[f] = r
        return d

