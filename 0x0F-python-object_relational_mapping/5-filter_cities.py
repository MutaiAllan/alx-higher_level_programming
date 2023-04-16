#!/usr/bin/python3
""" Takes a name of a state as an argument and lists all cities in it. """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities INNER JOIN states ON \
            states.id=cities.state_id WHERE states.name LIKE BINARY \
            %(states_name)s \
            ORDER BY cities.id ASC", {'states_name': sys.argv[4]})
    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))
