from fastapi import APIRouter, HTTPException
from fastapi.params import Depends

from apartments.apartment_class import Apartment
from apartments.schemas import ApartmentInScheme
from sqlalchemy.ext.asyncio import AsyncSession

from database.database_config import get_async_db_session
from apartments.crud.crud_insert import insert_apartment
from apartments.crud.crud_get import get_apartment_from_db

apartment_app = APIRouter()


apartments: list[Apartment] = []


@apartment_app.get("/show_all_apartments", summary="List all apartments")
def list_apartments():
    return [vars(apartment) for apartment in apartments]

@apartment_app.get("/get_info_about_one_apartment/{apartment_name}", summary="Get info about one apartment")
async def get_info_about_one_apartment(apartment_name: str, db: AsyncSession = Depends(get_async_db_session)):
    if await get_apartment_from_db(db, apartment_name):
        return await get_apartment_from_db(db, apartment_name)
    else:
        raise HTTPException(status_code=404, detail="Apartment not found")

@apartment_app.post("/create_a_new_apartment", summary="Create a new apartment")
async def create_apartment(apartment_in: ApartmentInScheme, db: AsyncSession = Depends(get_async_db_session)):
    await insert_apartment(apartment_in.floor, apartment_in.apartment_name, apartment_in.number_of_rooms, apartment_in.square_meter,
                           apartment_in.bathrooms, apartment_in.has_a_balcony, apartment_in.has_foreigners,db)
    return "congratulations, just added a new apartment!"

