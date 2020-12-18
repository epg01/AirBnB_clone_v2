#!/usr/bin/python3
""" Place Module for HBNB project
    Place inherits from BaseModel
    and Base (respect the order)
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
import os


place_amenity = Table('place_amenity', Base.metadata, Column(
    'place_id', String(60), ForeignKey('places.id'), primary_key=True,
    nullable=False), Column(
    'amenity_id', String(60),
    ForeignKey('amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """ A place to stay
        Place inherits from BaseModel
        and Base (respect the order)
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="all,delete")
        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            back_populates="place_amenities", viewonly=False)

    @property
    def reviews(self):
        """ the getter method for the cities """
        from models import storage
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            return
        reviews = []
        filestorage = storage.FileStorage_objects
        for key, value in filestorage.items():
            lista = key.split()
            if lista[0] == "Review":
                if value.to_dict()["place_id"] == self.id:
                    reviews.append(value)
        return reviews

    # @property
    # def amenities(self):
    #     """ the getter method for the cities """
    #     from models import storage
    #     if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    #         return
    #     amenities = []
    #     filestorage = storage.FileStorage_objects
    #     for key, value in filestorage.items():
    #         lista = key.split()
    #         if lista[0] == "Amenity":
    #             if value.to_dict()["place_amenities"] == self.id:
    #                 amenities.append(value)
    #     return amenities
    # city_id = ""
    # user_id = ""
    # name = ""
    # description = ""
    # number_rooms = 0
    # number_bathrooms = 0
    # max_guest = 0
    # price_by_night = 0
    # latitude = 0.0
    # longitude = 0.0
    # amenity_ids = []
