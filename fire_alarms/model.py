from sqlalchemy import Column, Date, ForeignKey, Integer, Time
from sqlalchemy.orm import relationship

from database.base import Base


class FireAlarm(Base):
    __tablename__ = "fire_alarm"

    alarm_ID = Column(Integer, primary_key=True, autoincrement=True)
    registered_at_date = Column(Date)
    registered_at_time = Column(Time)
    apartment_building_ID = Column(
        Integer,
        ForeignKey("apartment_building.apartment_building_ID"),
    )
    floor = Column(Integer)

    apartment_building = relationship("ApartmentBuilding", back_populates="fire_alarms")
