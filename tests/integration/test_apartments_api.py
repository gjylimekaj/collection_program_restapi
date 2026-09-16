async def test_create_and_get_apartment(client):
    payload = {
        "floor": 2,
        "apartment_name": "A101",
        "number_of_rooms": 3,
        "square_meter": 55.5,
        "bathrooms": 1,
        "has_a_balcony": True,
        "has_foreigners": False,
    }

    create_response = await client.post("/apartments/create_a_new_apartment", json=payload)
    assert create_response.status_code == 200

    get_response = await client.get("/apartments/get_info_about_one_apartment/A101")
    assert get_response.status_code == 200
    body = get_response.json()
    assert body["apartment_name"] == "A101"
    assert body["number_of_rooms"] == 3
    assert body["has_a_balcony"] is True


async def test_get_unknown_apartment_returns_404(client):
    response = await client.get("/apartments/get_info_about_one_apartment/does-not-exist")
    assert response.status_code == 404
