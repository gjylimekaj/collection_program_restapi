class Apartment:
    def __init__(self, floor, apartment_name, number_of_rooms, square_meter):
        self.floor = floor
        self.apartment_name = apartment_name
        self.number_of_rooms = number_of_rooms
        self.square_meter = square_meter
        self.bathrooms = 1
        self.has_a_balcony = True

        self.has_foreigner = False



    def apartment_without_balcony(self) -> None:
        self.has_a_balcony = False

    def number_of_bathrooms(self, number_of_bathrooms:int) -> None:
        self.bathrooms = number_of_bathrooms


    def update_status_with_foreigner(self) -> None:
        self.has_foreigner = True
        print("A foreigner lives here.")
        print("at which appartment?")
        print(" apartment number ::::" , self.apartment_name)
        print('hehecjcj')


    def show_square_meter(self) -> int:
        return self.square_meter

    def show_floor_of_the_apartment(self):
        return f"{self.apartment_name} is on the {self.floor} floor"
