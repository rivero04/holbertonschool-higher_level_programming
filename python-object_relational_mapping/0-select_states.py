#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

user = sys.argv[1]
password = sys.argv[2]
db_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=password, db=db_name)
cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

print("id | name")
print("---|------")
for row in cursor.fetchall(): #uso fetchall para recuperar los registros restantes que quedaron en cursor
    print(f"{row[0]} | {row[1]}")