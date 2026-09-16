from apartments.apartment_building_class import ApartmentBuilding
from districts.district_class import DistrictClass


def make_district():
    return DistrictClass("Downtown", 1234)


def test_show_post_number():
    district = make_district()
    assert district.show_post_number() == 1234


def test_add_apartment_building_to_district():
    district = make_district()
    building = ApartmentBuilding("Main Street 1", 3, 6)

    result = district.add_apartment_building_to_district(building)

    assert result == [building]
    assert district.list_of_apartment_buildings == [building]


def test_add_apartment_building_rejects_wrong_type():
    district = make_district()

    result = district.add_apartment_building_to_district("not a building")

    assert result is None
    assert district.list_of_apartment_buildings == []


def test_show_all_apartments_in_a_district():
    district = make_district()
    building = ApartmentBuilding("Main Street 1", 3, 6)
    district.add_apartment_building_to_district(building)

    assert district.show_all_apartments_in_a_district() == [building]
