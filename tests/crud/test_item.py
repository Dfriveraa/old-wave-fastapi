import asyncio
from fastapi.testclient import TestClient
from app.schemas.item import CreateItem
from tests.utils.create_item import default_item
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