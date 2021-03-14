from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

import os

TESTING = os.environ.get("TESTING", False)

if TESTING:
    DATABASE_URI = os.environ["TESTING_DATABASE_URI"]
else:
    DATABASE_URI = os.environ["DATABASE_URI"]

engine = create_engine(DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def getDB():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



