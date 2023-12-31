#!/usr/bin/python3
"""
Module script to list state passed as arg
"""


import sys
import MySQLdb

if __name__ == '__main__':
    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])

    cur = db.cursor()
    sql_cmd = "SELECT * FROM states WHERE name='{:s}'\
                ORDER BY id".format(name,)
    cur.execute(sql_cmd)
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
