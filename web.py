#coding: utf-8

import os

import bottle
from bottle import Bottle, run, template, TEMPLATE_PATH
from bottle import request

from engine import Searcher

programDir = os.path.split(__file__)[0]
dataDir = os.path.join(programDir, "data")
templateDir = os.path.join(programDir, "view")
TEMPLATE_PATH.append(templateDir)

app = Bottle()

@app.route('/', method='get')
def index_get():
    return template('index', result_table=None, query_string=None)

@app.route('/', method='post')
def index_post():
    query_string = request.forms.get('query')
    searcher = Searcher(dataDir)
    
    d = searcher.search(query_string)
    result_table = {}
    for k, v in d.iteritems():
        result_table[k.decode('utf-8')] = \
                [L.decode('utf-8') for L in filter(None, v.split('\n'))]
    
    return template('index', 
            result_table=result_table, query_string=query_string)

bottle.debug(True)
run(app, host='localhost', port=8081)

