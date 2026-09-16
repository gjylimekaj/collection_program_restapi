from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database.database_config import get_async_db_session

from fire_alarms.schemas import FireAlarmScheme
from fire_alarms.crud.crud_insert import insert_fire_alarm
from fire_alarms.crud.crud_read import get_apartment_building_from_db


import datetime
import os

fire_alarm_app = APIRouter()
@fire_alarm_app.post("/OLD_register_alarm")
async def register_alarm(alarm: FireAlarmScheme, db: AsyncSession = Depends(get_async_db_session)):
    a_date = datetime.date.today()
    time = datetime.datetime.now().time()
    admin_code = os.getenv("FIRE_ALARM_ADMIN_CODE", "").replace("'", "")
    if admin_code == alarm.admin_password:
        await insert_fire_alarm(a_date, time,alarm.apartment_building_id, alarm.apartment_floor_id,db)
        return "Alarm registered! Thank you so much :)"
    else:
        raise HTTPException(status_code=400, detail="Invalid admin password")

@fire_alarm_app.post("/register_alarm")
async def register_alarm(alarm: FireAlarmScheme, db: AsyncSession = Depends(get_async_db_session)):
    a_date = datetime.date.today()
    time = datetime.datetime.now().time()
    admin_code = os.getenv("FIRE_ALARM_ADMIN_CODE", "").replace("'", "")
    if admin_code != alarm.admin_password:

        raise HTTPException(status_code=400, detail="Invalid admin password")
    else:

        check_if_address_exist = await get_apartment_building_from_db(db, alarm.address)
        if not check_if_address_exist:
            raise HTTPException(status_code=400, detail="You have typed incorrect address")
        else:
            print("The address is correct:)")
            print(check_if_address_exist)
            print(check_if_address_exist.apartment_building_ID)
            the_ID = check_if_address_exist.apartment_building_ID
            await insert_fire_alarm(a_date, time, the_ID, alarm.apartment_floor_id, db)
            return "Alarm registered! Thank you so much :)"

