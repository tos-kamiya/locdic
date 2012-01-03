#coding: utf-8

import os

import bottle
from bottle import Bottle, run, template, TEMPLATE_PATH
from bottle import request

from engine import Searcher
from config import dataDir, ignoreFiles, moduleDir

templateDir = os.path.join(moduleDir, "view")
TEMPLATE_PATH.append(templateDir)

searcher = Searcher(dataDir, ignoreFiles)

app = Bottle()

@app.route('/', method='get')
def index_get():
    return template('index', result_table=None, query_string=None)

@app.route('/', method='post')
def index_post():
    query_string = request.forms.get('query')
    
    d = searcher.search(query_string)
    result_table = {}
    for k, v in d.iteritems():
        result_table[k.decode('utf-8')] = \
                [L.decode('utf-8') for L in filter(None, v.split('\n'))]
    
    return template('index', 
            result_table=result_table, query_string=query_string)

usage = """
usage: web [OPTIONS...]
options
  -b <browser>: browser. default is %(browserCommand)s.
  -p <portnum>: port number. default is %(port)d.
"""[1:-1]

def main():
    import sys
    import getopt
    
    port = 8081
    browserCommand = "firefox"
    
    opts, args = getopt.gnu_getopt(sys.argv[1:], "b:p:h")
    for k, v in opts:
        if k == "-h":
            sys.stdout.write("%s\n" % (usage % locals()))
            sys.exit(0)
        elif k == "-b":
            browserCommand = v
        elif k == "-p":
            port = int(v, 10)
        else:
            assert False
    
    if not searcher.get_data_files():
        sys.exit("""
No files in ./data directory.
(Installation is not completed. Put some utf-8 text files 
in ./data directory.)
"""[1:-1])

    bottle.debug(True)
    run(app, host='localhost', port=8081)
    os.system("%s http://localhost:%d" % (browserCommand, port))

if __name__ == '__main__':
    main()
