#coding: utf-8

import glob
import sys

# synset_offset  lex_filenum  ss_type  w_cnt  word  lex_id  [word  lex_id...]  p_cnt  [ptr...]  [frames...]  |   gloss 

wordnetFiles = glob.glob("data.*")

if len(wordnetFiles) == 0:
    sys.exit("error: no file found")

with open("wordnet.utf8", "w") as outp:
    for wf in wordnetFiles:
        with open(wf, "r") as inp:
            for li, L in enumerate(inp):
                try:
                    L = L.rstrip()
                    if L.find('|') < 0: continue
                    wordsStr, description = L.split('|')
                    fields = wordsStr.split(' ')
                    ss_type = fields[2]
                    countOfWords = int(fields[3], 16)
                    words = [fields[4 + i * 2] for i in range(countOfWords)]
                    words = [s.replace('_', ' ') for s in words]
                    outp.write("%s\t%s %s\n" % (", ".join(words), ss_type, description))
                except:
                    sys.exit("error: converting failure, file %s line %d" % (wf, li + 1))