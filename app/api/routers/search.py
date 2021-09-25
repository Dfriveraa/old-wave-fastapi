from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    Query
)
from fastapi.responses import JSONResponse, Response

from app.schemas.item import Item, ItemList, SearchItem
from app.services.item import item_service

router = APIRouter()




@router.get(
    "",
    response_class=JSONResponse,
    response_model=ItemList,
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
    items_list = ItemList(items=items, query=search.name__icontains, total=len(items))
    return items_list


