#!/usr/bin/python3
"""mysql state from dayae"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    dbnames = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    query = dbnames.cursor()
    query.execute("SELECT cities.id, cities.name, states.name\
                  FROM cities INNER JOIN states ON states.id=cities.state_id")

    for i in query.fetchall():
        print(i)

    query.close()
    dbnames.close()
