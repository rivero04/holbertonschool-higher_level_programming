#!/usr/bin/python3
"""
Lists all states from the `hbtn_0e_0_usa` database
with names starting with 'N', ordered by id.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access the database and get the status
    from the database.
    """

    user = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query, (state_name,))
  

# uso fetchall para recuperar los registros restantes que quedaron en cursor
    for row in cursor.fetchall():
        print(row)
