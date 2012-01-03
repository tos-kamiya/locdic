#coding: utf-8

import os
import subprocess

class Searcher:
    def __init__(self, dataDir=None, ignoreFiles=None):
        self.dataDir = None
        self.dataFiles = None
        if dataDir:
            self.set_data_dir(dataDir)
    
    def set_data_dir(self, dataDir, ignoreFiles=None):
        assert os.path.isdir(dataDir)
        ignoreFiles = set(ignoreFiles) if ignoreFiles else ()
        self.dataDir = dataDir
        
        dataFiles = [f for f in os.listdir(dataDir) \
                if os.path.isfile(os.path.join(dataDir, f))]
        self.dataFiles = filter(lambda f: f not in ignoreFiles, dataFiles)

    def get_data_files(self):
        if self.dataFiles is None:
            return None
        return list(self.dataFiles)

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
                d[f] = r
            except subprocess.CalledProcessError as e:
                d[f] = ''
        return d

