async def test_create_district_is_stored_in_real_db(client, test_prefix):
    name = f"{test_prefix}Downtown"

    create_response = await client.post(
        "/districts/create_a_new_district",
        json={"name": name, "post_number": 9999},
    )
    assert create_response.status_code == 200

    list_response = await client.get("/districts/show_all_districts")
    assert list_response.status_code == 200
    created = [d for d in list_response.json() if d["district_name"] == name]
    assert len(created) == 1
    assert created[0]["post_number"] == 9999


async def test_create_district_without_name_returns_422(client):
    response = await client.post(
        "/districts/create_a_new_district",
        json={"post_number": 9999},
    )
    assert response.status_code == 422
