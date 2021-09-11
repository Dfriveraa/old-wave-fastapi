from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.city import City, CreateCity, SearchCity, UpdateCity
from app.schemas.general import CountDB
from app.services.city import city_service

router = APIRouter()


@router.get(
    "/count",
    response_class=JSONResponse,
    response_model=CountDB,
    status_code=200,
    responses={
        200: {"description": "Total cities"},
    },
)
async def count(
    search: SearchCity = Depends(SearchCity),
):
    cities = await city_service.count(payload=search.dict(exclude_none=True))
    return {"count": cities}


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[City],
    status_code=200,
    responses={
        200: {"description": "Cities found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(99999),
    search: SearchCity = Depends(SearchCity),
):
    cities = await city_service.get_all(
        skip=skip,
        limit=limit,
        payload=search.dict(exclude_none=True),
    )
    return cities


@router.post(
    "",
    response_class=JSONResponse,
    response_model=City,
    status_code=201,
    responses={
        201: {"description": "City created"},
    },
)
async def create(new_city: CreateCity):
    city = await city_service.create(obj_in=new_city)
    return city


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=City,
    status_code=200,
    responses={
        200: {"description": "City found"},
        404: {"description": "City not found"},
    },
)
async def by_id(id: int = Path(...)):
    city = await city_service.get_byid(id=id)
    if city is None:
        raise HTTPException(status_code=404, detail="City not found")
    return city


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "City update"},
        404: {"description": "City not found"},
    },
)
async def update(update_city: UpdateCity, id: int = Path(...)):
    await city_service.update(id=id, obj_in=update_city)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "City delete"},
    },
)
async def delete(id: int = Path(...)):
    city = await city_service.delete(id=id)
    if city == 0:
        raise HTTPException(status_code=404, detail="City not found")
