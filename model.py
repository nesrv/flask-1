import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:aatpotug_22@localhost/database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people2"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)


Base.metadata.create_all(bind=engine)
