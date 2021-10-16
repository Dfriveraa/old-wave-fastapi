import asyncio
from app.infra.postgres.models import Item
from app.infra.postgres.crud.item import crud_item
from app.schemas.item import CreateItem
from tests.crud.test_city import create_default_city

default_item = {
    "name": "iphone",
    "description": "celular",
    "brand": "Samsung",
    "price": 2000000,
    "rating": 5,
    "city_id": 1,
    "pictures": ["https://dev-empresariales.s3.amazonaws.com/Imagen+78.png"],
    "thumbnail": "https://dev-empresariales.s3.amazon.com",
}


def create_default_item(event_loop: asyncio.AbstractEventLoop):
    item_in = CreateItem(**default_item)
    item_db = event_loop.run_until_complete(crud_item.create(obj_in=item_in))
    return item_db


def test_create_item(event_loop: asyncio.AbstractEventLoop):
    create_default_city(event_loop)
    item_db = create_default_item(event_loop)
    assert isinstance(item_db, Item)
    assert item_db.name == "iphone"
