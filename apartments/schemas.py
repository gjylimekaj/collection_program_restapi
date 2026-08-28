from pydantic import BaseModel




class ApartmentIn(BaseModel):
    floor: int
    apartment_name: str
    number_of_rooms: int
    square_meter: float
