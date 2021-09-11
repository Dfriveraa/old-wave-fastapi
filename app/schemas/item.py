from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic.networks import AnyHttpUrl

from app.schemas.city import City
from app.schemas.general import Seller


class ItemBase(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)
    brand: str = Field(...)
    pictures: Optional[List[AnyHttpUrl]] = Field(None)
    price: float = Field(...)
    rating: float = Field(...)


class CreateItem(ItemBase):
    city_id: int = Field(None)


class UpdateItem(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    brand: Optional[str] = Field(None)
    pictures: Optional[List[AnyHttpUrl]] = Field(None)
    price: Optional[float] = Field(None)
    rating: Optional[float] = Field(None)
    city_id: Optional[int] = Field(None)


class SearchItem(BaseModel):
    name__icontains: Optional[str] = Field(None, alias="q")


class ItemInDB(ItemBase):
    city: Optional[City] = Field(None)


class Item(ItemInDB):
    seller: Seller = Field(Seller())

    class Config:
        orm_mode = True


class ItemList(BaseModel):
    query: str = Field(...)
    total: int = Field(...)
    items: List[ItemInDB] = Field(...)
    seller: Seller = Field(Seller())

    class Config:
        orm_mode = True
