#!/usr/bin/python3
# List all State objects from the database hbtn_0e_6_usa.
# Usage: ./10-model_state_my_get.py <mysql username> /
#                                   <mysql password> /
#                                   <database name>

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ = "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Session = Session()

    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break
        if found is False:
            print("Not found")

