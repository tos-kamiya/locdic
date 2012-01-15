#coding: utf-8

import os
import sys
import sqlite3
import glob
import re
import datetime

from _config import historyDir

def add_to_history(word, options, thetime, accessfrom):
    dateStr = thetime.strftime("%Y-%m-%d")
    timeStr = thetime.strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(historyDir):
        os.makedirs(historyDir, mode=0755)
        
    dbFile = os.path.join(historyDir, "log-" + dateStr + ".sqlite3")
    con = sqlite3.connect(dbFile, isolation_level=None)
    try:
        try:
            sql = u"create table history (word text, options text, time text, accessfrom text)"
            con.execute(sql)
        except:
            pass # maybe the table already exists
        sql = u"insert into history values (?, ?, ?, ?)"
        con.execute(sql, (u'' + word, u' '.join(sorted(options)), u'' + timeStr, u'' + accessfrom))
    finally:
        con.close()

def __get_history(dbFile):
    con = sqlite3.connect(dbFile)
    try:
        cur = con.cursor()
        return [history for history in cur.execute(u"select * from history")]
    finally:
        con.close()

def get_history_of_day(day):
    dateStr = day.strftime("%Y-%m-%d")
    dbFile = os.path.join(historyDir, "log-" + dateStr + ".sqlite3")
    if not os.path.isfile(dbFile):
        return []
    return __get_history(dbFile)

def get_history_iter(reverse=True):
    pat = re.compile("^log-([0-9]+)-([0-9]+)-([0-9]+).sqlite3$")
    dbFiles = glob.glob(os.path.join(historyDir, "log-*.sqlite3"))
    for dbFile in sorted(dbFiles, reverse=reverse):
        f = os.path.split(dbFile)[1]
        m = pat.match(f)
        y, m, d = [int(m.group(i)) for i in (1, 2, 3)]
        day = datetime.date(y, m, d)
        history = __get_history(dbFile)
        if reverse:
            history = sorted(history, key=lambda qota: qota[2], reverse=True)
        yield day, history
        
def main():
    for day, history in get_history_iter():
        for item in history:
            sys.stdout.write("%s\n" % '\t'.join(item))
        
if __name__ == '__main__':
    main()
