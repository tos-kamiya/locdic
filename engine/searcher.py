#coding: utf-8

import os
import subprocess
import glob

class Searcher:
    def __init__(self, dataDir=None, ignoreFiles=None):
        self.dataDir = None
        self.dataFiles = None
        if dataDir:
            self.set_data_dir(dataDir, ignoreFiles)
    
    def set_data_dir(self, dataDir, ignoreFiles=None):
        if not os.path.isdir(dataDir): return
        
        ignoreFiles = list(ignoreFiles)
        self.dataDir = dataDir
        
        dataFiles = [f for f in os.listdir(dataDir) \
                if os.path.isfile(os.path.join(dataDir, f))]
        ifs = []
        for i in ignoreFiles:
            ifs.extend(glob.glob(os.path.join(dataDir, i)))
        ifs = [os.path.split(p)[1] for p in ifs]
        self.ignoreFiles = sorted(set(ifs))
        self.dataFiles = filter(lambda f: f not in self.ignoreFiles, dataFiles)

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

