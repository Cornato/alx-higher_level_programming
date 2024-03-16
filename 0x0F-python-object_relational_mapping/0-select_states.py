#!/usr/bin/python3
"""mysql state from dayae"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    
    dbnames = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], dbnames=argv[3])
    
    query = dbnames.cursor()
    query.execute("SELECT * FROM states")
    
    rows = query.fetchall()
    for i in rows:
        print(i)
        
    query.close()
    dbnames.close()
