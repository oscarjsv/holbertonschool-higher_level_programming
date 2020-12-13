#!/usr/bin/python3
"""Lists all states"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        charset="utf8",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cur = conn.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id=cities.state_id ORDER BY id ASC"
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
