#!/usr/bin/python3
"""mysql state from dayae"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3], charset="utf8")

    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")

    rows = c.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)

    c.close()
    db.close()
