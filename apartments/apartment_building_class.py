from apartments.apartment_class import Apartment

class ApartmentBuilding:
    def __init__(self, name, floors, number_of_apartments):
        self.name = name
        self.floors = floors
        self.number_of_apartments = number_of_apartments
        self.list_of_apartments = []

        self.number_of_foreigners_in_this_building = 0



    def get_number_of_apartments(self) -> int:
        return self.number_of_apartments

    def get_floors(self) -> int:
        return self.floors


    def add_apartment_to_building(self, apartment: Apartment):

        print()
        print("adding apartment to building")
        #print("which apartment?", apartment)

        self.list_of_apartments.append(apartment)

        print("apartment sucessfully added")
        print()


    def show_square_meters_of_the_apartments(self):
        for objects in self.list_of_apartments:
            print(objects.show_square_meter())


    def show_name_of_all_apartments(self):
        for apartments in self.list_of_apartments:
            print(apartments.apartment_name)

    def add_a_new_floor(self):
        self.floors += 1
        self.add_four_new_apartments()

    def add_two_floors(self):
        self.floors += 2
        self.add_four_new_apartments()
        self.add_four_new_apartments()


    def add_four_new_apartments(self):
        self.number_of_apartments = self.number_of_apartments + 4


    def erase_building(self):
        self.floors = 0
        self.number_of_apartments = 0
        self.list_of_apartments.clear()
        self.number_of_foreigners_in_this_building = 0





