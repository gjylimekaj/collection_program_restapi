from pydantic import BaseModel

class FireAlarmScheme(BaseModel):
    apartment_building_id: int
    apartment_floor_id: int
    admin_password: str