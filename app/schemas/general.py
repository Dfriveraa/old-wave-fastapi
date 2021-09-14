from typing import Any, TypeVar

from pydantic import BaseModel, Field
from pydantic.networks import AnyHttpUrl
from tortoise.models import Model
from fastapi import Form
ModelType = TypeVar("ModelType", bound=Model)

CrudType = TypeVar("CrudType", bound=Any)

CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


def form_body(cls):
    cls.__signature__ = cls.__signature__.replace(
        parameters=[
            arg.replace(default=Form(...))
            for arg in cls.__signature__.parameters.values()
        ]
    )
    return cls

class CountDB(BaseModel):
    count: int = Field(...)


class Seller(BaseModel):
    id: int = Field(7)
    name: str = Field("FastAPI")
    logo: AnyHttpUrl = Field("http://the-best-logo")
