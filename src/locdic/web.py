#!/usr/bin/env python
#coding: utf-8

import os
import time
import threading
import cgi
import datetime

import bottle

bottleVersion = tuple([int(s) for s in bottle.__version__.split(".")[:2]])

from bottle import run, template, TEMPLATE_PATH
from bottle import route, request, static_file

from engine import Searcher
from _config import dataDir, ignoreFiles, moduleDir, historyDir
from _config import version
from history import *

templateDir = os.path.join(moduleDir, "view")
TEMPLATE_PATH.append(templateDir)

searcher = Searcher(dataDir, ignoreFiles)

initialOptions = {}
optionHistory = None

pathPattern = "<filename:path>" if bottleVersion >= (0, 10) else ":filename#.+#"

@route('/static/' + pathPattern)
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
            option_wholeword=initialOptions.get('wholeword'), 
            option_approximate=initialOptions.get('approximate'), 
            option_ignorecase=initialOptions.get('ignorecase', True))

def marking(line):
    i = line.find(":")
    posStr = line[:i]
    text = line[i + 1:]
    startPosStr, endPosStr = posStr.split("-")
    startPos = int(startPosStr, 10)
    endPos = int(endPosStr, 10)
    u8Text = text.encode('utf-8')
    return cgi.escape(u8Text[:startPos].decode('utf-8'), True) + \
            '<font color="red">' + \
            cgi.escape(u8Text[startPos:endPos].decode('utf-8'), True) + \
            '</font>' + \
            cgi.escape(u8Text[endPos:].decode('utf-8'), True)

queryOptionSet = set(["-i", "-w"] + ["-%d" % i for i in xrange(0, 10)])

@route('/', method='post')
def index_post():
    remote_addr = request.remote_addr
    query_string = request.forms.get('query', '')
    wholeword = request.forms.get('wholeword', 'off') == 'on'
    approximate = int(request.forms.get('approximate', '0'))
    ignorecase = request.forms.get('ignorecase', 'off') == 'on'
    if not query_string:
        tbl = dict((k, []) for k in searcher.get_data_files())
        return template('index', result_table=tbl, query_string=None,
                option_wholeword=wholeword, option_approximate=approximate, option_ignorecase=ignorecase)
    
    options = ["--show-position"]
    if wholeword: options.append("-w")
    if approximate: options.append("-%d" % approximate)
    if ignorecase: options.append("-i")
    
    if optionHistory:
        d = datetime.datetime.today()
        add_to_history(query_string, [opt for opt in options if opt in queryOptionSet], 
                d, remote_addr)
    
    d = searcher.search_raw(query_string, options)
    d = searcher.sort_result_by_column(d, remove_position_str=False)
    d = searcher.decode_result(d)
    result_table = {}
    for k, v in d.items():
        result_table[k] = \
                [marking(L) for L in filter(None, v.split('\n'))]
    
    return template('index', 
            template_settings={'noescape': True},
            result_table=result_table, query_string=cgi.escape(query_string, True),
            option_wholeword=wholeword, option_approximate=approximate, option_ignorecase=ignorecase)

dayPattern = "<day:int>" if bottleVersion >= (0, 10) else ":day#[0-9]+"

@route('/history/' + dayPattern)
def history(day):
    y = day // 10000
    m = day % 10000 // 100
    d = day % 100
    day = datetime.date(y, m, d)
    history = get_history_of_day(day)
    return template('history', date="%04d/%02d/%02d" % (y, m, d), history=history)

usage = """
usage: web [OPTIONS...]
options
  -I: turns off ignore-case option.
  -p <portnum>: port number. default is %(port)d.
  -s: web server (only) mode. not try to invoke a browser.
  -w: turns on word-match option.
  --no-history: do not record querys.
  --version: shows version.
"""[1:-1]

def main():
    global optionHistory
    
    import sys
    import getopt
    
    port = 8081
    optionServerMode = None
    optionMismatch = None
    optionIgnoreCase = None
    optionWholeWordMatch = None
    optionHistory = True
    
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if re.match("^-[0-9]$", a):
            optionMismatch = int(a[1:])
            del a[i]
            break
     
    opts, args = getopt.gnu_getopt(args, "hiIp:sw", [ "version", "no-history" ])
    for k, v in opts:
        if k == "-h":
            sys.stdout.write("%s\n" % (usage % locals()))
            sys.exit(0)
        elif k == "-p":
            port = int(v, 10)
        elif k == "-s":
            optionServerMode = True
        elif k == "--version":
            sys.stdout.write("locdic.web %s\nsee http://www.remics.org/locdic/ for more information.\n" % version)
            sys.exit(0)
        elif k == "-i":
            optionIgnoreCase = True
        elif k == "-I":
            optionIgnoreCase = False
        elif k == "-w":
            optionWholeWordMatch = True
        elif k == "--no-history":
            optionHistory = False
        else:
            assert False
    
    if optionWholeWordMatch: initialOptions['wholeword'] = True
    if optionIgnoreCase: initialOptions['ignorecase'] = True
    if optionMismatch: initialOptions['approximate'] = optionMismatch
    
    bottle.debug(True)

    if optionServerMode:
        run(host='localhost', port=port)
    else:    
        serverThread = threading.Thread(target=run, kwargs={ 'host': 'localhost', 'port': port })
        serverThread.daemon = not optionServerMode # not a daemon if server mode.
        serverThread.start()
        time.sleep(0.1) # waits server thread get ready.
        
        if not serverThread.is_alive():
            message = "error: can't invoke a web server. (another locdic/web.py is already running?, or port %d is used by the other program?)\n" % port
            try:
                import browserwindow
                browserwindow.error_dialog(message)
                sys.exit(1)
            except:
                sys.exit(message)
            
        import browserwindow # this module packages PyGtk and pywebkitgtk (not standard lib, platform depends) so import when it is really needed.
        url = "http://localhost:%d" % port
        browserwindow.start_event_loop(url, title="LocDic", size=(0.33, 0.8))

    sys.exit(0)

if __name__ == '__main__':
    main()
