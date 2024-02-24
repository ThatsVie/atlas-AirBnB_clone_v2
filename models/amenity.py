#!/usr/bin/python3
"""Amenity Module for HBNB project"""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Defines the Amenity class"""

    # Table name in the database
    __tablename__ = "amenities"

    # Column definition for Amenity name
    name = Column(String(128), nullable=False)

    # Relationship with Place model through association table
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        viewonly=False
    )
