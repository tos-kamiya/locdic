#coding: utf-8

import os
import subprocess

r = subprocess.check_output(["nkf", "-u", "gene.txt"])
lines = [L.rstrip() for L in r.split("\n")]

with open("gene.utf8", "wb") as f:
    for L1, L2 in zip(lines[::2], lines[1::2]):
        f.write(L1 + "\t" + L2 + "\n")

os.rename("gene.txt", "gene.txt.original")

