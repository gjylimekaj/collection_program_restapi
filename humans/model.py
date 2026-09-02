from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class Human(Base):
    __tablename__ = "humans"

    human_ID = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    age = Column(Integer)
    gender = Column(String(255))
    civil_status = Column(String(255))
    is_foreigner = Column(Boolean)
    apartment_class_ID = Column(Integer, ForeignKey("apartments.apartment_class_ID"))

    apartment = relationship("Apartment", back_populates="humans")
