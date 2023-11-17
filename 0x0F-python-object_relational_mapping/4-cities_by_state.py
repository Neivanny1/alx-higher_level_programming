#!/usr/bin/python3
"""
Module to List all states from db
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
    cur.execute("""SELECT cities.id, cities.name, states.name As states_name
                FROM cities INNER JOIN states ON
                cities.state_id=states.id;""")
    cities = cur.fetchall()
    for city in cities:
        print(city)
    cur.close()
    db.close()
