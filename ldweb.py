#!/usr/bin/env python
#coding: utf-8

import os
import subprocess
import threading

import bottle
assert map(int, bottle.__version__.split(".")) >= [0, 10, 0]

from bottle import run, template, TEMPLATE_PATH
from bottle import route, request, static_file

from engine import Searcher
from _config import dataDir, ignoreFiles, moduleDir
from _config import version

templateDir = os.path.join(moduleDir, "view")
TEMPLATE_PATH.append(templateDir)

searcher = Searcher(dataDir, ignoreFiles)

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=os.path.join(moduleDir, "static"))

@route('/', method='get')
def index_get():
    if not searcher.get_data_files():
        title ="Installation Error"
        text = """
No files in directory "%(dataDir)s".
Installation is not completed. 
Put some utf-8 text files in directory "%(dataDir)s".
"""[1:-1] % { 'dataDir' : dataDir }

        return template('errormessage', title=title, text=text)
    
    tbl = dict((k, []) for k in searcher.get_data_files())
    return template('index', result_table=tbl, query_string=None,
            option_wholeword=None, option_approximate=None, option_ignorecase=1)

@route('/', method='post')
def index_post():
    query_string = request.forms.get('query', '')
    wholeword = 1 if request.forms.get('wholeword', 'off') == 'on' else 0
    approximate = int(request.forms.get('approximate', '0'))
    ignorecase = 1 if request.forms.get('ignorecase', 'off') == 'on' else 0
    if not query_string:
        tbl = dict((k, []) for k in searcher.get_data_files())
        return template('index', result_table=tbl, query_string=None,
                option_wholeword=wholeword, option_approximate=approximate, option_ignorecase=ignorecase)
    
    options = []
    if wholeword: options.append("-w")
    if approximate: options.append("-%d" % approximate)
    if ignorecase: options.append("-i")
    
    d = searcher.search(query_string, options)
    result_table = {}
    for k, v in d.iteritems():
        result_table[k.decode('utf-8')] = \
                [L.decode('utf-8') for L in filter(None, v.split('\n'))]
    
    return template('index', 
            result_table=result_table, query_string=query_string, 
            option_wholeword=wholeword, option_approximate=approximate, option_ignorecase=ignorecase)

usage = """
usage: ldweb [OPTIONS...]
options
  -b <browser>: browser. default is %(browserCommand)s.
  -b -: don't invoke a browser.
  -p <portnum>: port number. default is %(port)d.
  --version: shows version.
"""[1:-1]

def main():
    import sys
    import getopt
    
    port = 8081
    browserCommand = "firefox"
    
    opts, args = getopt.gnu_getopt(sys.argv[1:], "b:p:h", [ "version" ])
    for k, v in opts:
        if k == "-h":
            sys.stdout.write("%s\n" % (usage % locals()))
            sys.exit(0)
        elif k == "-b":
            if v == '-':
                browserCommand = None
            browserCommand = v
        elif k == "-p":
            port = int(v, 10)
        elif k == "--version":
            sys.stdout.write("ldweb %s\n" % version)
            sys.exit(0)
        else:
            assert False
    
    if browserCommand:
        def invoke_browser(): 
            subprocess.call([browserCommand, "http://localhost:%d" % port])
        threading.Timer(0.1, invoke_browser).start()
    
    bottle.debug(True)
    try:
        run(host='localhost', port=port)
    except IOError:
        sys.stderr.write("warning: port %d is already used (locdic/web.py already running?)\n" % port)

if __name__ == '__main__':
    main()
