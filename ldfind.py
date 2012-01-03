#!/usr/bin/python
#coding: utf-8

import os
import sys

from engine import Searcher

programDir = os.path.split(__file__)[0]
dataDir = os.path.join(programDir, "data")

usage = """
usage: ldfind <word> [OPTIONS...]
  searchs word from text files in ./data directory.
options
  -#: max mismatch count. 
  -c: counts the matched lines, instead of showing the lines.
  -i: ignores case.
  -w: word search.
"""[1:-1]

def main():
    searcher = Searcher(dataDir)
    
    opts, args = [], []
    for a in sys.argv[1:]:
        if a.startswith("-"):
            if a in ("-h", "--help"):
                sys.stdout.write("%s\n" % usage)
                sys.exit(0)
            opts.append(a)
        else:
            args.append(a)
    
    if len(args) >= 2:
        sys.exit("too many command-line arguments")
    
    d = searcher.search(args[0], options=(opts if opts else None))
    
    output = sys.stdout
    for f, r in sorted(d.iteritems()):
        output.write("%s:\n" % f)
        output.write("%s\n" % r)

if __name__ == '__main__':
    main()

