#!/usr/bin/python3
""" Prints all City objects from the daatabase hbtn_0e_14_usa. """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City, State).join(State)
    for city, state in cities.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
