#!/usr/bin/python3
"""
Module script to list state passed as arg
"""


import sys
import MySQLdb

if __name__ == '__main__':
    name = sys.argv[4]
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host=host, port=port, user=user,
                         passwd=passwd, db=database)
    cur = db.cursor()

    _query = "SELECT * FROM states WHERE name='{}' ORDER BY id;".format(name)
    cur.execute(_query)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
