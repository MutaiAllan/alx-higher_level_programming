#!/usr/bin/python3
""" Defines a class City. """
from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    Attributes:
        __tablename__: table name.
        id: id of the object.
        name: name of the object.
        state_id: The State of the city.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
