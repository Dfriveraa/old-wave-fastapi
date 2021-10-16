import asyncio
from fastapi.testclient import TestClient
from app.infra.postgres.crud.city import crud_city
from app.schemas.city import CreateCity

route = "/api/v1/cities"


def test_get_city_by_id(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    city_in = CreateCity(name="Paolakistan")
    city_db = event_loop.run_until_complete(crud_city.create(obj_in=city_in))
    response = test_app.get(f"{route}/{city_db.id}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert type(response.json()) == dict
    json = response.json()
    for i in ["name", "id"]:
        assert i in json
    assert json["id"] == city_db.id


def test_failed_get_city_by_id(
    test_app: TestClient, event_loop: asyncio.AbstractEventLoop
):
    city_in = CreateCity(name="Paolakistan")
    event_loop.run_until_complete(crud_city.create(obj_in=city_in))
    response = test_app.get(f"{route}/9999")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert type(json) == dict
    assert json == {"detail": "City not found"}


def test_all_citys(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    cities_in = ["Paolakistan", "Amagayork", "Medallo"]
    for i in cities_in:
        event_loop.run_until_complete(crud_city.create(obj_in=CreateCity(name=i)))
    response = test_app.get(route)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert type(json) == list
    assert type(json[0]) == dict
    assert len(json) == len(cities_in)


def test_get_all_cities_paginated(
    test_app: TestClient, event_loop: asyncio.AbstractEventLoop
):
    cities_in = ["Paolakistan", "Amagayork", "Medallo"]
    for i in cities_in:
        event_loop.run_until_complete(crud_city.create(obj_in=CreateCity(name=i)))
    response = test_app.get(route, params={"limit": 1})
    assert response.status_code == 200
    json = response.json()
    assert type(json) == list
    assert type(json[0]) == dict
    assert len(json) == 1
