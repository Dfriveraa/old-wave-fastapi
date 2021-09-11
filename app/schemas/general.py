from typing import Any, TypeVar

from pydantic import BaseModel, Field
from pydantic.networks import AnyHttpUrl
from tortoise.models import Model

ModelType = TypeVar("ModelType", bound=Model)

CrudType = TypeVar("CrudType", bound=Any)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CountDB(BaseModel):
    count: int = Field(...)


class Seller(BaseModel):
    id: int = Field(7)
    name: str = Field("FastAPI")
    logo: AnyHttpUrl = Field("http://the-best-logo")
