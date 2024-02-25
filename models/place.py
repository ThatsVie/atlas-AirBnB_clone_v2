#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.amenity import Amenity


# Association table for Place and Amenity relationship
place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False
    )
)


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"

    # Columns for Place model
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []  # List to store Amenity IDs

    # Define relationships based on storage type
    if getenv("HBNB_TYPE_STORAGE") == "db":
        # Relationship with Review model
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete"
        )
        # Relationship with Amenity model through association table
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities"
        )
    else:
        # Property to get reviews related to this place
        @property
        def reviews(self):
            """Returns list of Review instances associated with this place."""
            reviews_list = []
            for review in models.storage.all('Review').values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        # Property to get amenities related to this place
        @property
        def amenities(self):
            """Returns list of Amenity instances associated with this place."""
            amenities_list = []
            for amenity in models.storage.all('Amenity').values():
                if amenity.id in self.amenity_ids:
                    amenities_list.append(amenity)
            return amenities_list

        # Setter method for amenities
        @amenities.setter
        def amenities(self, value):
            """Setter for amenity_ids list."""
            if isinstance(value, Amenity) and value.id not in self.amenity_ids:
                self.amenity_ids.append(value.id)
