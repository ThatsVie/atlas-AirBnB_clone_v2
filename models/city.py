#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The City class represents a city in the project."""

    # Table name in the database
    __tablename__ = 'cities'

    # Define columns
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    # Define relationship with the Place class
    places = relationship(
        "Place",
        backref="cities",
        cascade="all, delete-orphan"
    )
