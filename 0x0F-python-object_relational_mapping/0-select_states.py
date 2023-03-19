#!/usr/bin/python3

# Lists all states from btn_0e_0_usa database.

import sys
import MySQLdb

if __name__=="__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM 'states' ORDER BY 'states.id' ASC ")
    [print(state) for state in c.fetchall()]
