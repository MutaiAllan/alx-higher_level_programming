#!/usr/bin/python3
"""
Takes a name as an argument and displays values
in the 'states' table of hbtn_0e_0_usa that matches.
Free from SQLi.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %(name)s \
            ORDER BY states.id ASC", {'name': sys.argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
