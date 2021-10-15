import asyncio
from app.infra.postgres.models import City
from app.infra.postgres.crud.city import crud_city
from app.schemas.city import CreateCity


def create_default_city(event_loop: asyncio.AbstractEventLoop):
    city_in = CreateCity(name="Paolakistan")
    city_db = event_loop.run_until_complete(crud_city.create(obj_in=city_in))
    return city_db


def test_create_city(event_loop: asyncio.AbstractEventLoop):
    city_db = create_default_city(event_loop)
    assert isinstance(city_db, City)
    assert city_db.name == "Paolakistan"
