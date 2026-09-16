async def test_create_and_list_districts(client):
    create_response = await client.post(
        "/districts/create_a_new_district",
        json={"name": "Downtown", "post_number": 1000},
    )
    assert create_response.status_code == 200

    list_response = await client.get("/districts/show_all_districts")
    assert list_response.status_code == 200
    districts = list_response.json()
    assert len(districts) == 1
    assert districts[0]["district_name"] == "Downtown"
    assert districts[0]["post_number"] == 1000


async def test_show_all_districts_starts_empty(client):
    response = await client.get("/districts/show_all_districts")
    assert response.status_code == 200
    assert response.json() == []
