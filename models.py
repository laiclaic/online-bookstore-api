# model file to create classes

from typing import Union, Optional
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# sqlalchemy engine
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# base class for orm models
Base = declarative_base()

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True)
    title = Column(String, index=True)
    author = Column(String, index=True) 
    classification = Column(String, index=True)
    publisher = Column(String, index=True)
    desc = Column(String, nullable=True)
    price = Column(Float)

# create tables
Base.metadata.create_all(bind=engine)