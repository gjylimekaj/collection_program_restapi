from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class ApartmentBuilding(Base):
    __tablename__ = "apartment_building"

    apartment_bulding_ID = Column(Integer, primary_key=True, autoincrement=True)
    street_name = Column(String(255))
    floors = Column(Integer)
    number_of_apartments = Column(Integer)
    number_of_foreigners_in_this_building = Column(Integer)
    district_ID = Column(Integer, ForeignKey("district.district_ID"))

    district = relationship("District", back_populates="apartment_buildings")
    apartments = relationship("Apartment", back_populates="apartment_building")


class Apartment(Base):
    __tablename__ = "apartments"

    apartment_class_ID = Column(Integer, primary_key=True, autoincrement=True)
    floor = Column(Integer)
    apartment_name = Column(String(255))
    number_of_rooms = Column(Integer)
    square_meter = Column(Integer)
    bathrooms = Column(Integer)
    has_a_balcony = Column(Boolean)
    has_foreigners = Column(Boolean)
    apartment_bulding_ID = Column(Integer, ForeignKey("apartment_building.apartment_bulding_ID"))

    apartment_building = relationship("ApartmentBuilding", back_populates="apartments")
    humans = relationship("Human", back_populates="apartment")
