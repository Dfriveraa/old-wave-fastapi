from typing import List, Optional

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    HTTPException,
    Path,
    Query,
    UploadFile,
)
from fastapi.responses import JSONResponse, Response

from app.schemas.general import CountDB
from app.schemas.item import (
    CreateItem,
    Item,
    ItemList,
    ItemResponse,
    SearchItem,
    UpdateItem,
)
from app.services.item import item_service
from app.services.s3 import s3_service

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


@router.post(
    "",
    response_class=JSONResponse,
    response_model=ItemResponse,
    status_code=201,
    responses={
        201: {"description": "Item created"},
    },
)
async def create(
    city_id: int = Form(None),
    name: str = Form(...),
    description: Optional[str] = Form(None),
    brand: str = Form(...),
    price: float = Form(...),
    rating: Optional[float] = Form(None),
    pictures_file: List[UploadFile] = File(..., media_type="image"),
    thumbnail: UploadFile = File(...),
):
    s3_service.validate_format(files=pictures_file)
    s3_service.validate_format(files=[thumbnail])

    urls = [s3_service.upload_file(picture) for picture in pictures_file]
    url_thumbnail = s3_service.upload_file(thumbnail)
    complete_item = CreateItem(
        city_id=city_id,
        name=name,
        description=description,
        brand=brand,
        price=price,
        rating=rating,
        pictures=urls,
        thumbnail=url_thumbnail,
    )

    item = await item_service.create(obj_in=complete_item)
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
