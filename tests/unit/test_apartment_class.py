from apartments.apartment_class import Apartment


def make_apartment():
    return Apartment(floor=2, apartment_name="A101", number_of_rooms=3, square_meter=55)


def test_apartment_defaults():
    apt = make_apartment()
    assert apt.floor == 2
    assert apt.apartment_name == "A101"
    assert apt.number_of_rooms == 3
    assert apt.square_meter == 55
    assert apt.bathrooms == 1
    assert apt.has_a_balcony is True
    assert apt.has_foreigner is False


def test_apartment_without_balcony():
    apt = make_apartment()
    apt.apartment_without_balcony()
    assert apt.has_a_balcony is False


def test_number_of_bathrooms():
    apt = make_apartment()
    apt.number_of_bathrooms(3)
    assert apt.bathrooms == 3


def test_update_status_with_foreigner():
    apt = make_apartment()
    apt.update_status_with_foreigner()
    assert apt.has_foreigner is True


def test_show_square_meter():
    apt = make_apartment()
    assert apt.show_square_meter() == 55


def test_show_floor_of_the_apartment():
    apt = make_apartment()
    assert apt.show_floor_of_the_apartment() == "A101 is on the 2 floor"
