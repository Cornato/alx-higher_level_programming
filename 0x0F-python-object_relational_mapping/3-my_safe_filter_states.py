#!/usr/bin/python3
"""mysql state from dayae"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    dbnames = MySQLdb.connect(
        host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3]
    )

    query = dbnames.cursor()
    query.execute("SELECT * FROM states WHERE LIKE BINARY name = %s", [argv[4]])

    for i in query.fetchall():
        print(i)

    query.close()
    dbnames.close()
