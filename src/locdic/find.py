#!/usr/bin/env python
#coding: utf-8

import sys

from engine import Searcher
from _config import dataDir, ignoreFiles
from _config import version

usage = """
usage: find <word> [OPTIONS...]
  searches word from text files in ./data directory.
options
  -#: max mismatch count. 
  -c: counts the matched lines, instead of showing the lines.
  -i: ignores case.
  -w: word match.
  --color: shows positions where word appears in each line.
  --sort-by-column: sorts results by number of column where 
    the searched word appears.
  --version: shows version. 
"""[1:-1]

def main():
    if len(sys.argv) == 1:
        sys.stdout.write("%s\n" % usage)
        sys.exit(0)
        
    searcher = Searcher(dataDir, ignoreFiles)

    if not searcher.get_data_files():
        sys.exit("""
No files in ./data directory.
(Installation is not completed. Put some utf-8 text files 
in ./data directory.)
"""[1:-1])
    
    optionSortByColumn = None
    showPositionIsAppeared = False
    
    opts, args = [], []
    for a in sys.argv[1:]:
        if a.startswith("-"):
            if a in ("-h", "--help"):
                sys.stdout.write("%s\n" % usage)
                sys.exit(0)
            elif a == "--version":
                sys.stdout.write("locdic.find %s\nsee http://www.remics.org/locdic/ for more information.\n" % version)
                sys.exit(0)
            elif a == "--sort-by-column":
                optionSortByColumn = True
            else:
                if a == "--show-position":
                    showPositionIsAppeared = True
                opts.append(a)
        else:
            args.append(a)
    
    if len(args) >= 2:
        sys.exit("error: too many command-line arguments")
        
    if optionSortByColumn and showPositionIsAppeared:
        sys.exit("error: options are mutually exclusive: --sort-by-column, --show-position")
    
    if optionSortByColumn:
        d = searcher.search_raw(args[0], options=opts + ["--show-position"])
        d = searcher.sort_result_by_column(d, remove_position_str=True)
        d = searcher.decode_result(d)
    else:
        d = searcher.search(args[0], options=opts)
    
    output = sys.stdout
    for f, r in sorted(d.items()):
        output.write("%s:\n" % f)
        output.write("%s\n" % r)

if __name__ == '__main__':
    main()

