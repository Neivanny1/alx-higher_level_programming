#!/usr/bin/python3
"""
Module to list all cities from the city passed as an argument
"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost',
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.name FROM cities INNER JOIN
                   states ON cities.state_id=states.id
                   WHERE states.name=%s;""", (sys.argv[4],))
    cities = cur.fetchall()
    print(", ".join([city[0] for city in cities]))
    cur.close()
    db.close()
