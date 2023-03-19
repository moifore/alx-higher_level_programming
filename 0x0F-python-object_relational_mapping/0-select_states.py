#!/usr/bin/python3

# Lists all states from btn_0e_0_usa database.

import sys
import MySQLdb

if __name__=="__main__":
    connect_db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], connect_db=sys.argv[3])
    c = connect_db.cursor()
    c.execute("SELECT * FROM 'states' ORDER BY 'states.id' ASC ")
    [print(state) for state in c.fetchall()]
