from typing import Optional

from pydantic import BaseModel, Field


class CityBase(BaseModel):
    name: str = Field(...)


class CreateCity(CityBase):
    pass


class UpdateCity(BaseModel):
    name: Optional[str] = Field(None)


class SearchCity(BaseModel):
    name__icontains: Optional[str] = Field(None, alias="q")


class CityInDB(CreateCity):
    id: int = Field(...)


class City(CityInDB):
    class Config:
        orm_mode = True
