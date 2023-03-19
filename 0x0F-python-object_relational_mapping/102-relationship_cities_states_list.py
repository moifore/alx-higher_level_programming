#!/usr/bin/python3
# Lists all City objects from the database bhtn_0e_101_usa.
# Usage: ./102-relationship_cities_states_list.py <mysql username> /
#                                   <mysql password> /
#                                   <database name>

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ = "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
            .format(sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Session = Session()

    session.add(City(name="San Francisco", state=State(name="California")))
    session.commit()

    for city in session.query(City).order_by(City.id):
        print("{}: {} -> {}" .format(city.id, city.name, city.state.name))
        
