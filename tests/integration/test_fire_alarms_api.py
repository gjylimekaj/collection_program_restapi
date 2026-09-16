from apartments.model import ApartmentBuilding

ADMIN_CODE = "test-admin-code"


async def _add_apartment_building(db_session, street_name="Main Street 1"):
    building = ApartmentBuilding(
        street_name=street_name,
        floors=3,
        number_of_apartments=6,
        number_of_foreigners_in_this_building=0,
    )
    db_session.add(building)
    await db_session.commit()
    await db_session.refresh(building)
    return building


async def test_register_alarm_success(client, db_session):
    await _add_apartment_building(db_session)

    response = await client.post(
        "/fire_alarm/register_alarm",
        json={
            "address": "Main Street 1",
            "apartment_floor_id": 2,
            "admin_password": ADMIN_CODE,
        },
    )

    assert response.status_code == 200


async def test_register_alarm_wrong_password(client, db_session):
    await _add_apartment_building(db_session)

    response = await client.post(
        "/fire_alarm/register_alarm",
        json={
            "address": "Main Street 1",
            "apartment_floor_id": 2,
            "admin_password": "wrong-password",
        },
    )

    assert response.status_code == 400


async def test_register_alarm_unknown_address(client):
    response = await client.post(
        "/fire_alarm/register_alarm",
        json={
            "address": "Unknown Street",
            "apartment_floor_id": 2,
            "admin_password": ADMIN_CODE,
        },
    )

    assert response.status_code == 400
