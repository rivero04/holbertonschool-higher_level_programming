#!/usr/bin/python3
"""
script that lists all State objects containing the letter 'a'
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    user = argv[1]
    password = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a')).\
        order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
