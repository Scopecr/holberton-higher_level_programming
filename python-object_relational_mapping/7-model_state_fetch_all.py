#!/usr/bin/python3
"""Lists all states objects from the database"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usaername, password, db_name = sys.arg[1], sys.argv[2], sys.arg[3]
    engine =  create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}')
    
    session = sessionmaker(bind=engine)
    session = session()
    
    states = session.query(State).order_by(State.id).all()
    
    for state in states:
        print(f"{state.id}: {states.name}")
                            