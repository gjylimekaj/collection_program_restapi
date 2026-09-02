from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from districts.model import District

async def get_all_districts(db: AsyncSession):
    all_districts = await db.execute(select(District))
    district_found = all_districts.scalars().all()
    return district_found