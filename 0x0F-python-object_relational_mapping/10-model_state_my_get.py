#!/usr/bin/python3
"""
Prints the State object with the name passed as argument
from the database hbtn_oe_6_usa.
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
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is not None:
        print('{0}'.format(state.id))
    else:
        print("Not found")
