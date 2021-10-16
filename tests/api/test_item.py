import asyncio
from fastapi.testclient import TestClient
from app.schemas.item import CreateItem
from tests.utils.create_item import (
    default_item,
    default_item_bad_format,
    default_item_without_name,
)
from tests.mock_data.item import create_item_mock, get_all_item_mock
from tests.crud.test_city import create_default_city

route = "/api/v1/items"


def test_post_item(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    create_default_city(event_loop)
    response = test_app.post(route, **default_item)
    assert response.status_code == 201
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert CreateItem(**json)
    item = CreateItem(**json)
    assert item.name == "Televisor"


def test_get_item_by_id(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    create_default_city(event_loop)
    response = test_app.post(route, **default_item)
    json = response.json()
    assert "id" in json
    item_id = response.json()["id"]
    response = test_app.get(f"{route}/{item_id}")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert json.keys() == create_item_mock.keys()


def test_get_item_by_id_not_found(test_app: TestClient):
    item_id = 99
    response = test_app.get(f"{route}/{item_id}")
    assert response.status_code == 404
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert "detail" in json
    assert json["detail"] == "Item not found"


def test_failed_create_item(test_app: TestClient):
    bad_item = default_item_without_name.copy()
    response = test_app.post(route, **bad_item)
    assert response.status_code == 422
    assert response.headers["content-type"] == "application/json"


def test_bad_picture_format(test_app: TestClient):
    bad_item = default_item_bad_format.copy()
    response = test_app.post(route, **bad_item)
    assert response.status_code == 422
    assert response.headers["content-type"] == "application/json"


def test_get_all_item_scheme(test_app: TestClient):
    response = test_app.get(route)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json().keys() == get_all_item_mock.keys()


def test_get_all_items_empty(test_app: TestClient):
    response = test_app.get(route)
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json()["items"] == []


def test_get_all_items(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    create_default_city(event_loop)
    default = default_item.copy()
    response = test_app.post(route, **default)
    assert response.status_code == 201
    test_app.post(route, **default_item)
    response = test_app.get(route)
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert len(json["items"]) == 2


def test_search_item_schema(test_app: TestClient):
    response = test_app.get("/api/v1/search")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json().keys() == get_all_item_mock.keys()


def test_search_item_param(test_app: TestClient, event_loop: asyncio.AbstractEventLoop):
    create_default_city(event_loop)
    default = default_item.copy()
    test_app.post(route, **default)
    response = test_app.get("/api/v1/search", params={"q": "NONE SEARCH"})
    assert response.headers["content-type"] == "application/json"
    json = response.json()
    assert len(json["items"]) == 0
    response = test_app.get("/api/v1/search", params={"q": "televisor"})
    json = response.json()
    assert len(json["items"]) == 1
