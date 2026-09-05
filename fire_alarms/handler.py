from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database_config import get_async_db_session

from fire_alarms.schemas import FireAlarmScheme
from fire_alarms.crud.crud_insert import insert_fire_alarm


import datetime
import os

fire_alarm_app = APIRouter()
@fire_alarm_app.post("/register_alarm")
async def register_alarm(alarm: FireAlarmScheme, db: AsyncSession = Depends(get_async_db_session)):
    a_date = datetime.date.today()
    time = datetime.datetime.now().time()
    admin_code = os.getenv("FIRE_ALARM_ADMIN_CODE", "").replace("'", "")
    if admin_code == alarm.admin_password:
        await insert_fire_alarm(a_date, time,alarm.apartment_building_id, alarm.apartment_floor_id,db)
        return "Alarm registered! Thank you so much :)"
    else:
        raise HTTPException(status_code=400, detail="Invalid admin password")