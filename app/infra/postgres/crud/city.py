from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models import City
from app.schemas.city import CreateCity, UpdateCity


class CRUDCity(CRUDBase[City, CreateCity, UpdateCity]):
    ...


crud_city = CRUDCity(model=City)
