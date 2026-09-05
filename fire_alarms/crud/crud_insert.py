from datetime import date, time

from sqlalchemy.ext.asyncio import AsyncSession

from fire_alarms.model import FireAlarm


async def insert_fire_alarm(registered_at_date: date,
                            registered_at_time: time,
                            apartment_building_ID: int,
                            floor: int, db: AsyncSession,):
    new_fire_alarm = FireAlarm(
        registered_at_date=registered_at_date,
        registered_at_time=registered_at_time,
        apartment_building_ID=apartment_building_ID,
        floor=floor,
    )
    db.add(new_fire_alarm)
    await db.commit()
    await db.refresh(new_fire_alarm)
    return new_fire_alarm
