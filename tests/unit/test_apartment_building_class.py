from apartments.apartment_building_class import ApartmentBuilding
from apartments.apartment_class import Apartment


def make_building():
    return ApartmentBuilding(name="Main Street 1", floors=3, number_of_apartments=6)


def test_initial_state():
    building = make_building()
    assert building.get_floors() == 3
    assert building.get_number_of_apartments() == 6
    assert building.list_of_apartments == []
    assert building.number_of_foreigners_in_this_building == 0


def test_add_apartment_to_building():
    building = make_building()
    apt = Apartment(1, "A1", 2, 40)
    building.add_apartment_to_building(apt)
    assert building.list_of_apartments == [apt]


def test_add_a_new_floor_also_adds_four_apartments():
    building = make_building()
    building.add_a_new_floor()
    assert building.floors == 2
    assert building.number_of_apartments == 10


def test_add_two_floors_adds_eight_apartments():
    building = make_building()
    building.add_two_floors()
    assert building.floors == 5
    assert building.number_of_apartments == 14


def test_erase_building_resets_everything():
    building = make_building()
    building.add_apartment_to_building(Apartment(1, "A1", 2, 40))
    building.erase_building()
    assert building.floors == 0
    assert building.number_of_apartments == 0
    assert building.list_of_apartments == []
    assert building.number_of_foreigners_in_this_building == 0
