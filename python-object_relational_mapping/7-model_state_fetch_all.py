#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlahcmely.orm import sessionmaker
from models_state import Base, State


if __name__ == '__main__':
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]


engine = create_engine(
    f"mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}"
)

Base.metadata.create_all(engine)
Sessions = sessionmaker(bind=engine)


session = Session()
