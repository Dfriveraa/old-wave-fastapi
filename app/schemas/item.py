from typing import List, Optional

from fastapi import Form
from pydantic import BaseModel, Field
from pydantic.networks import AnyHttpUrl

from app.schemas.city import City
from app.schemas.general import Seller, form_body


class ItemBase(BaseModel):
    name: str = Field(...)
    description: Optional[str] = Field(None)
    brand: str = Field(...)
    price: float = Field(...)
    rating: Optional[float] = Field(None)


@form_body
class ItemBaseForm(BaseModel):
    city_id: int = Form(None)
    name: str = Form(...)
    description: Optional[str] = Form(None)
    brand: str = Form(...)
    price: float = Form(...)
    rating: Optional[float] = Form(None)


class CreateItem(ItemBase):
    pictures: List[AnyHttpUrl] = Field(...)
    thumbnail: AnyHttpUrl = Field(...)
    city_id: int = Field(None)


class ItemResponse(CreateItem):
    id: int = Field(None)


class UpdateItem(BaseModel):
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    brand: Optional[str] = Field(None)
    price: Optional[float] = Field(None)
    rating: Optional[float] = Field(None)
    city_id: Optional[int] = Field(None)


class SearchItem(BaseModel):
    name__icontains: Optional[str] = Field("", alias="q")


class ItemInDB(ItemBase):
    city: Optional[City] = Field(None)
    id: int = Field(...)

    class Config:
        orm_mode = True


class ItemListDB(ItemInDB):
    thumbnail: AnyHttpUrl = Field(...)


class Item(ItemInDB):
    seller: Seller = Field(Seller())
    pictures: List[AnyHttpUrl] = Field(...)

    class Config:
        orm_mode = True


class ItemList(BaseModel):
    query: Optional[str] = Field("")
    total: int = Field(...)
    items: List[ItemListDB] = Field(...)
    seller: Seller = Field(Seller())

    class Config:
        orm_mode = True
