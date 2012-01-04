#!/usr/bin/env python
#coding: utf-8

import sys

from engine import Searcher
from _config import dataDir, ignoreFiles
from _config import version

usage = """
usage: ldfind <word> [OPTIONS...]
  searches word from text files in ./data directory.
options
  -#: max mismatch count. 
  -c: counts the matched lines, instead of showing the lines.
  -i: ignores case.
  -w: word search.
  --version: shows version.
"""[1:-1]

def main():
    searcher = Searcher(dataDir, ignoreFiles)

    if not searcher.get_data_files():
        sys.exit("""
No files in ./data directory.
(Installation is not completed. Put some utf-8 text files 
in ./data directory.)
"""[1:-1])
    
    opts, args = [], []
    for a in sys.argv[1:]:
        if a.startswith("-"):
            if a in ("-h", "--help"):
                sys.stdout.write("%s\n" % usage)
                sys.exit(0)
            elif a == "--version":
                sys.stdout.write("ldfind %s\n" % version)
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

