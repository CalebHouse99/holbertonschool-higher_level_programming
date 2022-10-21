#!/usr/bin/python3
"""List all state objects from hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    first_row = []
    for state in session.query(State).order_by(State.id).all():
        first_row.append("{}: {}".format(state.id, state.name))
    if first_row[0] is not None:
        print(first_row[0])
    else:
        print("\n")
    session.close()
