from typing import Any, Dict, Generic, List, Optional, Union

from app.schemas.general import CreateSchemaType, ModelType, UpdateSchemaType


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, *, model: ModelType) -> None:
        self.model = model

    async def get_all(
        self,
        *,
        payload: Dict[str, Any] = {},
        skip: int = 0,
        limit: int = 10,
    ) -> List[ModelType]:
        model = await self.model.filter(**payload).all().offset(skip).limit(limit)
        return model

    async def create(self, *, obj_in: CreateSchemaType) -> ModelType:
        model = await self.model.create(**obj_in.dict())
        return model

    async def update(self, *, id: Union[str, int], obj_in: Dict[str, Any]) -> bool:
        model = await self.model.get(id=id)
        await model.update_from_dict(obj_in).save()
        return True

    async def delete(self, *, id: Union[str, int]) -> int:
        delete = await self.model.get(id=id).delete()
        return delete

    async def get_byid(self, *, id: Union[str, int]) -> Optional[ModelType]:
        model = await self.model.get_or_none(id=id)
        return model

    async def count(self, *, payload: Dict[str, Any] = {}) -> int:
        count = await self.model.filter(**payload).all().count()
        return count
