from fastapi import APIRouter

from apartments.apartment_class import Apartment
from apartments.schemas import ApartmentIn

apartment_app = APIRouter()


apartments: list[Apartment] = []


@apartment_app.get("/show_all_apartments", summary="List all apartments")
def list_apartments():
    return [vars(apartment) for apartment in apartments]


@apartment_app.post("/create_a_new_apartment", summary="Create a new apartment")
def create_apartment(apartment_in: ApartmentIn):
    apartment = Apartment(
        floor=apartment_in.floor,
        apartment_name=apartment_in.apartment_name,
        number_of_rooms=apartment_in.number_of_rooms,
        square_meter=apartment_in.square_meter,
    )
    apartments.append(apartment)
    return vars(apartment)
