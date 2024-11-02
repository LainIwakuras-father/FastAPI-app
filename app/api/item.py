from typing import Annotated
from fastapi import APIRouter, Depends

from app.api.dependencies import item_service
from app.schemas.item_schema import ItemWrite, ItemUpdate

from app.services.item import ItemService

item_router = APIRouter(prefix="/Item", tags=["Items"])

@item_router.post("/ItemAdd")
async def todo_post(item_data:ItemWrite,
                    service: Annotated[ItemService,Depends(item_service)]):
    item_id = await service.add_item(item_data)
    return {'item_id':item_id}


@item_router.put('/updateItem')
async def update_item(
        id:int,
        item_data:ItemUpdate,
        service: Annotated[ItemService,Depends(item_service)])->str:
        item = await service.update_info(id, item_data)
        return item


@item_router.delete('/deleteItem')
async def delete_item(
        id:int,
        service: Annotated[ItemService,Depends(item_service)])->str:
    res = await service.delete_item(id)
    return res



