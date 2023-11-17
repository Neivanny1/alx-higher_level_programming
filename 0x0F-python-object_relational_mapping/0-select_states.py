#!/usr/bin/python3
"""
Module script to list all states in db hbtn_0e_0_usa
"""
import sys
import MySQLdb
if __name__ == "__main__":
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    passwd = sys.argv[2]
    dbName = sys.argv[3]
    conn = MySQLdb.connect(host=host, port=port, user=user,
            passwd=passwd, db=dbName)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id;")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
