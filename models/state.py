#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state', cascade='delete')
    else:
        name = ""

        @property
        def cities(self):
            """return list of city objects from storage
               lined to the current state in self"""
            city_list = []
            cities = models.storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
