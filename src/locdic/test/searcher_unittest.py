#coding: utf-8

import unittest
import os
import shutil
import sys

sys.path.append("..")
from engine import Searcher

moduleDir = os.path.split(__file__)[0]
testTempDir = os.path.join(moduleDir, "tmp")

class SearcherTest(unittest.TestCase):
    def setUp(self):
        if not os.path.exists(testTempDir):
            os.makedirs(testTempDir)

    def tearDown(self):
        shutil.rmtree(testTempDir, ignore_errors=True)
    
    def testDictSearch(self):
        dictFile = "sampledict.txt"
        dictFilePath = os.path.join(testTempDir, dictFile)
        with open(dictFilePath, "wb") as f:
            f.write("%s\t%s\n" % ("abc", "the first 3 characters"))
        try:
            searcher = Searcher(testTempDir)
            self.assertTrue(dictFile in searcher.get_data_files())
        finally:
            os.remove(dictFilePath)
        
    def testDictSearchWithIgnoreFiles(self):
        dictFile = "sampledict.txt"
        dictFilePath = os.path.join(testTempDir, dictFile)
        with open(dictFilePath, "wb") as f:
            f.write("%s\t%s\n" % ("abc", "the first 3 characters"))
        try:
            searcher = Searcher(testTempDir, ignoreFiles=["*.txt"])
            self.assertTrue(dictFile not in searcher.get_data_files())
        finally:
            os.remove(dictFilePath)
        
    def testSearch(self):
        dictFile = "sampledict.txt"
        dictFilePath = os.path.join(testTempDir, dictFile)
        with open(dictFilePath, "wb") as f:
            f.write("%s\t%s\n" % ("abc", "the first 3 characters"))
        try:
            searcher = Searcher(testTempDir)
            d = searcher.search("abc")
            self.assertTrue(dictFile in d)
            self.assertTrue(d[dictFile].startswith("abc\t"))
        finally:
            os.remove(dictFilePath)
        
    def testSearchWholeWord(self):
        dictFile = "sampledict.txt"
        dictFilePath = os.path.join(testTempDir, dictFile)
        with open(dictFilePath, "wb") as f:
            f.write("%s\t%s\n" % ("abc", "the first 3 characters"))
        try:
            searcher = Searcher(testTempDir)
            d = searcher.search("abc", options=["-w"])
            self.assertTrue(dictFile in d)
            self.assertTrue(d[dictFile].startswith("abc\t"))
            d = searcher.search("ab", options=["-w"])
            self.assertTrue(dictFile in d)
            self.assertTrue(not d[dictFile])
        finally:
            os.remove(dictFilePath)
        
    def testSort(self):
        dictFile = "sampledict.txt"
        dictFilePath = os.path.join(testTempDir, dictFile)
        with open(dictFilePath, "wb") as f:
            f.write("%s\t%s\n" % ("abc", "the 3 characters before 'def'"))
            f.write("%s\t%s\n" % ("def", "the 3 characters after 'abc'"))
        try:
            searcher = Searcher(testTempDir)
            normalD = searcher.search("def")
            self.assertTrue(dictFile in normalD)
            self.assertTrue(normalD[dictFile].startswith("abc\t"))
            d = searcher.search_raw("def",options=["--show-position"])
            d = searcher.sort_result_by_column(d, remove_position_str=True)
            sortedD = searcher.decode_result(d)
            self.assertTrue(dictFile in sortedD)
            self.assertTrue(sortedD[dictFile].startswith("def\t"))
        finally:
            os.remove(dictFilePath)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()