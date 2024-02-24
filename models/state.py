#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship between State and City models if using database storage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship(
            "City", backref="state", cascade="all, delete"
        )
    else:
        # Define a property to get cities related to the state
        @property
        def cities(self):
            """Returns list of City instances related to this state."""
            city_instances = []
            for city_obj in models.storage.all(City).values():
                if city_obj.state_id == self.id:
                    city_instances.append(city_obj)
                    return city_instances
