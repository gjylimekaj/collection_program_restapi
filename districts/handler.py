from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database.database_config import get_async_db_session
from districts.district_class import DistrictClass
from districts.crud.crud_get import get_all_districts
from districts.crud.crud_insert import insert_new_district
from districts.schemas import DistrictScheme

district_app = APIRouter()

districts: list[DistrictClass] = []

@district_app.get("/show_all_districts", summary="List all districts")
async def show_all_districts(db: AsyncSession = Depends(get_async_db_session)):
    return await get_all_districts(db)

@district_app.post("/create_a_new_district", summary="Create a new district")
async def create_a_new_district(human:DistrictScheme, db: AsyncSession = Depends(get_async_db_session)):
    await insert_new_district(human.name, human.post_number, db)

    return "new district added!"



