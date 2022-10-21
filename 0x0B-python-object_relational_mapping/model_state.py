#!/usr/bin/python3
"""Class of State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """The class of State"""
    