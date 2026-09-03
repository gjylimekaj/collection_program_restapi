from sqlalchemy.ext.asyncio import AsyncSession
from apartments.model import Apartment

async def insert_apartment(floor, apartment_name, number_of_rooms, square_meter, bathrooms, has_a_balcony, has_foreigners, db: AsyncSession ):
    new_apartment = Apartment(floor=floor, apartment_name=apartment_name, number_of_rooms=number_of_rooms,
                              square_meter=square_meter, bathrooms=bathrooms, has_a_balcony=has_a_balcony,
                             has_foreigners=has_foreigners)
    db.add(new_apartment)
    await db.flush()
    await db.commit()