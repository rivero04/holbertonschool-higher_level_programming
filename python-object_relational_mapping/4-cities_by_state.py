#!/usr/bin/python3
"""
Lists all cities from the `hbtn_0e_4_usa` database, ordered by id.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the cities
    from the database.
    """

    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name,states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC""")

# Uso de fetchall para recuperar los registros restantes q quedaron en cursor
    for row in cursor.fetchall():
        print(row)
