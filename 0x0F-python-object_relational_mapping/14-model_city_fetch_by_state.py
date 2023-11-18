#!/usr/bin/python3
"""
Module that lists all City objects from db
"""

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import Session
    from sqlalchemy import (create_engine)
    from sqlalchemy import Table

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session.query(State, City)\
                              .filter(City.state_id == State.id)\
                              .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
