from humans.human_class import HumanClass


def make_human():
    return HumanClass(
        name="Jane Doe",
        age=30,
        gender="female",
        living_address="Main Street 1",
        civil_status="single",
    )


def test_defaults():
    human = make_human()
    assert human.is_foreigner is False


def test_get_information_returns_tuple():
    human = make_human()
    assert human.get_information() == ("Jane Doe", 30, "female", "Main Street 1", "single")


def test_move_in_to_apartment_updates_address():
    human = make_human()
    human.move_in_to_appartment("Apartment 5B")
    assert human.living_address == "Apartment 5B"


def test_change_living_address_updates_address():
    human = make_human()
    human.change_living_address("New Street 2")
    assert human.living_address == "New Street 2"


def test_setters_and_getters():
    human = make_human()
    human.set_age(40)
    human.set_civil_status("married")
    human.set_gender("other")

    assert human.get_age() == 40
    assert human.civil_status == "married"
    assert human.gender == "other"
