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
        
        ignoreFiles = list(ignoreFiles) if ignoreFiles else []
        self.dataDir = dataDir
        
        dataFiles = [f for f in os.listdir(dataDir) \
                if os.path.isfile(os.path.join(dataDir, f))]
        ifs = []
        for i in ignoreFiles:
            ifs.extend(glob.glob(os.path.join(dataDir, i)))
        ifs = [os.path.split(p)[1] for p in ifs]
        self.ignoreFiles = sorted(set(ifs))
        self.dataFiles = [f for f in dataFiles if f not in self.ignoreFiles]

    def get_data_files(self):
        if self.dataFiles is None:
            return None
        return list(self.dataFiles)

    def search_raw(self, query, options=None):
        assert self.dataDir is not None
        cmdLine = ["tre-agrep", query]
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

    def search(self, query, options=None):
        d = self.search_raw(query, options)
        return self.decode_result(d)

    @staticmethod
    def decode_result(d):
        return dict((f, (result.decode('utf-8') if result else result)) \
                for f, result in d.items())
    
    @staticmethod
    def sort_result_by_column(d, remove_position_str=False, delimiter='\t'):
        """
        Sorts the result of search_raw() by number of the column where 
        the pattern is found.
        The argument should be a return value of search_raw()
        with a keyword argument options including '--show-position'.
        For example:
        > s = Searcher(....)
        > d = s.search_raw("key word", options=['--show-position'])
        > sd = s.sort_result_by_column(d)
        """
        
        sortedD = {}
        for f, result in d.items():
            lines = filter(None, (L.rstrip() for L in result.split('\n')))
            candls = []
            for L in lines:
                i = L.find(':'); assert i >= 0
                posStr, text = L[:i], L[i+1:]
                startPos = int(posStr.split("-")[0], 10)
                columnNumber = text[:startPos].count(delimiter)
                candls.append((columnNumber, (text if remove_position_str else L)))
            candls.sort()
            sortedD[f] = "\n".join(ls for c, ls in candls) + "\n"
        return sortedD
        