from pydantic import BaseModel


class FireAlarmScheme(BaseModel):
    address: str
    apartment_floor_id: int
    admin_password: str