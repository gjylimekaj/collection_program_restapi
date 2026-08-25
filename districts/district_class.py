


from apartments.apartment_building_class import ApartmentBuilding
from apartments.apartment_class import Apartment

class DistrictClass:


    def __init__(self,district_name, post_number):
        self.district_name = district_name
        self.post_number = post_number

        self.list_of_apartment_buildings = []



    def show_post_number(self):
        print(self.post_number)
        return self.post_number



    def add_apartment_building_to_district(self, apartment_building: ApartmentBuilding):
        if not isinstance(apartment_building, ApartmentBuilding):
            print("ERROR, we can not accept int or string, only apartmentBuildingClass")

        else:
            #print("The list BEFORE appending:")
            #print(self.list_of_apartment_buildings)

            self.list_of_apartment_buildings.append(apartment_building)

            #print("The list AFTER appending:")
            #print(self.list_of_apartment_buildings)

            return self.list_of_apartment_buildings

    def show_all_apartments_in_a_district(self):
        print(self.list_of_apartment_buildings)
        return self.list_of_apartment_buildings

    def show_apartments_name_in_a_district(self):
        for name in self.list_of_apartment_buildings:
            print(name.name)


    def show_floors_at_all_apartments(self):
        for floors in self.list_of_apartment_buildings:
            print(floors.floors)

    def show_all_apartments_with_more_rooms(self):
        for building in self.list_of_apartment_buildings:
            for apt in building.list_of_apartments:
                if apt.number_of_rooms >= 2:
                    print("The apartment has", apt.number_of_rooms, "rooms")