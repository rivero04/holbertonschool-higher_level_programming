#!/usr/bin/python3
"""
script that changes the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa
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

    update_state2 = session.query(State).filter(State.id == 2).first()

    if update_state2 is not None:
        update_state2.name = "New Mexico"
        session.commit()
