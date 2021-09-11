from typing import List

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from fastapi.responses import JSONResponse, Response

from app.schemas.general import CountDB
from app.schemas.item import CreateItem, Item, SearchItem, UpdateItem
from app.services.item import item_service

router = APIRouter()


@router.get(
    "/count",
    response_class=JSONResponse,
    response_model=CountDB,
    status_code=200,
    responses={
        200: {"description": "Total items"},
    },
)
async def count(
    search: SearchItem = Depends(SearchItem),
):
    items = await item_service.count(payload=search.dict(exclude_none=True))
    return {"count": items}


@router.get(
    "",
    response_class=JSONResponse,
    response_model=List[Item],
    status_code=200,
    responses={
        200: {"description": "Items found"},
    },
)
async def get_all(
    skip: int = Query(0),
    limit: int = Query(99999),
    search: SearchItem = Depends(SearchItem),
):
    items = await item_service.get_all(
        skip=skip,
        limit=limit,
        payload=search.dict(exclude_none=True),
    )
    return items


@router.post(
    "",
    response_class=JSONResponse,
    response_model=Item,
    status_code=201,
    responses={
        201: {"description": "Item created"},
    },
)
async def create(new_item: CreateItem):
    item = await item_service.create(obj_in=new_item)
    return item


@router.get(
    "/{id}",
    response_class=JSONResponse,
    response_model=Item,
    status_code=200,
    responses={
        200: {"description": "Item found"},
        404: {"description": "Item not found"},
    },
)
async def by_id(id: int = Path(...)):
    item = await item_service.get_byid(id=id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.patch(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Item update"},
        404: {"description": "Item not found"},
    },
)
async def update(update_item: UpdateItem, id: int = Path(...)):
    await item_service.update(id=id, obj_in=update_item)


@router.delete(
    "/{id}",
    response_class=Response,
    response_model=None,
    status_code=204,
    responses={
        204: {"description": "Item delete"},
    },
)
async def delete(id: int = Path(...)):
    item = await item_service.delete(id=id)
    if item == 0:
        raise HTTPException(status_code=404, detail="Item not found")
