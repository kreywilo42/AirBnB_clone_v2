#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""


class DBStorage:
    """This class manages database storage of hbnb models"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new model"""
        import os
        from sqlalchemy import (create_engine)
        from models.base_model import Base, BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'), os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'), os.getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        new_dict = {}
        if cls is None:
            for item in self.__session.query(User).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
            for item in self.__session.query(State).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
            for item in self.__session.query(City).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
            for item in self.__session.query(Amenity).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
            for item in self.__session.query(Place).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
            for item in self.__session.query(Review).all():
                key = item.__class__.__name__ + '.' + item.id
                new_dict[key] = item
        else:
            for item in self.__session.query(cls).all():
                key = "{}.{}".format(item.__class__.__name__,  item.id)
                new_dict[key] = item
        self.__session.close()
        return new_dict

    def new(self, obj):
        """Adds new object to storage"""
        from sqlalchemy.orm import sessionmaker
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        self.__session.add(obj)

    def save(self):
        """commit all changes"""
        self.__session.commit()
        # self.__session.close()

    def delete(self, obj=None):
        """Delete object from database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from sqlalchemy.orm import scoped_session
        from sqlalchemy.orm import sessionmaker
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ Closes a session """
        self.__session.close_all()
