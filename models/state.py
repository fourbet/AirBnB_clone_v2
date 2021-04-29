#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="delete", backref='state')

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Getter for cities when using FileStorage mode"""
            ret = []
            for c in models.storage.all(City).values():
                if c.state_id == self.id:
                    ret.append(c)
            return ret
