
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from apartments.model import Apartment

async def get_all_apartments(db: AsyncSession):
    all_apartments = await db.execute(select(Apartment))
    apartment_found = all_apartments.scalars().all()
    return apartment_found

async def get_apartment_from_db(db: AsyncSession, apartment_name: str):
    apartment = await db.execute(select(Apartment).where(Apartment.apartment_name == apartment_name))
    apartment_found = apartment.scalars().first()
    return apartment_found