#!/usr/bin/python3
""" A class definition of a City, that inherit
from Base. Link to the MySql table Cities
# class attribute id that represents a column of an auto-generated,
    unique integer, can’t be null and is a primary key
# class attribute name that represents a column of a string with
    maximum 128 characters and can’t be null
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base
Base = declarative_base()


class City(Base):
    """ class City that mapped to cities db """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
