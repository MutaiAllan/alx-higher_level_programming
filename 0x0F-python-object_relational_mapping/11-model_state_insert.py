#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'\
            .format(sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(db)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    session.add(new_state)
    new_object = session.query(State).filter_by(name='Louisiana').first()
    print(new_object.id)
    session.commit()
