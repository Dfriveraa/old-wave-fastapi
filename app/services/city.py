from app.infra.postgres.crud.city import crud_city
from app.infra.services.base_service import BaseService


class CityService(BaseService):
    ...


city_service = CityService(crud=crud_city)
