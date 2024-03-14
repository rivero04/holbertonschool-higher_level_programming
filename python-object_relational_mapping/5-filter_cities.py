#!/usr/bin/python3
"""
Lists all cities from a specified state in the
`hbtn_0e_4_usa` database, ordered by id.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the specified state in the database.
    """

    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("""SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC""", (state_name,))

# Uso de fetchall para recuperar los registros restantes q quedaron en cursor
    if cursor.fetchall():
        print(", ".join([row[0] for row in cursor.fetchall()]))
