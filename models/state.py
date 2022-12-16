#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", cascade="all, delete, delete-orphan", backref="states", lazy="joined")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        from models.city import City
        super().__init__(*args, **kwargs)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Get cities for FileStorage"""
            from models.city import City
            from models import storage
            city_dict = storage.all(City)
            city_list = []
            for city in city_dict.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
