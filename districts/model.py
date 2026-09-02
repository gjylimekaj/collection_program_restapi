from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from database.base import Base


class District(Base):
    __tablename__ = "district"

    district_ID = Column(Integer, primary_key=True, autoincrement=True)
    district_name = Column(String(255))
    post_number = Column(Integer)

    apartment_buildings = relationship("ApartmentBuilding", back_populates="district")
