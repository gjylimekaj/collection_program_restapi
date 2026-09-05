from pydantic import BaseModel




class ApartmentInScheme(BaseModel):
    floor: int
    apartment_name: str
    number_of_rooms: int
    square_meter: float
    bathrooms: int
    has_a_balcony: bool
    has_foreigners: bool
