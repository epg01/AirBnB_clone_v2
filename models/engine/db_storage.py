#!/usr/bin/python3
""" New engine """
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, MetaData
from models.base_model import BaseModel, Base
import os
import json
from models.place import Place
from models.review import Review
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class DBStorage:
    """ class DBStorage """

    __engine = None
    __session = None

    def __init__(self):
        """ the init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.environ.get("HBNB_MYSQL_USER"),
            os.environ.get("HBNB_MYSQL_PWD"),
            os.environ.get("HBNB_MYSQL_HOST"),
            os.environ.get("HBNB_MYSQL_DB")),
            pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == 'test':
            Base.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """ class all
        """
        list_aux = {}
        aux_classes = {'State': State, 'Place': Place, 'City': City,
                       'Amenity': Amenity, 'Review': Review, 'User': User}
        if cls:
            for row in self.__session.query(aux_classes[cls]):
                key = "{}.{}".format(row.__class__.__name__, row.id)
                list_aux[key] = row
        else:
            for rows in aux_classes:
                for row in self.__session.query(aux_classes[rows]):
                    key = "{}.{}".format(row.__class__.__name__, row.id)
                    list_aux[key] = row
        return list_aux

    def new(self, obj):
        """ add the object to the current database session
        """
        self.__session.add(obj)
        self.save()

    def save(self):
        """ commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from the current database session
        """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ reload all
        """
        Base.metadata.create_all(bind=self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """close method close from sqlalchemy
           Close this Session.
           This clears all items and ends any transaction in progress."""
        self.__session.close()
