from sqlalchemy.ext.asyncio import AsyncSession

from districts.model import District


async def insert_new_district(district_name, post_number, db: AsyncSession):
    new_district = District(district_name=district_name,
                            post_number=post_number)
    db.add(new_district)
    await db.flush()
    await db.commit()