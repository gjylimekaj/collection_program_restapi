from fastapi import APIRouter

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends
from database.database_config import get_async_db_session
from districts.district_class import DistrictClass
from districts.crud.crud_get import get_all_districts

district_app = APIRouter()

districts: list[DistrictClass] = []

@district_app.get("/show_all_districts", summary="List all districts")
async def show_all_districts(db: AsyncSession = Depends(get_async_db_session)):
    return await get_all_districts(db)

