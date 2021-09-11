from typing import Any, Dict, List, Optional, Union

from app.infra.postgres.crud.base import CRUDBase
from app.infra.postgres.models import Item
from app.schemas.item import CreateItem, UpdateItem


class CRUDItem(CRUDBase[Item, CreateItem, UpdateItem]):
    async def get_all(
        self,
        *,
        payload: Dict[str, Any] = {},
        skip: int = 0,
        limit: int = 10,
    ) -> List[Item]:
        model = (
            await self.model.filter(**payload)
            .prefetch_related()
            .all()
            .offset(skip)
            .limit(limit)
        )
        return model

    async def get_byid(self, *, id: Union[str, int]) -> Optional[Item]:
        model = await self.model.get_or_none(id=id).prefetch_related("city")
        return model


crud_item = CRUDItem(model=Item)
