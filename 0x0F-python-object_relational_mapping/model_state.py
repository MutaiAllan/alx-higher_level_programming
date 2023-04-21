#!/usr/bin/python3
"""
Contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Inherits from case class. """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
