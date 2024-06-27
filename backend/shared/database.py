import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

def get_session() -> object:
    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/{}'.format(
            os.getenv("USER_SESSION"), os.getenv("PASSWORD_SESSION"),
            os.getenv("HOST_SESSION"), os.getenv("PORT_SESSION"),
            os.getenv("DATABASE_SESSION")
        )
    )
    Session = sessionmaker(bind=engine)
    return Session()