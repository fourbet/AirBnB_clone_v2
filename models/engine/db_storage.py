#!/usr/bin/python3
"""This module defines a class to manage db storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import Base
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """This class manages storage of hbnb models in SQLAlchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """Initialization of instance of DBStorage"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        ret = {}
        if cls is None:
            for elem in self.__session.query(State).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(User).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(City).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Amenity).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Place).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
            for elem in self.__session.query(Review).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
        else:
            for elem in self.__session.query(cls).all():
                ret[elem.__class__.__name__ + "." + elem.id] = elem
        return ret

    def new(self, obj):
        """Adds new object to sessio,"""
        self.__session.add(obj)

    def delete(self, obj=None):
        """Delete obj from __objects"""
        if obj is None:
            return
        self.__session.delete(obj)

    def save(self):
        """Saves session"""
        self.__session.commit()

    def reload(self):
        """Loads tables and create session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Remove method on the provate session attribute"""
        self.__session.close()
