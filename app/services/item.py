from app.infra.postgres.crud.item import crud_item
from app.infra.services.base_service import BaseService


class ItemService(BaseService):
    ...


item_service = ItemService(crud=crud_item)
