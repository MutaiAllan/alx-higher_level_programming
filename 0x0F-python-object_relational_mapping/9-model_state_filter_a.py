#!/usr/bin/python3
"""
Lists all State objects that contain the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = "mysql+mysqldb://{}:{}@localhost:3306/{}"\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.contains('a'))
    for state in states:
        print('{0}: {1}'.format(state.id, state.name))
