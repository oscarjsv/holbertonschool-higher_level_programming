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
        "SELECT cities.id, cities.name, states.name FROM states\
            INNER JOIN cities ON states.id=cities.state_id\
                 WHERE states.name = %s ORDER BY cities.id ASC", (argv[4], )
    )
    rows = cur.fetchall()
    print(", ".join([row[1] for row in rows]))
    cur.close()
    conn.close()
