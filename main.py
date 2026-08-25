from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from apartments.apartment_class import Apartment

app = FastAPI(title="Collection Program REST API")

apartments: list[Apartment] = []


class ApartmentIn(BaseModel):
    floor: int
    apartment_name: str
    number_of_rooms: int
    square_meter: float


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/apartments")
def list_apartments():
    return [vars(apartment) for apartment in apartments]


@app.post("/apartments")
def create_apartment(apartment_in: ApartmentIn):
    apartment = Apartment(
        floor=apartment_in.floor,
        apartment_name=apartment_in.apartment_name,
        number_of_rooms=apartment_in.number_of_rooms,
        square_meter=apartment_in.square_meter,
    )
    apartments.append(apartment)
    return vars(apartment)
