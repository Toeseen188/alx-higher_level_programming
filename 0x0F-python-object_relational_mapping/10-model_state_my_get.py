#!/usr/bin/python3
""" a script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
#Usage: ./10-model_state_my_get.py root root hbtn_0e_6_usa state
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    search = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    found = False
    for state in session.query(State):
        if state.name == str(search):
            print("{}".format(state.id))
            found = True
    if found is False:
        print("Not found")
    session.close()
