from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from apartments.model import ApartmentBuilding
from fire_alarms.model import FireAlarm

async def get_apartment_building_from_db(db: AsyncSession, apartment_building_name: str):
    apartment_building = await db.execute(select(ApartmentBuilding).where(ApartmentBuilding.street_name == apartment_building_name))
    apartment_found = apartment_building.scalars().first()
    return apartment_found