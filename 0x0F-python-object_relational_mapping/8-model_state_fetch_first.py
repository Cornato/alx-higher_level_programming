#!/usr/bin/python3
"""mysql state from dayae"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import *

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1], argv[2], argv[3]),
        pool_pre_ping=True,
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    row = session.query(State).order_by(State.id).first()

    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")

    session.close()
