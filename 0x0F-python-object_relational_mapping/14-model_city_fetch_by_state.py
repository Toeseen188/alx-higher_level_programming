#!/usr/bin/python3
""" Write a script that prints all City objects from
the database hbtn_0e_14_usa
#Usage:./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for city, state in session.query(
            City, State).order_by(
                    City.id).filter(
                            State.id == City.state_id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
