from sqlalchemy import Column, String, Boolean, Integer
from sqlalchemy.ext.declarative import declarative_base
from ..database import Base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, index=True)
    name = Column(String)
    goal = Column(String)
    onboarded = Column(Boolean, default=False)


class Config(Base):
    __tablename__ = "configs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    value = Column(String, nullable=False)
